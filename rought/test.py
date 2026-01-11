# Given variables
budget_dollars = 50
item_cost_dollars = 15
tax_percent = 3

# Intermediary calculations
item_sp = item_cost_dollars + item_cost_dollars * tax_percent/100
print("item_sp = ", item_sp)

# Final output
money_left = budget_dollars - item_sp
print("money_left: ", money_left)