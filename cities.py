prompt = "\nPlease enter the name of the cities you have visited: "
prompt += "\n(Enter 'quit' when you have finished)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I would love to go to {city.title()}")