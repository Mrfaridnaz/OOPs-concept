class maths:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def mult(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1/self.num2

adder = maths(5, 7)
mult = maths(3,8)
Div = maths(25,6)


result1 = adder.add()
result2 = mult.mult()
result3 = Div.div()
print("The sum is:", result1)
print("The mult is:", result2)
print("The div is:", result3)
