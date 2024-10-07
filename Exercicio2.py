#nome: ContaA
#objetivo: verificar se uma determinada frase contém ou não contém a letra 'a' ou 'A'
# - frase: frase a ser verificada, se possui ou não a letra "A" (parâmetro de entrada de dados)
# Valor de retorno: Contador, variável que retorna o número de vezes que a letra 'A' foi encontrada na frase
def Conta_A(frase):
    contador = 0
    for letra in frase:
        if letra.lower() == 'a':
            contador = contador + 1
    return contador

#Inicialização das frases
frases = ["sou seu amigo", "Bom dia!", "Feliz Natal", "Tchau, até amanhã!"]
#laço para o teste das frases
for frase in frases:
    print(Conta_A(frase))

