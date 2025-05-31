# Define a list of students 
students=["Yuwika","Sita","Ram","Batman","David","Eve"]
# writing a list to a file
with open("data/student.txt", "w") as file:
  for student in students:
    file.write(student + "\n")

# reading the contents from the file
with open("data/student.txt", "r") as file:
  contents=file.readlines()

# display the contents
print("List of Students:")
for line in contents:
  print(line.strip()) #Displays each name, removing the extra newline character.