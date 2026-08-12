content = input("Enter content to write to the file: ")

file = open("student.txt", "w")
file.write(content)
file.close()

print("Content written successfully.")