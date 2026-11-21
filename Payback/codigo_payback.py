# Começo do projeto Payback.

print('Use o ponto no lugar de vírgula. Isso é temporário.')
valor_maquina = float(input('Qual o valor do maquinário? R$'))
unidades = int(input('Quantas unidades são produzidas? '))
horas_producao = float(input('Em quantas horas? '))
preco_venda = float(input('Preço de venda de cada unidade? R$'))
custo_unidade = float(input('Custo de produção de cada unidade? R$'))
horas_dias = float(input('Horas trabalhadas por dia? '))
dias_mes = int(input('Dias trabalhados por mês? '))
despesas_fixas = float(input('Despesas fixas mensais da máquina? R$'))

unidades_hora = unidades / horas_producao
producao_mes = unidades_hora * horas_dias * dias_mes
lucro_unidade = preco_venda - custo_unidade
lucro_mensal = producao_mes * lucro_unidade - despesas_fixas

if lucro_mensal <= 0:
    print('Com esses números a máquina não se paga.')
else:
    meses_pagar = valor_maquina / lucro_mensal
    print('Lucro mensal: R${:.2f}'.format(lucro_mensal))
    print('A máquina se paga em {:.2f} meses.'.format(meses_pagar))
