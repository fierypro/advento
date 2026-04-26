import calendar
import math
from datetime import date
from typing import TypedDict

# TEACH: Using TypedDict (Python 3.8+) improves type hinting and IDE autocomplete support.
# This makes dictionaries structured and easier to maintain compared to plain dicts.
class Metrics(TypedDict):
    budget: float
    remaining: float
    current_avg: float
    projected: float
    diff_avg: float
    can_spend: float
    days_left: int

def get_user_spending() -> float:
    # TEACH: Python 3.11+ handles exceptions at zero-cost, making try/except inside 
    # a while loop highly efficient for input validation.
    while True:
        try:
            spent = float(input("How much have you spent this month: ₹"))
            if spent < 0:
                print("Please enter a positive value.")
                continue
            return spent
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_month_details(today: date) -> tuple[int, int]:
    # TEACH: Type hinting tuple[int, int] clarifies return values. Unpacking makes it readable.
    total_days = calendar.monthrange(today.year, today.month)[1]
    return today.day, total_days

def calculate_metrics(total_days: int, ideal_daily_average: float, spent: float, day: int) -> Metrics:
    budget = total_days * ideal_daily_average
    remaining = max(budget - spent, 0.0)

    # TEACH: Handled exact last day edge case to prevent zero-division errors.
    days_left = total_days - day
    current_daily_average = spent / day if day > 0 else 0.0

    # OPTIMIZATION: Projected spend is simply the current average multiplied by total days.
    # The previous logic (current_avg * days_left + spent) skewed results if days_left was forced to 1 at month-end.
    projected = current_daily_average * total_days
    diff_in_avgs = ideal_daily_average - current_daily_average

    # OPTIMIZATION: Prevent ZeroDivisionError explicitly for the last day of the month.
    can_spend = remaining / days_left if days_left > 0 else remaining

    return {
        "budget": budget,
        "remaining": remaining,
        "current_avg": current_daily_average,
        "projected": projected,
        "diff_avg": diff_in_avgs,
        "can_spend": can_spend,
        "days_left": days_left
    }

def analyze(metrics: Metrics, spent: float, ideal_daily_avg: float, day: int) -> None:
    if metrics["diff_avg"] < 0:
        print("\n⚠️ Bad Spending\n")
        print(f"You should ideally spend ₹{ideal_daily_avg:.2f} or less per day")

        # OPTIMIZATION & TEACH: Replaced O(N) while-loop with O(1) mathematical formula.
        # Logic: We need spent / (day + coverup) <= ideal_daily_avg
        # Solving for coverup: coverup >= (spent / ideal_daily_avg) - day
        # math.ceil() ensures we round up to the nearest whole day required.
        required_total_days = spent / ideal_daily_avg
        coverup = max(0, math.ceil(required_total_days - day))
        
        print(f"You need to pause your spending for {coverup} day(s) to recover.\n")
    else:
        print("\n✅ Good Spending\n")

def display_summary(metrics: Metrics, spent: float) -> None:
    # TEACH: Aligning the multiline f-string entirely to the left prevents 
    # unwanted leading whitespace/indentation in the final console output.
    print(f"""--- Summary ---

Budget = ₹{metrics['budget']:.2f}
Spent = ₹{spent:.2f}
Remaining = ₹{metrics['remaining']:.2f}

You spend on average ₹{metrics['current_avg']:.2f}/day
Projected month-end spend = ₹{metrics['projected']:.2f}

You can safely spend ₹{metrics['can_spend']:.2f}/day going forward
Days left this month : {metrics["days_left"]}""")

def main() -> None:
    today = date.today()
    day, total_days = get_month_details(today)

    # TEACH: Constants should ideally be uppercase per PEP 8 standards.
    IDEAL_DAILY_AVERAGE = 180.00 

    print("")
    spent = get_user_spending()

    metrics = calculate_metrics(total_days, IDEAL_DAILY_AVERAGE, spent, day)
    
    analyze(metrics, spent, IDEAL_DAILY_AVERAGE, day)
    display_summary(metrics, spent)

if __name__ == "__main__":
    main()