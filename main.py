print("Enter the number of friends joining (including you):")
number_of_friends = int(input())
if number_of_friends < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(number_of_friends):
        friends[input()] = 0
    print(friends)