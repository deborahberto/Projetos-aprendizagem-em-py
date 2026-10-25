#A variante usada neste problema envolve a construção de retângulos. O jogo consiste em, dado um conjunto de varetas de comprimentos variados, desenhar retângulos no chão, utilizando as varetas como lados dos retângulos, sendo que cada vareta pode ser utilizada em apenas um retângulo, e cada lado de um retângulo é formado por uma única vareta. Nesse jogo, duas crianças recebem dois conjuntos iguais de varetas. Ganha o jogo a criança que desenhar o maior número de retângulos com o conjunto de varetas.
#Dado um conjunto de varetas de comprimentos inteiros, você deve escrever um programa para determinar o maior número de retângulos que é possível desenhar.

while True:
    num_dif_varetas = int(input())
    if num_dif_varetas == 0:
        break
    
    soma_varetas = 0
    for _ in range(num_dif_varetas):
        tamanho, qtdade = [int(x) for x in input().split()]
        soma_varetas += qtdade // 2 * 2

    num_retangulos = soma_varetas // 4
    print(num_retangulos)