from acelib import get_int

# Constants
MIN_HEIGHT_CM = 60
MAX_HEIGHT_CM = 274
MIN_WEIGHT_KG = 28
MAX_WEIGHT_KG = 635
MIN_AGE_YRS = 0
MAX_AGE_YRS = 130

UNDERWEIGHT = 18.5
NORMAL = 25
OVERWEIGHT = 30

# Functions
def get_float(message, minimum, maximum):
    while True:
        try:
            number = float(input(message))
            if number < minimum or number > maximum:
                print("Enter a realistic value!")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_user_data():
    name = input("\nWhat should I call you?: ").strip()
    
    while True:
        age = get_int("How old are you?: ")
        if age < MIN_AGE_YRS or age > MAX_AGE_YRS:
            print("Enter a valid age")
            continue
        else:
            break
    
    print()

    height_cm = get_float(f"Alright {name}, what is your height in cms?: ", MIN_HEIGHT_CM, MAX_HEIGHT_CM)
    height_m = height_cm / 100

    weight = get_float("One last thing, what is your weight in kgs?: ", MIN_WEIGHT_KG, MAX_WEIGHT_KG)
    
    print()
    return {
        "height": height_m,
        "weight": weight,
        "age": age,
        "name": name
    }

def calculate_bmi(wt, ht):
    return wt / (ht ** 2)

def categorize(bmi):
    if bmi < UNDERWEIGHT:
        return "You are Underweight"
    elif bmi < NORMAL:
        return "You are Healthy Weight"
    elif bmi < OVERWEIGHT:
        return "You are Overweight"
    else:
        return "You are Obese"
    
def bmi_analysis(weight, height):
    bmi = calculate_bmi(weight, height)
    category = categorize(bmi)
    return bmi, category


def main():
    data = get_user_data()
    bmi, category = bmi_analysis(data["weight"], data["height"])

    print(f"So your BMI is {bmi:.2f}\n{category}\n")

if __name__ == "__main__":
    main()
