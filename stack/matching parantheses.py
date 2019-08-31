s=input().strip()
op=['(', '[', '{']
cl=[')', ']', '}']
stack = []
count = 0
for i in s:
    if i in op:
        stack.append(i)
    elif(cl.index(i)==op.index(stack[-1])):
        stack.pop()
        count += 1
if stack:
    print("not matched")
else:
    print("matched")
print("numnber of matched pairs is", count)
