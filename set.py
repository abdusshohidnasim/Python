student1 = {1,2,3,4,5,6,7,8,9,10}
student2 = set([11,12,13,14,15,16,17,18,19,20])
print(student1)
print(student2)
print(0 in student1) # student1 er moddhe 1 ache kina check korbe
print(student1.remove(1)) # student1 er moddhe 1 remove korbe
print(student1 | student2) # student1 and student2 er value add korbe
print(student1 & student2) # student1 and student2 er common value print korbe
print(student1 - student2) # student1 er value student2 er value theke remove kore print korbe
print(student1 ^ student2) # student1 and student2 er common
print(student1.union(student2)) # student1 and student2 er value add korbe
print(student1.intersection(student2)) # student1 and student2 er common value print korbe
print(student1.difference(student2)) # student1 er value student2 er value theke remove kore print korbe
print(student1.symmetric_difference(student2)) 
print(student1.isdisjoint(student2))
