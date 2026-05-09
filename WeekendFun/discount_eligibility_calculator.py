#-Collect user input
#-Calculate discount percentage
#-Calculate final amount
#-Display results

total_bill = float(input("Enter total bill amount: "))
is_member = input("Are you a member? (yes/no): ").strip().lower()

if total_bill >= 1000:
    if is_member == "yes":
        discount_percent = 0.10
        message = "10% Member Discount applied!"
    else:
        discount_percent = 0.05
        message = "5% Discount applied!"
else:
    discount_percent = 0.0
    message = "No discount applied."

discount_amount = total_bill * discount_percent
final_amount = total_bill - discount_amount

print(f"\n{message}")
print(f"Final Amount: ${final_amount:.2f}")
