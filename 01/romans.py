import math

def int_to_roman(num):
    
    resultado = []
    
    if num > 3999:
        print('O número inserido é maior que 3999.')
        return
    if num >= 1000:
        Quo = num / 1000
        Quo = math.floor(Quo)
        res = int(Quo)*str("M")
        resultado.append(res)
        num = num % 1000
    if num >= 900:
        Quo = num / 900
        Quo = math.floor(Quo)
        res = int(Quo)*str("CM")
        resultado.append(res)
        num = num % 900
    if num >= 500:
        Quo = num / 500
        Quo = math.floor(Quo)
        res = int(Quo)*str("D")
        resultado.append(res)
        num = num % 500
    if num >= 400:
        Quo = num / 400
        Quo = math.floor(Quo)
        res = int(Quo)*str("CD")
        resultado.append(res)
        num = num % 400
    if num >= 100:
        Quo = num / 100
        Quo = math.floor(Quo)
        res = int(Quo)*str("C")
        resultado.append(res)
        num = num % 100
    if num >= 90:
        Quo = num / 90
        Quo = math.floor(Quo)
        res = int(Quo)*str("XC")
        resultado.append(res)
        num = num % 90
    if num >= 50:
        Quo = num / 50
        Quo = math.floor(Quo)
        res = int(Quo)*str("L")
        resultado.append(res)
        num = num % 50
    if num >= 40:
        Quo = num / 40
        Quo = math.floor(Quo)
        res = int(Quo)*str("XL")
        resultado.append(res)
        num = num % 40
    if num >= 10:
        Quo = num / 10
        Quo = math.floor(Quo)
        res = int(Quo)*str("X")
        resultado.append(res)
        num = num % 10
    if num >= 9:
        Quo = num / 9
        Quo = math.floor(Quo)
        res = int(Quo)*str("IX")
        resultado.append(res)
        num = num % 9
    if num >= 5:
        Quo = num / 5
        Quo = math.floor(Quo)
        res = int(Quo)*str("V")
        resultado.append(res)
        num = num % 5
    if num >= 4:
        Quo = num / 4
        Quo = math.floor(Quo)
        res = int(Quo)*str("IV")
        resultado.append(res)
        num = num % 4
    if num >= 1:
        Quo = num / 1
        Quo = math.floor(Quo)
        res = int(Quo)*str("I")
        resultado.append(res)
        num = num % 1
    
    resultado = "".join(resultado)
    
    return resultado 
    
    #Este código estúpidamente gigante e ineficiente é original.

def roman_to_int(num):
    
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    prev_value = 0

    for numeral in reversed(num):
        value = roman_numerals[numeral]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value

    return decimal
    
    # O código acima foi obtido através do CHAT GPT
