import unittest
import pytest
import Gegevensinvoerenenverwerken

LijstIntegerControleren = [("", False),
                           ("a", False),
                           ("1", True),
                           ("22", True),
                           ("+", False),
                           ("1234", True)]
LijstOpnieuw = [(True, "5", "5"),
                (True, "123", "123"),
                (True, "1", "1"),
                (True, "35345245", "35345245"),
                (True, "1235", "1235")]
LijstPuntenControle = [("5", "5"),
                       ("123", "123"),
                       ("1", "1"),
                       ("35345245", "35345245"),
                       ("1235", "1235")]
LijstJson = [(("j" ,"j" , "j", "j", "j", "j", "j", "j", "j", "j", 1), "Dit was het eerste gegeven"),
             (("hoi" ,"m" , "1000", "hallo", "straat", "Postcode", "345", "nee", "hallo@hoi.nl", "8790432123", 1), "De extra gegevens zijn opgeslagen"),
             (("1" ,"1" , "1", "1", "1", "1", "1", "1", "1", "1", 1), "De extra gegevens zijn opgeslagen"),
             (("+" ,"+" , "+", "+", "+", "+", "+", "+", "+", "+", 1), "De extra gegevens zijn opgeslagen"),
             ((), "De tuple is te kort")]
LijstCsv = [(("j" ,"j" , "j", "j", "j", "j", "j", "j", "j", "j", 1), "gegevens zijn opgeslagen"),
            (("hoi" ,"m" , "1000", "hallo", "straat", "Postcode", "345", "nee", "hallo@hoi.nl", "8790432123", 1), "gegevens zijn opgeslagen"),
            (("1" ,"1" , "1", "1", "1", "1", "1", "1", "1", "1", 1), "gegevens zijn opgeslagen", ),
            (("+" ,"+" , "+", "+", "+", "+", "+", "+", "+", "+", 1), "gegevens zijn opgeslagen", ),
            ((), "De tuple is te kort")]


@pytest.mark.parametrize('Tekens,Bool', LijstIntegerControleren)
def test_integer_controleren(Tekens, Bool):
        assert Gegevensinvoerenenverwerken.integerControleren(Tekens) == Bool




@pytest.mark.parametrize('Bool,Tekens,Uitkomst', LijstOpnieuw)
def test_opnieuw_invoeren(Bool, Tekens, Uitkomst):
        assert Gegevensinvoerenenverwerken.opnieuwInvoeren(Bool, Tekens) == Uitkomst




@pytest.mark.parametrize('Tekens,Uitkomst', LijstPuntenControle)
def test_punten_controleren(Tekens, Uitkomst):
        assert Gegevensinvoerenenverwerken.puntenControleren(Tekens) == Uitkomst




@pytest.mark.parametrize('Tup,Uitkomst', LijstJson)
def test_gegevens_verwerken_naar_json(Tup, Uitkomst):
        assert Gegevensinvoerenenverwerken.gegevensVerwerkenNaarJson(Tup) == Uitkomst




@pytest.mark.parametrize('Tup,Uitkomst', LijstCsv)
def test_schrijf_naar_csv(Tup, Uitkomst):
        assert Gegevensinvoerenenverwerken.schrijfNaarCSV(Tup) == Uitkomst




@pytest.mark.parametrize('Tekens,Bool', LijstIntegerControleren)
def test_is_invoer_correct(Tekens, Bool):
        assert Gegevensinvoerenenverwerken.isInvoerCorrect(Tekens) == Bool
