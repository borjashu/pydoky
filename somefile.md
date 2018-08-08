{% set var = 1 %} 
{% markdown %}
# 4.8. Planungsdokumente
# 4.8.1 {% block kategorien %}{% endblock kategorien%}

{{ includeImage('abb29.jpg','Übersicht der Planunterlagenkategorien',var,parent_template_var)}} {% set var = var+1 %} 




{% if  EnableFeature(parent_template_var ,'feature_admin_element_edit') %}
{% block feature_admin_element_edit %} {% endblock feature_admin_element_edit%}
{% endif %}

{% block toeb_berechtigungen  %} {% endblock toeb_berechtigungen %}

                                           {# robob & sh & !hh #}

# Zugehörige Dokumente und zugehörige Funktionen unterhalb der Kategorie sichtbar
Jeweils unterhalb der Kategorie werden die entsprechenden zur Kategorie hochgeladenen Dokumententitel angezeigt 
und darüber hinaus, ob das Dokument freigeschaltet ist (grüner Kreis mit Häkchen) und ob Stellungnahmen zu diesen
 Dokumenten abgegeben werden können (grünes Mikro). Sollte keine Stellungnahme möglich sein, ist das Mikro-Symbol
rot und durchgestrichen.Die Funktionen lassen sich per Klick mit der Maus auf das Symbol aktivieren oder deaktivieren.

                                        {# END robob & sh & !hh #}

{{ includeImage('abb30.jpg',' Übersicht der zur Kategorie zugehörigen Dokumente und Funktionen',var,parent_template_var)}} {% set var = var+1 %} 
                                          {# robob & sh & hh #}
Die Detailansicht einer Kategorie wird über einen Klick auf den Eintrag in der Liste erreicht.

{{ includeImage('abb31.jpg',' Detailansicht Planunterlagenkategorie „Ergänzende Unterlagen“',var,parent_template_var)}} {% set var = var+1 %} 

# 4.8.2. Dokumente einer Kategorie zuordnen
 
In der Detailansicht (Abbildung 31: Detailansicht Planunterlagenkategorie) besteht in den Kategorien „FNP-Berichtigung“, 
„Ergänzende Unterlagen“, „Landschaftsplan-Änderung“, „weitere Informationen“ die Möglichkeit zum Upload von Dokumenten.
Innerhalb der Kategorien, können beliebig viele Dokumente zur Verfügung gestellt werden (z.B. verschiedene das Planverfahren 
betreffende Untersuchungen).

`Hinweis: Die Kategorien Gesamtstellungnahme, Fehlanzeige und Planzeichnung können nicht mit Dokumenten versehen werden. `

Um Dokumente neu anzulegen, klicken Sie in der Detailansicht einer Kategorie unten auf der Seite auf den Button „Neu“ 
(Abbildung 31: Detailansicht Planunterlagenkategorie). Es öffnet sich eine neue Ansicht. (Abbildung 32).

{{ includeImage('abb32.jpg',' Neuanlegen einer Planunterlage',var,parent_template_var)}} {% set var = var+1 %} 

Die Ansicht zum Anlegen eines Dokumentes (Abbildung 32) enthält folgende Felder:

* Textfeld zur Eingabe der Überschrift (d.h. eine Bezeichnung), die für den TöB erscheint
* Auswahlfeld: Stellungnahme möglich – „Ja“ oder „Nein“. Die Option „Ja“ ermöglicht die Abgabe einer Stellungnahme 
    zum ausgewählten Dokument. Für TöB und angemeldete Bürger erscheint unterhalb des Dokuments ein Button „neue Stellungnahme“
* Datei-Upload-Feld zum Hochladen des Planungsdokumentes im PDF-Format: Mit einem Klick auf „Durchsuchen“ kann das Dokument 
    ausgewählt werden. Der Pfad erscheint im Textfeld
    
Die Angaben werden mit Klick auf den Button „Speichern“ übernommen.

{{ includeImage('abb33.jpg',' Hinzugefügtes PDF erscheint in der Detailansicht der Kategorie',var,parent_template_var)}} {% set var = var+1 %} 

Das neu angelegte Dokument erscheint in der Listenansicht innerhalb der zuvor ausgewählten Kategorie 
sowie im Frontend in der jeweiligen Kategorie unter Planungsdokumente (33).

Die Dokumente werden den TöB in der jeweiligen Kategorie anschließend zur Ansicht und 
Download oder auch zur Abgabe einer Stellungnahme angeboten (Abbildung 34). 

{{ includeImage('abb34.jpg',' Ansicht der Planungsdokumentekategorien in der Bürgerebene',var,parent_template_var)}} {% set var = var+1 %} 

# 4.8.3.  Dokumente bearbeiten

Um ein (oder mehrere) Dokumente zu löschen, werden sie in der Listenansicht mit einem Klick auf die Checkbox markiert 
(Abbildung 31: Detailansicht Planunterlagenkategorie) und durch die Auswahl des Buttons „Löschen“ von der Liste entfernt.

`Hinweis: Die Planunterlagenkategorien können weder neu angelegt noch gelöscht werden. Hintergrund: mit den vordefinierten
 Kategorien wird in Schleswig-Holstein eine Einheitlichkeit über alle Verfahren hinweg hergestellt. Somit können sich die 
 Beteiligten besser zurechtfinden und werden nicht bei jedem Verfahren mit neuen Kategorien konfrontiert.`
 
                                                {#END robob & sh & hh #}
                                                
# 4.9. Begründung und Textliche Festsetzung

{% block Begründung_hinweis%} {% endblock Begründung_hinweis%}
												
												 {# robob & sh & hh #}
												  {#move Textliche Festsetzung because !hh (?) #}
{{ includeImage('abb35.jpg',' Begründung und Textliche Festsetzung als Bestandteil der Planungsdokumente',var,parent_template_var)}} {% set var = var+1 %} 

Im Gegensatz zu den anderen Kategorien kann bei Textlicher Festsetzung und Begründung ein formatiertes Dokument für eine 
absatzbezogene Darstellung sowie ein PDF Dokument hochgeladen werden. Die Abätze und das PDF Dokument werden den TöB und angemeldeten 
Bürgern sowie unangemeldeten Besuchern in der Bürgerebene angezeigt.

{{ includeImage('abb36.jpg','Fachplaner-Ansicht der Überschriften der Begründung',var,parent_template_var)}} {% set var = var+1 %} 

Wurde eine Textliche Festsetzungen hochgeladen, ist sie für TöB im Menü „Planungsdokumente“, Untermenü „Textliche Festsetzungen“
 vorzufinden (Abbildung 32).

{{ includeImage('abb37.jpg','Textliche Festsetzungen absatzbezogen in der Beteiligungsebene (TöB & Bürger)',var,parent_template_var)}} {% set var = var+1 %} 

# 4.9.1. Dokument für den Import vorbereiten (Word-HTML oder Docx)

#HTML-Dokument
Sie haben die Möglichkeit, die Absätze automatisch einzupflegen, indem sie diese aus einer gefilterten Word-HTML-Datei importieren. 
Beachten Sie für die Erstellung des Dokuments für die Textliche Festsetzungen bitte das folgende Vorgehen:

* Das Dokument muss unter Microsoft Word im Format „Webseite, gefiltert (*.html; *.htm)“ abgespeichert werden. Wenn Sie ein 
Word-Dokument öffnen, können Sie über „Speichern unter“ das Format auswählen.
* Wurden im Word-Dokument Formatvorlagen zur Definition von Gliederungsebenen verwendet, dann werden diese von der Importer-Software in BOB-SH erkannt und angelegt. Die Gliederungsebenen werden über die Standard-Formatvorlage „Überschrift“ in Word definiert (Abbildung 38: Dokument für den Import vorbereiten).
* Eine Nummerierung der Gliederungsebenen muss manuell vorgenommen werden.
* Die Software unterstützt den Import von Tabellen. Diese werden aus der Word-Datei automatisch in die Absätze eingebunden. 

{{ includeImage('abb38.jpg','Dokument für den Import vorbereiten',var,parent_template_var)}} {% set var = var+1 %} 

# Docx-Dokument für den Import vorbereiten

Seit Release 2.1 kann das absatzbezogene Dokument als zusätzliche Möglichkeit auch als Docx-Format erstellen und hochgeladen werden. 
Beachten Sie für die Erstellung des Dokuments für die Textliche Festsetzungen bitte das folgende Vorgehen:

* Stellen Sie eine Kopie Ihres Originaldokumentes her, dass Sie anschließend wie folgt neu formatieren
* Erhalten Sie die Überschriftsformatierungen bei den Bereichen, die als Absatz mit eigenem Stellungnahmebutton dargestellt werden sollen. Wenn Sie nicht möchten, dass jedes Unterkapitel einen eigenen Absatz darstellen soll, entfernen Sie die Formatierung der entsprechenden Kapitelüberschriften.
* Das Dokument muss unter Microsoft Word im Format Docx abgespeichert werden. Wenn Sie ein Word-Dokument öffnen, können Sie über „Speichern unter“ das Format auswählen.

`Hinweis: über das Docx-Format können auch Bilder, Tabellen, Fußnoten, Sonderzeichen und Kopfzeilen importiert werden`

# 4.9.2.  Absätze in Begründung/Textlicher Festsetzung hochladen/ importieren

Um die Begründung zu importieren, klicken Sie den Button „Datei zum Upload auswählen“ (Nr. 1 in Abbildung 39). Es öffnet sich
 ein neues Fenster. Wählen Sie das zu importierende Word-HTML- oder Docx-Dokument über die Ordnerstruktur aus. 
Über den Button „Öffnen“ bestätigen Sie die Dokumentenauswahl. (Nr. 2 in Abbildung 39)

{{ includeImage('abb39.jpg','Import der Textlichen Festsetzungen als Word XML- oder Docx-Dokument',var,parent_template_var)}} {% set var = var+1 %} 


Um das Dokument zu importieren, müssen Sie nun nur noch auf den Button „Hochladen beginnen“ klicken und anschließend speichern. (Nr. 3 in Abbildung 39)
Nach erfolgreichem Import werden die Absätze Ihrer Textlichen Festsetzungen in der Listenansicht angezeigt.

#  4.9.3.  Absatz in Begründung /Textlicher Festsetzung neu anlegen

Im Regelfall werden Sie die Dokumente über die Import-Funktion einpflegen. Zusätzlich besteht die Möglichkeit, einzelne Absätze manuell anzulegen.
Über den Klick auf den Button „Neuen Absatz anlegen“ legen Sie einen neuen Absatz in der Begründung oder Textlichen Festsetzungen an.

{{ includeImage('abb40.jpg','Manuelles Anlegen eines Absatzes',var,parent_template_var)}} {% set var = var+1 %} 

Durch den Klick auf den Button „Neuen Absatz anlegen“ (Abbildung 40) öffnet sich eine neue Ansicht (Abbildung 41) über die ein 
Absatz manuell hinzugefügt werden kann.

`Hinweis: Diese Vorgehensweise wird jedoch nicht empfohlen, da dann das hochgeladene 
Original-Dokument in seiner Struktur verändert wird. Es kann jedoch Situationen geben, in welchen die Funktion weiterhelfen kann.`

* Gliederung, wird mit der Nummerierung ausgefüllt
* Absatzüberschrift, beinhaltet die eigentliche Überschrift
* Gliederung und Absatzüberschrift bündelt den Inhalt der bei Gliederung und Absatzüberschrift eingetragen wurde.
* Absatztext: Hier wird der Text des Absatzes eingetragen. Sie können den Text aus einer anderen Anwendung herauskopieren.
* Textfeld zur Eingabe einer Artikel-ID (vorheriger Absatz) (derzeit nicht relevant)
* Textfeld zur Eingabe einer Artikel-ID (nächster Absatz) (derzeit nicht relevant)
* Textfeld zur Eingabe der Absatzreihenfolge 
Nachdem Sie Ihre Eingabe vorgenommen haben, gelangen Sie durch den Speichern-Button wieder auf die Übersichtsseite und sehen dort den hinzugefügten Absatz.

#  4.9.4.  Absatz in Begründung/Textlichen Festsetzungen bearbeiten

Ein Klick auf den Namen eines Absatzes öffnet eine neue Ansicht, mit der Möglichkeit, Änderungen vorzunehmen. 
Mit einem Klick auf den Button „Speichern“, werden die Änderungen gesichert. 

`Hinweis: seit Release 2.7 können in absatzbezogen dargestellten Dokumenten mit dem Editor Querverweise erstellt werden. Links können 
innerhalb von Planungsdokumentabsätzen mithilfe eines TinyMCE Plug-Ins gesetzt werden. Im Absatz ist ein Textfeld vorhanden, 
in dem der Absatztext bearbeitet werden kann. Dort wurde das Plug-In zum Linkanlegen in der Kopfleiste des Texteditors rechts außen hinzugefügt. 
Man muss zunächst einen Teil des Textes markieren und danach das Link-Plug-In auswählen. Die URL, auf die verwiesen werden soll, kann in dem 
sich öffnenden Fenster hinterlegt werden.`

{{ includeImage('abb41.jpg','Verlinkungsfunktion bei Absatz bearbeiten',var,parent_template_var)}} {% set var = var+1 %} 

Verwiesen werden kann damit auf alles, dass über eine URL verfügt - z.B. andere BOB-Dokumente, Kapitel von BOB-Dokumenten, BOB-Verfahren 
oder andere Webseiten. Um auf Kapitel des gleichen oder anderen Dokuments in BOB zu verweisen, müssen diese Dokumente in der Beteiligungsansicht
aufgerufen werden. Mit Klick auf die entsprechenden Kapitel im Inhaltsverzeichnis wird eine URL generiert, die in der Browserleiste angezeigt wird.
Diese URL muss kopiert und als URL im Link-Plug-In hinterlegt werden.

# 4.9.5.  Absatz aus Begründung/Textlichen Festsetzungen löschen

Um einen Absatz zu löschen, markieren Sie den zu löschenden Absatz mit einem Klick auf die Checkbox vor dem Absatz.

{{ includeImage('abb42.jpg','Löschen eines Absatzes aus der Textlichen Festsetzungen',var,parent_template_var)}} {% set var = var+1 %} 

Nachdem der Absatz markiert wurde, klicken Sie auf den Button „Löschen“. Der Absatz wird aus der Liste entfernt. 
Das System gibt eine Fehlermeldung aus, wenn der Button „Löschen“ geklickt wird, ohne dass vorher ein Absatz ausgewählt wurde.

#  4.9.6.  PDF-Version der Begründung/ Textlichen Festsetzungen hochladen

Das PDF-Dokument der Begründung/Textlichen Festsetzungen kann ebenfalls hier hochgeladen werden. Klicken Sie auf den Button „PDF zum Upload auswählen“
und wählen Sie anschließend das Dokument aus. Anschließend muss der Button „hochladen beginnen“ betätigt werden und nach dem erfolgreichen Upload
gespeichert werden.

{{ includeImage('abb43.jpg','Upload der PDF-Version',var,parent_template_var)}} {% set var = var+1 %} 

#  4.10. Konfiguration GIS-Layer, Planzeichnung, Geltungsbereich, Planzeichenerklärung, PDF-Version, Planstand

Die GIS-Layer und Einstellungen im Menü „Planzeichnung“ steuern die interaktive Karten-Anwendung mit Karten und Planzeichnung, die den TöB und der 
Öffentlichkeit angezeigt wird.

{{ includeImage('abb44.jpg','Planzeichnung: Anzeige der verfügbaren Karten-Layer, Kartenausschnitt, Geltungsbereich, Planzeichenerklärung, PDF-Planzeichnung, Planstand',var,parent_template_var)}} {% set var = var+1 %} 
												 {# robob & sh & hh #}
#  4.10.1.  Neuen GIS-Layer anlegen

Über den Button „Neuen GIS-Layer anlegen“ erscheint eine neue Ansicht, die folgende Felder enthält:

* Radio-Button WMS: Hier kann zwischen verschiedenen Arten von WMS gewählt werden.

`Hinweis: Die Felder Typ und Startkarte werden ja nach gewähltem WMS bereits vorbelegt.`

* Planzeichnung: Hier handelt es sich um den B-Plan. Er wird üblicherweise als Overlay angelegt. Es ist jedoch denkbar, dass der Plan mit einer
 Grundkarte verbunden ist, dann kann hier auch die Einstellung Grundkarte sinnvoll sein. Die Auswahl des Radio-Buttons „Planzeichnung“ bewirkt,
  dass der WMS-Layer über den Button in der Karte auf der Verfahrensseite in der Bürgerebene ein- und ausgeblendet werden kann.
* X-Plan: hier können spezielle XPlanlayer eingefügt werden. Das Formular eröffnet eine zusätzliche Funktion "Nutze die vordefinierten Standard
 XPlan-Layer", die per Häkchensetzung aktiviert werden kann.
* Der Geltungsbereich ist der Umriss des Plans. Er ist fix als Overlay definiert. Die Auswahl bewirkt, dass der Geltungsbereich über den Button 
in der Karte auf Verfahrensseiten in der Bürgerebene ein- und ausgeblendet werden kann.
* Grundkarte: Soll eine weitere Grundkarte, zusätzlich zu den bereits verfügbaren, hinterlegt werden, wird diese Option gewählt.
* Overlay: Die Option wird für Layer gewählt, die nicht Planzeichnung oder Geltungsbereich sind, aber dennoch als Overlay hinterlegt und variabel
 über der Grundkarte zuschaltbar sein sollen.
* Name definiert den Namen des Layers, der in der Karte in der Layerauswahl angezeigt wird. 

`Hinweis: Der Name sollte nicht zu lang gewählt werden.`

* URL: Hier steht die Adresse des Kartendienstes, d.h. die Internetadresse des WMS (Web Map Service). Der WMS kann durch das Geodatenuploadportal
 von Dataport oder andere GIS Anwendung erzeugt und gehostet werden.
* Layer: Dies sind die Layer-Namen des WMS-Dienstes, die im Geodatenuploadportal mitgeteilt werden. Layer-Namen werden durch Semikolon getrennt.
* Typ: Hier kann bestimmt werden, ob die Karte als Grundkarte oder als Overlay dargestellt wird. Möglicherweise liegt eine Vorbelegung vor (siehe oben).
* Checkbox Druck-Layer: Die ausgewählten Druck-Layer werden in den Screenshots der Einzeichnungen in den Stellungnahmelisten angezeigt. Es sollte 
nur eine nicht transparente Karte (Grundkarte) ausgewählt sein. Für transparente Karten (B-Pläne) gilt, dass zwar mehrere ausgewählt sein können,
die Lesbarkeit der Karte aber in den Druckansichten geprüft werden sollte. Ist kein Druck-Layer definiert oder wird der entsprechende Layer gelöscht,
 wird automatisch der WebAtlas für den Druck angezogen.
* Checkbox Startkarte: Hierüber kann ausgewählt werden, welche Karte standardmäßig beim Aufruf der Planzeichnung angezeigt wird. Die Einstellung 
gilt für den TöB-Bereich, für angemeldete Bürger und in der Bürgerebene.
* Sichtbar: Hierüber kann der Layer aus oder eingeblendet werden und ist entsprechend für TöB und Öffentlichkeit verfügbar oder nicht.
Nach dem Speichern der Einträge, erscheint die Karte in der Liste der GIS-Layer (Abbildung 44: Planzeichnung: Anzeige der verfügbaren Karten-Layer).

{% block img45 %} {% endblock %}

{% block img46 %} {% endblock %}

# 4.7.1.1 Einträge bearbeiten
Veränderungen eines GIS-Layers können in der Detailansicht (Abbildung 45) vorgenommen werden, die mit einem Klick auf die Überschrift aufgerufen 
wird. Nach dem Speichern werden die Änderungen übernommen.
# 4.7.1.2 Einträge löschen
Um einen GIS-Layer zu entfernen, markieren sie den entsprechenden Eintrag in der Übersicht mit einem Klick auf die Checkbox und klicken
Sie anschließend auf „Löschen“.
# 4.7.1.3 Kartenausschnitt definieren
Über den Link „Kartenausschnitt definieren“ (Abbildung 47: ) werden folgende Einstellungen vorgenommen:

* „Startausschnitt“ definiert, an welcher Stelle der sichtbare Ausschnitt der Karte ausgerichtet wird, wenn TöB und Öffentlichkeit die 
Planzeichnung aufrufen.Der Startkartenausschnitt kann über die abgebildete Karte mit dem Zoom-Fenster oder über Doppelklick ausgewählt werden.
Mit dem Klick auf „Startkartenausschnitt übernehmen“ werden die Koordinaten in das vorgesehene Feld übertragen und angezeigt. Wichtig ist 
die Bestätigung über den Klick auf „Speichern“
* Bounds (auch Bounding Box) definieren die Grenzen der sichtbaren Karte.

`Hinweis: Es wird empfohlen, die Bounds auf Schleswig-Holstein zu setzen. Wenn die Bounds nicht den Startkartenausschnitt enthalten, wir der 
TöB keine Karte sehen. `

* Sachdaten-URL: Sachdaten sind textuelle Informationen die über den gleichnamigen Button in der interaktiven Planzeichnung angezeigt werden. 
Sichern Sie die Konfiguration mit einem Klick auf „Speichern“.

{% block img47 %} {% endblock %}

Für TöB/Bürger ist die Karte unter dem Reiter „Interaktive Karte“ einsehbar:

{% block img48 %} {% endblock %}

#  4.10.2. Geltungsbereich als WMS

Der Geltungsbereich stellt den äußeren Rand des Planes dar. Er enthält abgesehenen von der abgrenzenden Linie keine Informationen
(im Gegensatz zur Planzeichnung) und soll auf einen Blick anzeigen, ob ein bestimmter Bereich (z.B. das Grundstück eines Anwohners) innerhalb
des überplanten Gebietes liegt.
Entsprechend dem in Kap. 4.6.2 beschriebenen Vorgehen kann der Geltungsbereich als WMS hinterlegt werden. Dazu wird der entsprechende Layer 
im Dropdown „Geltungsbereich“ auf „ja“ geschaltet. 

`Hinweis: Bei der Produktion des B-Plans als WMS kann der Geltungsbereich ohne großen Aufwand mit erstellt werden.`

#  4.10.3.  Geltungsbereich zeichnen

Alternativ zum WMS kann der Geltungsbereich eingezeichnet werden. Wählen Sie dazu „Geltungsbereich zeichnen“. Eine Karte wird geladen mit dem 
Ausschnitt der Planzeichnung, sofern diese hinterlegt wurde. Über ein Zeichenwerkzeug kann der Geltungsbereich (Umrandung des Planes) eingezeichnet 
werden. Nach „Speichern“ ist der Geltungsbereich in der Planzeichnung in der Bürgerebene hinterlegt und kann dort ein- und ausgeblendet werden.

`Hinweis: Der Geltungsbereich kann über „Geltungsbereich löschen“ entfernt und anschließend neu gezeichnet werden.`

`Hinweis: Ist sowohl ein WMS als Geltungsbereich definiert, als auch ein Geltungsbereich eingezeichnet, wird der WMS in der Bürgerebene
angezeigt, der eingezeichnete Geltungsbereich hingegen ignoriert.`

`Hinweis: Bei der Einzeichnung des Geltungsbereichs muss darauf geachtet werden, dass präzise gearbeitet wird. Selbst kleine Abweichungen können
 die Aussage verfälschen (z.B. bei der Frage, ob ein Grundstück innerhalb des überplanten Bereichs liegt oder nicht.`
 
# 4.10.4.  Planzeichnung im PDF-Format

Die Planzeichnung kann über „Planzeichnung“ als PDF-Dokument hochgeladen werden. Das sich öffnende Formular enthält ein Uploadfeld zum Hochladen 
der Planzeichnung. Mit einem Klick auf den Button „Durchsuchen wählen Sie das Dokument aus und bestätigen über den Button „OK. Es wird der Pfad
zum Dokument angezeigt. Mit einem Klick auf „Speichern“ sichern Sie die Auswahl und das Dokument wird auf die Plattform geladen.

# 4.10.5.  Planzeichenerklärung

Die Planzeichenerklärung kann über „Planzeichnung“ als PDF-Dokument hochgeladen werden. Das sich öffnende Formular enthält ein Uploadfeld zum
Hochladen der Planzeichenerklärung. Mit einem Klick auf den Button „Durchsuchen“ wählen Sie das Dokument aus und bestätigen über den Button „OK. 
Es wird der Pfad zum Dokument angezeigt. Mit einem Klick auf „Speichern“ sichern Sie die Auswahl und das Dokument wird auf die Plattform geladen.

# 4.10.6.  Planstand

Der Planstand wird als Datum eingegeben. Die Anzeige erscheint für TöB in den Ansichten „Textliche Festsetzungen“ und „Begründung“ in den Boxen am 
oberen Ende der Seite.


{% endmarkdown %}

