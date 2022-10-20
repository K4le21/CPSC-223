sandwich_orders = ["pastrami", "blt", "pastrami", "pastrami", "roast beef", "tuna", "chicken"]
finished_sandwiches = []
current_order = ""
index = 0

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I made your {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)

print(finished_sandwiches)