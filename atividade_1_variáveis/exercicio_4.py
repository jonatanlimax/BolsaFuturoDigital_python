# 4. Dicion´arios
# Crie um dicion´ario chamado aluno com:
# • "nome": ”Maria”
# • "idade": 22
# • "curso": ”Engenharia”
# Depois:
# • Adicione uma nova chave "notas" com a lista [8.5, 7.0, 9.2]
# • Imprima apenas o valor da chave "curso"

#--------------------#

aluno={"nome":"maria","idade":22,"curso":"engenharia"}

#adicionando a chave 'notas'
aluno["notas"]=[8.5,7.0,9.2]

#imprimindo o valor da chave 'curso'
print(aluno["curso"])