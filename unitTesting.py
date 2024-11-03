from Latihan import calories_burned
from latihan2 import total_session_burned_cal
import unittest

class testKalori(unittest.TestCase):
    def test_Kalori(self):
        result = calories_burned(60, "berenang")
        self.assertEqual(result, 720) #ekspektasi hasilnya sama
    
    def test_DurasiKalori(self):
        result = total_session_burned_cal("berenang","bersepeda", each_session_duration=10)
        self.assertEqual(result, 150)
        self.assertGreater(result, 1)#berekspektasi hasil lebih besar

if __name__ =="__main__":
    unittest.main()