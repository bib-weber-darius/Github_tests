from datetime import datetime
daten = [ [ "Meier", "Arnold", "M", datetime(1992,7,6), "Brüssel", 72.4, 83.2] ,
[ "Nelles", "Marita", "W", datetime(2001,4,12), "Malmedy", 62.5 , 73.2],
[ "Kalles", "Norbert", "M", datetime(1980,11,12), "Eupen", 83.2, 70.9],
[ "Trantes", "Karl-Heinz", "M", datetime(1974,2,28), "Sankt Vith", 65.3, 52.4],
[ "Müller", "Verena", "W", datetime(1982,12,24), "Eupen", 71.3, 62.5],
[ "Weynand", "Karla", "W", datetime(1988,5,5), "Lüttich", 67.7, 70.0]
]

for nachname,vorname,geschlecht,geburtdt,geburtsort,gewicht,resultat in daten:
    "{nachname} {vorname} {geschlecht} {geburtdt} {geburtsort} {gewicht} {resultat}".format(nachname1=nachname,vorname1=vorname,geschlecht1=geschlecht,geburtdt1=geburtdt,geburstort1=geburtsort,gewicht1=gewicht,resultat=resultat )