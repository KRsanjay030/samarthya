class Car:
   def __init__(self, brand, horsepower, color, model):
      self.brand = brand
      self.horsepower = horsepower
      self.color = color
      self.model = model
   def myfunc(self):
      print(f"The car is {self.brand}, it has a HP of {self.horsepower}. It's color is {self.color} and it's model is {self.model}")
   def __str__(self):
      return "Brand: " + self.brand + ", HP: " + str(self.horsepower) + ", color: " + str(self.color) + ", model: " + str(self.model)
p1 = Car("BMW", 620, "white", "iX")
p1.myfunc()
print(p1)