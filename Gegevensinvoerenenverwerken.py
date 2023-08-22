import json
import datetime
import csv
import os

def integerControleren(String): #controleert of van een string een integer gemaakt kan worden returnt true als het kan en false als het niet kan.
    try:
        int(String)
        return True
    except ValueError:
        print("Voer een integer in.")
        return False

def puntenControleren(Punten): # controleert of van invoer een integer gemaakt kan worden en vraagt opnieuw om een invoer als dat niet kan.
    Controle = integerControleren(Punten)
    Punten = opnieuwInvoeren(Controle, Punten)
    return str(Punten)

def isInvoerCorrect(Tekens): #controleert of van een string een integer gemaakt kan worden returnt true als het kan en false als het niet kan.
    if str(Tekens) == "":
        return False
    for Teken in str(Tekens):
        if Teken not in "1234567890":
            return False
    return True

def opnieuwInvoeren(WaarOfNietWaar, OorspronkelijkeTekens): #Functie om opnieuw om een invoer te vragen als blijkt dat van een string geen integer gemaakt kan worden.
    if WaarOfNietWaar == False:                             #Returnt oorspronkelijke string als dat daarbij kon, of een nieuwe string waar wel een integer van gemaakt kan worden.
        while WaarOfNietWaar == False:
            Cijfers = input("Voer een correcte positieve integer in. ")
            WaarOfNietWaar = integerControleren(Cijfers)
            if WaarOfNietWaar == True:
                return str(Cijfers)
    else:
        return str(OorspronkelijkeTekens)

def gegevensInvoeren():                 #Hier worden gegevens ingevoerd, returnt een tuple met de ingevoerde gegevens
    StartTijd = datetime.datetime.now() #in deze volgorde: Naam, Geslacht, GeboorteJaar, Woonplaats, Straat, PostCode, HuisNummer, Werk, Email, TelefoonNummer, TijdIngevuld
    Goed = False
    while not Goed:
        Naam = input("Wat is uw naam?")
        Corrigeer = input("Is " + str(Naam) + " uw naam? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    Goed = False
    while not Goed:
        Geslacht = input("Wat is uw geslacht?")
        Corrigeer = input("Is " + str(Geslacht) + " uw geslacht? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    Goed = False
    while not Goed:
        GeboorteJaar = input("In welk jaar bent u geboren?")
        Corrigeer = input("Is " + str(GeboorteJaar) + " uw geboortejaar? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    Goed = False
    while not Goed:
        Woonplaats = input("Waar woont u?")
        Corrigeer = input("Is " + str(Woonplaats) + " uw woonplaats? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    Goed = False
    while not Goed:
        Straat = input("In welke straat woont u?")
        Corrigeer = input("Is " + str(Straat) + " uw straat? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    Goed = False
    while not Goed:
        PostCode = input("Wat is uw postcode?")
        Corrigeer = input("Is " + str(PostCode) + " uw postcode? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    Goed = False
    while not Goed:
        HuisNummer = input("Wat is uw huisnummer?")
        Corrigeer = input("Is " + str(HuisNummer) + " uw huisnummer? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    Goed = False
    while not Goed:
        Werk = input("Wat voor werk doet u?")
        Corrigeer = input("Is " + str(Werk) + " uw werk? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    Goed = False
    while not Goed:
        Email = input("Wat is uw e-mail adres? (Verplicht)")
        Corrigeer = input("Is " + str(Email) + " uw e-mail? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    Goed = False
    while not Goed:
        TelefoonNummer = input("Wat is uw telefoonnummer")
        Corrigeer = input("Is " + str(TelefoonNummer) + " uw telefoonnummer? (j/n) ")
        if Corrigeer in "jJ" and Corrigeer != "":
            Goed = True
        else:
            print("Voer een correcte waarde in.")

    EindTijd = datetime.datetime.now()
    TijdIngevuld = EindTijd - StartTijd
    TijdIngevuld = TijdIngevuld.total_seconds() / 60
    TijdIngevuld = round(TijdIngevuld, 2)
    return (Naam, Geslacht, GeboorteJaar, Woonplaats, Straat, PostCode, HuisNummer, Werk, Email, TelefoonNummer, TijdIngevuld)

def puntenToekennen():                                   #Deze functie is om punten in te vullen bij bepaalde data die opgehaald is. returnt een tuple met tuples met daarin wat de waarde die moet zijn
    if os.stat("Klantgegevens_JSON.JSON").st_size == 0:  #ingevuld voor de punten en het toe te kennen aantal punten voor die ingevulde waarde. de tuples in tuples zijn in deze volgorde: Geslacht, GeboorteJaar, Woonplaats, Straat, Postcode, PuntenWerk, TijdIngevuld
        return print("Er zijn geen opgeslagen gegevens.")
    PuntenGeslacht = ("", 0)
    PuntenGeboorteJaar = ("", 0)
    PuntenWoonplaats = ("", 0)
    PuntenStraat = ("", 0)
    PuntenPostcode = ("", 0)
    PuntenWerk = ("", 0)
    PuntenTijdIngevuld = ("", 0)



    Geslacht = input("Wilt u punten toekennen aan een bepaald geslacht? (j/n)")
    if Geslacht in "jJ" and Geslacht != "":
        Naam = input("Aan welk geslacht wilt u punten toekennen?")
        Punten = input("Hoeveel punten wilt u aan dit geslacht geven?")
        Punten = puntenControleren(Punten)
        PuntenGeslacht = (Naam, int(Punten))

    GeboorteJaar = input("Wilt u punten toekennen aan een bepaald geboortejaar? (j/n)")
    if GeboorteJaar in "jj" and GeboorteJaar != "":
        Naam = input("Aan welk geboortejaar wilt u punten toekennen?")
        Controle = integerControleren(Naam)
        Naam = opnieuwInvoeren(Controle, Naam)
        Punten = input("Hoeveel punten wilt u aan dit geboortejaar toekennen? (j/n)")
        Punten = puntenControleren(Punten)
        PuntenGeboorteJaar = (Naam, int(Punten))
    else:
        PuntenGeboorteJaar = ("", "0")

    Woonplaats = input("Wilt u punten toekennen aan een woonplaats? (j/n)")
    if Woonplaats in "jJ" and Woonplaats != "":
        Naam = input("Aan welke woonplaats wilt u punten toekennen?")
        Punten = input("Hoeveel punten wilt u aan deze woonplaats geven?")
        Punten = puntenControleren(Punten)
        PuntenWoonplaats = (Naam, int(Punten))


    Straat = input("Wilt u punten toekennen aan een bepaalde straat? (j/n)")
    if Straat in "jJ" and Straat != "":
        Naam = input("Aan welke straat wilt u punten toekennen?")
        Punten = input("Hoeveel punten wilt u aan deze straat geven?")
        Punten = puntenControleren(Punten)
        PuntenStraat = (Naam, int(Punten))

    Postcode = input("Wilt u punten toekennen aan een bepaalde postcode? (j/n)")
    if Postcode in "jJ" and Postcode != "":
        Naam = input("Aan welke postcode wilt u punten toekennen?")
        Punten = input("Hoeveel punten wilt u aan deze postcode geven?")
        Punten = puntenControleren(Punten)
        PuntenPostcode = (Naam, int(Punten))

    Werk = input("Wilt u punten toekennen aan een bepaald beroep? (j/n)")
    if Werk in "jJ" and Werk != "":
        Naam = input("Aan welk beroep wilt u punten toekennen?")
        Punten = input("Hoeveel punten wilt u aan dit beroep geven?")
        Punten = puntenControleren(Punten)
        PuntenWerk = (Naam, int(Punten))

    TijdBesteed = input("Wilt u punten toekennen aan hoeveel tijd is besteed aan het invullen? (j/n)")
    if TijdBesteed in "jJ" and TijdBesteed != "":
        Naam = input("Aan hoeveel tijd besteed wilt u punten geven?")

        Punten = input("Hoeveel punten wilt u aan deze tijd geven?")
        Punten = puntenControleren(Punten)
        PuntenTijdIngevuld = (Naam, int(Punten))

        #Geeft alleen nog punten aan een specifieke tijd.



    return (PuntenGeslacht, PuntenGeboorteJaar, PuntenWoonplaats, PuntenStraat, PuntenPostcode, PuntenWerk, PuntenTijdIngevuld)   #returnt een tuple met daarin waar punten aan gegeven zullen worden en de hoeveelheid punten die gegeven moeten worden in int formaat.


def puntenVerwerken(TupleMetToegekendePunten):     #Hier gaat de tuple in die is gereturnt bij puntentoekennen. De volgorde is Geslacht, GeboorteJaar, Woonplaats, Straat, Postcode, PuntenWerk, TijdIngevuld
    if os.stat("Klantgegevens_JSON.JSON").st_size == 0:  #Deze functie is om de JSON en CSV file te updaten met de gegeven punten.
        return input("Er zijn geen klantgegevens.")     #Als er geen klantgegevens zijn wordt dit gemeld en wordt het programma afgesloten.


    JsonBestand = open("Klantgegevens_JSON.JSON", "r")
    JsonBewerken = json.load(JsonBestand)
    PuntenGeslacht = 0
    PuntenGeboorteJaar= 0
    PuntenWoonplaats = 0
    PuntenStraat = 0
    PuntenPostcode = 0
    PuntenWerk = 0
    PuntenDuratie = 0

    for Sleutel in JsonBewerken:      #hier wordt elke key gecontroleert in de json file
        JsonBewerken[Sleutel]["Punten"] = 0
        if JsonBewerken[Sleutel]["Geslacht"] == TupleMetToegekendePunten[0][0]:                                # Hier wordt gekeken of de waarde bij geslacht hetzelfde is als wat hier is ingevuld bij punten toekennen(geslacht is de 0e index van tuple met toegekende punten
            JsonBewerken[Sleutel]["Punten"] = JsonBewerken[Sleutel]["Punten"] + TupleMetToegekendePunten[0][1]  # en het gekozen geslacht is de 0de index van de tuple in de tuple, en het aantal toegekende punten aan het gekozen geslacht staat in de 1e index van de tuple in de tuple.
            PuntenGeslacht = TupleMetToegekendePunten[0][1]

        if JsonBewerken[Sleutel]["Geboortejaar"] == TupleMetToegekendePunten[1][0]:
            JsonBewerken[Sleutel]["Punten"] = JsonBewerken[Sleutel]["Punten"] + TupleMetToegekendePunten[1][1]
            PuntenGeboorteJaar = TupleMetToegekendePunten[1][1]

        if JsonBewerken[Sleutel]["Woonplaats"] == TupleMetToegekendePunten[2][0]:
            JsonBewerken[Sleutel]["Punten"] = JsonBewerken[Sleutel]["Punten"] + TupleMetToegekendePunten[2][1]
            PuntenWoonplaats = TupleMetToegekendePunten[2][1]

        if JsonBewerken[Sleutel]["Straat"] == TupleMetToegekendePunten[3][0]:
            JsonBewerken[Sleutel]["Punten"] = JsonBewerken[Sleutel]["Punten"] + TupleMetToegekendePunten[3][1]
            PuntenStraat = TupleMetToegekendePunten[3][1]

        if JsonBewerken[Sleutel]["Postcode"] == TupleMetToegekendePunten[4][0]:
            JsonBewerken[Sleutel]["Punten"] = JsonBewerken[Sleutel]["Punten"] + TupleMetToegekendePunten[4][1]
            PuntenPostcode = TupleMetToegekendePunten[4][1]

        if JsonBewerken[Sleutel]["Werk"] == TupleMetToegekendePunten[5][0]:
            JsonBewerken[Sleutel]["Punten"] = JsonBewerken[Sleutel]["Punten"] + TupleMetToegekendePunten[5][1]
            PuntenWerk = TupleMetToegekendePunten[5][1]

        if JsonBewerken[Sleutel]["Duratie invullen(minuten)"] == TupleMetToegekendePunten[6][0]:
            JsonBewerken[Sleutel]["Punten"] = JsonBewerken[Sleutel]["Punten"] + TupleMetToegekendePunten[7][1]
            PuntenDuratie = TupleMetToegekendePunten[6][1]


    JsonMaken = json.dumps(JsonBewerken, indent=10)  #hierin wordt de waarde die de variabele Jsonbewerken bezit omgezet naar JSON notatie.
    JsonBestand = open("Klantgegevens_JSON.JSON", "w")
    JsonBestand.truncate(0)
    JsonBestand.write(JsonMaken)                         #Hier wordt het hele JSON bestand verwijdert en wordt de geupdate informatie opgeschreven.
    JsonBestand.close()

    CsvBestand = open("Klantgegevens_CSV.CSV", "r")
    RegelsCsvBestand = CsvBestand.readlines()
    CsvBestand.close()
    VeldNamen = "Klantnummer;Naam;Geslacht;Geboortejaar;Woonplaats;Straat;Postcode;Huisnummer;Werk;E-mail;Telefoonnummer;Duratie invullen(minuten);Punten\n"
    CsvBestand = open("Klantgegevens_CSV.CSV", "w")
    CsvBestand.truncate(0)
    CsvBestand.write(VeldNamen)
    CsvBestand.close()
    CsvBestand = open("Klantgegevens_CSV.CSV", "a")
    Json = open("Klantgegevens_JSON.JSON", "r")

    JsonInhoud = json.load(Json)  #via de JSON file worden de punten van het csv bestand genoteerd.
    for Sleutel in JsonInhoud:
        CsvBestand.write(str(Sleutel) + ";" + str(JsonInhoud[Sleutel]["Naam"]) + ";" + str(JsonInhoud[Sleutel]["Geslacht"]) + ";" + str(JsonInhoud[Sleutel]["Geboortejaar"]) + ";" + str(JsonInhoud[Sleutel]["Woonplaats"]) + ";" + str(JsonInhoud[Sleutel]["Straat"]) + ";" + str(JsonInhoud[Sleutel]["Postcode"]) + ";" + str(JsonInhoud[Sleutel]["Huisnummer"]) + ";" + str(JsonInhoud[Sleutel]["Werk"]) + ";" + str(JsonInhoud[Sleutel]["Email"]) + ";" + str(JsonInhoud[Sleutel]["Telefoonnummer"]) + ";" + str(JsonInhoud[Sleutel]["Duratie invullen(minuten)"]) + ";" + str(JsonInhoud[Sleutel]["Punten"]) + "\n")
    CsvBestand.close()
    Json.close()


def testJsonFile(): #Dit is om te testen of de JSON file aanwezig is.
    try:
        bestand = open("Klantgegevens_JSON.JSON", "x")
        bestand.close()
    except:
        ""


def gegevensVerwerkenNaarJson(TupleMetKlantGegevens):#Deze functie is om de ingevoerde gegevens te verwerken en op te slaan in JSON format
    #De tuple moet hieruit bestaan in de volgorde zoals het genoteerd is: Naam, Geslacht, GeboorteJaar, Woonplaats, Straat, PostCode, HuisNummer, Werk, Email, TelefoonNummer#

    #OpslagKlantGegevens = open("Klantgegevens JSON.txt", "a")
    if len(TupleMetKlantGegevens) != 11:
        return "De tuple is te kort"
    VorigKlantNummer = open("Huidig klantnummer.txt", "r+")
    InhoudBestand = VorigKlantNummer.readline()



    Teller = int(InhoudBestand)
    VorigKlantNummer = VorigKlantNummer.close()
    VorigKlantNummer = open("Huidig klantnummer.txt", "w")

    VorigKlantNummerUpdate = VorigKlantNummer.write(str(Teller + 1))
    VorigKlantNummer = VorigKlantNummer.close()
    KlantGegevens = {str(Teller) : {"Naam" : TupleMetKlantGegevens[0], "Geslacht" : TupleMetKlantGegevens[1], "Geboortejaar" : TupleMetKlantGegevens[2], "Woonplaats" : TupleMetKlantGegevens[3], "Straat" : TupleMetKlantGegevens[4], "Postcode" : TupleMetKlantGegevens[5], "Huisnummer" : TupleMetKlantGegevens[6], "Werk" : TupleMetKlantGegevens[7], "Email" : TupleMetKlantGegevens[8], "Telefoonnummer" : TupleMetKlantGegevens[9], "Duratie invullen(minuten)" : TupleMetKlantGegevens[10], "Punten" : 0 }}
    OmzettenNaarJsonFormat = json.dumps(KlantGegevens, indent=10)
    if os.stat("Klantgegevens_JSON.JSON").st_size != 0:#Dit is om nieuwe waardes op de juiste manier in het JSON bestand te schrijven. het enige moment dat dit op een andere manier moet is als het de eerste gegevens zijn die geschreven worden in het bestand.
        Formatcorrigeren = OmzettenNaarJsonFormat[1:]#De eerste accolade moet weg
        with open("Klantgegevens_JSON.JSON", "rb+") as Bestand:
            Bestand.seek(-3, os.SEEK_END)#Dit is om de laatste accolade en /n te verwijderen.
            Bestand.truncate()
            Bestand.close()
        Bestand = open("Klantgegevens_JSON.JSON", "a")
        Bestand.write(",\n" + str(Formatcorrigeren)) #hier wordt eerst een , en /n toegevoegd aan het document en dan wordt de informatie geschreven.
        Bestand.close()
        return "De extra gegevens zijn opgeslagen"

    else:#Als het het eerste opgeslagen gegeven is kan het zonder iets extra's te doen in het JSON document geschreven worden.
        OpslagKlantGegevens = open("Klantgegevens_JSON.JSON", "a")
        OpslagKlantGegevens.write(OmzettenNaarJsonFormat)
        OpslagKlantGegevens.close()
        return "Dit was het eerste gegeven"



def startMenu():  #in dit menu kunje kiezen om een klant een formulier in te laten vullen of om punten toe te kennen. Maakt ook de benodigde files aan als die er niet zijn
    testJsonFile()#en test of het klantnummer goed is.
    testCsv()
    testKlantNummer()
    KlantTest = open("Huidig klantnummer.txt", "r")
    Regel = KlantTest.readline()
    Controle = integerControleren(Regel)
    testJsonKlantNummer(Controle, KlantTest)
    Keuze = input("Wilt u een klant een formulier laten invullen? (1)\n"
                  "Wilt u punten toekennen aan bepaalde gegeven waardes? (2)\n")
    while Keuze != "1" and Keuze != "2":
        Keuze = input("Voer een correcte keuze in (1 voor invulformulier, 2 voor punten toekennen. ")


    if Keuze == "1":
                GegevensInvoeren = gegevensInvoerenEnVerwerken()
    elif Keuze == "2":
                PuntenToekennen = puntenToekennen()
                PuntenVerwerken = puntenVerwerken(PuntenToekennen)


def testJsonKlantNummer(Controle, KlantTest):#Deze functie is om te testen of het klantnummer correct is. om ervoor te zorgen dat er geen dubbele keys zijn
    if os.stat("Klantgegevens_JSON.JSON").st_size == 0:
        CSV = open("Klantgegevens_CSV.CSV", "w")
        CSV.truncate(0)
        if Controle == False:
            KlantTest.close()
            KlantTest = open("Huidig klantnummer.txt", "w")
            KlantTest.write("1")
            KlantTest.close()
    else:
        Json = open("Klantgegevens_JSON.JSON")
        JsonBewerken = json.load(Json)
        SleutelLijst = []
        for Sleutel in JsonBewerken:
            SleutelLijst.append(Sleutel)
        KlantTest.close()
        KlantTest = open("Huidig klantnummer.txt", "w")
        KlantTest.write(str(int(SleutelLijst[len(SleutelLijst) - 1]) + 1))
        KlantTest.close()


def gegevensInvoerenEnVerwerken():#Deze functie vraagt om gegevens in te vullen en schrijft de gegevens daarna naar JSON en CSV.
    invoer = gegevensInvoeren()
    CsvNoteren = schrijfNaarCSV(invoer)
    noteren = gegevensVerwerkenNaarJson(invoer)

def testCsv():#Deze functie maakt het klantgegevens.csv bestand aan als het er nog niet is.
    try:
        Bestand = open("Klantgegevens_CSV.CSV", "x")
    except:
        "Bestand bestaat al"

def testKlantNummer():#Deze functie maakt een nieuw klantnummer bestand aan en schrijft er 1 in als het er nog niet is.
    try:
        Bestand = open("Huidig klantnummer.txt", "x")
        Bestand.close()
        Bestand = open("Huidig klantnummer.txt", "w")
        Bestand.write("1")
        Bestand.close()
    except:
        "Bestand bestaat al"




def schrijfNaarCSV(TupleMetKlantGegevens):#Deze functie schrijft de klantgegevens in een csv file door eerst de veldnamen en /n te schrijven en daarna wordt er een lijst met de klantgegevens geschreven en worden daarbij alle onnodige tekens verwijderd
    if len(TupleMetKlantGegevens) != 11:
        return "De tuple is te kort"
    OpslagKlantGegevens = open("Klantgegevens_CSV.CSV", "a")
    VeldNamen = ["Klantnummer","Naam","Geslacht","Geboortejaar","Woonplaats","Straat","Postcode","Huisnummer","Werk" ,"E-mail","Telefoonnummer","Duratie invullen(minuten)","Punten\n"]
    VorigKlantNummer = open("Huidig klantnummer.txt", "r+")
    InhoudBestand = VorigKlantNummer.readline()

    Teller = int(InhoudBestand)
    if os.path.getsize("Klantgegevens_CSV.CSV") == 0:
        OpslagKlantGegevens.write("Klantnummer;Naam;Geslacht;Geboortejaar;Woonplaats;Straat;Postcode;Huisnummer;Werk;E-mail;Telefoonnummer;Duratie invullen(minuten);Punten\n")
    LijstVoorCSV = [str(Teller), str(TupleMetKlantGegevens[0]), str(TupleMetKlantGegevens[1]), str(TupleMetKlantGegevens[2]), str(TupleMetKlantGegevens[3]), str(TupleMetKlantGegevens[4]), str(TupleMetKlantGegevens[5]), str(TupleMetKlantGegevens[6]), str(TupleMetKlantGegevens[7]), str(TupleMetKlantGegevens[8]), str(TupleMetKlantGegevens[9]), str(TupleMetKlantGegevens[10]),0]
    OpslagKlantGegevens.write(str(LijstVoorCSV).replace("[", "").replace("]", "").replace("'","").replace(",",";").replace(" ", "") + "\n")

    OpslagKlantGegevens.close()
    VorigKlantNummer.close()
    return "gegevens zijn opgeslagen"


startMenu()
