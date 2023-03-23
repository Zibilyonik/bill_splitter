import random
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
        print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
        if input() == "Yes":
            lucky_one = random.choice(list(friends.keys()))
            print(lucky_one, "is the lucky one!")
            for friend in friends:
                friends[friend] = round(bill / (number_of_friends - 1), 2)
            friends[lucky_one] = 0
        else:
            print("No one is going to be lucky")      
            for friend in friends:
                friends[friend] = round(bill / number_of_friends, 2)
        print(friends)