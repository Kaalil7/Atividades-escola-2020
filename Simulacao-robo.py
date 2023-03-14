import os
print("=-" *20 )
print("Bem vindo ao Hospital Belas Artes!")
print("=-"*20)

escolha = input("\n Seja bem vindo! Escolha a opção de sua escolha!\n\n 1 - Dúvidas\n 2 - Consultas presencialmente\n 3 - Telemedicina\n 4 - Marcar examas\n 5 - Pegar exames\n\n")

os.system("clear")

if (escolha == "1" or escolha == "Dúvidas"):
  print("=-"*40)
  print("Dúvidas frequentes:\n")
  print("Nosso hospital se encontra na Avenida Paulista, nº 1103")
  print("Fazemos todos os tipos de exames!")
  print("O prédio 1 é apenas o hospital, o láboratorio é no prédio 2!")
  print("=-"*40)
  input("\nQual sua dúvida?\n\n- ")
  input("\nDigite seu nome:\n\n- ")
  input("\nDigite seu e-mail:\n\n- ")
  input("\nDigite seu telefone:\n\n- ")
  print("Obrigado pela escolha! Entraremos em contato assim que possível!")
elif (escolha == "2" or escolha == "Consultas presencialmente"):
  input("\nQual consulta gostaria?\n\n- ")
  input("\nQual dia você gostaria?(Dia e mês)\n\n- ")
  input("\nDigite seu nome:\n\n- ")
  input("\nDigite seu e-mail:\n\n- ")
  input("\nDigite seu telefone:\n\n- ")
  print("\nObrigado pela escolha! Entraremos em contato assim que possível!")
elif (escolha == "3" or escolha == "Telemedicina"):
  input("\nQuais são seus sintomas?\n\n- ")
  input("\nHá quanto tempo está tendo estes sintomas?\n\n- ")
  input("\nJá tomou algum medicamento?\n\n- ")
  input("\nEstá sentindo alguma dor?\n\n- ")
  input("\nDigite seu nome:\n\n- ")
  input("\nDigite seu e-mail:\n\n- ")
  input("\nDigite seu telefone:\n\n- ")
  print("\nObrigado pela escolha! Um médico entrará em contanto com você assim que possível!\n")
  print("=-"*40)
  print("OBSERVAÇÃO: Dependendo dos sintomas, você será recomendado a vir ao hospital!")
  print("=-"*40)
elif (escolha == "4" or escolha == "Marcar Exame"):
  input("\nQual exame gostaria?\n\n- ")
  input("\nQual dia você gostaria?(Dia e mês)\n\n- ")
  input("\nDigite seu nome:\n\n- ")
  input("\nDigite seu e-mail:\n\n- ")
  input("\nDigite seu telefone:\n\n- ")
  print("\nObrigado pela escolha! Entraremos em contato assim que possível!")
elif (escolha == "5" or escolha == "Pegar exames"):
  print("=-"*40)
  print("Nosso laborátorio fica aberto de segunda a sexta, das 6:00h às 17:30h")
  print("Você poderá busca-lo em algum destes dias e horários!")
  input("=-"*40)
  os.system("clear")
  print("=-"*40)
  print("Para recebe-lo em casa, basta concluir o cadastro abaixo!\n")
  print("=-"*40)
  input("Qual o exame que deseja receber?\n\n- ")
  input("\nQual seu nome?\n\n- ")
  input("\nQual seu endereço?\n\n- ")
  input("\nQual seu e-mail?\n\n- ")
  input("\nQual seu telefone?\n\n- ")
  print("\nObrigado pela escolha! Você receberá uma ligação dentro de alguns minutos!")
else:
  print("Opção inválida.")