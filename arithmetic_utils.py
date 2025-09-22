def add(a, b): print(f"{a} + {b} = {a+b}")
def subtract(a, b): print(f"{a} - {b} = {a-b}")
def multiply(a, b): print(f"{a} * {b} = {a*b}")
def divide(a, b): print("Hata: sıfıra bölünemez!" if b==0 else f"{a} / {b} = {a/b:.2f}")

a, b = 10, 2
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)

print("Bravo")