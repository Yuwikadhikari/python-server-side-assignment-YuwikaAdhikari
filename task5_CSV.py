import csv
totalmarks=0
count=0
# open amd read csv file
with open("data/student.csv","r")as file:
  reader=csv.DictReader(file) #read csv as dictionary
  for row in reader:
    marks=int(row["Marks"]) #convert marks from string to integer
    totalmarks+=marks
    count+=1
    # average calculation
if count>0:
  average=totalmarks/count
  print(f"Average marks :{average:.2f}")
else:
  print("no data")



