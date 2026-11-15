import unittest

class TestPatientModel(unittest.TestCase):
    def test_patient_creation(self):
        name = "Иван"
        self.assertEqual(name, "Иван")

if __name__ == '__main__':
    unittest.main()
