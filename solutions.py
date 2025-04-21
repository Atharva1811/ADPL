
# Q1: Even numbers from 1 to 50
print("Q1: Even numbers from 1 to 50:")
print([i for i in range(1,51) if i%2==0])
print()

# Q2: Count vowels in a string
sample_str = "Hello World"
print("Q2: Vowel count in 'Hello World':")
count = sum(1 for c in sample_str.lower() if c in 'aeiou')
print(count)
print()

# Q3: Factorial of a given number (e.g. 5)
n = 5
print("Q3: Factorial of 5:")
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
print()

# Q4: Average of 5 numbers
numbers = [10,20,30,40,50]
print("Q4: Average of [10,20,30,40,50]:")
print(sum(numbers)/len(numbers))
print()

# Q5: Print pattern
print("Q5: Pattern:")
for i in range(1,6):
    print("* " * i)
print()

# Q6: Multiplication table of a number (e.g. 7)
num = 7
print("Q6: Multiplication table of 7:")
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
print()

# Q7: Sum of first 100 natural numbers
print("Q7: Sum of first 100 natural numbers:")
print(sum(range(1,101)))
print()

# Q8: Check divisibility by 2 and 4 for a number (e.g. 8)
num = 8
print("Q8: Is 8 divisible by 2 and 4?")
print(num%2==0 and num%4==0)
print()

# Q9: Check odd or even (e.g. 7)
num = 7
print("Q9: 7 is even?")
print(num%2==0)
print()

# Q10: Check if 't' in string (e.g. 'test')
s = "test"
print("Q10: Does 'test' contain 't'?")
print('t' in s)
print()

# Q11: Divisible by 5 and 11 (e.g. 55)
num = 55
print("Q11: Is 55 divisible by 5 and 11?")
print(num%5==0 and num%11==0)
print()

# Q12: Check if 'a' in string (e.g. 'apple')
s = "apple"
print("Q12: Does 'apple' contain 'a'?")
print('a' in s)
print()

# Q13: Convert list to tuple
lst = [1,2,3]
print("Q13: Convert [1,2,3] to tuple:")
print(tuple(lst))
print()

# Q14: Intersection of two sets
set1 = {1,2,3}
set2 = {2,3,4}
print("Q14: Intersection of {1,2,3} and {2,3,4}:")
print(set1 & set2)
print()

# Q15: Largest and smallest in a list
lst = [5,3,9,1]
print("Q15: Largest and smallest in [5,3,9,1]:")
print(max(lst), min(lst))
print()

# Q16: Sum of even numbers in a list
lst = [1,2,3,4,5,6]
print("Q16: Sum of even numbers in [1,2,3,4,5,6]:")
print(sum(i for i in lst if i%2==0))
print()

# Q17: Sort list in descending order
lst = [3,1,4,2]
print("Q17: Descending sort of [3,1,4,2]:")
print(sorted(lst, reverse=True))
print()

# Q18: Words starting with vowel
words = ["apple","banana","orange","umbrella","kiwi"]
print("Q18: Words starting with vowel:")
print([w for w in words if w[0].lower() in 'aeiou'])
print()

# Q19: Reverse a string
s = "hello"
print("Q19: Reverse 'hello':")
print(s[::-1])
print()

# Q20: Replace vowels with '*'
s = "hello world"
print("Q20: Replace vowels in 'hello world' with '*':")
print(''.join('*' if c.lower() in 'aeiou' else c for c in s))
print()

# Q21: Dictionary with values squared
print("Q21: Dictionary with keys 1-5 and squared values:")
d = {i:i*i for i in range(1,6)}
print(d)
print()

# Q22: Tuple unpacking
t = (1,2,3)
print("Q22: Unpacking (1,2,3):")
a,b,c = t
print(a,b,c)
print()

# CHAPTER-III File operations
filename = "/mnt/data/test_file.txt"
# Q23: Create new file and write name
print("Q23: Write name to file and read back:")
with open(filename,'w') as f:
    f.write("Your Name")
with open(filename) as f:
    print(f.read())
print()

# Q24: Append user input
print("Q24: Append 'Appended text' to file and read back:")
with open(filename,'a') as f:
    f.write("\nAppended text")
with open(filename) as f:
    print(f.read())
print()

# Q25: Read file line by line
print("Q25: Read lines:")
with open(filename) as f:
    for line in f:
        print(line.strip())
print()

# Q26: Count lines
print("Q26: Number of lines:")
with open(filename) as f:
    print(len(f.readlines()))
print()

# Q27: Count words
print("Q27: Total words:")
with open(filename) as f:
    print(len(f.read().split()))
print()

# Q28: Overwrite file
print("Q28: Overwrite file with 'New Content':")
with open(filename,'w') as f:
    f.write("New Content")
with open(filename) as f:
    print(f.read())
print()

# Q29: Check if file exists
print("Q29: Does test_file.txt exist?")
print(os.path.exists(filename))
print()

# CHAPTER-IV OOP
# Q30 Person class
print("Q30: Person class details:")
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
p = Person("Alice",30)
p.display()
print()

# Q31 Rectangle class
print("Q31: Rectangle area and perimeter:")
class Rectangle:
    def __init__(self,l,w):
        self.l = l; self.w = w
    def area(self): return self.l*self.w
    def perimeter(self): return 2*(self.l+self.w)
r = Rectangle(5,3)
print(r.area(), r.perimeter())
print()

# Q32 Circle class
print("Q32: Circle area for radius 4:")
class Circle:
    def __init__(self,r): self.r=r
    def area(self): return math.pi*self.r*self.r
c = Circle(4)
print(c.area())
print()

# Q33 Book class
print("Q33: Book details:")
class Book:
    def __init__(self,t,a,p):
        self.title=t; self.author=a; self.price=p
    def display(self): print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")
b = Book("1984","Orwell",9.99)
b.display()
print()

# Q34 Animal and Dog
print("Q34: Dog bark:")
class Animal:
    def __init__(self,name): self.name=name
class Dog(Animal):
    def bark(self): print(f"{self.name} says Woof!")
d = Dog("Buddy")
d.bark()
print()

# Q35 BankAccount class
print("Q35: BankAccount init:")
class BankAccount:
    def __init__(self,holder,balance):
        self.holder=holder; self.balance=balance
    def display(self): print(f"Holder: {self.holder}, Balance: {self.balance}")
acc = BankAccount("Bob",1000)
acc.display()
print()

# Q36 super() example
print("Q36: super() usage:")
class Base:
    def __init__(self):
        print("Base init")
class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Derived init")
d = Derived()
print()

# Q37 Patient class
print("Q37: Patient class:")
class Patient:
    def __init__(self,name,disease):
        self._name=name; self._disease=disease
    def get_info(self):
        return (self._name, self._disease)
    def update_disease(self,new):
        self._disease=new
pat = Patient("John","Flu")
print(pat.get_info())
pat.update_disease("Cold")
print(pat.get_info())
