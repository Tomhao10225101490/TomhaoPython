from datetime import datetime
f = open("appendtime.txt","a")
now = str(datetime.now()) + "\n"
print(f.write(now))