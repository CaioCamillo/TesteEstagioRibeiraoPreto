def pertencefibonacci(numero):
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    return False

numeroinformado = int(input("Informe um numero para verificar se pertence a sequencia de Fibonacci: "))

if pertencefibonacci(numeroinformado):
    print(f"O numero {numeroinformado} pertence a Fibonacci")
else:
    print(f"O numero {numeroinformado} nao pertence a Fibonacci")