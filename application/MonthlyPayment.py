def monthly_smallest_installment(balance, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12
    monthly_payment_lb = balance / 12
    monthly_payment_ub = (balance * (1 + monthly_interest_rate) ** 12) / 12

    return (monthly_payment_lb + monthly_payment_ub) / 2


