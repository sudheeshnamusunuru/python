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