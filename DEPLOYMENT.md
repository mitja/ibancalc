# Deployment with Dokku

## Pre-requisites

- A server with Dokku installed
- A domain name pointing to the server
- lets-encrypt plugin installed on the Dokku server

## Initial Deployment

1. Set the environment variables
2. Create the app
3. Add the app on the dokku host as git remote
4. Set the deploy branch to main
5. Push the code to the dokku host
6. Add the domain to the app
7. Enable letsencrypt for the app

```bash
export DOKKU_HOST=example.com
export APP_DOMAIN=ibancalc.com
ssh dokku@$DOKKU_HOST dokku apps:create ibancalc
git remote add dokku dokku@$DOKKU_HOST:ibancalc 
ssh dokku@$DOKKU_HOST dokku git:set ibancalc deploy-branch main
git push dokku main 
ssh dokku@$DOKKU_HOST domains:add ibancalc $APP_DOMAIN
ssh dokku@$DOKKU_HOST letsencrypt:enable ibancalc
```

## Update Deployment

1. Make changes to the code, test locally, commit
2. Push the code to the dokku host (and your normal git remote, as well)

```bash
git push dokku main
```

## A Heads Up from Dokku About Let's Encrypt Credentials

"Your account credentials have been saved in your Let's Encrypt configuration directory at "/certs/accounts".
       
You should make a secure backup of this folder now. This configuration directory will also contain certificates and private keys obtained from Let's Encrypt so making regular backups of this folder is ideal."