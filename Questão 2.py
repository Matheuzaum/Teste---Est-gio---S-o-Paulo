"""loop que identifica o número informado e deixa ele como int adequadamente"""
while True:
    NumeroInformado = input("Digite aqui, um número para ver se ele pertence a sequência de Fibonacci :")
    try:
        NumeroInformado = int(NumeroInformado)
        break
    except:
        print("Isso não é um número inteiro, não tem como ser da sequência de Fibonacci")
        print("Vou te dar outra chance :")

"""Valores básicos para o loop do fibonacci funcionar adequadamente"""
NumeroFibonacci = 0
NumeroAnteriorFibonacci = 1
NumeroIteracoes = 0
PertenceFibonacci = False

""""loop que percorre o Fibonacci e identifica se o numero faz parte da sequência, sendo que, não faz parte, a não ser que se prove o contrário"""
while NumeroFibonacci <= NumeroInformado:
    if NumeroFibonacci == NumeroInformado:
        PertenceFibonacci = True
        break
    else:
        NumeroFibonacci += NumeroAnteriorFibonacci
        NumeroAnteriorFibonacci = NumeroFibonacci - NumeroAnteriorFibonacci
        NumeroIteracoes += 1

if PertenceFibonacci:
    print(f"O número que você digitou faz parte da sequência de Fibonacci e é o {NumeroIteracoes}º número da sequência!!!")

else:
    print("O número não pertence a sequência Fibonacci :c")