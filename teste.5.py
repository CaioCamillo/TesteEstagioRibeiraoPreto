def inverter_string(string):
    string_invertida = ""
    for char in string:
        string_invertida = char + string_invertida
    return string_invertida

string_original = input("Digite algo em string para inverter: ")

string_invertida = inverter_string(string_original)1
print("String original:", string_original)
print("String invertida:", string_invertida)