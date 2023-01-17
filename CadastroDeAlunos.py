# ATIVIDADE ESPECIAL - CADASTRO DE ALUNOS

# MENU
def menu():
    print("-="*35)
    print("\n|                        CADASTRO DE ALUNOS                          |")
    print("-="*35)
    print("1.Incluir  2.Editar  3.Consultar  4.Deletar  5.Imprimir  6.Sair")
    print("-="*35)    
menu()
opcao = int(input("Informe uma opção: "))
#Dados em Lista
nomeL = list()
cursoL = list()
idadeL = list()
cidadeL = list()

#Funções
def incluir():
    nome = input("Nome: ").strip().title()
    nomeL.append(nome)
    idade =  int(input("Idade: "))
    idadeL.append(str(idade).strip())
    cidade =  input("Cidade: ").strip().title()
    cidadeL.append(cidade)
    curso = input("Curso: ").strip().title()
    cursoL.append(curso)

def imprimir():
    print("\nListagens de Alunos") 
    print("-"*30)
    print("Nome - Idade - Cidade / Curso") 
    print("-"*30)

    for x in range(0,len(nomeL)):
        print(nomeL[x],"-",idadeL[x],"anos","-",cidadeL[x],"/",cursoL[x])

def consultar():
    for x in range(0,len(nomeL)):
        print(nomeL[x],"-", idadeL[x],"anos","-", cidadeL[x],"/", cursoL[x])

def editar():
    editar = int(input("Informe o cadastro para editar: "))
    nomeL[editar] = (input("Nome: ")).strip().title()
    idadeL[editar] = int(input("Idade: ")) 
    cidadeL[editar] = input("Cidade: ").strip().title()
    cursoL[editar] = input("Curso: ").strip().title()
      
def deletar():
    deletar = int(input("Qual aluno você deseja apagar? "))
    del(nomeL[deletar], idadeL[deletar], cidadeL[deletar], cursoL[deletar])
    
#Condição no MENU

while True: 
    if opcao == 6:
        print("FIM!")
        break
    if opcao == 1:
        incluir()
    if opcao == 2:
        editar()
    if opcao == 3:
        consultar()
    if opcao == 4:
        deletar()
    if opcao == 5:
        imprimir()
    opcao = int(input("Por favor, Informe outra opção:"))
    
    

