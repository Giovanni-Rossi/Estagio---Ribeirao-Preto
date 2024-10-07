#nome: verify_fibonnaci
#objetivo: verificar se um determinado número pertence a sequencia de fibonacci
# - num: numero a ser verificado, se pertence ou nã a sequência de fibonacci (parâmetro de entrada de dados)
# Valor de retorno: String contendo a informação se pertence ou não pertence a sequência

def verify_fibonacci(num):
    ok  = False
    if num == 0 or num == 1:
        ok = True
    else:
        ok = fibonacci_iterativo(num)

    if ok == True:
        return "O numero " + str(num) + " pertence a sequencia de fibonacci."            
    else:
        return "O numero " + str(num) + " nao pertence a sequencia de fibonacci."

#nome: fibonacci_iterativo
#objetivo: verificar se um determinado número pertence a sequencia de fibonacci iterativamente
# - num: numero a ser verificado, se pertence ou nã a sequência de fibonacci (parâmetro de entrada de dados)
# Valor de retorno: Bool, sendo True ou False
def fibonacci_iterativo(num):
    ok = False
    primeiro = 1
    segundo = 2
    while segundo < num:
        bau = segundo
        segundo = primeiro + segundo
        primeiro = bau

    if segundo == num:
        ok = True
    
    return ok

#inicialização de vetor contendo valores para teste
valores = [2, 3, 5, 7, 10, 12, 19, 23, 30, 41]
#teste e exibição da mensagem, se pertence ou não pertence
for valor in valores:
    print(verify_fibonacci(valor))