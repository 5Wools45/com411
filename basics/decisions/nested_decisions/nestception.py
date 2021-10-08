print("Where should I look?")
#ask the user which room to look in
room = str(input())
if room == "in the bedroom":
    print("Where in the bedroom shall i look?")
    #ask user where in the bedroom to look
    bedroom2 = str(input())
    if bedroom2 == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")


elif room == "in the bathroom":
    print("Where in the bathroom shall i look?")
    #ask the user where in the bathroom to look
    bathroom2 = str(input())
    if bathroom2 == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

elif room == "in the lab":
    print("Where in the lab should I look?")
    #ask the user where in the lab to look
    lab2 = str(input())
    if lab2 == "on the table":
        print("Yes! I found my battery")
    else:
        print("Found some tools but no battery")

else:
    print("I do not know where that is but I will keep looking")

