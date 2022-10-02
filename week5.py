print("\nTask3")
class Calculator:
    def addition(self):
        print(a + b)
    def subtraction(self):
        print(a - b)

    def multiplication(self):
        print(a * b)
    def division(self):
        print(a / b)
a = int(input("Enter first number:"))
b = int(input("Enter first number:"))

obj = Calculator()

choice = 1
while choice != 0:
    print("1) addition")
    print("2)substraction")
    print("3)multiplication")
    print("4)division")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(obj.addition())
    elif choice == 2:
        print(obj.subtraction())
    elif choice == 3:
        print(obj.multiplication())
    elif choice == 4:
        print(obj.division())
    else:
        print("Invalid choice")
        
print("\nTask1")
class Rectangle:
  def init (self , color="green", width=100, height=100):
   self.color = color
   self.width = width
   self.height =height
   
  def square(self):
   return self.width * self.height

  
rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
rect1 = Rectangle("yellow", 23, 34)
print(rect1.color)
print(rect1.square())

print("\nTask2")
class Name:
     def init(self,first_name,last_name):
         self.first_name = first_name[0].upper() + first_name[1:len(first_name)].lower()
         self.last_name = last_name[0].upper() + last_name[1:len(last_name)].lower()
         def repr(self):
           print(f"{self.first_name} {self.last_name}")
           name=Name("AKKUMIS","sARsenova" )
           print(person.first_name)
           print(person.last_name)
           name.repr



