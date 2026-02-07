"""
================================================
NOOR - My Kind Islamic Chatbot
Created by: AI Superheroes Workshop Students
Date: February 7, 2026
Session: 3 - Introduction to Python Programming
================================================

This is a simple Islamic chatbot built by kids aged 9-14!
It uses basic Python concepts:
- Variables (to store information)
- Print (to show messages)
- Input (to ask questions)
- If/Else (to make decisions)
- Lists (to store Q&A pairs)
- Loops (to keep the conversation going)

HOW IT WORKS:
1. The chatbot greets you
2. It asks your name
3. You can ask it questions about Islam
4. It searches for the answer in its knowledge base
5. If it knows the answer, it tells you
6. If it doesn't know, it says "I'm learning!"
7. Type 'bye' to exit
"""

# ================================================
# STEP 1: Welcome Message
# ================================================
print("╔════════════════════════════════╗")
print("║   As-salamu alaykum! 🌙       ║")
print("║   I am Noor, your kind        ║")
print("║   Islamic helper chatbot!     ║")
print("╚════════════════════════════════╝")
print()  # Empty line for spacing


# ================================================
# STEP 2: Get User's Name
# ================================================
user_name = input("What is your name? ")
print("Nice to meet you,", user_name, "! 😊")
print()


# ================================================
# STEP 3: Create Knowledge Base (Q&A Database)
# ================================================
# These are the questions Noor knows about
# We use LOWERCASE so we can match easier!
questions = [
    "who created us",
    "how many times do we pray",
    "what do we say before eating",
    "what is the quran",
    "how should we treat others",
    "what is ramadan",
    "who is prophet muhammad",
    "what are the five pillars",
    "why do we fast",
    "what is zakat"
]

# These are Noor's answers
# Each answer matches the question at the SAME position!
# Question 0 → Answer 0, Question 1 → Answer 1, etc.
answers = [
    "Allah (SWT) created us and everything in the universe! He is the Creator of all things. ☝️",
    "We pray 5 times a day: Fajr (dawn), Dhuhr (noon), Asr (afternoon), Maghrib (sunset), and Isha (night)! 🕌",
    "We say 'Bismillah' (In the name of Allah) before eating! It reminds us to be grateful. 🍎",
    "The Quran is Allah's beautiful message revealed to Prophet Muhammad ﷺ. It guides us in life! 📖",
    "We should treat everyone with kindness, respect, and love - just like Prophet Muhammad ﷺ taught us! ❤️",
    "Ramadan is the blessed month when Muslims fast from dawn to sunset. It's a time to get closer to Allah! 🌙",
    "Prophet Muhammad ﷺ is the last messenger of Allah and our perfect role model. He taught us how to be kind and just! ✨",
    "The five pillars are: 1) Shahada (faith), 2) Salah (prayer), 3) Zakat (charity), 4) Sawm (fasting), 5) Hajj (pilgrimage)! 🕋",
    "We fast during Ramadan to practice self-control, feel empathy for the hungry, and grow closer to Allah! 🌟",
    "Zakat is giving money to help poor people. It's one of the five pillars of Islam! 💚"
]


# ================================================
# STEP 4: Main Chatbot Loop (The Brain!)
# ================================================
print("You can ask me anything about Islam!")
print("Type 'bye' when you want to leave.")
print()

# This loop keeps the conversation going
while True:
    # Get the user's question and make it lowercase
    # .lower() makes "WHO CREATED US?" become "who created us?"
    user_question = input(user_name + ": ").lower()
    
    # Check if the user wants to exit
    if user_question == "bye":
        print("Noor: Wa alaykumu as-salam! May Allah bless you! 🤲")
        break  # This stops the loop
    
    # Track whether we found an answer
    found_answer = False
    
    # Search through all our questions
    # range(len(questions)) gives us: 0, 1, 2, 3, ... up to the number of questions
    for i in range(len(questions)):
        # Check if our question is IN what the user typed
        # Example: if user says "tell me who created us", 
        # it contains "who created us" so we match!
        if questions[i] in user_question:
            # We found a match! Print the answer
            print("Noor:", answers[i])
            found_answer = True
            break  # Stop searching, we found it!
    
    # If we didn't find any matching answer
    if not found_answer:
        print("Noor: I'm still learning! Can you ask in a simpler way? 🤔")
        print("Noor: Try asking: 'who created us' or 'what is ramadan'")
    
    print()  # Empty line for readability


# ================================================
# STEP 5: Goodbye Message
# ================================================
print("─" * 40)
print("Thank you for chatting with me,", user_name, "! 💚")
print("Remember: Always be kind, curious, and caring!")
print("As-salamu alaykum! ✨")
print("─" * 40)


# ================================================
# 🎉 CONGRATULATIONS! 🎉
# ================================================
# You just built a real chatbot using Python!
# You learned:
# ✅ Variables (storing information)
# ✅ Print (showing messages)
# ✅ Input (asking questions)
# ✅ If/Else (making decisions)
# ✅ Lists (organizing Q&A)
# ✅ Loops (keeping conversation going)
#
# YOU ARE A PYTHON PROGRAMMER! 🐍💪
# ================================================


# ================================================
# 🚀 OPTIONAL: Extension Ideas to Try at Home
# ================================================

"""
EXTENSION IDEA #1: Add Greetings
Add this code BEFORE the for loop:

    # Respond to greetings
    if "salam" in user_question or "hello" in user_question:
        print("Noor: Wa alaykumu as-salam! How can I help you today? 😊")
        continue  # Skip to next question


EXTENSION IDEA #2: Add a Story
Add this code BEFORE the for loop:

    # Tell a story
    if "story" in user_question:
        print("Noor: Let me tell you about Prophet Yunus (Jonah)...")
        print("He was swallowed by a big fish, but never stopped praying!")
        print("Allah saved him because he always had faith! 🐋")
        continue


EXTENSION IDEA #3: Add Daily Duas
Add this code BEFORE the for loop:

    # Suggest duas
    if "morning" in user_question or "dua" in user_question:
        print("Noor: Morning dua: Alhamdulillah for this new day! ☀️")
        print("Noor: Say: 'Alhamdulillah alladhi ahyana ba'da ma amatana wa ilayhi an-nushur'")
        continue


EXTENSION IDEA #4: Count Questions
Add this BEFORE the while loop:
    
    question_count = 0

Then INSIDE the loop (after user_question =), add:
    
    question_count = question_count + 1

Then in the goodbye message, add:
    
    print("You asked me", question_count, "questions today!")


EXTENSION IDEA #5: Add Safety Check
Add this code RIGHT AFTER getting the user_question:

    # Safety check for private information
    unsafe_topics = ["password", "address", "phone", "credit card", "age"]
    for unsafe_word in unsafe_topics:
        if unsafe_word in user_question:
            print("Noor: That's private information! Never share it online. 🛡️")
            print()
            continue


Try these and become an even better coder! 🌟
"""
