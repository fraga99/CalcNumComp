def base10para2(num):
  # Separar a parte inteira da fracionaria
  parte_inteira = int(num)
  parte_frac = num - parte_inteira

  #converter a parte inteira para binario
  binario_inteiro = ''
  if parte_inteira == 0:
    binario_inteiro = '0'
  else:
    while parte_inteira > 0:
      binario_inteiro = str(parte_inteira % 2) + binario_inteiro
      parte_inteira = parte_inteira // 2 # trunca para o menor inteiro proximo

  # converter a parte fracionaria para binario
  binario_frac = ''
  contador = 0
  while parte_frac > 0 and contador < 10: # limitar precisao em 10 digitos
    parte_frac *= 2
    bit = int(parte_frac)
    binario_frac += str(bit)
    parte_frac -= bit
    contador = contador + 1

  # combinar a parte inteira com a fracionaria
  if binario_frac:
    return f"{binario_inteiro}.{binario_frac}"
  else:
    return binario_inteiro

num = 2345.625
print(f"O numero decimal {num} em binario é: {base10para2(num)}")

#### print do resultado ####
# O numero decimal 2345.625 em binario é: 100100101001.101

