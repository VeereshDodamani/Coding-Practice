## Write the pyhon code for the following requirements
# IP: {"Orange": "Fruit", "Potato": "Vegetables", "Banana": "Fruit"}
# OP: {"Fruit": ["Banana","Orange"], "Vegetables": ["Potato"]}


my_dict = {'Orange': 'Fruit', 'Potato': 'Vegetables', 'Banana': 'Fruit'}
output = {}

for item, category in my_dict.items():
    if category not in output:
        output[category] = [item]  # Initialize with a list
    else:
        output[category].append(item)

print(output)
