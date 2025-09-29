i = 1
while i <= 100: # print the number in ascending order
    print(i) 
    i += 1

i = 100
while i >= 1:
    print(i) # print the number in descending order
    i -= 1

n = int(input("enter the number: "))
i = 1
while i  <= 10:
    print(n * i)
    i += 1

nums = [4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(nums):
    print(nums[i]) #nums[0],nums[1],nums[2],nums[3],nums[4],nums[5],nums[6],nums[7],nums[8]
    i += 1


'''
text = "python"
reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text

print("reversed:", reversed_text)
'''


name = "manish"
# rev =''.join(reversed(name))
# print(rev)


name = "manish"
rev = name[::-1] 
print(rev)

alp = "manish is good boy"
count = 0
for ch in alp:
    if ch.lower() in "aeiou":
        count += 1

print(alp)
print(count)

text = ["manish",5,8,5,"manish","sagar",5.66,6,5.66]
unique_items = []
for item in text:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)

nums =  (1, 4 ,9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36
i = 0
while i <len(nums):

 if(nums[i] == x):
  print("Found index", i)
  break
 else:
  print("finding..")
  i += 1

if i == len(nums):
 print("value not found")
print("end of loop")



nums =  [1, 4 ,9, 16, 25, 36, 49, 64, 81, 100]

for val in nums:
    print(val)

nums =  (1, 4 ,9, 16, 25, 36, 49, 64, 81, 100, 81)

x = 81
i = 0
for val in nums:
    if (val == x):
        print("found",i)
    i += 1
    

for i in  range(10):
    print(i)

seq = range(30) # range(stop)
for i in seq:
    print(i)

for i in range(10,20): #range (start, stop)
    print(i)

for i in range(5,20,5): #range(start ,stop, step)
    print(i) # start 5 se , and 5 se increase, 20 ke pahle stop


seq = range(30) # range(stop)
for i in seq:
    if i % 2 == 0:
        print(i)

for i in range(10,20): #range (start, stop)
    if i % 2 == 0:
     print(i)

for i in range(1,101):# print number from 1 to 100
    print(i)

for i in range(100,0,-1):   #print number from 100 to 1
    print(i)/

table = int(input("Enter numbr: "))

for i in range(1, 11):
    print(table*i)

n = 10
sum = 0
for i in range(1,n+1):
    sum += i
print("total sum is",sum)