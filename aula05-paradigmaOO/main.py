from aluno import Aluno

aluno1 = Aluno(20231050, 'fulaninho', [])

print(aluno1.nome)
print(aluno1.matricula)
print(aluno1.matriculaFormatada)
aluno1.nome = 'macaco'
print(aluno1.nome)
aluno1.adicionaNota(5)
aluno1.adicionaNota(10)
aluno1.adicionaNota(8)
print(aluno1.media())