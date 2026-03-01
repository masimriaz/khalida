##Variable and Print Statement
#chatbot_name = "Noor";
#age=10;
#print("Hello! My name is " + chatbot_name + " and I am " + str(age) + " years old.");

#Input and Output
#user_name = input("Enter your name: "); #Input
#a = input("Enter a number: ");
#b = input("Enter another number: ");
#print(str(int(a) + int(b))); #Output

#print("Hello, " + user_name + "! Nice to meet you.");

#Conditional Statements If-Else
#feeling = input("happy or sad? ") 
#if feeling == "happy": 
#    print("Alhamdulillah!, I'm happy") 
#else: 
#    print("Allah is with you. I'm sad")


#List is type of variable that can store multiple values. It is ordered and changeable. You can access items by their index, 
# and you can also add or remove items from the list. For example:
#Lists and Loops
#fruits = ["apple", "banana", "cherry"]; 
#duas = ["Bismillah", "Alhamdulillah", "Subhanallah", "Istaghfirullah"];
#Loops are used to repeat a block of code multiple times. In this case, we are using a for loop to iterate through each item in the list of duas and print it out.
#  The output will be:
#for dua in duas: 
 #   print(dua);

#################### Noor Chatbot ####################
# Noor says hello! 
print("As-salamu alaykum! I am Noor.");
print("I can answer simple Islamic questions.");
print("Type 'bye to end'");

#Build Noor's LLM Brain (lists)
# Noor's brain: questions + answers 
questions = ["who created us?", #Question 0
             "how many times do we pray?", 
             "what is the quran?", 
             "what is ramadan?", 
             "what do we say before eating?", 
             "who is prophet Muhammad?",
             "Who is the last Prophet?",
             "How many pillars are in Islam?" ] 
answers = ["Allah (SWT) created us!", #Answer 0
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
#found = False 
for i in range(len(questions)): 
   if questions[i] in user_question: print("Noor:", answers[i])  
   else: print("Noor: Sorry, I don't know the answer to that question.")
   found = True 
   break

#varibales ?
#input and output ?
#conditional statements If-Else ?
#lists and loops ?

#Using these concepts, we can build a simple chatbot that can answer questions about Islam. 
# We can also add more questions and answers to Noor's brain to make it smarter!