def displayInfo(assignment_name):
    name = "Delena Davis"
    course = "Programming for Technology Professional"
    instructor = "Professor Mora"
    date = "April 20, 2026"

    print("=" * 40)
    print("STUDENT INFORMATION".center(40))
    print("=" * 40)
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Instructor: {instructor}")
    print(f"Assignment: {assignment_name}")
    print(f"Date: {date}")
    print("=" * 40)
    print() 
    import random
from displayInfo import displayInfo


def load_responses():
    """Loads responses from a text file into a list."""
    try:
        with open("responses.txt", "r") as file:
            responses = [line.strip() for line in file if line.strip()]
        return responses
    except FileNotFoundError:
        print("❌ responses.txt file not found.")
        return []


def magic_8_ball():
    """Main Magic 8 Ball logic."""
    responses = load_responses()

    if not responses:
        return

    print("🎱 Welcome to the Magic 8 Ball!")

    while True:
        question = input("\nAsk a question (or type 'quit' to exit): ")

        if question.lower() == "quit":
            print("👋 Goodbye!")
            break

        if not question.strip():
            print("❌ Please ask a valid question.")
            continue

        answer = random.choice(responses)
        print("🎱 Answer:", answer)


def main():
    # MUST DISPLAY FIRST
    displayInfo("Magic 8 Ball Assignment")

    # Run program
    magic_8_ball()


if __name__ == "__main__":
    main()