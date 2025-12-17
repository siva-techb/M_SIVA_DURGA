class Calculator:
    def init(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def result(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero not allowed"
        else:
            return "Invalid operation"


# taking inputs
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add / sub / mul / div): ")

# creating object
calc = Calculator(a, b, operation)

# printing result
print("Result:", calc.result())
