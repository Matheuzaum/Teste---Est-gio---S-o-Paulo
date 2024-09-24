# Recebe a string que o usuário quer inverter
string_original = input("Digite a string que você quer que seja invertida :")

# Inicializa uma variável para armazenar a string invertida
string_invertida = ""

# Percorre a string original de trás para frente
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

# Exibe a string invertida
print("String original:", string_original)
print("String invertida:", string_invertida)
