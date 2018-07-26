file_p = open("C:\\Users\\mathua5\\Workspace\\python.txt", "w+")
file_p.write("Python is fun")
file_p.write("\nI'm enjoying python")
file_p.close()

# use 'with' to open a file which closes the file automatically after completing the block of code.

with open("C:\\Users\\mathua5\\Workspace\\python.txt", 'r') as f:
    f_data = f.read()
    print(f_data)
