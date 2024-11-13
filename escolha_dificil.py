# Leitura das entradas
Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

# Calcula quantos passageiros ficarão sem suas escolhas
faltam_frango = max(0, Cr - Ca)
faltam_bife = max(0, Br - Ba)
faltam_massa = max(0, Pr - Pa)

# Calcula o total de refeições que faltam
total_faltam = faltam_frango + faltam_bife + faltam_massa

# Imprime o resultado
print(total_faltam)
