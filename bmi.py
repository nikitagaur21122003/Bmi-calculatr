# BMI Calculator in Python

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero."
    except Exception as e:
        return str(e)

def get_bmi_category(bmi):
    """Return the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """Main function to run the BMI calculator."""
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        
        if isinstance(bmi, str):  # Check if an error message was returned
            print(f"Error: {bmi}")
        else:
            print(f"Your BMI is: {bmi:.2f}")
            print(f"BMI Category: {get_bmi_category(bmi)}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
