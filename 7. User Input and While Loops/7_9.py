sandwich_orders = ["pastrami", "blt", "pastrami", "pastrami", "roast beef", "tuna", "chicken"]
finished_sandwiches = []
current_order = ""
index = 0

print("The Deli has run out of pastrami!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I made your {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)

print(finished_sandwiches)