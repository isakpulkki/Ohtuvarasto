import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varasto_ei_vuoda_yli(self):
        self.varasto.lisaa_varastoon(50)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_varasto_ei_ota_yli_saldon(self):
        self.assertEqual(self.varasto.ota_varastosta(100), 0)

    def test_tilavuus_ei_voi_olla_alle_0(self):
        self.varasto = Varasto(-1)
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_saldo_ei_voi_olla_alle_0(self):
        self.varasto = Varasto(1, -1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_varastoon_ei_voi_lisää_0(self):
        self.assertEqual(self.varasto.lisaa_varastoon(-1), None)

    def test_varastosta_ei_voi_ottaa_alle_0(self):
        self.assertEqual(self.varasto.ota_varastosta(-1), 0)

    def test_print_varasto(self):
        tuloste = str(self.varasto)
        self.assertEqual(
            tuloste, f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")
