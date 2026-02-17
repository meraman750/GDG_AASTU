from collections import Counter
# num = int(input("The number of items u want: "))
# if num > 3:
#     print("Discount applied")
# else:
#     print("No discount")

# grades = {"John": "A", "Sara": "B", "Musa": "A"}

# inverted = {}

# for value, key in grades.items():
#     if key not in inverted:
#         inverted[key] = []
#     inverted[key].append(value)
# print(inverted)
    
# sentence = input("Enter word: ")

# words = sentence.split(" ")

# dictionary = Counter(words)

# print(dictionary)

# scores = {"John": 85, "Sara": 92, "Fraol": 78}

# lower_cases = {k.lower():val for k, val in scores.items()}

# name = input("Enter a student name: ").lower()
# if name in lower_cases:
#     print(lower_cases[name])
# else:
#     print("Sorry student doesnt exist !")

# sales = []

# with open("sales.txt", "r") as file:
#     for line in file:
#         line = line.strip()
#         try:
#             num = int(line)
#             sales.append(num)
#         except ValueError:
#             continue

# print("Total sales: ", sum(sales))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_(self):
        return f"My name is {self.name}, age: {self.age}."
    
p1 = Person("Mussie", 23)
print(p1.print_())

    


