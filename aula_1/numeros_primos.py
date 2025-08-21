numero = int(input())
eh_primo = True

for i in range(2, numero): # Esse range tem que ir de 2 até numero porque se começasse em 0 daria erro por
    if numero % i == 0:    # causa da divisão por 0, e se começassem em 1 eh_primo sempre seria verdadeiro 
        eh_primo = False   # porque até números primos são divisíveis por 1. E o range termina em numero e
                           # não em numero + 1 porque se terminasse no próprio número, como qualquer
if eh_primo == False:      # número é divisível por ele mesmo, eh_primo seria sempre true. Então o loop
    print('não é primo')   # for desse caso itera de 2 até 1 número antes do valor inserido
else:
    print('é primo')         