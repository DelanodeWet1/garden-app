# Take user input on the season and plant_type
while True:
    try:
        season = int(input('''Please enter the season:

1. Spring
2. Summer
3. Autumn
4. Winter

'''))
        if season not in (1, 2, 3, 4):
            print("Input not recognized. Please input an integer from the menu.")
        break
    except ValueError:
        print("Input not recognized. Please input an integer from the menu.")

while True:
    try:
        plant_type = int(input('''Please enter the type of plant:

1. Flower
2. Vegetable
3. Fruit
4. Shrub
5. Tree
6. Other
'''))
        if plant_type not in (1, 2, 3, 4, 5, 6):
            print("Input not recognized. Please input an integer from the menu.")
        break
    except ValueError:
        print("Input not recognized. Please input an integer from the menu.")
    

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == 2:
    advice += "Water your plants regularly and provide some shade.\n"
elif season == 4:
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"
    
# Recommend plants based on the season
if season == 1:
    advice += "The best plants to grow in spring are tomatoes, peppers and green beans.\n"
elif season == 2:
    advice += "The best plants to grow in summer are corn, cucumbers, squash and pumpkins.\n"
elif season == 3:
    advice += "The best plants to grow in autumn are lettuce, kale, onions and turnips.\n"
elif season == 4:
    advice += "The best plants to grow in winter are broccoli, cabbage, garlic and spinach.\n"
else:
    advice += "No plants to recommend for this season.\n"

# Determine advice based on the plant type
if plant_type == 1:
    advice += "Use fertiliser to encourage blooms."
elif plant_type == 2:
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
