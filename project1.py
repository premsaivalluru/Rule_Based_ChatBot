import pandas as pd

attendance = {
    "23331A0759": "59%",
    "23331A0757": "75%",
    "23331A0758": "82%",
    "23331A0760": "68%",
}

time_table = {
    "CSE": {
        "9:15-10:15": "Data Structures",
        "10:15-11:15": "Operating Systems",
        "11:15-12:15": "Database Management Systems",
        "1:00-2:00": "Computer Networks",
        "2:00-3:00": "Software Engineering"
    },
    "ECE": {
        "9:15-10:15": "Analog Circuits",
        "10:15-11:15": "Digital Signal Processing",
        "11:15-12:15": "Microprocessors",
        "1:00-2:00": "Communication Systems",
        "2:00-3:00": "Control Systems"
    },
    "ME": {
        "9:15-10:15": "Thermodynamics",
        "10:15-11:15": "Fluid Mechanics",
        "11:15-12:15": "Manufacturing Processes",
        "1:00-2:00": "Machine Design",
        "2:00-3:00": "Heat Transfer"
    },
    "CE": {
        "9:15-10:15": "Engineering Graphics",
        "10:15-11:15": "Strength of Materials",
        "11:15-12:15": "Structural Analysis",
        "1:00-2:00": "Geotechnical Engineering",
        "2:00-3:00": "Water Resources Engineering"
    }
}

courses = {
    "CSE": [
        "Data Structures",
        "Operating Systems",
        "Database Management Systems",
        "Computer Networks",
        "Software Engineering"
    ],
    "ECE": [
        "Analog Circuits",
        "Digital Signal Processing",
        "Microprocessors",
        "Communication Systems",
        "Control Systems"
    ],
    "ME": [
        "Thermodynamics",
        "Fluid Mechanics",
        "Manufacturing Processes",
        "Machine Design",
        "Heat Transfer"
    ],
    "CE": [
        "Engineering Graphics",
        "Strength of Materials",
        "Structural Analysis",
        "Geotechnical Engineering",
        "Water Resources Engineering"
    ]
}

marks = {
    "23331A0759": {
        "Data Structures": 85,
        "Operating Systems": 78,
        "Database Management Systems": 92,
        "Computer Networks": 88,
        "Software Engineering": 90
    },

    "23331A0757": {
        "Data Structures": 75,
        "Operating Systems": 80,
        "Database Management Systems": 85,
        "Computer Networks": 82,
        "Software Engineering": 88
    },

    "23331A0758": {
        "Data Structures": 90,
        "Operating Systems": 92,
        "Database Management Systems": 95,
        "Computer Networks": 94,
        "Software Engineering": 96
    },

    "23331A0760": {
        "Data Structures": 70,
        "Operating Systems": 68,
        "Database Management Systems": 72,
        "Computer Networks": 65,
        "Software Engineering": 78
    }
}

responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help you?",
    "exams": "Which exam schedule would you like to know? (mid / sem)",
    "timetable": "Please specify your branch (CSE/ECE/ME/CE).",
    "courses": "Please specify your branch (CSE/ECE/ME/CE).",
    "attendance": "Please enter your registered number.",
    "marks": "Please enter your registered number.",
    "mid": "The next midterm exams are scheduled for the first week of October.",
    "sem": "The next semester exams are scheduled for the second week of November.",
    "default": "I'm sorry, I didn't understand that.",
    "exit": "Goodbye! If you have any more questions, feel free to ask.",
    "additional": "Any other information you need? (Type Exit to quit)"
}


# ---------------- FUNCTIONS ---------------- #

def greet_user(user):
    print("Bot:", responses[user])


def show_exam_schedule():
    print("Bot:", responses["exams"])


def show_timetable():
    print("Bot:", responses["timetable"])

    branch = input("You: ").upper().strip()

    if branch in time_table:

        print(f"\nBot: Today's timetable for {branch}:\n")

        df = pd.DataFrame(
            list(time_table[branch].items()),
            columns=["Time", "Subject"]
        )

        print(df.to_string(index=False))
        print("\nBot:", responses["additional"])

    else:
        print("Bot:", responses["default"])


def show_courses():
    print("Bot:", responses["courses"])

    branch = input("You: ").upper().strip()

    if branch in courses:

        print(f"\nBot: Courses for {branch}:\n")

        for course in courses[branch]:
            print("-", course)

        print("\nBot:", responses["additional"])
    else:
        print("Bot:", responses["default"])
    


def show_attendance():
    print("Bot:", responses["attendance"])

    reg_number = input("You: ").upper().strip()

    if reg_number in attendance:

        print(
            "Bot: Your attendance for the current semester is:",
            attendance[reg_number]
        )
        print("\nBot:", responses["additional"])

    else:
        print("Bot:", responses["default"])


def show_marks():
    print("Bot:", responses["marks"])

    reg_number = input("You: ").upper().strip()

    if reg_number in marks:

        print("\nBot: Here are your marks:\n")

        df = pd.DataFrame(
            list(marks[reg_number].items()),
            columns=["Subject", "Marks"]
        )

        print(df.to_string(index=False))

        average = sum(marks[reg_number].values()) / len(marks[reg_number])

        print(f"\nBot: Your average marks are: {average:.2f}")
        print("\nBot:", responses["additional"])
    else:
        print("Bot:", responses["default"])


# ---------------- MAIN FUNCTION ---------------- #

def main():

    print("\n******** Smart Student Support Chatbot ********\n")

    print(
        "Bot: Hey there! I'm your Smart Student Support Chatbot."
    )

    print("Bot: How can I assist you today? (Type Exit to quit)\n")

    while True:

        user = input("You: ").lower().strip()

        if user == "exit":
            print("Bot:", responses["exit"])
            break

        elif user in ["hello", "hi"]:
            greet_user(user)

        elif user == "exams":
            show_exam_schedule()

        elif user in ["mid", "sem"]:
            print("Bot:", responses[user])

        elif user == "timetable":
            show_timetable()

        elif user == "courses":
            show_courses()

        elif user == "attendance":
            show_attendance()

        elif user == "marks":
            show_marks()

        else:
            print("Bot:", responses["default"])


# ---------------- RUN PROGRAM ---------------- #

if __name__ == "__main__":
    main()