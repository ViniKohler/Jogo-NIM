def computador_escolhe_jogada(n, m):
    computadorRemove = 1

    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove

        else:
            computadorRemove += 1

    return computadorRemove


def usuario_escolhe_jogada(n, m):
    jogadaValida = False

    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças quer tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print('Jogada Inválida')
            print()

        else:
            jogadaValida = True

    return jogadorRemove


def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print(numeroRodada, 'ª Rodada')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Você 0 X 3 Computador')


def partida():
    escolhaInvalida = True

    while escolhaInvalida == True:
        n = int(input('Quantas peças teremos? '))
        m = int(input('Qual será o limite de peças por jogada? '))
        if m > n or n <= 0:
            print('Escolha inválida!')
        else:
            escolhaInvalida = False

    vezDoPC = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print('O computador tirou 1 peça')
            else:
                print()
                print('O computador tirou', computadorRemove, 'peças')

            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('Você tirou 1 peça')
            else:
                print()
                print('Você tirou', jogadorRemove, 'peças')
            vezDoPC = True
        if n == 1:
            print('Resta apenas 1 peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()
print('1 - para jogar uma partida isolada')
tipoDePartida = int(input('2 - para jogar um campeonato '))
print()

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()
