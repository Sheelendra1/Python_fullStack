# class Students:
#     name = "Sheelendra"
#     grade = 90
#     pass
# student1 = Students()
# print(student1.name)
# print(student1.grade)
# student2 = Students()
# print(student2.name)
# print(student2.grade)

class Person:
  def __init__(self, name, age):
    self.name=name
    self.age = age

p1 = Person("Sheelendra", 19)
print(p1.name)
print(p1.age)