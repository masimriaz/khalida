#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌟 My Kind Islamic Chatbot 🌟
A Simple Python Chatbot for Kids (Ages 9-14)
Created with love and respect for Islamic values

This chatbot is like a friendly helper that answers questions about Islam!
It uses simple Python code that you can understand and modify.
"""

# ============================================
# STEP 1: Setting Up Our Chatbot's Knowledge
# ============================================

# Think of this like a chatbot's brain - a list of questions and answers!
# Each entry is like a flashcard: question on one side, answer on the other

chatbot_knowledge = [
    {
        "question": "assalamu alaikum",
        "answer": "Wa Alaikum Assalam! 🌟 How can I help you today?"
    },
    {
        "question": "what is your name",
        "answer": "My name is Noor! It means 'light' in Arabic. I'm here to help you learn about Islam! ✨"
    },
    {
        "question": "who created you",
        "answer": "I was created by amazing kids like you in the AI Superheroes Workshop! You're learning to build helpful technology! 🚀"
    },
    {
        "question": "who is allah",
        "answer": "Allah is the One and Only God, the Creator of everything. He is Most Merciful and Most Compassionate. 🤲"
    },
    {
        "question": "what is islam",
        "answer": "Islam is a beautiful way of life that teaches us to worship Allah, be kind to others, and live in peace. It means 'submission to Allah's will'. 🌙"
    },
    {
        "question": "what are the five pillars",
        "answer": "The Five Pillars are: 1) Shahada (faith), 2) Salah (prayer), 3) Zakat (charity), 4) Sawm (fasting in Ramadan), 5) Hajj (pilgrimage). These are like the foundation of Islam! 🕌"
    },
    {
        "question": "how many times do we pray",
        "answer": "Muslims pray 5 times a day: Fajr (dawn), Dhuhr (noon), Asr (afternoon), Maghrib (sunset), and Isha (night). Prayer connects us with Allah! 🤲"
    },
    {
        "question": "what is ramadan",
        "answer": "Ramadan is a special holy month when Muslims fast from sunrise to sunset. It teaches patience, gratitude, and helps us think about those who are hungry. 🌙✨"
    },
    {
        "question": "what is the quran",
        "answer": "The Quran is Allah's final message to humanity, revealed to Prophet Muhammad (peace be upon him). It's our guide for a good life! 📖"
    },
    {
        "question": "who is prophet muhammad",
        "answer": "Prophet Muhammad (peace be upon him) is the last messenger of Allah. He was kind, honest, and taught us how to live a good life. 🌟"
    },
    {
        "question": "tell me a dua",
        "answer": "Here's a simple dua: 'Alhamdulillah' - It means 'All praise is for Allah'. Say this to thank Allah for everything! 🤲💚"
    },
    {
        "question": "how should i be kind",
        "answer": "Be kind by smiling, helping others, sharing, respecting your parents, and being honest. The Prophet (PBUH) said the best people are those who benefit others! 💝"
    },
    {
        "question": "what is sadaqah",
        "answer": "Sadaqah is voluntary charity or good deeds. Even a smile is sadaqah! Helping others makes Allah happy and makes the world better! 😊"
    },
    {
        "question": "why do we say bismillah",
        "answer": "We say 'Bismillah' (In the name of Allah) before starting anything to ask for Allah's blessings and help. It's like saying 'Please Allah, help me do this well!' 🌟"
    },
    {
        "question": "goodbye",
        "answer": "Ma'a salama! May Allah bless you! Come back anytime you want to learn! 🌟💚"
    },
    {
        "question": "thank you",
        "answer": "You're very welcome! Remember, knowledge is a gift from Allah. Keep learning! 📚✨"
    },
]

# ============================================
# STEP 2: Teaching the Chatbot to Find Answers
# ============================================

def find_answer(user_question):
    """
    This function is like a smart detective! 🔍
    It searches through our chatbot's knowledge to find the right answer.
    
    How it works:
    1. Takes the user's question
    2. Makes it lowercase (so "Hello" and "hello" are the same)
    3. Looks through all the questions we taught it
    4. If it finds a match, returns that answer!
    """
    
    # Make the question lowercase to make matching easier
    user_question = user_question.lower().strip()
    
    # Look through each question-answer pair we taught the chatbot
    for qa_pair in chatbot_knowledge:
        # Check if the user's question contains the keywords
        if qa_pair["question"] in user_question:
            return qa_pair["answer"]
    
    # If we didn't find an answer, be honest and kind
    return "I'm still learning! 🌱 I don't know the answer to that yet. Try asking about Allah, prayer, Ramadan, or how to be kind!"

# ============================================
# STEP 3: Making Our Chatbot Safe and Kind
# ============================================

def is_safe_question(question):
    """
    This function is like a safety guard! 🛡️
    It checks if a question is appropriate and safe.
    
    We don't answer questions about:
    - Mean or hurtful topics
    - Adult topics
    - Anything that could harm someone
    """
    
    # List of words that indicate unsafe topics
    unsafe_words = ["bad", "hate", "stupid", "violence", "weapon"]
    
    # Check if the question contains any unsafe words
    question_lower = question.lower()
    for word in unsafe_words:
        if word in question_lower:
            return False
    
    return True

# ============================================
# STEP 4: The Main Chatbot Function
# ============================================

def chatbot_response(user_input):
    """
    This is the main brain of our chatbot! 🧠
    It decides what to say based on what the user types.
    """
    
    # First, check if the question is safe
    if not is_safe_question(user_input):
        return "Let's talk about kind and positive things! 😊 Ask me about Islam, prayer, or how to be a good person!"
    
    # If it's safe, find the answer!
    return find_answer(user_input)

# ============================================
# STEP 5: Starting Our Chatbot! 🎉
# ============================================

def start_chatbot():
    """
    This function starts our chatbot and lets us talk to it!
    """
    
    print("=" * 60)
    print("🌟 Welcome to Noor - Your Kind Islamic Chatbot! 🌟")
    print("=" * 60)
    print()
    print("Hi! I'm Noor, which means 'light' in Arabic! ✨")
    print("I can answer questions about Islam and help you learn!")
    print()
    print("Try asking me:")
    print("  - About Allah or Islam")
    print("  - About prayer or Ramadan")
    print("  - How to be kind")
    print("  - For a simple dua")
    print()
    print("Type 'goodbye' when you want to leave.")
    print("=" * 60)
    print()
    
    # This loop keeps the chatbot running until the user says goodbye
    while True:
        # Get input from the user
        user_input = input("You: ")
        
        # Check if user wants to leave
        if "goodbye" in user_input.lower() or "bye" in user_input.lower():
            print("Noor: Ma'a salama! May Allah bless you! 🌟💚")
            break
        
        # Get the chatbot's response
        response = chatbot_response(user_input)
        
        # Show the response
        print(f"Noor: {response}")
        print()

# ============================================
# STEP 6: Run the Chatbot!
# ============================================

# This special line checks if we're running this file directly
# If yes, start the chatbot!
if __name__ == "__main__":
    start_chatbot()

# ============================================
# 🎓 LEARNING NOTES FOR KIDS 🎓
# ============================================
"""
WHAT YOU LEARNED TODAY:

1. VARIABLES: We created a 'chatbot_knowledge' list to store information
   - Like a box that holds our chatbot's brain!

2. LISTS: We used lists (with []) to store many question-answer pairs
   - Like a collection of flashcards!

3. DICTIONARIES: Each Q&A pair uses {} to store question and answer together
   - Like a mini filing cabinet for each topic!

4. FUNCTIONS: We created special helpers (functions) like find_answer() and chatbot_response()
   - Functions are like mini-robots that do specific jobs!

5. IF/ELSE: We used if/else to make decisions
   - "If the question is safe, answer it. Else, say something kind!"

6. LOOPS: We used 'while True' to keep the chatbot running
   - Like a circle that keeps going until we say goodbye!

7. INPUT/OUTPUT: 
   - input() gets what YOU type
   - print() shows what the CHATBOT says

CHALLENGE FOR YOU! 🌟

Can you add more questions and answers to chatbot_knowledge?
Try adding:
- Your favorite Islamic story
- A dua you know
- Facts about the Prophet (PBUH)

Remember: Every big program starts with simple code like this!
You're doing AMAZING! 🚀
"""
