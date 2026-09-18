#list in python
#List is an ordered and changeable collection that can store and it is mutable
marks = [80,90,75,85]
print(marks)

#accessing elements in a list

marks = [80,90,75,85]

print(marks[0])
print(marks[1])
print(marks[3])

#change elements in a list

marks = [80,90,75]

marks[1] = 95

print(marks)

marks[2] = 78

print(marks)

#add elements to a list

marks = [80,90,75]
marks.append(85)
print(marks)

#remove elements from a list

marks = [80,90,75]
marks.remove(75)
print(marks)

#insert method
numbers = [10,20,30]
numbers.insert(1,15)
print(numbers)

#extend method
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#clear method
numbers = [10,20,30]
numbers.clear()
print(numbers)

#index method
numbers = [10,20,30,40]
print(numbers.index(30))

#count method
numbers = [10,20,30,40,20,40]
print(numbers.count(20))

#sort method
numbers = [40,10,30,20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#reverse method
numbers=[10,20,30,40]
numbers.reverse()
print(numbers)

#copy method
a=[1,2,3]
b=a.copy()
print(b)


numbers=[10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#Tuples in python
#Tuple is a collection of multiple values that is ordered and cannot be changed after creation and it is not mutable
student = ("Bhargavi",98,"Python")
print(student[0]) 

#access values in a tuple
student = ("Bhargavi",21,85.5)
print(student[0])
print(student[1])
print(student[2])

#immutable nature of tuples

#tuples are immutable, meaning they cannot be changed after 
numbers = (10,20,20,30,20)
print(numbers.count(20))

#index method
numbers = (10,20,30,40)
print(numbers.index(30))

numbers = (10,20,30,40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and mutable
numbers = {10,20,30,20,10}
print(numbers)

#why use set?

#suppose students have selected subjects
subjects = {"Python", "Java", "Python", "SQL", "Java"}
print(subjects)

#add values to a set 
subjects = {"Python","Java"}
subjects.add("SQL")
print(subjects)

#remove values from a set
subjects = {"Python","Java","SQL"}
subjects.remove("Java")
print(subjects)

#Sets do not allow duplicate values
numbers = {1,2,2,3,3,4}
print(numbers)


#slice method
#start,stop,step
numbers=[10,20,30,40,50,60,70,80]
print(numbers[1:7:2])
print(numbers[6:1:-2])

#dictionary in python
#dictionary is a collection of  key value pairs and unordered and mutable

student = {
    "name":"Bhargavi",
    "age":00,
    "course":"Python"
}
print(student)


#access elements in dictionary
print(student["name"])
print(student["age"])
print(student["course"])


#change values in a dictionary
student["age"] = 11
print(student["age"])


#add new data to a dictionary
student["city"] = "vijayawada"
print(student)

#remove data
student.pop("city")
print(student)
#when we use pop method it removes last inserted method in the list

#dictionary
student = {
    "name":"Bhargavi",
    "age":21,
    "course":"Python"
}
print(student.keys())
#keys() returns all the keys in the dictionary
print(student.values())
#values returns all the values in the dictionary
print(student.items())
#items()returns all key value pairs
print(student.get("name"))
#get()returns the value of the specified key
student.update({"age":22})
#update()updates the value of specified key
print(student)
student.pop("age")
#pop()removes the specified key and its value
print(student)

#popitem()removes the last inserted key-value pair
student = {
    "name":"Bhargavi",
    "age":21,
    "course":"Python"
}
student.popitem()
print(student)

student = {
    "name": "Bhargavi"
}
student.setdefault("age",21)
print(student)

#clear method
student.clear()
print(student)

#copy method
student = {
   "name":"Bhargavi",
   "age":21
}
new_student = student.copy()
print(new_student)

#order of evaluation(BODMAS)
result = 2+13*2
print(result)

result = (10+5)*2
print(result)