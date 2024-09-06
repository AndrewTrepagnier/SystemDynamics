# allow us to work with sequential data
# alot of functionality

# example is a list of courses

courses = ['History', 'Math', 'Physics', 'CompSci']
print(len(courses))
print(courses)

#access one of the entities in the list

print(courses[1])
# -1 WILL ALWAYS BE THE LAST ITEM

print(courses[0:2]) # up to but not including 2(physics)

print(courses[2:]) # This is called slicing

courses.append('Art')
print()
courses.insert(2, 'Art')
print(courses)


