Score = 0
responses = []
answers = [4, 5, 1, 3, 2]

print("""Welcome to the Numbers Quiz! This quiz will have 5 questions, each with the answers being the numbers 1-5. Each number can only be guessed once and answers cannot be changed once submitted. Good Luck!" 
     
      """)
# Question 1

while True:
    response = input("In Binary, how many possible numbers can be made with only 2 digits? ")
    try:
        int(response)
        if response in range(1, 6):
            responses.append(response)
            break
        else:
            print("Invalid Response, answers must be 1-5")
    except:
        print("Answer must be a valid integer from 1-5 with No special characters")

while True:
    response = input("How many legs are on a standard office chair? ")
    try:
        int(response)
        if not response in responses and response in range(1, 6):
            responses.append(response)
            break
        elif response in responses and response in range(1, 6):
            print("Answer already used")
        else:
            print("Invalid Response, answers must be 1-5")
    except:
        print("Answer must be a valid integer from 1-5 with No special characters")

while True:
    response = input("What number is associated with the word mono? ")
    try:
        int(response)
        int(response)
        if not response in responses and response in range(1, 6):
            responses.append(response)
            break
        elif response in responses and response in range(1, 6):
            print("Answer already used")
        else:
            print("Invalid Response, answers must be 1-5")
    except:
        print("Answer must be a valid integer from 1-5 with No special characters")


while True:
    response = input("How many strikes can you have in baseball? ")
    try:
        int(response)
        int(response)
        if not response in responses and response in range(1, 6):
            responses.append(response)
            break
        elif response in responses and response in range(1, 6):
            print("Answer already used")
        else:
            print("Invalid Response, answers must be 1-5")
    except:
        print("Answer must be a valid integer from 1-5 with No special characters")

while True:
    response = input("What is 5 take away 3? ")
    try:
        int(response)
        int(response)
        if not response in responses and response in range(1, 6):
            responses.append(response)
            break
        elif response in responses and response in range(1, 6):
            print("Answer already used")
        else:
            print("Invalid Response, answers must be 1-5")
    except:
        print("Answer must be a valid integer from 1-5 with No special characters")

print("""
Congratulations, you finished the quiz, lets see how you did!
      """)
print("Your Answers were: ", responses[0], " ", responses[1], " ", responses[2], " ", responses[3], " ", responses[4])
print("The Correct Answers were: ", answers[0], " ", answers[1], " ", answers[2], " ", answers[3], " ", answers[4])
