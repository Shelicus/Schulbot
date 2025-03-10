# Schulbot der FOS-Schifferstadt

## Beschreibung:
Dieser Bot wurde entwickelt, um den [Discord-Server](https://discord.gg/92sdCZvsMY) der FOS Schifferstadt zu verwalten. Der Bot übernimmt die Rollenzuweisung der einzelnen Klassen und bietet zusätzliche Funktionen, u. a. eine Schnittstelle zu einer Wetter-API. Leider wird er nicht mehr gewartet und ist nur noch im "Read-Only"-Modus verfügbar.

## Verzeichnis:
> **Schnellster Start:** Quick-Start-Vorbereitung und Quick-Start-Befehle
* [Beschreibung](#Beschreibung)
* [Verzeichnis](#Verzeichnis)
* [Vorbereitung](#Vorbereitung)
  * [Quick-Start-Vorbereitung](#Quick-Start-Vorbereitung)
  * [Weitere Vorbereitung](#Weitere-Vorbereitung)
* [Bedienung](#Bedienung)
  * [Quick-Start-Befehle](#Quick-Start-Befehle)
  * [Weitere Befehle](#Weitere-Befehle)
* [Kompatibilität](#Kompatibilität)
  * [Client-Betriebssysteme](#Client-Betriebssysteme)
  * [Server-Betriebssysteme](#Server-Betriebssysteme)
  * [Kompiler-Version](#Kompiler-Version)
  * [Verwendete Bibliotheken](#Verwendete-Bibliotheken)
* [Lizenz](#Lizenz)
* [Mitwirkende](#Mitwirkende)

## Vorbereitung:

### Quick-Start-Vorbereitung:
1. Bot erstellen und auf dem Server mit Admin-Rechten einladen.
2. Token des Bots im Skript einfügen.
3. Wetter-API-Key im Skript einfügen.
4. Channels in `Verarbeitung.py` einfügen.
5. Python installieren.
6. [Bibliotheken von Python installieren](#Verwendete-Bibliotheken).
7. Skript `Schulbotmain.py` starten (das Skript `Schulbotmain.py` muss im gleichen Ordner wie `Vorbereitung.py` sein).

> Ab hier keine Quick-Start-Vorbereitung mehr!

### Weitere Vorbereitung:
8. Anpassung der Funktionen des Bots durch Löschen einzelner Funktionen.
9. Emojis können durch Einfügen des Unicode geändert werden (Achtung: Nicht alle Emojis können von Discord dargestellt werden).
10. Befehlsbezeichner können durch Ersetzen der Wörter nach dem `$` angepasst werden.

## Bedienung:

### Quick-Start-Befehle:
| Befehl       | Funktion                                               |
|:------------:|:------------------------------------------------------:|
| `$help`      | Zeigt alle Funktionen des Bots an                      |
| `hello bot`  | Überprüft die Aktivität des Bots -> mit Rückgabe       |
| `$plscontactme` | Meldet sich per Privat-DM                           |

> Ab hier keine Quick-Start-Befehle mehr!

### Weitere Befehle:
| Befehl             | Funktion                                           |
|:------------------:|:--------------------------------------------------:|
| `$playgame`        | Beschreibung von Roulette                          |
| `$playroulette`    | Start einer Roulett-Runde                          |
| `$wetter`          | Abfrage des Wetters                                |
| `$wetter2`         | Ausführliche Abfrage des Wetters                   |
| `$slap (person)`   | Um jemanden zu schlagen                            |

## Kompatibilität:

### Client-Betriebssysteme:
| Betriebssystem   | Version             | Test-Ergebnis |
|:----------------:|:-------------------:|:-------------:|
| Windows          | Windows 10          | ![funk](https://img.shields.io/badge/checks-passing-green) |
| Windows          | Windows 11          | ![funk](https://img.shields.io/badge/checks-passing-green) |
| Arch Linux       | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| CentOS           | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| Debian           | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| Elementary OS    | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| Fedora           | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| Gentoo Linux     | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| Kali Linux       | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| macOS Mojave     | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| macOS High Sierra| Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| macOS Sierra     | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| OS X El Capitan  | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

#

### Server-Betriebssysteme:
| Betriebssystem   | Version             | Test-Ergebnis |
|:----------------:|:-------------------:|:-------------:|
| Ubuntu           | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |
| Debian           | Aktuellste Version  | ![funk](https://img.shields.io/badge/checks-passing-green) |
| Windows Server   | Aktuellste Version  | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

#

### Kompiler-Version:
| Kompiler   | Version             | Test-Ergebnis |
|:----------:|:-------------------:|:-------------:|
| Python     | 3.9                 | ![funk](https://img.shields.io/badge/checks-passing-green) |
| Python     | 3.10                | ![funk](https://img.shields.io/badge/checks-passing-green) |
| Python     | Aktuellste Version   | ![funk_n](https://img.shields.io/badge/checks-not%20tested-red) |

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

#

### Verwendete Bibliotheken:
| Bibliothek  | Version             | Test-Ergebnis |
|:-----------:|:-------------------:|:-------------:|
| random      | Aktuellste Version  | ![funk](https://img.shields.io/badge/checks-passing-green) |
| requests    | Aktuellste Version  | ![funk](https://img.shields.io/badge/checks-passing-green) |
| datetime    | Aktuellste Version  | ![funk](https://img.shields.io/badge/checks-passing-green) |
| pycord      | Aktuellste Version  | ![funk](https://img.shields.io/badge/checks-passing-green) |
| asyncio     | Aktuellste Version  | ![funk](https://img.shields.io/badge/checks-passing-green) |

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

## Lizenz:

Die Lizenz zur weiteren Verwendung dieses Projekts wird durch das **Creative Commons**-Modell festgelegt. 
Sollte eine Nutzung des Projekts in einer Weise erfolgen, die nicht durch die unten aufgeführten Piktogramme oder diese Lizenz gedeckt ist, muss vor der Nutzung des Projekts die Zustimmung eingeholt werden.

| Verwendet | Piktogramm | Bezeichnung | Verlinkung |
|:---:|:---:|:---:|:---:|
| :x: | ![Lizenz_eins](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png) | Namensnennung 4.0 International | [Details](https://creativecommons.org/licenses/by/4.0/legalcode.de) |
| :x: | ![Lizenz_zwei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png) | Namensnennung-Share Alike 4.0 International | [Details](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de) |
| :x: | ![Lizenz_drei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nd.png) | Namensnennung-Keine Bearbeitungen 4.0 International | [Details](https://creativecommons.org/licenses/by-nd/4.0/legalcode.de) |
| :x: | ![Lizenz_vier](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.eu.png) | Namensnennung-Nicht kommerziell 4.0 International | [Details](https://creativecommons.org/licenses/by-nc/4.0/legalcode.de) |
| :heavy_check_mark: | ![Lizenz_fünf](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.eu.png) | Namensnennung-Nicht kommerziell-Share Alike 4.0 International | [Details](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.de) |
| :x: | ![Lizenz_sechs](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-nd.eu.png) | Namensnennung-Nicht kommerziell-Keine Bearbeitungen 4.0 International | [Details](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.de) |

> Verwendete Lizenz: :heavy_check_mark: Nicht verwendete Lizenzen: :x:

# Mitwirkende:

clurky (Alina), Shelicus (David)
