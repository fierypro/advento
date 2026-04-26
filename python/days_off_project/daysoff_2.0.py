from datetime import date
import calendar

def get_user_spending():
    while True:
        try:
            spent = float(input("How much have you spent this month: ₹"))
            if spent < 0:
                print("Please enter a positive value.")
                continue
            return spent
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_month_details(today):
    day = today.day # By default
    total_days = calendar.monthrange(today.year, today.month)[1]
    return day, total_days

def calculate_metrics(total_days, ideal_daily_average, spent, day):
    budget = total_days * ideal_daily_average
    remaining = max(budget - spent, 0)

    days_left = max(total_days - day, 1)
   
    current_daily_average = spent / day

    projected = spent + (current_daily_average * (days_left))
    diff_in_avgs = ideal_daily_average - current_daily_average

    can_spend = remaining / days_left

    return {
        "budget": budget,
        "remaining": remaining,
        "current_avg": current_daily_average,
        "projected": projected,
        "diff_avg": diff_in_avgs,
        "can_spend": can_spend,
        "days_left": days_left
    }

def analyze(metrics, spent, ideal_daily_avg, day):
    if metrics["diff_avg"] < 0:
        print("\n⚠️ Bad Spending\n")

        print(f"You should ideally spend ₹{ideal_daily_avg:.2f} or less per day")

        coverup = 1
        while True:
            corrected_avg = spent / (day + coverup)
            if corrected_avg - ideal_daily_avg <= 0:
                break
            else:
                coverup += 1
        
        print(f"You need to pause your spending for {coverup} day(s) to recover.\n")
    else:
        print("\n✅ Good Spending\n")

def display_summary(metrics, spent):
    print(f"""--- Summary ---
          
Budget = ₹{metrics['budget']:.2f}
Spent = ₹{spent:.2f}
Remaining = ₹{metrics['remaining']:.2f}

You spend on average ₹{metrics['current_avg']:.2f}/day
Projected month-end spend = ₹{metrics['projected']:.2f}

You can safely spend ₹{metrics['can_spend']:.2f}/day going forward
Days left this month : {metrics["days_left"]}""")

###### Main
def main():
    today = date.today()
    day, total_days = get_month_details(today)

    ideal_daily_average = 180.00 ## You can change this as required

    print("")
    spent = get_user_spending()

    metrics = calculate_metrics(
        total_days, ideal_daily_average, spent, day
    )

    analyze(metrics, spent, ideal_daily_average, day)
    
    display_summary(metrics, spent)

if __name__== "__main__":
    main()
