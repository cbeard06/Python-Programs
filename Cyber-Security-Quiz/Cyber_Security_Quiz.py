# Cyber Security Quiz
# This is a beginner cyber security quiz with 10 questions. 
# Each question has 4 answer options (A, B, C, D) and only one correct answer. 
# The user will be prompted to enter their answer for each question, and at the end of the quiz, their total score will be displayed.


print("Welcome to the beginner cyber security quiz!")
print("There will be 10 questions, so do your best!")


# Define the quiz questions and answers in a dictionary
quiz = {
    "What does DNS do on a network?" : {
        "A": "Encrypts internet traffic", 
        "B": "Translates domain names to IP addresses", 
        "C": "Blocks malicious websites", 
        "D": "Creates Wi-Fi passwords" ,
        "Answer": "B"
    },   
    "Which protocol is used to securely remotely access a computer?" : {
        "A": "Telnet",
        "B": "FTP",
        "C": "SSH",
        "D": "HTTP",
        "Answer": "C"
    },
    "What is the main difference between TCP and UDP?" : {
        "A": "TCP is wireless, UDP is wired",
        "B": "TCP is faster and less reliable than UDP",
        "C": "TCP provides reliable delivery, UDP focuses on speed",
        "D": "UDP can only be used on LAN networks",
        "Answer": "C"
    },
    "Which of these is a private IP address?" : {
        "A": "8.8.8.8", 
        "B": "192.168.1.1",
        "C": "255.255.255.255",
        "D": "1.1.1.1",
        "Answer": "B"
    },
    'What does malware called "ransomware" do?' : {
        "A": "Steals personal information",
        "B": "Encrypts files and demands payment for decryption",
        "C": "Spams your email contacts",
        "D": "Hijacks your web browser",
        "Answer": "B"
    },
    "Which port is commonly associated with SSH?" : {
        "A": "21",
        "B": "22",
        "C": "80",
        "D": "443",
        "Answer": "B"
    },
    "What is social engineering in cybersecurity?" : {
        "A": "Using technical exploits to break into systems",
        "B": "Manipulating people into divulging confidential information",
        "C": "Creating strong passwords",
        "D": "Encrypting data to protect it from hackers",
        "Answer": "B"
    },
    "Which of these is considered multi-factor authentication?" : {
        "A": "Using a password and a security question",
        "B": "Using a password and a fingerprint scan",
        "C": "Using two different passwords",
        "D": "Using a password and a CAPTCHA",
        "Answer": "B"
    },
    "What does a brute-force attack attempt to do?" : {
        "A": "Overwhelm a system with traffic to cause a denial of service",
        "B": "Guess passwords by trying every possible combination",
        "C": "Exploit vulnerabilities in software to gain unauthorized access",
        "D": "Phish users into revealing their credentials",
        "Answer": "B"
    },
    "Which command is commonly used to view network configuration information on Windows?" : {
        "A": "ifconfig",
        "B": "ipconfig",
        "C": "netstat",
        "D": "ping",
        "Answer": "B"
    }

}

# Initialize the user's score
score = 0

# Loop through the quiz questions
for number, (question, choices) in enumerate(quiz.items()):
    print(f"\n{number + 1}. {question}")
    print("--------------------------------------")
    print(f"A. {choices['A']}")
    print(f"B. {choices['B']}")
    print(f"C. {choices['C']}")
    print(f"D. {choices['D']}")

    # Get the user's answer
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()

    # Check if the user's answer is correct
    if user_answer == choices["Answer"]:
        print("\nCorrect!")
        score += 1
    else:
        print(f"\nIncorrect. The correct answer is {choices['Answer']}.")

# Display the user's total score at the end of the quiz
print(f"\nYour total score is : {score} out of {len(quiz)}")
percentage = (score / len(quiz)) * 100
print(f"You scored a {percentage:.0f}% on the quiz!")

# Wait for the user to press Enter before exiting the quiz
input("\nPress Enter to exit the quiz.")
