# """Bycicles Example"""

# bycicles = ['trek', 'cannondale', 'redline', 'specialised']
# print(bycicles[0].title())
# print(bycicles[1].title())
# print(bycicles[3].title())
# print(bycicles[-1].title())
# print(f"My first bycicle was a {bycicles[0].title()}")

"""List's exercise 3-1"""

# names = ['shakil', 'babar', 'genghis', 'abdul', 'yasin', 'yakub']

# print(names[0].title())
# print(names[1].title())
# print(names[3].title())

"""List's xercise 3-2"""
# print(f"{names[1].title()} is a twat")
# print(f"{names[3].title()} is a wasteman")
# print(f"{names[4].title()} is a good guy")
# print(f"{names[-1].title()} Is a good guy")

# """Motorcycles example"""

# motorcycles = []

# motorcycles.append("honda")
# motorcycles.append("yamaha")
# motorcycles.append("suzuki")

# print(motorcycles)

# popped_motorcyle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcyle)

# """List's exercise 3-4"""

# dinner_invite = ["mark", "flynn", "jacob", "charlie"]

# print(f"\n{dinner_invite[0].title()} is invited to my dinner")
# print(f"{dinner_invite[1].title()}, the cakes are good")
# print(f"{dinner_invite[2].title()}, the steak is excellent")

# """List's exercise 3-5"""
# print(f"\n{dinner_invite}")
# print(f"{dinner_invite[0].title()}, can't make it ")
# dinner_invite[0] = 'China'
# print(dinner_invite)
# print(f"{dinner_invite[0].title()} is coming instead")
# print(f"\n{dinner_invite[1].title()}, {dinner_invite[2].title()}, {dinner_invite[3].title()} are still coming")

# """List exercixe 3-6"""

# dinner_invite.insert(0, "Smith")
# dinner_invite.insert(2, "Mathew")
# dinner_invite.append("Yaldo")
# print(f"\n{dinner_invite}")
# print(f"{dinner_invite[0]}, {dinner_invite[2]}, {dinner_invite[-1]} will also be joining us for dinner")

# """List exercise 3-7"""

# print("\nSadly the dinner table won't be arriving one time and there is space for only two guests")

# print(f"\n{dinner_invite}")
# cancel_invitation_1 = dinner_invite.pop(1)
# cancel_invitation_2 = dinner_invite.pop(3)
# cancel_invitation_3 = dinner_invite.pop(4)

# print(f"{cancel_invitation_1}, "
      # f"{cancel_invitation_2}, "
      # f"{cancel_invitation_3}, we don't have enough spaces, therefore you won't bee attending")

# print(dinner_invite)

# cancel_invitation_4 = dinner_invite.pop(0)
# cancel_invitation_5 = dinner_invite.pop(1)

# print(f"{cancel_invitation_4}",
      # f"{cancel_invitation_5} you guys will also not be attending")

# print(f"\n{dinner_invite}")
# print(f"{dinner_invite[0]}, {dinner_invite[1].title()} you guys are still invited")

# del dinner_invite[0]
# del dinner_invite[0]
# print(dinner_invite)

"""List's exercise 3-8"""

# my_location = ['china', 'japan', 'south korea', 'hungary', 'venezuela']
# print(my_location)

# print("\nHere is the sorted listed using the sorted function without modifying the actual list: ")
# print(sorted(my_location))

# print("\nThe list is still in it's original order as sorted function is temporary: ")
# print(my_location)

# print("\nHere is the reverse of the list using the sorted function: ")
# print(sorted(my_location, reverse=True))

# print("\nThe list is still in the original order: ")
# print(my_location)

# print("Original reversed list: ")
# my_location.reverse()
# print(my_location)

# print("\nList reversed back to original: ")
# my_location.reverse()
# print(my_location)

# print("\nHere is the sort function with the list: ")
# my_location.sort()
# print(my_location)

# print("\nAfter the sort function, I have now reversed the list: ")
# my_location.sort(reverse=True)
# print(my_location)