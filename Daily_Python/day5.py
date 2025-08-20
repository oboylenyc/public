#Title: Shopping List Manager
#
#Difficulty: Beginner
#
#Challenge Description:
#Write a program that asks the user to enter items for a shopping list until they type "done".
#
#Store all items in a list.
#
#After the user finishes, print the total number of items and then print the complete list.

l = []

while True:
    item = input("Enter an item for a grocery list, when done type 'Done' ")
    if item.lower() == "done":
        break
    else: 
        l.append(item)
l.sort(key=str.lower)

print(f"You have {len(l)} items in your grocery list.")
print(l)