def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket. \n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print(f"OR, we can use variable from out script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do match inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variable and match:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers)
