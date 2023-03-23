print("Enter the number of friends joining (including you):")
try:
    number_of_friends = int(input())
except:
    print("No one is joining for the party")
else:
    if number_of_friends < 1:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        friends = {}
        for _ in range(number_of_friends):
            friends[input()] = 0
        print("Enter the total bill value:")
        bill = float(input())
        for i in friends:
            friends[i] = round(bill / number_of_friends, 2)
        print(friends)