try:
    file = open("sample.txt", "r")
    print("Reading file content:")

    line_number = 1
    for line in file:
        print("Line", line_number, ":", line.strip())
        line_number += 1

    file.close()                     

except:
    print("Error: The file 'sample.txt' was not found.")

