
std_dict = {"Ajit":70,"Ravi":86,"Prathmes":65,"Shravan":72,"Suraj":89}
std_name=input("Enter student's name:- ")

if std_name in std_dict:
    print(f"{std_name}'s marks:- {std_dict[std_name]}")
else:
    print("student not found")
