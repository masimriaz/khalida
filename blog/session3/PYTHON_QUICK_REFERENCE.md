# 🐍 Python Quick Reference Card for Kids

## AI Superheroes - Session 3 Cheat Sheet

---

## 📦 VARIABLES (Treasure Boxes)

**Creating a Variable:**

```python
name = "Noor"              # Text (string)
age = 10                   # Number (integer)
is_kind = True             # True/False (boolean)
```

**Rules:**

- No spaces in names (use_underscore)
- Start with letter (not number)
- Case matters: `Name` ≠ `name`

---

## 🖨️ PRINT (Show Messages)

**Basic Print:**

```python
print("Hello!")                    # Shows: Hello!
print("My name is", name)          # Shows: My name is Noor
print(name, "is", age, "years old") # Shows: Noor is 10 years old
```

**Special Characters:**

```python
print()         # Empty line (spacing)
\n              # New line inside text
```

---

## 🎤 INPUT (Ask Questions)

**Getting Input:**

```python
name = input("What is your name? ")
age = input("How old are you? ")
```

**Important:**

- Input always returns TEXT (even if you type a number!)
- To get a number: `age = int(input("Age? "))`

---

## 🤔 IF/ELSE (Making Decisions)

**Basic If:**

```python
if age == 10:
    print("You're 10!")
```

**If-Elif-Else:**

```python
if time == "morning":
    print("Good morning!")
elif time == "afternoon":
    print("Good afternoon!")
else:
    print("Hello!")
```

**Rules:**

- Use `:` (colon) after if/elif/else
- INDENT the code inside (Tab or 4 spaces)
- Use `==` to check if equal (not `=`)

**Comparison Symbols:**

```python
==    # Equal to
!=    # Not equal to
>     # Greater than
<     # Less than
>=    # Greater or equal
<=    # Less or equal
```

---

## 📚 LISTS (The Backpack)

**Creating Lists:**

```python
names = ["Ali", "Fatima", "Yusuf"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Noor", 10, True]
```

**Accessing Items:**

```python
names[0]    # First item → "Ali"
names[1]    # Second item → "Fatima"
names[2]    # Third item → "Yusuf"
```

**Remember:** Counting starts at 0!

**List Actions:**

```python
names.append("Ahmad")     # Add to end
len(names)                # Count items (length)
```

---

## 🔄 LOOPS (Repeat Actions)

**While Loop (Keep Going):**

```python
while True:
    # This runs forever (until break)
    answer = input("Continue? (yes/no) ")
    if answer == "no":
        break    # Stop the loop!
```

**For Loop (Count Through):**

```python
for i in range(5):
    print(i)    # Shows: 0, 1, 2, 3, 4

for name in names:
    print(name)    # Shows each name
```

---

## 🔍 CHECKING IF SOMETHING IS IN TEXT

**The `in` Operator:**

```python
if "pray" in user_question:
    print("Let me tell you about prayer!")
```

**The `.lower()` Method:**

```python
text = "HELLO"
text.lower()    # Makes it: "hello"
```

---

## 💬 COMMENTS (Notes for Yourself)

**Single Line:**

```python
# This is a comment - Python ignores it!
name = "Noor"  # You can add comments after code too
```

**Multi-Line:**

```python
"""
This is a long comment
across multiple lines!
"""
```

---

## 🐛 COMMON ERRORS & FIXES

| Error              | What It Means           | Fix                        |
| ------------------ | ----------------------- | -------------------------- |
| `IndentationError` | Wrong spacing           | Use consistent tabs/spaces |
| `NameError`        | Variable not found      | Check spelling             |
| `SyntaxError`      | Missing `:` or `"`      | Add missing symbol         |
| `IndexError`       | List item doesn't exist | Check list length          |

---

## 🎨 STRING TRICKS

**Combining Strings:**

```python
first = "As-salamu"
last = "alaykum"
greeting = first + " " + last    # "As-salamu alaykum"
```

**Special Characters:**

```python
\n    # New line
\t    # Tab
```

---

## 🤖 CHATBOT PATTERN

**Basic Chatbot Structure:**

```python
# 1. Welcome
print("Welcome!")

# 2. Get name
name = input("What is your name? ")

# 3. Set up Q&A
questions = ["question1", "question2"]
answers = ["answer1", "answer2"]

# 4. Main loop
while True:
    user_input = input("Ask: ").lower()

    if user_input == "bye":
        break

    found = False
    for i in range(len(questions)):
        if questions[i] in user_input:
            print(answers[i])
            found = True
            break

    if not found:
        print("I don't know that yet!")

# 5. Goodbye
print("Goodbye!")
```

---

## 🎯 PYTHON TIPS FOR SUCCESS

**Before Running Code:**

1. ✅ Save your file (.py)
2. ✅ Check for typos
3. ✅ Check indentation
4. ✅ Check all quotes and brackets match

**When Debugging:**

1. Read error message carefully
2. Check the line number it mentions
3. Look for:
   - Missing `:` after if/while/for
   - Missing `"` around text
   - Wrong indentation
   - Typos in variable names

**Best Practices:**

- Use clear variable names
- Add comments to explain code
- Test small pieces before combining
- Save often!

---

## 🌟 PYTHON WORDS TO KNOW

| Word        | What It Means                |
| ----------- | ---------------------------- |
| `print()`   | Show a message               |
| `input()`   | Ask a question               |
| `if`        | If this is true...           |
| `elif`      | Else if...                   |
| `else`      | Otherwise...                 |
| `while`     | Keep doing this              |
| `for`       | Do this for each item        |
| `break`     | Stop the loop                |
| `True`      | Yes                          |
| `False`     | No                           |
| `len()`     | Count items                  |
| `range()`   | Make a sequence of numbers   |
| `.lower()`  | Make text lowercase          |
| `.append()` | Add to a list                |
| `in`        | Check if something is inside |

---

## 🛡️ SAFETY REMINDERS

**Never share in code:**

- ❌ Real addresses
- ❌ Phone numbers
- ❌ Passwords
- ❌ Credit card info

**Chatbot should:**

- ✅ Be kind and respectful
- ✅ Say "I don't know" when unsure
- ✅ Give accurate information
- ✅ Respect all people

---

## 🚀 QUICK DEBUGGING CHECKLIST

When your code doesn't work:

☐ Read the error message  
☐ Check line number mentioned  
☐ Look for red underlines in editor  
☐ Check spelling of variables  
☐ Check indentation (all same)  
☐ Check for missing `:` after if/while  
☐ Check all `"` and `(` are closed  
☐ Try printing variables to see values  
☐ Ask for help if stuck!

---

## 💡 REMEMBER

**Every coder:**

- Makes mistakes (that's how we learn!)
- Starts as a beginner
- Asks questions
- Practices to get better

**You are a REAL coder!** 🐍💪

---

## 📝 PRACTICE EXERCISES

**Easy:**

1. Make a variable with your favorite color
2. Print a welcome message
3. Ask for user's age

**Medium:** 4. Make a list of 5 duas 5. Use if/else to check if number > 10 6. Print each item in a list using a loop

**Challenge:** 7. Make a simple quiz with 3 questions 8. Count how many times user says "yes" 9. Add greetings to your chatbot

---

**Keep this card nearby when coding!**  
**You've got this, AI Superhero! 🌟**

---

_AI Superheroes Workshop_  
_Khalida Foundation - February 2026_  
_Print this card and keep it at your desk!_
