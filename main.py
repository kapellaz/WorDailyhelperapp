def gerir_dicionario(origem,destino): # nao chamar mais esta função
    with open(origem, 'r') as fi:
        with open(destino, 'w') as ff:
            for word in fi:
                #word = word[0:len(word)-1]
                #aqui temos a word
                if '-' not in word and ('A' in word or 'E' in word or 'I' in word or 'O' in word or 'U' in word):
                    ff.write(word)


def reduziu_print(tami,tamf):
    percentagem = str((tamf/tami) * 100)
    if percentagem != 100:
        print("Informação reduziu o tamanho da lista para", percentagem, "%")
    else:
        print("O número de palavras possíveis não se alterou")


def seleciona_words(origem,tam): # escolhe palavras só com o tamanho em jogo
    lista =[]
    with open(origem, 'r') as fi:
            for word in fi:
                word = word[0:len(word) - 1]
                # aqui temos a word
                if len(word) == tam:
                    lista.append(word)
    return lista


def letra_correta(lista,posicao,letra):
    lista_output = list()
    tam_lista = len(lista)
    i = 0
    while (i != tam_lista):
        if lista[i][posicao-1] == letra:
            lista_output.append(lista[i])
        i+=1
    reduziu_print(len(lista),len(lista_output))
    return lista_output


def letra_incerta(lista, posicao, letra):
    lista_output = list()
    tam_lista = len(lista)
    i = 0
    while (i != tam_lista):
        if letra in lista[i] and lista[i][posicao-1] != letra:
            lista_output.append(lista[i])
        i += 1
    reduziu_print(len(lista), len(lista_output))
    return lista_output


def letra_incorreta(lista,letra):
    lista_output = list()
    tam_lista = len(lista)
    i=0
    while (i != tam_lista):
        if letra not in lista[i]:
            lista_output.append(lista[i])
        i += 1
    return lista_output


def letra_incorreta_max(lista,cadeia):
    aux = len(lista)
    listaa = lista
    for i in cadeia:
        listaa = letra_incorreta(listaa,i)
    reduziu_print(aux, len(listaa))
    return listaa


def limita_rep(lista, letra, reps, certeza):
    lista_output = list()
    tam_lista = len(lista)
    i = 0
    while (i != tam_lista):
        count = 0
        for l in lista[i]:
            if l == letra:
                count += 1
        if certeza:
            if count == reps:
                lista_output.append(lista[i])
        else:
            if count >= reps:
                lista_output.append(lista[i])
        i += 1
    reduziu_print(tam_lista, len(lista_output))
    return lista_output



def tamanho():
    nletras_atual = 0
    while nletras_atual == 0:
        aux = int(input("Introduza o número de letras: "))
        if aux>3 and aux<8:
                nletras_atual = aux
        else:
            print("ERRO")
    return nletras_atual



def recebe_info(l, copia_seguranca):
    aux_copia = copia_seguranca
    copia_seguranca = l
    print("Escolha a opção: ")
    print("1 - Letra CERTA")
    print("2 - Letra INCERTA")
    print("3 - cadeia de letras ERRADAS")
    print("4 - pelo menos x REPETIÇÕES")
    print("5 - exatamente x REPETIÇÕES")
    print("6 - Ctr Z")
    opcao = int(input("opção: "))
    if opcao == 1:
        pos = int(input("posição: "))
        letra = input("letra: ").upper()
        l = letra_correta(l, pos, letra)
    elif opcao == 2:
        letra = input("letra: ").upper()
        pos = int(input("posição: "))
        l = letra_incerta(l, pos, letra)
    elif opcao == 3:
        letra = input("letra: ").upper()
        l = letra_incorreta_max(l, letra)
    elif opcao == 4:
        letra = input("letra: ").upper()
        reps = int(input("reps: "))
        l = limita_rep(l, letra, reps, False)
    elif opcao == 5:
        letra = input("letra: ").upper()
        reps = int(input("reps: "))
        l = limita_rep(l, letra, reps, True)
    elif opcao == 6:
        return aux_copia, aux_copia
    return l, copia_seguranca


def imprime_palavras(l):
    for p in l:
        print(p)



def main():
    tamanho_de_jogo = tamanho()
    lista_de_palavras_possiveis = seleciona_words("palavrastodas.txt", tamanho_de_jogo)
    copia_seguranca = list()
    if tamanho_de_jogo == 7:
        ultima = input("Última letra: ")
        lista_de_palavras_possiveis = letra_correta(lista_de_palavras_possiveis, 7, ultima.upper())
    while (True):
        print("##### Ainda há {" + str(len(lista_de_palavras_possiveis)) + "} palavras possíveis #####")
        print("________MENU_______")
        print("1 - Adicionar informação")
        print("2 - Imprimir palavras possíveis")
        print("0 - SAIR")
        opcao = int(input("opção: "))
        if opcao == 0:
            break
        elif opcao == 1:
            lista_de_palavras_possiveis, copia_seguranca = recebe_info(lista_de_palavras_possiveis, copia_seguranca)
        elif opcao == 2:
            imprime_palavras(lista_de_palavras_possiveis)


main()
#gerir_dicionario("dicionariofull.txt", "palavrastodas.txt")