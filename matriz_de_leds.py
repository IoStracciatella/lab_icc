leds = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6}

n_vezes = int(input())
valores = []

for _ in range(n_vezes):
    N = input()
    N.strip()
    qtde_leds = 0

    N2 = [int(i) for i in N]

    for i in N2:
        qtde_leds += leds[i]
    
    valores.append(qtde_leds)

[print(valor + 5, "leds") for valor in valores]