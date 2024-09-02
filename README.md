# [ibancalc.com](https://ibancalc.com)

## Der einfache IBAN Rechner

IBAN Calc ist ein einfacher IBAN Rechner. Er generiert die passende IBAN Nummer aus Land, Kontonummer und Bankleitzahl. Aktuell nur für Deutschland. 

## Warum gibt es diesen IBAN Rechner?

Es gibt diesen IBAN Rechner, weil ich mir die IBAN für meine eigene Kontonummer nicht merken kann und deswegen immer wieder einen anderen IBAN Rechner im Internet benutzte. Leider ist dieser IBAN Rechner so extrem mit Werbung überladen, dass ich einfach einen eigenen IBAN Rechner online stellen musste.

Wenn es Dir auch so geht, würde ich mich freuen, wenn Du wie ich statt des anderen IBAN Rechners von nun an IBAN Calc verwendest.

## Was ist die IBAN?

IBAN ist eine Abkürzung für "International Bank Account Number".

Die IBAN wird in der EU und einigen anderen Ländern verwendet, um Bankkonten zu identifizieren. Sie besteht aus einem Ländercode, einer Prüfziffer, einer Bankleitzahl und einer Kontonummer.

Die IBAN wird mit verschiedenen Methoden berechnet, die von Land zu Land und auch innerhalb von Ländern unterschiedlich sind (z. B. je nach Bankleitzahl, wie in Deutschland). Welche Regel für welche Bankleitzahl genutzt wird, steht in einer Datei, welche die Deutsche Bundesbank bereitstellt.

Eine IBAN kann auch validiert werden. Das folgt dann ebenfalls den Regeln des jeweiligen Landes.

## Wie funktioniert dieser IBAN Rechner

Dieser IBAN Rechner verwendet die Python Bibliothek [Schwifty](https://github.com/mdomke/schwifty) um die IBAN zu berechnen. Schwifty enthält die Regeln für die IBAN Berechnung und Validierung in der jeweils aktuellen Form. Damit sollten die mit diesem IBAN Rechner erzeugten IBANs stets korrekt sein.

Wenn Du genau wissen willst, wie dieser IBAN Rechner funktionert, dann kannst Du Dir den Quellcode ansehen. IBAN Calc ist Open Source (MIT Lizenz), den Quellcode findest Du auf GitHub unter [mitja/ibancalc](https://github.com/mitja/ibancalc)

## Dein Feedback und Verbesserungsvorschläge

Falls Du einen Fehler bei IBAN Calc feststellst, kannst Du gerne ein [Ticket](https://github.com/mitja/ibancalc/issues) anlegen. Falls es ein sicherheitsrelevantes Problem ist, sende mir bitte eine E-Mail an hi [at] mitjamartini [dot] com. Ich nehme gerne auch Verbesserungsvorschläge entgehen, kann allerdings nicht versprechen, dass ich sie umsetze.

## Datenschutz

Dieser IBAN Rechner wird bei [Hetzner](https://hetzner.com) in Deutschland gehostet. 

Die eingegebenen Daten (Land, Kontonummer und Bankleitzahl) und die errechnete IBAN werden nicht gespeichert. 

Cookies werden nicht verwendet.

Für die Analyse der Website Nutzung verwende ich Webserver Logs und [Plausible](https://plausible.io). Plausible speichert

* die Page URL,
* den HTTP Referrer, 
* den Browser und das Betriebssystem, 
* die Device Art (z. B. Desktop) und 
* das Land, die Region und Stadt. 


Die Ortsdaten werden anhand der IP-Adresse ermittelt. Die IP-Adresse wird nicht gespeichert und es gibt keine genauere Auswertung als auf Stadt-Ebene.

## Kontakt und Impressum

Verantwortlich für diese Website ist:

* Mitja Martini
* Helmkrautstraße 32
* 13503 Berlin
* Deutschland


E-Mail: hi [at] mitjamartini [dot] com