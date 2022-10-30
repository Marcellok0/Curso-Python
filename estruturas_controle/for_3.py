produto = {'Nome': 'Caneta chic', 'Preco': 14.99,
           'Importada': True, 'Estoque': 793}

for chave in produto:  # mostra a chave
    print(chave)

for valor in produto.values():  # mostra os valores
    print(valor)

for chave, valor in produto.items():  # mostra valores e chaves separado pelo =
    print(chave, '=', valor)
