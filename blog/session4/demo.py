
# name = "Ayesha";
# age= 10;
# input("What is your name? ");
# print("Hello, " + name + "! You are " + str(age) + " years old."); #output: Hello, Ayesha! You are 10 years old.
# if age > 10:
#     print("Your age is greater than 10");

# fruits = ["apple", "banana", "cherry"]; 
# duas = ["Bismillah", "Alhamdulillah", "Subhanallah", "Istaghfirullah"];
# print(fruits[0]); # Output: apple
# for dua in duas: 
#     print(dua);

######################################################################################3

#The Concept: What's a Dictionary?
#Real-world analogy: "A dictionary pairs questions with answers. Key = question, Value = answer."
#Contact card example: "Like a contact card: 'Name' → 'Alice', 'Age' → '11'."

# Noor learns to remember!
# questions = ["who created us?", #Question 0
#              "how many times do we pray?", 
#              "what is the quran?", 
#              "what is ramadan?", 
#              "what do we say before eating?", 
#              "who is prophet Muhammad?",
#              "Who is the last Prophet?",
#              "How many pillars are in Islam?" ] 
# answers = ["Allah (SWT) created us!", #Answer 0
#            "We pray 5 times a day.", 
#            "The Quran is Allah's message.", 
#            "Ramadan is the blessed month of fasting.", 
#            "We say Bismillah before eating.", 
#            "Prophet Muhammad ﷺ is our final messenger.",
#             "Prophet Muhammad ﷺ is the last Prophet.",
#             "There are 5 pillars in Islam." ]

# question_answer_dict = {
#     "who created us?": "Allah (SWT) created us!",
#     "how many times do we pray?": "We pray 5 times a day.",
#     "what is the quran?": "The Quran is Allah's message.",
#     "what is ramadan?": "Ramadan is the blessed month of fasting.",
#     "what do we say before eating?": "We say Bismillah before eating.",
#     "who is prophet Muhammad?": "Prophet Muhammad ﷺ is our final messenger.",
#     "Who is the last Prophet?": "Prophet Muhammad ﷺ is the last Prophet.",
#     "How many pillars are in Islam?": "There are 5 pillars in Islam."
# }

# fruits = ["apple", "banana", "cherry",2]; 
# print(fruits[3]); # Output: apple
# user_profile = {
#     "name": "Khadijah", #key-value pair
#     "favorite_dua": "Bismillah",
#     "age": 14, #key-value pair
#     "My favorite pet name is": "Simba"
# }
# print(user_profile["name"]); # Output: Khadijah
# print(user_profile["favorite_dua"]); # Output: Bismillah
# print(user_profile["age"]); # Output: 14

# Get user input
# user_input = input("Hello! Please tell me about yourself: ")

# # When the user says their name
# if "my name is" in user_input:
#     name = user_input.split("my name is ")[1]
#     user_profile["name"] = name
#     print("Noor: Nice to meet you, " + name)

# # Greeted with memory
# if user_profile["name"]:
#     print("Welcome back, " + user_profile["name"] + "!")

# # When the user shares their favorite dua
# if "my favorite dua is" in user_input:
#     dua = user_input.split("my favorite dua is ")[1]
#     user_profile["favorite_dua"] = dua
#     print("Noor: That's a beautiful dua! I'll remember that.")

# Test Case 1: Prayer question
test_input = "How many times do we pray?"
expected = "5 times a day"
actual = input("How many times do we pray?")
if expected in actual:
    print("✅ Test 1 PASSED!")
else:
    print("❌ Test 1 FAILED")
    print("Expected:", expected)
    print("Got:", actual)