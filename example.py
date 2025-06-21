print("hello world")

def greet():
    print("こんにちは")
greet()

def print_name(name):
    print(f"私の名前は{name}です")
print_name("岡さん")

def get_greet():
    return "おはようございます"
greeting = get_greet()
print(greeting)

def add(a, b):
    x = a + b
    return x
x = add(3, 4)
print(x)
