account_enabled = True
balance = 1000
withdrawal_amount = 500_00

if account_enabled and withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print(f"Withdrawal of ${withdrawal_amount} successful. New balance: ${balance}")
else:
    if not account_enabled:
        print("Account is disabled. Please contact support.")
    else:
        print("Insufficient funds or invalid withdrawal amount.")