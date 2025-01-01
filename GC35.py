print("\033c", "\033[A") # clears the screen
question = input("Player A, choose a question: ")
answer = input("Player A, choose an answer: ")

print("\033c", "\033[A") # clears the screen
print(question)
attempt = input("Player B, attempt an answer: ")
if attempt == answer:
    print("Correct!")
else:
    print("Incorrect.")
