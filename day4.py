# #problem 1
# dict = {
#     "table" : ("a piece of furniture" , "lists of facts and figures"),
#     "cat" : "a small animal"
# }
# print(dict)

# #problem 2
# subjects = {
#     "python", "java", "c++", "python", "javascript", "java",
#     "python",  "java", "c++", "c"
# }
# print(len(subjects))
# print(subjects)

# #problem 3
# marks = {}

# x =int(input("enter phy: "))
# marks.update({"phy" : x})

# y =int(input("enter math: "))
# marks.update({"math" : y})

# z =int(input("enter chem: "))
# marks.update({"chem" : z})

# print(marks)

# #problem 4
# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)
#=================================== Day 4 - ASSIGNMENT =====================================================================
#Problem - 1 My Info  Dictionary
# dict = {
#     "name" : "aribah", 
#     "age" : "17",
#     "city" : "hyderabad",
#     "school" : "Daffodils CBSE School",
#     "dreamjob" : "aiml-engineer"
# }
# print(dict.get("name"))
# print(dict.get("age"))
# print(dict.get("city"))
# print(dict.get("school"))
# print(dict.get("dreamjob"))

#Problem 2 - Dictionary Methods
# subjects = {
#     "phy" : "99",
#     "math" : "96",
#     "chem" : "92"
# }
# print(subjects.keys())
# print(subjects.values())
# print(subjects.items())

#Problem 3 - Update Dictionary
# friends = {
#     "nick" : "27",
#     "carrie" : "26"
# }
# print(friends.update({"sara" : "15"}))
# print(friends.update({"carrie" : "28"}))
# print(friends)

#Problem 4 - Sets
# set1 = {
#     "hindi", "english", "social"
# }
# set2= {
#     "maths", "hindi", "ai"
# }
# print(set1.union(set2))
# print(set1.intersection(set2))

#Problem 5 - No Duplicates
names = {"aribah", "sara", "aribah",
         "fatima", "sara", "zara"}
unique_names = set(names)
print(unique_names)