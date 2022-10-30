palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end='\n')
    print('\nFim')

aprovados = ['Raphaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print('\n', nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dia in dias_semana:
    print(f'Hoje é {dia}')
