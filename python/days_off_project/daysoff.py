#
# Personal Budget Analysis Software - Ace
#

from datetime import date # This imports the date, month and year for usage in other variables
import calendar # This imports the calendar to check for leap year

divider = "============================================================\n" # This is a formatting variable declared early since it has extensive usage

def analyze(ideal, day, total_spent, ratio, deviation, current): # This is the brain function of this program
    if ratio > 1: # Checking whether the spending is more than what is ideal

        print(divider)
        print("Bad spending")
        print(f"You should ideally spend ₹{ideal:.2f} or less per day")

        coverup = 1 # Variable to measure days of correction
            
        while True: # Actually measuring the days of correction
            new_current = (total_spent / (day + coverup)) 
            new_ratio = new_current / ideal
            if new_ratio <= 1:
                break
            else:
                coverup += 1

        print(f"You would have to hold spending for {coverup} days to reach ideal spend/day\n")

        print(f"You are spending {deviation:.2f}% more than ideal")
        print(f"That means you are spending ₹{current - ideal:.2f} more per day than ideal\n")

    else:

        print(divider)
        print("Good spending")
        print(f"You can ideally spend ₹{ideal:.2f} per day\n")

        print(f"You are saving {deviation:.2f}% more than ideal")
        print(f"That means you are spending ₹{ideal - current:.2f} less per day than ideal\n")    

        # print(f"You can now actually spend ₹{} per day or continue the good work!")    


print("\n============================================================")
print("               Welcome to the Budget Analysis!              ")
print("============================================================\n")

# budget = float(input("What is your monthly budget?: "))
# budget = 5000.00 # Set your budget manually here or uncomment the previous line

today = date.today() # Collecting the data required
year, month, day = today.year, today.month, today.day
leap = calendar.isleap(year)

if month == 2: # Checking whether the month falls in 30 or 31 day category or if it is February
    total_days = 29 if leap else 28
elif month in [4, 6, 9, 11]:
    total_days = 30
else:
    total_days = 31

budget = 180 * total_days

total_spent = float(input("How much have you spent till date: "))
print("")

ideal_daily_average = budget / total_days
current_daily_average = total_spent / day

spending_ratio = current_daily_average / ideal_daily_average # This helps make logic easier; If current is more than ideal then the ratio is greater than 1 
percentage_deviation = abs((1 - spending_ratio) * 100) # This gives a picture of how well or poorly one is doing

print(f"Your budget is ₹{budget:.2f}\nYou have used ₹{total_spent:.2f}\nYou have ₹{budget-total_spent:.2f} remaining for this month.\n")

analyze(ideal_daily_average, day, total_spent, spending_ratio, percentage_deviation, current_daily_average) # Calling the brain

print("============================================================")
print("             Thank you for using my software!               ")
print("============================================================")
