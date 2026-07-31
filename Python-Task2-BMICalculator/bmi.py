try:
    weight = float(input("Enter your weight (Kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0 :
        print("Error : Weight and Height must be greater than 0.")
    else:
        bmi_value = weight / (height ** 2 )

#bmi_value = float(input("Enter your Bmi_value: ")) #For Testing

    print("Your BMI value is :", round(bmi_value,2))

    if bmi_value < 18.5 :
        print("Category : Underweight")
    elif 18.5 <= bmi_value <= 24.9 :
        print("Category : Normal")
    elif 25 <= bmi_value <= 29.9 :
        print("Category :Overweight")
    elif bmi_value >= 30 :
        print("Category :Obese")
    else:
        print("Invalid input values")

except ValueError:
    print("Error : Please enter numeric values for weight and height.")