import pandas as pd
import os

path = "{}".format(os.path.abspath(os.getcwd()))


def calculate_BMI(input_data):
    """
    Get the data and calculate the BMI and generate the CSV file with BMI category and Health Risk information.
    :param input_data: Json data with hight, weight and gender information
    :return: success response if CSV file is generated or Exception if any error occur
    """
    headers = ["BMI Category", "BMI Range (kg/m^2)", "Health Risk"]
    persons_data = []
    count = 0
    try:
        for data in input_data:
            hight_in_meter = convert_centimeter_to_meter(data["HeightCm"])
            bmi = calculation_of_BMI(data["WeightKg"], hight_in_meter)
            bmi_obj = {"BMI category": "", "BMI_range": "", "Health Risk": ""}
            person_data = category_based_on_BMI(bmi, bmi_obj)
            persons_data.append([person_data["BMI category"], person_data["BMI_range"], person_data["Health Risk"]])
            if person_data["BMI category"] == "Overweight":
                count += 1
        print(f"Total person of overweight: {count}")
        csv_write = pd.DataFrame(persons_data, columns=headers)
        csv_write.to_csv("{}/BMI.csv".format(path), index=False)
        return {"result": True, "message": "Information are successfully generated in CSV file"}
    except Exception as e:
        return {"result": False, "message": "Error {} occur during calculating the BMI".format(e)}


def category_based_on_BMI(bmi, bmi_obj):
    """
    Define category based on BMI
    :param bmi: bmi of person
    :param bmi_obj: Person details based on his/her BMI.
    :return:
    """
    if bmi <= 18.4:
        bmi_obj["BMI category"] = "Underweight"
        bmi_obj["BMI_range"] = "18.4 and below"
        bmi_obj["Health Risk"] = "Malnutrition risk"
    elif 18.5 <= bmi <= 24.9:
        bmi_obj["BMI category"] = "Normal weight"
        bmi_obj["BMI_range"] = "18.5 - 24.9"
        bmi_obj["Health Risk"] = "Low risk"
    elif 25 <= bmi <= 29.9:
        bmi_obj["BMI category"] = "Overweight"
        bmi_obj["BMI_range"] = "25 - 29.9"
        bmi_obj["Health Risk"] = "Enhanced risk"
    elif 30 <= bmi <= 34.9:
        bmi_obj["BMI category"] = "Moderately obese"
        bmi_obj["BMI_range"] = "30 - 34.9"
        bmi_obj["Health Risk"] = "Medium risk"
    elif 35 <= bmi <= 39.9:
        bmi_obj["BMI category"] = "Severely obese"
        bmi_obj["BMI_range"] = "35 - 39.9"
        bmi_obj["Health Risk"] = "High risk"
    elif bmi >= 40:
        bmi_obj["BMI category"] = "Very severely obese"
        bmi_obj["BMI_range"] = "40 and above"
        bmi_obj["Health Risk"] = "Very high risk"
    return bmi_obj


def convert_centimeter_to_meter(val):
    """
    convert the centimeter to meter
    :param val: Height in Centimeter
    :return: Hight in meter
    """
    return val / 100


def calculation_of_BMI(weight, hight):
    """
    Calculate the BMI using weight and height
    :param weight: weight of person in KG
    :param hight: height of person in meter
    :return: BMI of person
    """
    return float("{:.2f}".format(weight / (hight * hight)))


if __name__ == "__main__":
    input_data = [
        {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
        { "Gender": "Male", "HeightCm": 161, "WeightKg": 85},
        { "Gender": "Male", "HeightCm": 180, "WeightKg": 77},
        { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
    ]
    response = calculate_BMI(input_data)
    print(response)
