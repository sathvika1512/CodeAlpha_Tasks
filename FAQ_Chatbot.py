questions = ["what is ai", "what is python"]
answers = ["AI is Artificial Intelligence", "Python is a programming language"]

user = input("Ask: ").lower()

if user in questions:
    index = questions.index(user)
    print(answers[index])
else:
    print("Sorry, I don't know")
