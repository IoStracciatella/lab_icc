#include <stdio.h> //essas são as 2 bibiliotecas que usamos no código. esse stdio.h é a biblioteca de in out do C. e o math.h é pra podermos usar operações matemáticas tipo raiz quadrada
#include <math.h>

int main() {
    double a, b, c, x1, x2; //aqui eu to declarando as variáveis. sem inicilizar porque elas já vão receber um valor no scanf, então o lixo já vai sair
    double delta = 0; //declarei essa variável separada porque eu achei melhor inicializar ela

    scanf("%lf %lf %lf", &a, &b, &c); //aqui eu faço as variáveis receberem os valores do input do usuário

     if (a == 0) { 
        printf("nao eh uma equacao do segundo grau"); //esse if identifica se a = 0. se isso acontecer a equação não é do segundo grau
        return 0; //esse return 0 indica que o código termina aqui
    }

    delta = (b*b) - 4*a*c; //aqui eu faço operações básicas pra obter a fórmula do delta

    if (delta > 0) { //essa primeira parte do if identifica se delta > 0. sabemos que se uma equação do segundo grau tem delta maior que zero, ela tem 2 soluções reais. então, se delta for maior que zero, calculamos 2 valores para x

        x1 = (-b + sqrt(delta))/(2 * a); //formula para obter o valor de x. no caso com o sinal de soma
        x2 = (-b - sqrt(delta))/(2 * a); //mesma formula com o sinal de menos

        printf("x1 = %.5lf\nx2 = %.5lf", x1, x2); //printando os valores de x

    } else if (delta == 0) { //esse caso do if identifica se delta é zero. se delta for zero, a equação tem apenas um valor de x como solução

         x1 = -b/(2 * a); //formula para calcular o valor de x quando x = 0
        printf("Existe apenas um valor x = %.5lf que satisfaz a equacao", x1); //printando o valor de x

    } else if (delta < 0) { //finalmente, nesse caso identificamos se delta < 0. se delta for menor que zero, a equação não tem solução real

        printf("nao existe x real que satisfaca a equacao"); 

    }

    return 0; //sempre que terminar um código em C, tem que ter esse return 0
}
