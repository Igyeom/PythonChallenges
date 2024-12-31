from random import choice
n = int(input("Number of students: "))
l = ["This student has been keeping up a good attitude and understanding in class.", "This student needs more encouragement on the subject.", "This student is doing really well in Economics!", "This student might need a bit of support."]
for i in range(1, n+1):
    print(f"Student #{i}. {choice(l)}")
