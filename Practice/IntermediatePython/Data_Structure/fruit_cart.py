"""
With sets, you are one step closer to becoming a Python Data Manipulator. 🧗

🫐🍇🍌 Let's go back to fruits! 🍓🍒🍎

Grocery shopping is great until you forget what was on your list. 😥

Before you head out, your best friend ask you to pick up some fruit for her too. Let's combine the lists!

-> Create two sets representing your favorite fruits and your best friend's favorite fruits.
-> Print the union of the two sets would look like.
-> Print the intersection of the two sets.
"""

my_favorite_fruits = {"Orange", "Guava", "Pinneaple"}
my_friend_favorite_fruits = {'Apple', 'Guava', "Watermelon"}

# Print union
fruits_union = my_favorite_fruits.union(my_friend_favorite_fruits)
print("Union: ", fruits_union)

# Print Intersection
fruits_intersection = my_favorite_fruits.intersection(my_friend_favorite_fruits)
print("Intersection: ", fruits_intersection)
