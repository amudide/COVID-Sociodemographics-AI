with open("centers.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
content = [x[0:3] for x in content]

uniques=set(content)
print(len(content))
a = (list(uniques))
a.sort()
print(a)

print(len(uniques))