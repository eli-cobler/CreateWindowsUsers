#net user "pc1" "student" /add
#net localgroup "Users" "pc1" /add
#net localgroup "HomeUsers" "pc1" /add

import os

numberOfUsers = int(input("Number of users? "))

for i in range(1, numberOfUsers + 1):
    os.system('"net user "pc{}" "student" /add"'.format(i))
#subprocess.call(['runas', '/user:coblere', 'net user "pc1" "student" /add'])