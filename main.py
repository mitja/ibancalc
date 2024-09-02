from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schwifty import IBAN
from pydantic import BaseModel
import markdown
from bs4 import BeautifulSoup

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class IBANRequest(BaseModel):
    country_code: str
    bank_code: str
    account_code: str

class IBANResponse(BaseModel):
    iban: str

def read_readme(skip_lines=4):
    with open("README.md", "r") as f:
        content = f.readlines()[skip_lines:] 
    content = ''.join(content)
    html = markdown.markdown(content)
    
    # Parse the HTML and add classes to headings
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        tag['class'] = tag.get('class', []) + ['font-bold', 'mt-6', 'mb-4']
        if tag.name == 'h1':
            tag['class'].append('text-3xl')
        elif tag.name == 'h2':
            tag['class'].append('text-2xl')
        elif tag.name == 'h3':
            tag['class'].append('text-xl')
        else:
            tag['class'].append('text-lg')
    
    for p in soup.find_all('p'):
        p['class'] = p.get('class', []) + ['mb-4']
    
    for a in soup.find_all('a'):
        a['class'] = a.get('class', []) + ['text-blue-600', 'hover:text-blue-800', 'underline']

    return str(soup)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    readme_content = read_readme()
    return templates.TemplateResponse("index.html", {"request": request, "readme_content": readme_content})


@app.post("/generate_iban", response_model=IBANResponse)
async def generate_iban(request: IBANRequest):
    try:
        iban = IBAN.generate(
            country_code=request.country_code,
            bank_code=request.bank_code,
            account_code=request.account_code
        )
        return IBANResponse(iban=str(iban))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)