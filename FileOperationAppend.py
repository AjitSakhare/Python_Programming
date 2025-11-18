
print("Enter text to write to the file : - ")

with open("output.txt","wt") as fh:
    fh.write(input()+"\n")
    print("Data successfully written to the file")

print("Enter additional text to append: - ")
with open("output.txt","at") as fh:
    fh.write(input())
    print("Data successfully appended")

print("Final content of output.txt: ")
with open("output.txt","rt") as fh:
    print(fh.read())
