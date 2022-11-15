# Schulbot der FOS-Schifferstadt



## Beschreibung:
Dieser Bot wurde Entwickelt um den [Discord-Server]( https://discord.gg/92sdCZvsMY) der FOS von Schifferstadt zu verwalten. Hierbei Verwaltet der Bot die Rollenzuweisung der einzelnen Klassen und besitzt kleine extra Funktionen u.a. eine Schnittstelle zu einer Wetter API. 


## Verzeichnis:
> **Schnellster Start:** Quick-Start-Vorbereitung und Quick-Start-Befehle
* [Beschreibung](#Beschreibung)
* [Verzeichnis](#Verzeichnis)
* [Vorbereitung](#Vorbereitung)
  * [Quick-Start-Vorbereitung](#Quick-Start-Vorbereitung)
  * [Weitere Vorbereitung](#Weitere-Vorbereitung)
* [Bedienung](#Bedinung)
  * [Quick-Start-Befehle](#Quick-Start-Befehle)
  * [Weitere-Befehle](#Weitere-Befehle)
* [Kompatibilität](#Kompatibilität)
  * [Client Betriebsysteme](#Client-Betriebsysteme)
  * [Server Betriebsysteme](#Server-Betriebsysteme)
  * [Komiler Version](#Kompiler-Version)
  * [Verwendete Bibliotheken](#Verwendete-Bibliotheken)
* [Lizenz](#Lizenz)
* [Mitwirkende](#Mitwirkende)

## Vorbereitung:

### Quick-Start-Vorbereitung:
1. BOT-Erstellen und auf dem Server mit Admin Rolle einladen
2. Token vom Bot im Skript einfügen
3. Wetter API Key im Script einfügen
4. Channels in Verarbeitung.py einfügen
5. Python Installieren 
6. [Bibltiotheken von Python installieren](#Verwendete-Bibliotheken)
7. Script Schulbotmain.py starten (Script Schulbotmain.py muss im selben Ordner sein wie Vorbereitung.py)

> Ab hier kein Quick-Vorbereitung mehr!

### Weitere Vorbereitung: 
8. Anpassung der Funktionen vom Bot durch löschen von einzelnen Funktionen
9. Emojis können durch einfügen des Unicodes geändert werden (Achtung nicht alle Emojis können von Discord dargestellt werden)
10. Befehle Bezeichnungen können durch ersetzten der Wörter nach $ ersetzt werden

## Bedienung: 

### Quick-Start-Befehle:
|Befehl|Funktion|
|:---:|:---:|
|$help|Zeigt alle Funktionen des BOTs an|
|hello bot| Überprüfen von aktivität des Bot -> mit Rückgabe|
|$plscontactme|Meldet sich per Privat DM|

> Ab hier kein Quick-Befehle mehr!

### Weitere Befehle:
|Befehl|Funktion|
|:---:|:---:|
|$playgame|Beschreibung von Roulette|
|$playroulette|Start einer Roulett runde|
|$wetter|Abfrage des Wetters|
|$wetter2|Ausführliche abfrage vom Wetter|
|$slap (person)| Um jemanden zu Schlagen|

## Kompatibilität:

### Client Betriebsysteme:
|Betriebsystem|Version|Test Ergebnis|
|:---:|:---:|:---:|
|Windows|Windows 10|![funk](https://img.shields.io/badge/checks-passing-green)|
|Windows|Windows 11|![funk](https://img.shields.io/badge/checks-passing-green)|
|Arch Linux|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|CentOS|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Debian|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Elementary OS|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Fedora|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Gentoo Linux|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Kali Linux|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|macOS Mojave|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|macOS High Sierra|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|macOS Sierra|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|OS X El Capitan|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

#
### Server Betriebsysteme:
|Betriebsystem|Version|Test Ergebnis|
|:---:|:---:|:---:|
|Ubuntu|aktuellste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Debian|aktuellste Version|![funk](https://img.shields.io/badge/checks-passing-green)|
|Windows Server| aktuellste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)


#

### Kompiler Version:
|Kompiler|Version|Test Ergebnis|
|:---:|:---:|:---:|
|Python| 3.9 |![funk](https://img.shields.io/badge/checks-passing-green)|
|Python| 3.10 |![funk](https://img.shields.io/badge/checks-passing-green)|
|Python| aktuellste Version |![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

#

### Verwendete Bibliotheken:
|Bibliothek|Version|Test Ergebnis|
|:---:|:---:|:---:|
|random| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|requests| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|datetime| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|pycord| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|asyncio| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)


## Lizenz:

Die Lizenz zur weiter Verwendung dieses Projektes, wird durch das **Creative Common** Model angegeben. 
Bei Ablehnung jeglicher Verwendung durch meinerseits mit den Piktogrammen oder Sie möchten das Projekt in einer Form verwenden, die nicht hier genannt wurde, muss vor 
der Benutzung des Projektes die Zustimmung eingeholt werden.

|Verwendet|Piktogramm|Bezeichnung|Verlinkung|
|:---:|:---:|:---:|:---:|
|:x:|![Lizenz_eins](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png)|Namensnennung 4.0 International|[Details](https://creativecommons.org/licenses/by/4.0/legalcode.de)|
|:x:|![Lizenz_zwei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)|Namensnennung-Share Alike 4.0 International|[Details](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)|
|:x:|![Lizenz_drei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nd.png)|Namensnennung-Keine Bearbeitungen 4.0 International|[Details](https://creativecommons.org/licenses/by-nd/4.0/legalcode.de)|
|:x:|![Lizenz_vier](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.eu.png)|Namensnennung-Nicht kommerziell 4.0 International|[Details](https://creativecommons.org/licenses/by-nc/4.0/legalcode.de)|
|:heavy_check_mark:|![Lizenz_fünf](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.eu.png)|	Namensnennung-Nicht kommerziell-Share Alike 4.0 International|[Details](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.de)|
|:x:|![Lizenz_sex](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-nd.eu.png)|	Namensnennung-Nicht kommerziell-Keine Bearbeitungen 4.0 International|[Details](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.de)|

> Verwendete Lizenz: :heavy_check_mark: Nicht verwendete Lizenz: :x:


# Mitwirkende:

clurky (Alina), Shelicus (David) 
