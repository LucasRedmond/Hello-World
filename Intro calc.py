first_name = input("What is your first name? ")
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print(first_name + " " + "weighs in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print(first_name + " " + "weighs in Kgs: " + str(converted))






