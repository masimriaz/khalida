##Variable and Print Statement
#chatbot_name = "Noor";
#age=10;
#print("Hello! My name is " + chatbot_name + " and I am " + str(age) + " years old.");

#Input and Output
#user_name = input("Enter your name: ");
#print("Hello, " + user_name + "! Nice to meet you.");

#Conditional Statements If-Else
#feeling = input("happy or sad? ") 
#if feeling == "happy": 
#    print("Alhamdulillah!, I'm happy") 
#else: 
#    print("Allah is with you. I'm sad")

#Lists and Loops
#fruits = ["apple", "banana", "cherry"];
#duas = ["Bismillah", "Alhamdulillah", "Subhanallah", "Istaghfirullah"];
#print(duas[0]);
#for dua in duas:
#    print(dua);

#################### Noor Chatbot ####################
# Noor says hello! 
print("As-salamu alaykum! I am Noor.");
print("I can answer simple Islamic questions.");
print("Type 'bye to end'");

#Build Noor's LLM Brain (lists)
# Noor's brain: questions + answers 
questions = ["who created us?", 
             "how many times do we pray?", 
             "what is the quran?", 
             "what is ramadan?", 
             "what do we say before eating?", 
             "who is prophet Muhammad?",
             "Who is the last Prophet?",
             "How many pillars are in Islam?" ] 
answers = ["Allah (SWT) created us!", 
           "We pray 5 times a day.", 
           "The Quran is Allah's message.", 
           "Ramadan is the blessed month of fasting.", 
           "We say Bismillah before eating.", 
           "Prophet Muhammad ﷺ is our final messenger.",
            "Prophet Muhammad ﷺ is the last Prophet.",
            "There are 5 pillars in Islam." ]
#Ask the user for a question
user_question = input("Ask me a question: ").lower();

#searcgh Noor's brain for the answer
found = False 
for i in range(len(questions)): 
    if questions[i] in user_question: print("Noor:", answers[i])  
    else: print("Noor: Sorry, I don't know the answer to that question.")
    found = True 
    break
