#O programa deve receber o valor de M, calcular e receber k
entrada = input("Informe o valor de M: ")
M_qtd = len(entrada)
M_valor = int(entrada)
for i in range(M_qtd):
    lado_esquerdo = (2**i)-1
    lado_direito = M_qtd + i
    #print(lado_esquerdo, lado_direito)
    if lado_esquerdo >= lado_direito:
        break
print("O valor de K é:", i)
