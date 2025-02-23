import random
import math
# Floor
floor=math.floor(3.9)
print(floor)
# Truncate
truncate=math.trunc(-5.5)
print(truncate)
# Complex number
complexnum=2+ 3j
print(complexnum)
# Octal Base Number
octal=0o20
print(octal)
# Hex Number
hexnum=0xFF
print(hexnum)
# Binary
binary=0b1010
print(binary)


# METHOD FOR THESE NUMBERS
# oct()
# int()
# float()
# bin()
# hex()

# Bitwise Operations
x=1
a=x<<2
print(a)

# Random Metod
randomnum=random.randint(1,101)
print(randomnum)
# Random Choice
list_1=['lemon','masala','ginger','black']
randomchoice=random.choice(list_1)
print(randomchoice)
# Shuffle
randomshuf= random.shuffle(list_1)
print(list_1)

# Known Problems
decimal=(0.1+0.1+0.1)-0.3
print(decimal)
from decimal import Decimal
decimal1=Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
print(decimal1)


# Fractions
from fractions import Fraction
myfar=Fraction(3,7)
print(myfar)

# Set
setone={1,2,3,4}
union=setone|{1,3,5,7}
print(union)

# Bollean
True1=True==1
print(True1)


#Done