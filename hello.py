
print("Hello world")
print(3+8)
a=3
b=15
print(f"sum of {a} and {b} is {a+b}")

number=[12,23,45,67]
print(number)
key_map={
    "Name":"Zohaib",
    "Age":18
}
print(key_map["Name"])
print(f"After append {number.append(12)}")
print(f"Insert at specific index {number.insert(2,16)}")

print(f"Insert at specific index {number.pop(4)}")
print(f"Our new list will be {number}")


key_map["Country"]="Pakistan"
print(key_map["Country"])
print(key_map)


studentData=[
    {
        "Name":"Zohaib",
        "age":20,
        "Country":"Pakistan"
    },
    {
        "Name":"Testing",
        "age":12,
        "Country":"India"
        
    },
]
for student in studentData:
    print("Name is ",student["Name"])
    print("Age  is ",student["age"])
    print("Country is ",student["Country"])
    print()

for i in range(7):
    print(f"Number is {i}")
print("Bloc end here ")  

for i in range(10):
    if(i%2==0):
        print(f"{i} is even number")
    else:
        print(i,"is odd number")    

for i in range(10):
    if(i%2==0):
        continue
    elif(i==7):
        break
    else:
        print(i,"is without continue and break")

try:
    result=10/0

except ZeroDivisionError as e:
        print(f"Division by zero error {e}")


finally:
        print("Cleanup code")



def greet(name,message="Hello",):
     print(message,name)

greet("Zohaib")    