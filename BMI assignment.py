def calculate_bmi():
    try:
        height_cm=float(input("Enter your height in centimeters (cm): "))
        weight_kg=float(input("Enter your weight in kilograms (kg): "))
        height_cm=height_cm/100
        bmi=weight_kg/(height_cm**2)
        print(f"\nYour BMI is:{bmi:.2f}")
        if bmi<18.5:
            print("UNDERWEIGHT")
        elif 18.5<=bmi<25:
            print("NORMAL WEIGHT")   
        elif 25<=bmi<30:
            print("OVERWEIGHT")   
        else:
            print("You are obese")
    except ValueError:
        print("invalid input: plese enter a numeric value for height and weight") 
    except ZeroDivisionError:
        print("height can not be zero(0). Please enter a valid height ")   
calculate_bmi()
                

    

    