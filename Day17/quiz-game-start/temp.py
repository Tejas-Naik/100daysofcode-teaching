# Lists - to store a number of strings/letters/numbers/floats

students = ["Pranav", "Abhi", "Shalwa", "Prajwal"]
print(students)

# Adding student to a list
students.append("Rohan")
print(students)

# Indexing / accessing students
print(students[0])
print(students[1])
print(students[-1])
print(students[-2])

# Removing last item from a list
students.pop()

# Removing any item with index from a list
students.pop(1)
print(students)

# Getting the index of a particular name
index_of_prajwal = students.index("Prajwal")
print(index_of_prajwal)
