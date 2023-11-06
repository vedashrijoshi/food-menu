print("Welcome to Zero Point....")
print("We are here to take your order....")

weekly_menu = {
    "Monday": {
        "Breakfast": {
            "Poha": 30.0,
            "Idli": 70.0
        },
        "Lunch": {
            "Chapati": 7.0,
            "Watana sabji": 50.0,
            "Rice": 60.0
        },
        "Dinner": {
            "Chapati": 7.0,
            "Dal": 40.0,
            "Rice": 60.0
        }
    },
    "Tuesday": {
        "Breakfast": {
            "Pakoda": 20,
            "Usal": 30
        },
        "Lunch": {
            "Chapati": 7.0,
            "Brinjal sabji": 60.0,
            "Rice": 60.0
        },
        "Dinner": {
            "Chapati": 7.0,
            "Urad dal": 50.0,
            "Rice": 60.0
        }
    },
    "Thursday": {
        "Breakfast": {
            "Sandwich": 50,
            "Dahi wada": 60
        },
        "Lunch": {
            "Chapati": 7.0,
            "Potato sabji": 60.0,
            "Rice": 60.0
        },
        "Dinner": {
            "Chapati": 7.0,
            "Rajma": 50.0,
            "Rice": 60.0
        }
    },
    "Friday": {
        "Breakfast": {
            "Bread Jam": 40,
            "Aloo Tikki": 90
        },
        "Lunch": {
            "Chapati": 7.0,
            "Potato sabji": 60.0,
            "Rice": 60.0
        },
        "Dinner": {
            "Chapati": 7.0,
            "Dal tadka": 60.0,
            "Rice": 60.0
        }
    },
    "Friday": {
        "Breakfast": {
            "Bread Jam": 40,
            "Aloo Tikki": 90
        },
        "Lunch": {
            "Chapati": 7.0,
            "Potato sabji": 60.0,
            "Rice": 60.0
        },
        "Dinner": {
            "Chapati": 7.0,
            "Dal tadka": 60.0,
            "Rice": 60.0
        }
    },
    "Friday": {
        "Breakfast": {
            "chole bhature": 90,
            "Pakoda": 40
        },
        "Lunch": {
            "Chapati": 7.0,
            "Gattu sabji": 60.0,
            "Rice": 60.0
        },
        "Dinner": {
            "Veg Biryani": 100
        },
    },
}

day = input("Enter the day: ").capitalize()

if day in weekly_menu:
    meal_choice = input(f"What meal would you like on {day}? (Breakfast, Lunch, or Dinner): ").capitalize()

    if meal_choice in ["Breakfast", "Lunch", "Dinner"]:
        print(f"Menu for {meal_choice} on {day}:")
        total_cost = 0
        for item, price in weekly_menu[day][meal_choice].items():
            print(f"- {item}")
            quantity = 1  # Set quantity to 1 for one item
            total_cost += price * quantity

        print(f"Total cost for your {meal_choice} order on {day}: ${total_cost:.2f}")
    else:
        print("Invalid meal choice.")
else:
    print("Invalid day.")
