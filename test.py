# ex 1
data_scientist ={"Git", "SQL", "R", "Python"}
data_engineer = {"Hadoop", "Git", "SQL", "Scala", "java", "Python"}
data_scientist.add("SAS")
data_engineer.discard("Scala")
len(data_engineer)
print(data_engineer & data_scientist)
print(data_scientist.intersection(data_engineer)
      )
my_skills = {"Python", "SQL"}
print(my_skills.issubset(data_scientist))
# ex 2

a = (2, 5)
b = (3, -2)
#b[1] = 7 tuple is immutable
import math
distance = math.sqrt(b[0]-a[0] ** 2 + (b[1] - a[1]) ** 2)
print(f"Distance = { distance:.2f}")
print(a+b)
print(a.count(1))
print(a.index(5))
# del b
