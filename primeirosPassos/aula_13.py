# dicionarios, são estruturas que armazenam chaves e valores
# dicionario {chave:valor}

cargoEmpresa = {'Engenheiro':'Junior'}
print(cargoEmpresa)
print(cargoEmpresa['Engenheiro'])

cadastro = {'matricula': 123456,
            'dia_cadastro': 12,
            'mes_cadastro': 5,
            'turma': '4A'}
print(cadastro)
print(cadastro['matricula'])

# para manipular o dicionario, alterando o valor, podemos fazer dessa forma

cadastro['turma'] = '6A'
print(cadastro)
print(cadastro['turma'])

# e para adicionar mais um elemento basta fazer

cadastro['modalidade'] = 'EAD'
print(cadastro)
print(cadastro['modalidade'])
