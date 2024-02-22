def calculate_sales_tax(total_cost):
    tax_rate = 0.06  # 6% sales tax rate
    return round(total_cost * tax_rate, 2)

def calculate_total_after_tax(total_cost):
    sales_tax = calculate_sales_tax(total_cost)
    return round(total_cost + sales_tax, 2)
