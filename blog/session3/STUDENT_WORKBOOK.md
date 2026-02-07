# 🐍 AI Superheroes Session 3: Student Workbook

## Building Noor - My Islamic Chatbot with Python!

**Name:** ************\_************  
**Date:** February 7, 2026  
**My Chatbot's Name:** ************\_************

---

## 📖 The Python Story

**Fill in the blanks as we learn!**

Python was created by ********\_******** (person's name).

It's called Python after a ********\_******** (TV show / animal).

We love Python because it's:

- ☐ Easy to read
- ☐ Powerful
- ☐ Fun
- ☐ Free

---

## 🏗️ Part 1: Variables (Treasure Boxes)

### What I Learned:

A **variable** is like a ********\_******** that holds information.

### My Practice Code:

```python
# Create variables about yourself!
my_name = "_______________"
my_age = _____
favorite_subject = "_______________"

print("Hello! My name is", my_name)
print("I am", my_age, "years old")
print("I love learning about", favorite_subject)
```

**Did it work?** ☐ Yes! ☐ Not yet (that's OK!)

**What I learned from mistakes:**

---

---

---

## 🎤 Part 2: Input & If/Else

### What I Learned:

**input()** lets my program ********\_******** a question.

**if/else** helps my program make ********\_********.

### My Practice Code:

```python
# Create a greeting bot!
time_of_day = input("What time is it? (morning/afternoon/evening) ")

if time_of_day == "morning":
    print("___________________________________")
elif time_of_day == "afternoon":
    print("___________________________________")
elif time_of_day == "evening":
    print("___________________________________")
else:
    print("Have a blessed day!")
```

**Important Rule:** After `if`, `elif`, and `else`, I must use a **\_\_\_** (symbol)

**And I must ********\_******** the next line! (hint: press Tab or Space 4 times)**

---

## 📚 Part 3: Lists (The Backpack)

### What I Learned:

A **list** stores ********\_******** items in one place.

In Python, lists use these brackets: [ ]

Counting in lists starts at **\_** (not 1!)

### My Practice Code:

```python
# Create Q&A lists about Islam
my_questions = [
    "_____________________________________",
    "_____________________________________",
    "_____________________________________"
]

my_answers = [
    "_____________________________________",
    "_____________________________________",
    "_____________________________________"
]

# Test it!
print("Q:", my_questions[0])
print("A:", my_answers[0])
```

---

## 🤖 Part 4: Building Noor - The Complete Chatbot!

### Step 1: Welcome Message ✅

```python
print("╔════════════════════════════════╗")
print("║   As-salamu alaykum! 🌙       ║")
print("║   I am Noor, your kind        ║")
print("║   Islamic helper chatbot!     ║")
print("╚════════════════════════════════╝")
```

**My chatbot's custom welcome:**

```python
print("___________________________________")
print("___________________________________")
```

---

### Step 2: Get User's Name ✅

```python
user_name = input("What is your name? ")
print("Nice to meet you,", user_name, "!")
```

---

### Step 3: Q&A Database ✅

**I added these questions to my chatbot:**

1. ***
2. ***
3. ***
4. ***
5. ***

---

### Step 4: The Main Loop (The Brain!) ✅

**This is the most important part! Follow along carefully.**

```python
while True:
    user_question = input(user_name + ": ").lower()

    if user_question == "bye":
        print("Goodbye!")
        break

    found_answer = False

    for i in range(len(questions)):
        if questions[i] in user_question:
            print("Noor:", answers[i])
            found_answer = True
            break

    if not found_answer:
        print("I'm still learning!")
```

**What does `.lower()` do?**

---

**What does `break` do?**

---

---

## 🧪 Testing My Chatbot

### Questions I Tested:

1. ***
   - ☐ Worked! ☐ Didn't work

2. ***
   - ☐ Worked! ☐ Didn't work

3. ***
   - ☐ Worked! ☐ Didn't work

### Bugs I Found and Fixed:

**Bug:** ******************\_\_\_\_******************
**Fix:** ******************\_\_\_\_******************

**Bug:** ******************\_\_\_\_******************
**Fix:** ******************\_\_\_\_******************

---

## 🐛 Debugging Checklist

**If my code doesn't work, I will check:**

☐ Did I spell everything correctly?  
☐ Did I use quotes `"` around text?  
☐ Did I use a colon `:` after if/elif/else?  
☐ Did I indent properly? (Tab or 4 spaces)  
☐ Did I match my variable names exactly?  
☐ Did I close all my brackets `[ ]` and parentheses `( )`?

---

## 🚀 Extension Ideas (Try at Home!)

**Check off what you want to try:**

☐ **Add more Q&A** - Make Noor smarter!  
☐ **Add greetings** - Respond to "salam" and "hello"  
☐ **Add stories** - Tell Islamic stories  
☐ **Add duas** - Suggest prayers for different times  
☐ **Add emojis** - Make responses more fun!  
☐ **Safety check** - Warn about private information  
☐ **Question counter** - Count how many questions asked

**My own creative idea:**

---

---

---

## 📝 Today I Learned...

### 3 Things I'm Proud Of:

1. ***
2. ***
3. ***

### 1 Thing That Was Hard:

---

### How I Solved It (or will solve it):

---

---

---

## 🎯 My Goals for Next Session

**By next session, I will:**

1. ***
2. ***
3. ***

---

## 🏆 Python Skills Unlocked!

**Check off what you can do now:**

☐ Explain what Python is  
☐ Create variables  
☐ Use `print()` to show messages  
☐ Use `input()` to ask questions  
☐ Write `if/else` statements  
☐ Create and use lists  
☐ Build a complete chatbot  
☐ Test and debug my code  
☐ Explain how my chatbot works

---

## 💬 Share Your Success!

**I will show my chatbot to:**
☐ Mom/Dad  
☐ Siblings  
☐ Friends  
☐ Teacher  
☐ Grandparents

**When someone asks "How does it work?", I will explain:**

---

---

---

---

## 🤲 Islamic Values I Used Today

**Check off the values you practiced:**

☐ **Patience (Sabr)** - When code didn't work first try  
☐ **Perseverance** - Kept trying until it worked  
☐ **Helping Others** - Helped a classmate  
☐ **Seeking Knowledge** - Asked questions when confused  
☐ **Excellence (Ihsan)** - Did my best work

---

## 🌟 Homework Challenge

### This Week's Mission:

1. Add 5 new Q&A pairs to Noor
2. Teach Noor to tell one Islamic story
3. Test with 3 different people
4. Write down questions Noor struggled with
5. Bring to Session 4 to share!

### People I Tested With:

1. ********\_******** - Feedback: ********\_********
2. ********\_******** - Feedback: ********\_********
3. ********\_******** - Feedback: ********\_********

---

## 📸 Memory Box

**Draw or paste a picture of:**

- Your chatbot running on the screen
- You and your coding partner
- Your favorite line of code
- Anything else from today!

[ SPACE FOR DRAWING/PHOTO ]

---

## 🎉 Certificate Section

**I, ************\_************, successfully completed**  
**AI Superheroes Session 3: Python Programming!**

**Date:** February 7, 2026  
**Signature:** ************\_************  
**Teacher Signature:** ************\_************

---

## 💭 Reflection Corner

**The coolest thing I learned today:**

---

---

**Something I want to learn more about:**

---

---

**How I felt when my chatbot worked:**
☐ 🤩 Amazing!  
☐ 😊 Happy!  
☐ 😎 Proud!  
☐ 🎉 Excited!  
☐ All of the above!

**My favorite part of today's session:**

---

---

---

## 🔮 Looking Ahead - Session 4 Preview

**Next time we'll learn:**

- Making Noor smarter with AI
- Adding voice to our chatbot
- Understanding questions better
- Saving past conversations
- Local AI models

**I'm most excited about:**

---

---

## 📚 Resources to Explore at Home

**Practice Python:**

- Python.org (tutorials)
- Code.org (fun games)
- Your chatbot code!

**Learn Islamic Knowledge (to add to Noor):**

- Ask parents/teachers
- Islamic books for kids
- Quran and Hadith apps

---

## 🌈 Notes & Doodles

**Use this space for:**

- Code snippets you want to remember
- Drawings of how your chatbot thinks
- Ideas for future improvements
- Doodles and creative thoughts!

---

---

---

---

---

---

---

---

**Remember: You are an AI Superhero Coder! 💪🦸‍♀️🦸‍♂️**

**Keep coding, keep learning, keep being awesome! 🌟**

**As-salamu alaykum wa rahmatullahi wa barakatuh! ✨**

---

_AI Superheroes Workshop - Session 3_  
_Khalida Foundation_  
_February 7, 2026_
