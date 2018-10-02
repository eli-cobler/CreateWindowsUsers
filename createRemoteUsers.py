numberOfUsers = int(input("Number of users? "))

with open("windowsusers.txt", 'w') as f:
    for i in range(1, numberOfUsers + 1):
        f.write("pc{};".format(i))