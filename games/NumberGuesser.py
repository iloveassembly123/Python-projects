import time
from random import randint

# increment a file by 1 when winning, add a seperate thread timer

print("Make sure not to enter anything else then a number or the program crashes")
a = int(input("First number: "))
b = int(input("Second number:"))
t = int(input("How much tries?: "))

# debug disabled
c = randint(a, b)
s = False
s = True
print(f"Your random number has {len(str(c))} digits")
print(
    f"Your random number has {c % 10 if len(str(c)) != 1 else '(illegal, viewing this will be considered cheating)' } as its last digit."
)
# debug disabled print(c)
for _ in range(t):
    i = int(input("Number: "))
    if i == c:
        print("You won! (restart the game)")
        time.sleep(4)
        break
    elif i != c:
        print(
            f"Try again, incorrect guess. You have {t} {'tries' if t != 1 else 'try'} left."
        )
        t -= 1
