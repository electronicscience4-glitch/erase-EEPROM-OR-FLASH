import os
filename = "data.txt"
# 1. یەکەم سڕینەوەی فایلەکە (ئەگەر بوونی هەبێت)
if filename in os.listdir():
    os.remove(filename)
    print("faila konaka srayawa !")
# 2. دروستکردنی فایلێکی نوێ بە 512 ڕیز
with open(filename, "w") as f:
    for i in range(512):
        f.write("0\n") 
print(f"Faily nwy drwst kra 512 kvxy 0 dadanet ")
print(f"nawy fail brytya la : {filename}")

