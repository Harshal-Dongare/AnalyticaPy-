f = open(r"E:\Python Notes\13 Behind The Scenes - Loops\file1.py")

# print just one line
line = f.readline()
print(line, end="")

# print all lines
for line in f:
    print(line, end="")


