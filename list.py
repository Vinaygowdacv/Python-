l = [0,1,2,3,4,5,6,7,8,9,10,2]
print(l)

print("Minimum -" ,min(l))
print("Maximum -" ,max(l))

sum = sum(l)
print(sum)
average = sum /len(l)
print(average)
l.pop(0)
print("pop ",l)
l.append(100)
print("append ",l)
l.insert(7,500)
print("inserting ",l)
v = l[0:]
print("slicing ",v)
l.sort(reverse=True)
print("reversing",l)