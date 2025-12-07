# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print( f"Student Name: {self.name}, Age: {self.age}")

# student1 = Student("Alice", 20)
# student2 = Student("Akin", 26)

# student1.display_info()
# student2.display_info()


# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_value(self):
#         total = self.price * self.quantity
#         print(f"We have {total} worth of {self.name} in stock.")

# product1 = Product("Tampons", 10, 28)

# product1.total_value()


# HANDLING ZeroDivisionError

def divide(x, y):
  if y == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
  return x / y
  
  divide1 = divide(3, 0)
