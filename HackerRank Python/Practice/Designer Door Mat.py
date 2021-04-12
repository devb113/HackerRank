# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input().split(" ")
row = int(size[0])
col = int(size[1])
for i in range(1, row):
  if i % 2 != 0:
    print((".|." * i).center(col, "-"))
print("WELCOME".center(col,"-"))
for i in reversed(range(1, row)):
  if i % 2 != 0:
    print((".|." * i).center(col, "-"))