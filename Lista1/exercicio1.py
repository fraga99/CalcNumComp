def base2para10(num):
    # Separar a parte inteira e a parte fracionária
    partes = str(num).split('.')
    inteiro = partes[0]  # Parte inteira em binário como string
    frac = partes[1] if len(partes) > 1 else '0'  # Parte fracionária em binário como string

    # Converter a parte inteira de binário para decimal
    inteiro_decimal = 0
    for i, bit in enumerate(reversed(inteiro)):  # Reverter para trabalhar com potências crescentes de 2
        inteiro_decimal += int(bit) * (2 ** i)

    # Converter a parte fracionária de binário para decimal
    frac_decimal = 0
    for i, bit in enumerate(frac):
        frac_decimal += int(bit) * (2 ** -(i + 1))

    # Somar as partes
    resultado = inteiro_decimal + frac_decimal
    print(f"O valor binario {num} em decimal é: {resultado}")

base2para10('10101.001')

#### print do resultado ####
# O valor binario 10101.001 em decimal é: 21.125
