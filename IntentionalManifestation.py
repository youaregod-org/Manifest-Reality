datetime.date.today() - {gratitude}
print("Gratitude recorded!")
from datetime import date

def set_intention():
    """
    Guides the user to set a new intention.
"""
    intention = input("What is your intention? Be specific and clear: ")
    with open("intentions.txt", "a") as f:
        f.write(f"{date.today()} - {intention}\n")
    print("Intention recorded!")

def visualize():
    """Leads the user through a visualization exercise."""
    print("\nClose your eyes. Take a deep breath. Visualize your intention...")
    input("Press Enter when you're finished.")

def create_affirmation():
    """Helps the user create a new affirmation."""
    affirmation = input("Write an affirmation in the present tense: ")
    with open("affirmations.txt", "a") as f:
        f.write(f"{affirmation}\n")
    print("Affirmation saved!")

def repeat_affirmations():
    """Displays existing affirmations for the user to repeat."""
    try:
        with open("affirmations.txt", "r") as f:
            print("\nRepeat these affirmations:\n")
            print(f.read())
    except FileNotFoundError:
        print("No affirmations found. Create some first!")

def express_gratitude():
    """Prompts the user to list things they're grateful for."""
    print("\nList 3 things you're grateful for:")
    for i in range(3):
        gratitude = input(f"{i+1}. ")
        with open("gratitude.txt", "a") as f:
            f.write(f"{date.today()} - {gratitude}\n")
    print("Gratitude recorded!")

def main():
    """Main function to run the app."""
    while True:
        print("\nManifest App Menu:")
        print("1. Set Intention")
        print("2. Visualize")
        print("3. Create Affirmation")
        print("4. Repeat Affirmations")
        print("5. Express Gratitude")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '6':
            print("\nCongratulations on completing your manifestational attempt!")

        choice = input("Enter your choice: ")

        if choice == '1':
            set_intention()
        elif choice == '2':
            visualize()
        elif choice == '3':
            create_affirmation()
        elif choice == '4':
            repeat_affirmations()
        elif choice == '5':
            express_gratitude()
        elif choice == '6':
            print("\nCongratulations on completing your Intentional Manifestation session!")
            print("Your intentions, affirmations, and gratitude have been recorded via the vibrational and light frequencies")
            print("emitted by words, thoughts, and digital magnifications!")
            print("Remember, consistency is key. Keep manifesting your dreams!")
            break