class Student:
  def __init__(self):
    self.name=""
    self.roll_num=""
    self.marks=0

  def give_details(self):
    self.name=input("Enter name")
    self.roll_num=input("Enter roll number")
    self.marks=input("Enter marks")

  def display(self):
    print("\n------Student Details---------")
    print(f"Name         :{self.name}")
    print(f"Roll Number  :{self.roll_num}")
    print(f"Marks        :{self.marks}")
    print("-"*30)

yuwika=Student()
yuwika.give_details()
yuwika.display()