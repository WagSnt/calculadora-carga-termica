from time import sleep


def leiaInt(msg):
    while True:
        try:                                                                             # tenta isso
            n = int(input(msg))
        except (ValueError, TypeError):                                                  # se não der, tenta isso
            print('\033[0;31mERRO: Por favor, digite um número válido.\033[m')
            continue                                                                     # retorna pro while para perguntar novamente
        except KeyboardInterrupt:
            print('\n\033[0;33mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:                                                                             # foi validado, finalizar
            return n


def linha(tam=42):                                                                        # linha para estética
    return '-' * tam


def cabecalho(txt):                                                                       # cria o cabeçalho, para criação do título do mesmo
    print(linha())
    print(f'\033[1;34m{txt.center(42)}\033[m')
    print(linha())


def menu(lista):                                                                          # Onde irá ficar as opções do menu
    c = 1                                                                                 # criar um contador
    for item in lista:                                                                    # para cada item na lista
        print(f'\033[1;97m{c}\033[m - \033[;34m{item}\033[m')                             # 'c' é o número da opção do menu e item é o nome da opção
        c += 1                                                                            # a cada item, aumenta a contagem
    print(linha())
    opc = leiaInt('\033[1;97mSua Opção:\033[m ')                                          # opc vai fazer a leitura da opção escolhida pelo usuário através da função 'leiaInt
    return opc                                                                            # retornar da função com a 'opc' selecionada


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;33mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return n


def conv_kcalh_btu(num):
    btu = 3.966
    totbtu = num * btu
    print(f'Calculabndo {num} x {btu}...')
    sleep(1)
    return totbtu


def rec_btu(num):
    if num < 7000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 7000 BTUs')
    elif 7000 <= num < 9000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 9000 BTUs')
    elif 9000 <= num < 12000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 12000 BTUs')
    elif 12000 <= num < 15000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 15000 BTUs')
    elif 15000 <= num < 18000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 18000 BTUs')
    elif 18000 <= num < 21000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 21000 BTUs')
    elif 21000 <= num < 24000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 24000 BTUs')
    elif 24000 <= num < 27000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 27000 BTUs')
    elif 27000 <= num < 30000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 30000 BTUs')
    elif 30000 <= num < 36000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 36000 BTUs')
    elif 36000 <= num < 42000:
        return print(f'Com {num} BTUs/h, é recomendado um ar condicionado a partir de 42000 BTUs')
