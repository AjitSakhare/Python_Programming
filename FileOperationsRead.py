# file operation

file_name = "sample.txt"   # Sample file available in current project folder.
try:
    with open(file_name,"rt") as fh:    # open file in read mode
        print("Reading file context:")
        for index,item in enumerate(fh,1): # reading file line by line and using index to print line number.
            print(f"Line {index} : {item.strip()}")

except FileNotFoundError:                                   # if file not found then will get file not found message.
    print(f"Error: The file {file_name} was not found")