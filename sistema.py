estudantes_lista:str = ["Luana", "João", "Lucas"]

print("Bem vindo ao sistema academico:")
print("================================")

operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações / N - para sair): "))
operacao = operacao.upper()

if(operacao != "N" and operacao != "S"):
  print("Opção invalida")
  operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações / N - para sair): "))
  operacao = operacao.upper()

operacao = operacao.upper()


while(operacao == "S"):

  escolha_menu = int(input("Bem vindo ao menu principal, por favor escolha a opção desejada: \n 1. Estudantes \n 2. Disciplinas \n 3. Professores \n 4. Turmas \n 5. Matriculas \n 6. Sair \n"))

  if(escolha_menu == 1):
   escolha_pergunta = int(input("====== [ESTUDANTES] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial"))
   if(escolha_pergunta == 1):
     estudantes_lista = ["Luana", "João", "Lucas"]
     nome_estudante = str(input("Digite o nome do estudante que voce deseja inserir: "))
     estudantes_lista.append(nome_estudante)
     print("Estudante adicionado com sucesso")
   elif(escolha_pergunta == 2):
    estudantes_lista = ["Luana", "João", "Lucas"]
    for estudante in estudantes_lista:
                print(estudante)

   elif(escolha_pergunta == 3):
    print("Em desenvolvimento")

   elif(escolha_pergunta == 4):
    print("Em desenvolvimento")

   elif(escolha_pergunta == 5):
    print("Voltando ao menu inicial")
               


  elif(escolha_menu == 2):
   print("====== [DISCIPLINAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 3):
   print("====== [PROFESSORES] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 4):
   print("====== [TURMAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 5):
   print("====== [MATRICULAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 6):
   print("Obrigada por ultilizar nosso sistema, esperamos te ver em breve.")
  else:
   print("Opção invalida, por favor informe um numero valido, você sera direcionado para o menu inicial.")
  operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações e N para sair): "))
  operacao = operacao.upper()

  if(operacao == "N"):
   print("Bem vindo de volta ao menu do sistema academico")
   operacao = str(input("Deseja começar a fazer operações novamente? (S - Fazer operações e N para sair): "))
   operacao = operacao.upper()

print("===================================")
