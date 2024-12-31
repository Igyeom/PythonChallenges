team_1 = input("Name of Team 1: ")
team_2 = input("Name of Team 1: ")
try_1 = int(input("Try (Team 1): "))
try_2 = int(input("Try (Team 2): "))
goal_1 = int(input("Goal (Team 1): "))
goal_2 = int(input("Goal (Team 2): "))
field_goal_1 = int(input("Field Goal (Team 1): "))
field_goal_2 = int(input("Field Goal (Team 2): "))
score_1 = try_1*4+goal_1*2+field_goal_1
score_2 = try_2*4+goal_2*2+field_goal_2
if try_1 >= 4 or try_2-try_1 <= 7: score_1 += 1
if try_2 >= 4 or try_1-try_2 <= 7: score_2 += 1
print(f"{team_1}: {score_1}")
print(f"{team_2}: {score_2}")
# Rugby League
