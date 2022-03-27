import unittest
from calculate_BMI.calculate_BMI import convert_centimeter_to_meter, calculation_of_BMI, category_based_on_BMI


class TestBMICalculation(unittest.TestCase):

    def test_convert_centimeter_to_meter(self):
        self.assertEqual(convert_centimeter_to_meter(175), 1.75)
        self.assertEqual(convert_centimeter_to_meter(165), 1.65)
        self.assertEqual(convert_centimeter_to_meter(122), 1.22)

    def test_calculate_the__bmi(self):
        self.assertEqual(calculation_of_BMI(75, 1.75), 24.49)
        self.assertEqual(calculation_of_BMI(60, 1.05), 54.42)
        self.assertEqual(calculation_of_BMI(50, 1.10), 41.32)

    def test_category_based_on_BMI(self):
        bmi_obj = {"BMI category": "", "BMI_range": "", "Health Risk": ""}
        self.assertEqual(category_based_on_BMI(15.5, bmi_obj),
                    {"BMI category": "Underweight", "BMI_range": "18.4 and below", "Health Risk": "Malnutrition risk"})
        self.assertEqual(category_based_on_BMI(20, bmi_obj),
                    {"BMI category": "Normal weight", "BMI_range": "18.5 - 24.9", "Health Risk": "Low risk"})
        self.assertEqual(category_based_on_BMI(29.4, bmi_obj),
                    {"BMI category": "Overweight", "BMI_range": "25 - 29.9", "Health Risk": "Enhanced risk"})


if __name__ == '__main__':
    unittest.main(warnings='ignore')
