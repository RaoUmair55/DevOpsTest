# //list of 

students = [
    {"name" : "ALi", "id" : 10},
    {"name" : "Susheel", "id" : 11},
    {"name" : "Usman", "id" : 1},
]

print(students)

def Highest(students):
    highest_value = students[0]
    for student in students:
        if student["id"] > highest_value["id"]:
            highest_value = student
    return highest_value

highest = Highest(students)
print("person with greatest id ", highest)