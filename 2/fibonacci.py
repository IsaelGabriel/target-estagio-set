number: int = int(input("Insira um número: "))

last: int = 0
current: int = 1

while (current < number):
    step: int = current
    current += last
    last = step

if(current == number):
    print("O número pertence à sequência.")
else:
    print("O número não pertence à sequência.")