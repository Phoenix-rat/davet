import os

os.system("find / -type f -perm /u=s -exec ls -lsah {} \; 2>/dev/null")
