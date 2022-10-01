from lib.interface import *
from time import sleep

janela_leste = list()
janela_oeste = list()
totkcalh = 0


cabecalho('CALCULADORA SIMPLES DE CARGA TÉRMICA')
quant_janela = leiaInt('Quantas janelas possuem no leste? ')
for j in range(0, quant_janela):
    altura = leiaFloat(f'Digite a altura da {j+1}ª janela: ')
    largura = leiaFloat(f'Digite a largura da {j+1}ª janela: ')
    janela_leste.append(altura * largura)
    print(linha())
print(f'\033[1;97mTotal de janelas Leste:\033[m \033[1;34m{len(janela_leste)}\033[m')
print(f'\033[1;97mTotal de m² de janela no Leste:\033[m \033[1;34m{sum(janela_leste)}m²\033[m')
print(linha())

quant_janela = leiaInt('Quantas janelas possuem no Oeste? ')
for j in range(0, quant_janela):
    altura = leiaFloat(f'Digite a altura da {j+1}ª janela: ')
    largura = leiaFloat(f'Digite a largura da {j+1}ª janela: ')
    janela_oeste.append(altura * largura)
    print(linha())
print(f'\033[1;97mTotal de janelas Oeste:\033[m \033[1;34m{len(janela_oeste)}\033[m')
print(f'\033[1;97mTotal de m² de janela no Oeste:\033[m \033[1;34m{sum(janela_oeste)}m²\033[m')

parede_leste = leiaFloat('Quantos metros possui a parede Leste? ')
pedireito = leiaFloat('Quantos metros possui o pé direito? ')
totparede_leste = (parede_leste * pedireito) - sum(janela_leste)
print(f'Total de parede lado Leste: \033[1;34m{totparede_leste}\033[m')


# MENU: JANELAS INSOLAÇÃO - LESTE
cabecalho('JANELAS INSOLAÇÃO - LESTE')
print('As janelas possuem qual tipo de proteção:')
resposta = menu(['Sem proteção', 'Com proteção Interna', 'Com proteção Externa'])

if resposta == 1:
    totkcalh += sum(janela_leste) * 270
elif resposta == 2:
    totkcalh += sum(janela_leste * 130)
elif resposta == 3:
    totkcalh += sum(janela_leste * 85)
else:
    print('ERRO: Digite uma opção válida!')
print(f'\033[1;97mTotal de kcal/h:\033[m \033[1;34m{totkcalh}\033[m')


# MENU: JANELAS INSOLAÇÃO - OESTE
cabecalho('JANELAS INSOLAÇÃO - OESTE')
print('As janelas possuem qual tipo de proteção:')
resposta = menu(['Sem Proteção', 'Com Proteção Interna', 'Com Proteção Externa'])
if resposta == 1:
    totkcalh += sum(janela_oeste) * 500
elif resposta == 2:
    totkcalh += sum(janela_oeste) * 220
elif resposta == 3:
    totkcalh += sum(janela_oeste) * 150
else:
    print('ERRO: Digite uma opção válida!')
print(f'\033[1;97mTotal de kcal/h:\033[m \033[1;34m{totkcalh}\033[m')

# MENU: JANELAS TRANSMISSÃO
cabecalho('JANELAS TRANSMISSÃO')
resposta = menu(['Vidro Comum', 'Tijolo de Vidro'])
if resposta == 1:
    totkcalh += (sum(janela_leste) + sum(janela_oeste)) * 50
elif resposta == 2:
    totkcalh += (sum(janela_leste) + sum(janela_oeste)) * 25
else:
    print('ERRO: Digite uma opção válida!')
print(f'\033[1;97mTotal de kcal/h:\033[m \033[1;34m{totkcalh}\033[m')

# MENU: PAREDES EXTERNAS
cabecalho('PAREDES EXTERNAS')
ori_sul = leiaFloat('Quantos metros de parede externa no Sul? ')

if ori_sul > 0:
    print('Qual o tipo de construção do projeto: ')
    construcao = menu(['Leve', 'Pesada'])
    if construcao == 1:
        totkcalh += ori_sul * 13
    elif construcao == 2:
        totkcalh += ori_sul * 10
    else:
        print('ERRO: Digite uma opção válida!')

print(f'\033[1;97mTotal de kcal/h:\033[m \033[1;34m{totkcalh}\033[m')
ori_outra = leiaFloat('Quantos metros de parede externa nas demais orientações: ')
print('Qual o tipo de construção do projeto: ')
construcao = menu(['Leve', 'Pesada'])
if construcao == 1:
    totkcalh += ori_outra * 20
elif construcao == 2:
    totkcalh += ori_outra * 12
print(f'\033[1;97mTotal de kcal/h:\033[m \033[1;34m{totkcalh}\033[m')

# MENU: PAREDES INTERNAS
cabecalho('PAREDES INTERNAS')
parede_interna = leiaFloat('Quantos metros de parede interna no local: ')
totkcalh += parede_interna * 8
print(f'\033[1;97mTotal de kcal/h:\033[m \033[1;34m{totkcalh}\033[m')

# MENU TETO
cabecalho('TETO')
print('De que material o teto do projeto é feito: ')
resposta = menu(['Laje Exposta ao Sol sem Isolamento', 'Laje com 2.5 de isolação ou mais',
                 'Sob Telhado com Isolação', 'Sob Telhado Sem Isolação', 'Entre Andares'])
if resposta == 1:
    totkcalh += parede_interna * 75
elif resposta == 2:
    totkcalh += parede_interna * 30
elif resposta == 3:
    totkcalh += parede_interna * 18
elif resposta == 4:
    totkcalh += parede_interna * 50
elif resposta == 5:
    totkcalh += parede_interna * 13
else:
    print('ERRO: Digite uma opção válida!')
print(f'\033[1;97mTotal de kcal/h:\033[m \033[1;34m{totkcalh}\033[m')

# PISO
cabecalho('PISO')
totkcalh += parede_interna * 13
print(f'\033[1;97mTotal de kcal/h:\033[m \033[1;34m{totkcalh}\033[m')

# MENU: NÚMERO DE PESSOAS
cabecalho('NÚMERO DE PESSOAS')
pessoas = leiaInt('Digite quantas pessoas ficarão no local: ')
atividade = menu(['Repouso', 'Atividade Normal', 'Atividade Forte'])
if atividade == 1:
    totkcalh += pessoas * 175
elif atividade == 2:
    totkcalh += pessoas * 150
elif atividade == 3:
    totkcalh += pessoas * 750
else:
    print('ERRO: Digite uma opção válida!')
print(f'\033[1;97mTotal de kcal/h:\033[m \033[1;34m{totkcalh}\033[m')

# OUTRAS FONTES DE CALOR
cabecalho('OUTRAS FONTES DE CALOR')
print('Equipamentos elétricos e de iluminação:')
fonte_calor = leiaFloat('Digite em "W" o total de consumo dos equipamentos do local: ')
totkcalh += fonte_calor * 0.86
print(f'\033[1;97mTotal de kcal/h do projeto:\033[m \033[1;34m{totkcalh}\033[m')

# FATOR GEOGRÁFICO
regiao = str(input('O projeto é para o Sul do Brasil (RS, SC, PR)?[S/N] ')).strip().upper()[0]
if regiao in 'S':
    fg = 0.9
    totkcalh = totkcalh * fg
else:
    fg = leiaFloat('Qual o fator geográfico da sua região? ')
print(f'Aplicando o fator geográfico de {fg} no projeto...')
sleep(1)

# RESOLUÇÃO
totbtu = conv_kcalh_btu(totkcalh)
print('Cconvertendo kcal/h para BTU/h...')
sleep(2)
print('Reconhecendo o ar condicionado recomendado...')
sleep(2)
print(f'Total BTU/h: {totbtu:.4f}\nTotal TR: {totbtu / 12000:.4f}')
recomendacao = rec_btu(totbtu)
