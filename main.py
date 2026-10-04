# ==========================================================
#                 AI_STUDENT_ASSISTANT
#            Education Chatbot - Python
#                 No API Required
# ==========================================================

def show_welcome():
    print("=" * 60)
    print("              AI_STUDENT_ASSISTANT")
    print("             Education Chatbot")
    print("=" * 60)


def get_education_level():
    print("\nBot: Select your education level:")
    print("1. Primary School")
    print("2. High School")
    print("3. Higher Secondary")
    print("4. College")

    while True:
        choice = input("\nYou: ").strip()

        if choice == "1":
            return "Primary School"

        elif choice == "2":
            return "High School"

        elif choice == "3":
            return "Higher Secondary"

        elif choice == "4":
            return "College"

        else:
            print("Bot: Please choose 1, 2, 3, or 4.")


# ==========================================================
# QUESTIONS AND ANSWERS
# ==========================================================

primary_questions = {
    "what is 2 + 2":
        "2 + 2 = 4.",

    "what is 5 + 5":
        "5 + 5 = 10.",

    "what is the capital of india":
        "The capital of India is New Delhi.",

    "how many days are in a week":
        "There are 7 days in a week.",

    "how many months are in a year":
        "There are 12 months in a year.",

    "what is the color of the sky":
        "The sky usually appears blue.",

    "how many legs does a dog have":
        "A dog normally has 4 legs.",

    "what is a cat":
        "A cat is a small domesticated animal."
}


high_school_questions = {
    "what is photosynthesis":
        "Photosynthesis is the process by which green plants make food using sunlight, water, and carbon dioxide.",

    "what is newton's first law":
        "Newton's first law states that an object remains at rest or in uniform motion unless acted upon by an external force.",

    "what is 12 x 12":
        "12 × 12 = 144.",

    "what is a noun":
        "A noun is a word used to name a person, place, animal, thing, or idea.",

    "what is a verb":
        "A verb is a word that describes an action or state.",

    "what is the capital of india":
        "The capital of India is New Delhi.",

    "what is gravity":
        "Gravity is the force that attracts objects toward each other, such as objects toward Earth.",

    "what is water":
        "Water is a chemical compound made of hydrogen and oxygen, with the formula H2O."
}


higher_secondary_questions = {
    "what is an atom":
        "An atom is the smallest unit of an element that retains the chemical properties of that element.",

    "what is dna":
        "DNA is the molecule that carries genetic information in living organisms.",

    "what is an algorithm":
        "An algorithm is a step-by-step procedure used to solve a problem.",

    "what is artificial intelligence":
        "Artificial Intelligence is the field of creating computer systems that can perform tasks that normally require human intelligence.",

    "what is python":
        "Python is a high-level, interpreted programming language.",

    "what is machine learning":
        "Machine learning is a branch of AI where computers learn patterns from data.",

    "what is a compiler":
        "A compiler translates source code written in a programming language into machine code or another form that can be executed.",

    "what is a variable":
        "A variable is a named storage location used to hold a value in a program."
}


college_questions = {
    "what is machine learning":
        "Machine learning is a branch of Artificial Intelligence in which computers learn patterns from data and use them to make predictions or decisions.",

    "what is a database":
        "A database is an organized collection of data that can be stored, managed, and retrieved.",

    "what is an operating system":
        "An operating system is system software that manages computer hardware and provides services for applications.",

    "what is object oriented programming":
        "Object-oriented programming is a programming approach based on objects and classes. Important concepts include inheritance, encapsulation, abstraction, and polymorphism.",

    "what is python":
        "Python is a high-level, general-purpose programming language known for its simple and readable syntax.",

    "what is artificial intelligence":
        "Artificial Intelligence is a field of computer science focused on creating systems that can perform tasks requiring human-like intelligence.",

    "what is cloud computing":
        "Cloud computing provides computing resources such as servers, storage, and software over the internet.",

    "what is an api":
        "An API, or Application Programming Interface, allows different software applications to communicate with each other.",

    "what is cybersecurity":
        "Cybersecurity is the practice of protecting computers, networks, applications, and data from unauthorized access and attacks."
}


# ==========================================================
# SELECT QUESTIONS BASED ON EDUCATION LEVEL
# ==========================================================

def get_questions(level):

    if level == "Primary School":
        return primary_questions

    elif level == "High School":
        return high_school_questions

    elif level == "Higher Secondary":
        return higher_secondary_questions

    elif level == "College":
        return college_questions

    return {}


# ==========================================================
# SHOW AVAILABLE QUESTIONS
# ==========================================================

def show_questions(questions):
    print("\nBot: I can answer these questions:")

    number = 1

    for question in questions:
        print(f"{number}. {question}")
        number += 1


# ==========================================================
# MAIN CHATBOT
# ==========================================================

def main():

    show_welcome()

    # Get student's name
    name = input("\nBot: What is your name?\nYou: ").strip()

    if name == "":
        name = "Student"

    print(f"\nBot: Hello, {name}!")
    print("Bot: Welcome to AI_STUDENT_ASSISTANT.")

    # Get education level
    level = get_education_level()

    # Get questions
    questions = get_questions(level)

    print(f"\nBot: Your education level is {level}.")
    print("Bot: You can now ask me educational questions.")

    print("\nBot: Commands:")
    print("- Type 'help' to see available questions.")
    print("- Type 'level' to see your education level.")
    print("- Type 'hi' or 'hello' to greet me.")
    print("- Type 'bye' to exit.")

    # Chat loop
    while True:

        user = input("\nYou: ").lower().strip()

        # Exit
        if user == "bye":
            print(f"\nBot: Goodbye, {name}!")
            print("Bot: Keep learning and have a great day!")
            break

        # Greeting
        elif user in ["hi", "hello", "hey"]:
            print(f"Bot: Hello {name}! What would you like to learn?")

        # Help
        elif user == "help":
            show_questions(questions)

        # Show level
        elif user == "level":
            print(f"Bot: Your education level is {level}.")

        # Thank you
        elif user in ["thanks", "thank you", "thankyou"]:
            print("Bot: You're welcome!")
            print("Bot: Happy learning!")

        # Answer question
        elif user in questions:
            print(f"Bot: {questions[user]}")

        # Try partial matching
        else:
            found = False

            for question in questions:

                if user in question or question in user:
                    print(f"Bot: {questions[question]}")
                    found = True
                    break

            if not found:
                print("Bot: Sorry, I don't know the answer to that question.")
                print("Bot: Type 'help' to see the questions I can answer.")


# ==========================================================
# START PROGRAM
# ==========================================================

if __name__ == "__main__":
    main()