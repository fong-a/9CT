import random

# List of student names
students = ["Alice", "Bob", "Charlie", "Diana", "Evan", "Grace", "Henry", "Isla"]

# Function to simulate rolling two dice
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def roll_dice_carefully():
    return 12

# Main game loop
for student in students:
    action = input(f"{student}, press Enter to roll the dice or 'h' for a careful roll: ")

    # Roll the dice based on the action
    if action.lower() == 'h':
        result = roll_dice_carefully()
    else:
        result = roll_dice()

    # Output the result of their roll
    if result == 12:
        print(f"Wow, {student} rolled a 12! Enjoy your treat!")
    else:
        print(f"{student} rolled a {result}. Maybe next time!")

    print("-" * 20)  # Separator for readability
