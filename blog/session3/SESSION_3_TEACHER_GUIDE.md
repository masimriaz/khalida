# AI Superheroes Session 3: Teacher's Guide

## Coding Our Islamic Chatbot with Python

**Target Audience:** Kids aged 9-14  
**Duration:** 90 minutes  
**Prior Knowledge:** Sessions 1 & 2 completed  
**Materials Needed:** Computers with Python installed, projector, whiteboard

---

## 🎯 Learning Objectives

By the end of this session, students will be able to:

1. ✅ Explain what Python is and why it's used for AI
2. ✅ Create and use variables to store information
3. ✅ Use `print()` to display messages
4. ✅ Use `input()` to get user responses
5. ✅ Write `if/else` statements to make decisions
6. ✅ Create and use lists to store Q&A pairs
7. ✅ Build a working Islamic chatbot from scratch
8. ✅ Test and debug their code
9. ✅ Understand responsible AI coding practices

---

## 📋 Pre-Session Preparation

### For Teachers:

- [ ] Install Python 3.8+ on all student computers
- [ ] Test Python installation (`python --version` in terminal)
- [ ] Set up a code editor (VS Code, Thonny, or IDLE)
- [ ] Prepare the example chatbot code to demonstrate
- [ ] Print physical "treasure box" labels for variables demonstration
- [ ] Prepare flashcards for lists demonstration
- [ ] Have backup USB drives with Python installer
- [ ] Test projector setup

### Materials Checklist:

- [ ] Index cards (for "treasure box" variable activity)
- [ ] Markers/pens
- [ ] Printed code samples (optional backup if tech fails)
- [ ] Celebration stickers/certificates
- [ ] Snacks for break time

---

## ⏰ Detailed Timeline (90 Minutes)

### 🎬 SEGMENT 1: Welcome & Story Time (0-10 min)

**What to Do:**

1. **Greet students warmly** - "Welcome back, AI Superheroes!"
2. **Quick recap** - Ask volunteers:
   - "What did we learn in Session 1?" (AI basics, patterns)
   - "What did we build in Session 2?" (Noor chatbot design)
3. **Introduce today's adventure**: "Today we become REAL coders!"
4. **Tell the Python Story** (see blog post):
   - Who created Python (Guido van Rossum)
   - Why it's called Python (Monty Python TV show, not the snake!)
   - Why we love it (easy to read, powerful, fun)

**Teaching Tips:**

- Use enthusiasm! Your energy sets the tone
- Show Python logo on screen (🐍)
- Ask: "Who has heard of Python before?"
- Emphasize: "Python is like having a conversation with a computer!"

**Engagement Check:**

- "Raise your hand if you're excited to code!"
- "Who thinks they can teach Python to someone at home today?"

---

### 🏗️ SEGMENT 2: Python Basics Part 1 - Variables & Print (10-25 min)

**Concept 1: Variables (The Treasure Box)**

**Story Time (3 min):**
Tell the treasure box story from the blog post. Use physical demonstration:

- Show an index card labeled `chatbot_name`
- Write "Noor" on a piece of paper and put it "in" the box
- Say: "This is a variable! A labeled box that holds information!"

**Live Coding Demo (5 min):**

```python
# Type this on the projector, explain each line
chatbot_name = "Noor"
age = 10
is_kind = True

print("Variables created!")
```

**Key Points to Emphasize:**

- Variable names should be descriptive (no spaces, use underscore)
- `=` means "put this value in the box"
- Different types: text (strings), numbers, True/False

**Concept 2: Print (Making the Computer Talk)**

**Live Coding Demo (3 min):**

```python
print("As-salamu alaykum!")
print("My name is", chatbot_name)
print("I am", age, "years old")
```

**Interactive Moment:**

- Ask students to predict what will appear on screen
- Run the code together
- Celebrate: "You just made the computer speak Arabic!"

**👥 HANDS-ON ACTIVITY #1 (7 min):**

**Instructions:**
"Now it's YOUR turn! Create three variables about yourself and print them!"

Give students this starter template:

```python
# Your turn! Fill in your information
my_name = "___________"
my_age = __
favorite_subject = "___________"

print("Hello! My name is", my_name)
print("I am", my_age, "years old")
print("I love learning about", favorite_subject)
```

**Walk around and help!**

- Check for syntax errors (missing quotes, parentheses)
- Celebrate successes loudly
- Help struggling students patiently

**Share Out (2 min):**

- Ask 2-3 volunteers to run their code for the class
- Applaud each one!

**✅ CHECKPOINT #1:**
"Give yourself a high-five! You just learned how computers remember things!"

---

### 🎤 SEGMENT 3: Python Basics Part 2 - Input & If/Else (25-40 min)

**Concept 3: Input (Asking Questions)**

**Story Time (2 min):**
Tell the Smart Robot story from the blog.

**Live Coding Demo (4 min):**

```python
# Let's ask the user their name!
user_name = input("What is your name? ")
print("Nice to meet you,", user_name, "!")
```

**Run it together:**

- Type a name when prompted
- Watch it respond
- "Wow! The computer is listening to us!"

**Concept 4: If/Else (Making Decisions)**

**Story Continuation (2 min):**
"Now the robot needs to make choices based on what we say..."

**Live Coding Demo (6 min):**

```python
feeling = input("How are you feeling? (happy/sad) ")

if feeling == "happy":
    print("Alhamdulillah! I'm happy too! 😊")
elif feeling == "sad":
    print("Don't worry! Allah is always with you. 🤲")
else:
    print("I hope you have a blessed day!")
```

**Teaching Points:**

- `if` = "If this is true, do this!"
- `elif` = "Else if" (another condition)
- `else` = "If nothing else matched, do this"
- **INDENTATION MATTERS!** (4 spaces or 1 tab)
- `==` means "is equal to" (not `=`)

**Common Mistakes to Watch For:**

- Forgetting the colon (`:`) after if/elif/else
- Wrong indentation
- Using `=` instead of `==`
- Forgetting quotes around text

**👥 HANDS-ON ACTIVITY #2 (8 min):**

**Challenge:** Build a Greeting Bot

Give students this template:

```python
# Greeting Bot Challenge!
time_of_day = input("What time is it? (morning/afternoon/evening) ")

if time_of_day == "morning":
    print("Good morning! Start your day with Bismillah!")
elif time_of_day == "afternoon":
    print("Good afternoon! Hope your day is blessed!")
elif time_of_day == "evening":
    print("Good evening! Don't forget your evening dua!")
else:
    print("Have a blessed day!")
```

**Extension for Fast Finishers:**
"Try adding more times: night, lunch, school, etc."

**Share Out (3 min):**

- Ask 2-3 students to demonstrate
- Test with different inputs
- Celebrate each one!

**✅ CHECKPOINT #2:**
"Amazing! Your programs can now TALK and THINK! You're real coders!"

---

### 📚 SEGMENT 4: Python Basics Part 3 - Lists (40-55 min)

**Concept 5: Lists (The Backpack)**

**Story Time (3 min):**
Tell the backpack story. Physical demonstration:

- Show flashcards in a row
- Label them: Index 0, 1, 2, 3
- "Computers always count from ZERO!"

**Live Coding Demo (6 min):**

```python
# Create a list of duas
duas = ["Bismillah", "Alhamdulillah", "SubhanAllah"]

# Access items (counting from 0!)
print(duas[0])    # First item
print(duas[1])    # Second item
print(duas[2])    # Third item

# Add a new item
duas.append("MashaAllah")
print(duas)       # Show all items
```

**Key Teaching Points:**

- Lists use square brackets `[ ]`
- Items separated by commas
- Counting starts at 0 (not 1!)
- Can add items with `.append()`
- Can have text, numbers, or mixed items

**Why Lists for Chatbots? (2 min)**

**Explain:**
"Our chatbot needs to remember MANY questions and answers. Lists are perfect for this!"

```python
questions = ["Who created us?", "How many times do we pray?"]
answers = ["Allah created us!", "We pray 5 times a day!"]

# Match question 0 with answer 0!
```

**👥 HANDS-ON ACTIVITY #3 (6 min):**

**Challenge:** Create Your Q&A Lists

Template:

```python
# Your Islamic Q&A
my_questions = [
    "question 1 here",
    "question 2 here",
    "question 3 here"
]

my_answers = [
    "answer 1 here",
    "answer 2 here",
    "answer 3 here"
]

# Test it!
print("Q:", my_questions[0])
print("A:", my_answers[0])
```

**Walk around:**

- Help students think of kid-friendly Islamic Q&A
- Check syntax (quotes, commas)
- Celebrate creativity!

**✅ CHECKPOINT #3:**
"You're ready! You know ALL the basics! Time to build our chatbot!"

---

### 🤖 SEGMENT 5: Build the Chatbot! (55-75 min)

**Introduction (2 min):**
"Now we put EVERYTHING together! Follow along step by step!"

**Building Strategy:**
Build incrementally, test after each step!

**Step 1: Welcome Message (3 min)**
Type together on projector:

```python
print("╔════════════════════════════════╗")
print("║   As-salamu alaykum! 🌙       ║")
print("║   I am Noor, your kind        ║")
print("║   Islamic helper chatbot!     ║")
print("╚════════════════════════════════╝")
```

**TEST:** Run it! See the welcome message!

**Step 2: Get User's Name (2 min)**

```python
user_name = input("What is your name? ")
print("Nice to meet you,", user_name, "! 😊\n")
```

**TEST:** Run it! Type a name!

**Step 3: Q&A Database (4 min)**

```python
questions = [
    "who created us",
    "how many times do we pray",
    "what do we say before eating"
]

answers = [
    "Allah (SWT) created us! ☝️",
    "We pray 5 times a day! 🕌",
    "We say Bismillah! 🍎"
]
```

**Pause for student input:**
"Who wants to suggest another question to add?"
Add 2-3 more from volunteers.

**Step 4: The Loop (10 min) - MOST IMPORTANT PART!**

**Explain before coding:**
"This is the brain! The chatbot will keep asking questions until we say 'bye'."

```python
print("Ask me anything about Islam!")
print("Type 'bye' when you want to leave.\n")

while True:
    user_question = input(user_name + ": ").lower()

    if user_question == "bye":
        print("Noor: Wa alaykumu as-salam! 🤲")
        break

    found_answer = False

    for i in range(len(questions)):
        if questions[i] in user_question:
            print("Noor:", answers[i])
            found_answer = True
            break

    if not found_answer:
        print("Noor: I'm still learning! 🤔")

    print()
```

**Break this down SLOWLY:**

1. **`while True:`** - "Keep going forever (until we say break)"
2. **`.lower()`** - "Make everything lowercase so 'WHO' = 'who'"
3. **`if user_question == "bye":`** - "Check if they want to exit"
4. **`break`** - "Stop the loop!"
5. **`for i in range(len(questions)):`** - "Check each question"
6. **`if questions[i] in user_question:`** - "If our question is IN what they typed"
7. **`found_answer = False/True`** - "Did we find a match?"

**Teaching Strategy:**

- Draw a flowchart on whiteboard
- Act it out with volunteers
- "Computer starts at top, goes line by line"

**🎉 CELEBRATION MOMENT (2 min):**
"Let's run the COMPLETE chatbot!"

Type "Who created us?" → Watch it respond!
Type "bye" → Watch it exit!

**CELEBRATE LOUDLY:**
"YOU BUILT A REAL CHATBOT! YOU ARE CODERS!"

**Final Code Review (5 min):**
Show the complete code on screen:

```python
# Complete chatbot shown in blog post
```

**Offer to save/share:**
"I'll share this code with everyone. Save it as `noor_chatbot.py`"

---

### 🎉 SEGMENT 6: Test & Celebrate (75-85 min)

**Testing Party (7 min):**

**Activity: Partner Testing**
"Pair up! Test each other's chatbots!"

**Instructions:**

1. Partner A runs their chatbot
2. Partner B asks 3 questions
3. Switch roles!

**Walk around:**

- Help with errors
- Take photos/videos of successes
- Celebrate every working chatbot!

**Share Out (3 min):**
"Who wants to show their chatbot to the whole class?"

Pick 2-3 volunteers to demonstrate on the projector.

**✅ FINAL CELEBRATION:**
"Stand up if your chatbot worked!"
"Give yourselves a huge round of applause!"
"You are officially PYTHON PROGRAMMERS!"

---

### 🚀 SEGMENT 7: What's Next (85-90 min)

**Quick Preview (3 min):**
"Next time we'll make Noor even smarter with AI and voice!"

**Homework Challenge:**
Show the extension ideas from blog post:

- Add 5 new Q&A pairs
- Add greetings
- Add a story
- Test with 3 people

**Closing (2 min):**

- Thank everyone
- Reminder: Practice at home
- "See you next session, Code Warriors!"

---

## 🛡️ Troubleshooting Guide

### Common Student Errors & Fixes

| Error                                 | Cause                                    | Fix                                     |
| ------------------------------------- | ---------------------------------------- | --------------------------------------- |
| `IndentationError`                    | Wrong spacing                            | Show them to use consistent tabs/spaces |
| `NameError: name 'x' is not defined`  | Typo in variable name                    | Check spelling matches exactly          |
| `SyntaxError: invalid syntax`         | Missing `:` or quotes                    | Point to the line, find missing symbol  |
| Chatbot doesn't respond               | Keywords don't match                     | Explain `.lower()` and `in` operator    |
| `IndexError: list index out of range` | Trying to access item that doesn't exist | Check list length and index number      |

### What If Tech Fails?

**Backup Plan:**

1. Use one computer with projector
2. Do "call and response" coding (you type, they watch)
3. Give printed code to follow along
4. Promise to run their code next session

---

## 🎓 Extension Activities

### For Fast Finishers:

1. **Add emoji moods** to responses
2. **Create greeting detector** (responds to "salam", "hello")
3. **Add a counter** (how many questions asked)
4. **Make colorful output** (using ANSI codes)
5. **Add random responses** (variety in answers)

### Advanced Challenge:

```python
import random

greetings = ["As-salamu alaykum!", "Hello friend!", "Welcome!"]
print(random.choice(greetings))
```

---

## 📊 Assessment/Success Indicators

**Students successfully learned if they can:**

- [ ] Explain what a variable is (treasure box analogy)
- [ ] Write a print statement independently
- [ ] Create an if/else statement
- [ ] Create and access items in a list
- [ ] Run their chatbot without errors
- [ ] Test and debug simple mistakes
- [ ] Explain how their chatbot works to a partner

**Participation Indicators:**

- Engaged during story times
- Asked questions when confused
- Helped classmates
- Showed excitement when code worked
- Volunteered to share

---

## 🌟 Tips for Success

### Classroom Management:

1. **Set expectations early**: "We code together, we help each other"
2. **Use "freeze" signal**: When you need attention
3. **Celebrate mistakes**: "Errors are how we learn!"
4. **Pair struggling students** with patient helpers
5. **Have fidget tools** for kinesthetic learners

### Pacing:

- **Don't rush!** Better to finish less but understand more
- **Check for understanding** after each concept
- **Use the "thumbs" system**: Up=got it, Side=unsure, Down=help
- **Take a 5-min stretch break** around minute 45

### Making It Fun:

- Use silly examples occasionally
- Let kids name their chatbot
- Award "Bug Buster" stickers for finding errors
- End with a "Code of the Day" award
- Take group photo with working chatbots

### Cultural Sensitivity:

- Respect all students' Islamic knowledge levels
- Some may know more, some less - both OK!
- Encourage questions about Islamic concepts
- Verify Islamic information is accurate
- Emphasize: chatbot is a learning tool, not a scholar

---

## 📝 Follow-Up for Next Session

**Send home with students:**

1. Copy of their chatbot code
2. Extension challenge sheet
3. Celebration certificate
4. Link to Python learning resources

**For teachers to prepare:**

1. Collect student code samples (with permission)
2. Note which concepts need review
3. Prepare advanced topics for Session 4
4. Share photos/videos with parents (with consent)

---

## 🤲 Islamic Teaching Points

Throughout the session, weave in:

- **Patience** (Sabr): "Coding requires patience - Allah loves those who are patient"
- **Perseverance**: "Keep trying! The Prophet ﷺ never gave up"
- **Helping others**: "The best of people are those who help others - Hadith"
- **Seeking knowledge**: "Seeking knowledge is obligatory - Hadith"
- **Excellence** (Ihsan): "Allah loves when you do your work with excellence"

---

## 📚 Additional Resources

**For Teachers:**

- [Python.org Documentation](https://docs.python.org/3/)
- [Real Python - Teaching Kids](https://realpython.com/)
- [Thonny IDE](https://thonny.org/) - Beginner-friendly
- [Islamic Education Resources](https://khalidafoundation.org)

**For Students:**

- [Code.org](https://code.org)
- [Scratch](https://scratch.mit.edu/) - Visual programming
- [Python for Kids book](https://nostarch.com/pythonforkids)

---

## ✅ Session Checklist

**Before Session:**

- [ ] Python installed and tested
- [ ] Code editor ready
- [ ] Projector working
- [ ] Materials printed/prepared
- [ ] Backup plan ready
- [ ] Snacks/water available

**During Session:**

- [ ] Take attendance
- [ ] Start on time
- [ ] Check understanding frequently
- [ ] Walk around to help
- [ ] Take photos (with consent)
- [ ] Celebrate successes
- [ ] Handle errors positively

**After Session:**

- [ ] Share code with students
- [ ] Send parent update email
- [ ] Note what worked/didn't work
- [ ] Plan improvements for next time
- [ ] Follow up with struggling students

---

## 💚 Final Teacher Notes

Remember: **You are planting seeds of curiosity, problem-solving, and confidence!**

Some kids will "get it" immediately. Others will struggle. Both are 100% normal and okay!

Your job is to:

1. Make it fun
2. Keep it safe (emotionally and content-wise)
3. Celebrate every small win
4. Foster a growth mindset
5. Build confidence

The goal isn't to create perfect coders in 90 minutes.

The goal is to show them: **"I CAN DO THIS. I CAN CODE. I CAN BUILD THINGS."**

And you're doing amazing. Keep going, teacher! 💪

---

**Questions or need help? Contact: khalidafoundation@example.com**

**Share your success stories with #AISuperheroesKids**

---

_Last updated: February 7, 2026_  
_Version: 1.0_  
_Created with ❤️ for Khalida Foundation_
