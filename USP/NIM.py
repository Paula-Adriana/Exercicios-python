
def computador_escolhe_jogada (n, m):
    computadorTira = 1
    while (computadorTira != m):
        if (n - computadorTira) % (m+1) == 0:
            return computadorTira
        else:
            computadorTira += 1
    return computadorTira
  
def usuario_escolhe_jogada(n, m):
    usuarioJoga = False
    while not usuarioJoga:
        usuarioTira = int(input('Quantas peças você vai tirar? '))
        if (usuarioTira < 1) or (usuarioTira > m):
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        else:
            usuarioJoga = True
    return usuarioTira       

def campeonato():
    numeroRodada = 1
    while (numeroRodada <= 3):
        print('**** Rodada', numeroRodada, '****')
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador') #rever o placar

def partida ():
    n = (int(input('Quantas peças? ')))
    m = (int(input('Limite de peças por jogada? ')))
    print()
    computadorJoga = False
    if ((n%(m+1)) == 0):
        print('Você começa!')
    else:
        print('Computador começa!')
        computadorJoga = True
    
    while n > 0:
        if computadorJoga:
            computadorTira = computador_escolhe_jogada(n, m)
            n = n - computadorTira
            if computadorTira == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', computadorTira, 'peças')
            computadorJoga = False
        else:
            jogadorTira = usuario_escolhe_jogada(n, m)
            n = n - jogadorTira
            if jogadorTira == 1:
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogadorTira, 'peças')
            computadorJoga = True

        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')
    print()

print('Bem-vindo ao jogo NIM! Escolha:')
print('1 - para jogar uma partida isolada:')
escolha = input('2 - para jogar um campeonato: ')
if (escolha == '1'):
    print('Voce escolheu partida isolada!')
    print()
    partida()
else:
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
    




