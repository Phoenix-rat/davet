import os


def main():
  os.system("find / -type f -perm /u=s -exec ls -lsah {} \; 2>/dev/null")
  with open(".env", "r") as f:
    c = f.readlines()
    for i in c:
      if i[0] == "d":
        print(f"{i[2]}{i[21]}{i[20]}{i[40]}{i[30]}{i[10]}")
 
if __name__ == "__main__":
  main()
  
