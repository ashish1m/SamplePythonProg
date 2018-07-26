file1 = open("C:\\Users\\mathua5\\Desktop\\file1.txt", "r")
file2 = open("C:\\Users\\mathua5\\Desktop\\file2.txt", "r")

# for i in file1.readlines():
#     print(i)
#
# for j in file2.readlines():
#     print(j)
file1_data = file1.readlines()
file2_data = file2.readlines()

for i in range(len(file1_data)):
    file1_data[i] = file1_data[i].replace(" ", "")

for i in range(len(file2_data)):
    file2_data[i] = file2_data[i].replace(" ", "")


if file1_data == file2_data:
    print("Content is same in both file")
else:
    print("Different content")

file1.close()
file2.close()
