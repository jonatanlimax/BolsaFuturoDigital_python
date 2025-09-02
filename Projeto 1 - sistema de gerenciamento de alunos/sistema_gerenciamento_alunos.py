# ==============================================================
#   SISTEMA DE GERENCIAMENTO DE ALUNOS
# ==============================================================

# ------------------------
# Lista de alunos
# ------------------------
alunos = []


# ------------------------
# Função de login
# ------------------------
def menu_login():   #Mostrar uma mensagem ao iniciar o sistema
    print("======================================================\n")
    print("BEM VINDO(A) AO PROGRAMA BOLSA FUTURO DIGITAL - SOFTEX")
    print("\n======================================================\n\n")
    print("-------------------SISTEMA DE LOGIN-------------------\n\n")

# ------------------------
# Login Professor(a)
# ------------------------

usuario = "ana.clara"   # Usuário padrão do sistema                                                                        
senha = "123@abcd"      # Senha padrão do sistema                                                                       
logado = False          # Controla se o login foi realizado                                                                       
def login():
    # Solicitar usuário/senha, removendo espaços com strip() e ignorando maiúsculas com lower() 
    login = input("Usuário: ")                                             
    senha_1 = input("\nSenha: ")                                                  

    # Verificar se os campos foram preenchidos
    if not login or not senha_1: # bug corrigido
        print("\nUsuário e senha não podem estar vazios.")
        return False
    
    # Verificar se as credenciais estão corretas
    if login == usuario and senha_1 == senha:
        # Login bem-sucedido 
        print("\nAcesso permitido")                                                      
        return True
    else:
        # Credenciais inválidas
        print("\nAcesso negado. Usuário e/ou senha incorretos, tente novamente.")          
        return False

# ----------------------------------
# Função para cadastro de aluno
# ----------------------------------

def cadastrar_aluno():
    """Cadastra um novo aluno no sistema.""" 
    
    # Calcula o próximo ID com base no total de alunos já cadastrados
    alunos_existentes = 0
    for _ in alunos:                                                                          
        alunos_existentes += 1           
    id_novo = alunos_existentes + 1 # Próximo ID sequencial

    # Loop para coletar e validar o nome do aluno
    while True:
        # capitalize() Normaliza o nome para que a primeira letra seja maiúscula
        nome = input("Digite o nome do aluno(a): ").strip().capitalize()                 
                                                                                                                                                                                      
        # Validação de tamanho: evita nomes vazios ou muito longos
        if not (1 <= len(nome) <= 50):
            print("Nome inválido! Digite entre 1 e 50 caracteres.")
            continue                                                                     

        break  # sai do laço se o nome for válido

    # Loop para coletar e validar a idade do aluno 
    while True:  
        # Coleta e valida a idade do aluno.                                                                                             
        try:                                                                                  
            idade = int(input("Digite a idade do aluno(a): "))                     
        except ValueError:
            print("Erro: Digite apenas números inteiros para a idade.")
            continue
        # Com o if, a gente garante que a idade esteja dentro do intervalo permitido
        if 0 <= idade <= 120:                                                                 
            break   # break encerra o laço quando o valor está correto
        print(" Idade fora do intervalo (0 a 120). Digite novamente.")  #Se a idade for inválida, mostra aviso e repete a pergunta

    # Função auxiliar para ler e validar uma nota entre 0 e 10
    def ler_nota(rotulo):
        while True:
            # Solicita a nota ao usuário e remove espaços extras antes/depois
            entrada = input(f"{rotulo} (0 a 10): ").strip() 

            # Verifica se o usuário não digitou nada
            if not entrada:
                print("Entrada vazia. Digite uma nota entre 0 e 10.")
                continue

            # Verifica se o usuário usou vírgula em vez de ponto para decimais
            if "," in entrada:
                print("Use ponto (.) para decimais, não vírgula.")
                continue

            # Tenta converter a entrada para número decimal
            try:
                valor = float(entrada)                       
            except ValueError:
                print("Erro: Digite apenas números válidos.")# Mensagem de erro quando a entrada é inválida
                continue

            # Verifica se o número está dentro do intervalo permitido            
            # Semelhante ao input da idade, o if define o intervalo permitido
            if 0 <= valor <= 10:
                return valor   
                                                                                   
            print("Nota fora do intervalo (0 a 10). Digite novamente.") 

    # Leitura das três notas do aluno               
    nota1 = ler_nota("Nota 1")
    nota2 = ler_nota("Nota 2")
    nota3 = ler_nota("Nota 3")

    # Cria dicionário com os dados do aluno
    aluno = {                                                                                
        "id": id_novo,  # ID sequencial do aluno                                                                      
        "nome": nome,   # Nome do aluno                                                                    
        "idade": idade, # Idade do aluno
        "nota1": nota1, # Primeira nota
        "nota2": nota2, # Segunda nota
        "nota3": nota3  # Terceira nota
    }

    # Insere o dicionário contendo todos os dados do aluno na lista de alunos
    alunos.append(aluno)
    # Confirmação visual ao usuário de que o aluno foi cadastrado com sucesso, mostrando o ID gerado                                                                    
    print("OK, aluno cadastrado com ID:", id_novo)                                       
                                                                                             
# -------------------------------
# Função para listar alunos
# -------------------------------

def listar_alunos():
    # """Lista todos os alunos cadastrados."""

    # Verifica se a lista de alunos está vazia antes de tentar listar
    if len(alunos) == 0:                                                                     
        print("Nenhum aluno cadastrado.")
    else:
        # Itera sobre a lista e exibe os dados de cada aluno
        for aluno in alunos:
            print(
                "ID:", aluno["id"],
                "| Nome:", aluno["nome"],
                "| Idade:", aluno["idade"],
                "| Notas:", aluno["nota1"], aluno["nota2"], aluno["nota3"]
            )
        # Exibe o total de alunos cadastrados
        print(f"Total de alunos cadastrados: {len(alunos)}")                              

# ---------------------------------------------
# Função para buscar aluno (por nome ou ID)
# ---------------------------------------------

def buscar_aluno():
    # """
    # Busca um aluno no sistema pelo nome ou ID.
    # Faz tratamento de entradas inválidas.
    # """
    # Pergunta ao usuário se a busca será por nome ou ID
    escolha = input("Buscar por [1] Nome ou [2] ID: ").strip()                            

    if escolha == "1":
        # Busca por nome: solicita e normaliza a entrada
        nome = input("Digite o nome do aluno: ").strip().lower()
        if nome == "":
            print("Nome não pode ser vazio!")
            return
        
        # Filtra alunos cujo nome contenha a string informada
        encontrados = [aluno for aluno in alunos if nome in aluno["nome"].lower()]

        # Exibe os alunos encontrados ou mensagem de erro
        if encontrados:
            for aluno in encontrados:
                print(f"{aluno['id']} |  {aluno['nome']} |  Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}")
        else:
            print("Aluno não encontrado.")

    elif escolha == "2":
        #Busca por ID do aluno e valida como número inteiro
        try:
            id_aluno = int(input("Digite o ID do aluno: "))
        except ValueError:
            print("ID inválido. Digite apenas números.")
            return
        
        # Procura aluno com o ID informado
        for aluno in alunos:
            if aluno["id"] == id_aluno:
                print(f" {aluno['id']} |  {aluno['nome']} |  Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}")
                return
        print(" Aluno não encontrado.")

    else:
        # Caso a escolha seja diferente de 1 ou 2
        print(" Opção inválida.")

# --------------------------------------------
# Função para calcular média individual
# --------------------------------------------

def media_individual():
    #"""Mostra a média de cada aluno e se está aprovado ou reprovado."""

    # Verifica se existem alunos cadastrados antes de calcular a média
    if len(alunos) == 0:                                                                     
        print(" Nenhum aluno cadastrado.")
    else:
        # Itera sobre cada aluno para calcular e exibir a média
        for aluno in alunos:
            # Calcula a média das três notas - Soma as notas e divide por 3
            media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3
            print(aluno["nome"], "- Média:", round(media, 2))  # Mostra média com 2 casas decimais - Round(xxxxx, 2)                            

            # Critério de aprovação - Verifica se o aluno está aprovado (média >= 7) ou reprovado
            if media >= 7:
                print("Aprovado")
            else:
                print("Reprovado")

# --------------------------------------------
# Função para deletar aluno e alterar nota
# --------------------------------------------

def deletar_aluno():
    #"""Deleta um aluno ou altera UMA das notas USANDO O ID OU NOME.""" 

    # Verifica se existem alunos cadastrados
    if not alunos: 
        print("Nenhum aluno cadastrado para deletar ou alterar.")
        return
    
    # Menu de escolha do método de busca
    print("\nDeseja buscar o aluno por:")
    print("1 - ID")
    print("2 - Nome (ou parte dele)")
    escolha = input("Escolha: ").strip()

    # Inicializa variável para armazenar o aluno encontrado
    aluno_encontrado = None

    if escolha == "1":  
       # Busca pelo ID                                                                     
       while True: 
            try:
                id_busca = int(input("Digite o ID do aluno a ser deletado/alterado: "))  
                # Procura o aluno correspondente ao ID informado         
                for aluno in alunos:
                    if aluno["id"] == id_busca:
                        aluno_encontrado = aluno
                        break

                # Verifica se encontrou o aluno
                if aluno_encontrado:
                    break  #Sai do while
                else:
                    print(f"Nenhum aluno encontrado com o ID {id_busca}. Tente novamente.")

            except ValueError:
                # Trata erro caso o usuário digite algo que não seja um número inteiro
                print("Entrada inválida. O ID deve ser um número inteiro.")
                continue  #Volta ao início do loop para tentar novamente                                                                                
               
    elif escolha == "2":
        # Busca pelo nome ou parte dele
        while True:
            nome_busca = input("Digite o nome (ou parte dele): ").strip().lower() 

            # Verifica se o usuário digitou algo                                                                        
            if not nome_busca:                                                                
                print("Você precisa digitar algum nome.")
                continue #Volta ao início do loop para nova tentativa

            # Filtra a lista de alunos pelo nome digitado                                                                                
            possiveis = [aluno for aluno in alunos if nome_busca in aluno["nome"].lower()]

            # Trata os diferentes casos:
            # 0 alunos encontrados → exibe mensagem de erro
            # 1 aluno encontrado → seleciona automaticamente
            # Mais de 1 aluno encontrado → solicitar escolha pelo ID
            if len(possiveis) == 0:
                print("Nenhum aluno encontrado com esse nome.")
                return
            elif len(possiveis) == 1:
                aluno_encontrado = possiveis[0]
                break
            else:
                # Mais de um aluno encontrado → exibe lista e solicita ID para seleção
                print("\n Foram encontrados vários alunos:")
                for aluno in possiveis:
                    print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | Idade: {aluno['idade']}")

                # Loop de validação para garantir que o usuário digite um ID válido
                while True:   
                    try: 
                        id_escolhido = int(input("Digite o ID do aluno que deseja deletar/alterar: "))
                        # Procura na lista de possíveis alunos aquele que corresponde ao ID escolhido pelo usuário
                        for aluno in possiveis:
                            if aluno["id"] == id_escolhido:  # Armazena o aluno selecionado
                                aluno_encontrado = aluno
                                break    # Interrompe o loop assim que encontra o aluno correto

                        if aluno_encontrado:
                                break #Sai do loop de escolha de ID
                        else:
                            print("ID não encontrado entre os alunos listados.")
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro para o ID.") 
                break 

        # Caso não encontre nenhum aluno após a busca por nome         
        if aluno_encontrado is None:
            print("Aluno não encontrado.")
            return 

        # Exibe dados do aluno encontrado        
        aluno = aluno_encontrado
        print(f"\n Aluno encontrado: {aluno['nome']} (ID: {aluno['id']}) |  Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}")

    # Menu de ação: deletar aluno ou alterar nota
    print("\nO que deseja fazer?")
    print("1 - Deletar aluno completo")
    print("2 - Alterar uma nota")                                                            

    # Loop de validação da escolha da operação
    while True:        
        # Só sai do loop quando a entrada for "1" (deletar) ou "2" (alterar nota)
        opcao = input("Escolha: ")
        if opcao in ["1", "2"]:
            break  # Sai do loop se a escolha for válida
        print("Opção inválida. Digite 1 para deletar ou 2 para alterar uma nota.")   

    #deletar aluno completo          
    if opcao == "1":
        # Confirmação antes de deletar - retorna o valor da função de confirmação
        confirm = confirmar()                                                               
        if confirm == True: 
            # Remove o dicionário completo do aluno da lista                                                             
            alunos.remove(aluno_encontrado)                                                            
            print(f"O aluno '{aluno_encontrado['nome'].capitalize()}' foi deletado com sucesso!")

    #Modifica a nota        
    elif opcao == "2":
        # Menu para escolher qual nota alterar
        print("\nQual nota deseja alterar?")
        print("1 - Nota 1")
        print("2 - Nota 2")
        print("3 - Nota 3")

        # Validação da escolha da nota
        while True:
            nota_opcao = input("Escolha: ").strip()
            if nota_opcao in ["1", "2", "3"]:
                break # Sai do loop se a escolha for válida
            print(" Opção inválida. Digite 1, 2 ou 3.")
            
        # Validação da nova nota (0...10)com tratamento de erro acrescentado
        while True:
            try:
                # Solicita a nova nota ao usuário e tenta converter para float
                nova_nota = float(input("Digite a nova nota (0 a 10): "))

                # Verifica se a nota está dentro do intervalo permitido
                if 0 <= nova_nota <= 10:
                    break # Sai do loop se a nota for válida
                else:
                    print("Nota fora do intervalo. Digite um valor entre 0 e 10.")
            except ValueError:
                # Caso a entrada não seja um número válido, exibe mensagem de erro
                print("Entrada inválida. Por favor, insira uma nota entre 0 e 10.")

        # Atualiza a nota correspondente      
        if nota_opcao == "1":
            aluno_encontrado["nota1"] = nova_nota
        elif nota_opcao == "2":
            aluno_encontrado["nota2"] = nova_nota
        elif nota_opcao == "3":
            aluno_encontrado["nota3"] = nova_nota
        print(f"As notas atualizadas do aluno '{aluno_encontrado['nome'].capitalize()}': {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}")
    
# ----------------------------------------
# Função para calcular média geral
# ----------------------------------------

def media_geral():
    """Calcula a média geral de todos os alunos.""" 

    # Verifica se existem alunos cadastrados antes de calcular a média
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        soma_notas = 0  # Variável para acumular a soma de todas as notas
        total_notas = 0 # Variável para contar o total de notas cadastradas

        # Percorre cada aluno da lista para somar suas três notas
        for aluno in alunos:
            soma_notas += aluno["nota1"] + aluno["nota2"] + aluno["nota3"]
            total_notas += 3 # Cada aluno tem 3 notas

        # Calcula a média geral dividindo a soma total pelo número de notas
        media = soma_notas / total_notas
        
        # Exibe a média arredondada com 2 casas decimais
        print(f"Média geral da turma: {round(media, 2)}")

#--------------------------------
# Função de Confirmação
#--------------------------------
# Tratamento de erro incluído: valida a entrada para aceitar apenas 'S' ou 'N', garantindo confirmação segura.

def confirmar():
    # """
    # Solicita confirmação do usuário.
    # Retorna True se o usuário confirmar ('S') ou False se negar ('N').
    # """
    # Loop infinito até o usuário fornecer uma entrada válida
    while True:
        opcao_1 = input("Deseja confirmar (S/N): ").strip().lower()
        if opcao_1 == "s":
            return True # Retorna True se o usuário confirmar
        elif opcao_1 == "n":
            return False # Retorna False se o usuário negar
        else:
            # Mensagem de erro caso a entrada não seja 'S' ou 'N'
            print("Entrada inválida. Digite 'S' para sim ou 'N' para não.")

# ------------------------
# Menu principal
# ------------------------

#Função mais simples com PRINTS apenas para mostrar opções aos usuarios e \n para pular 1 linha.
def exibir_menu():
    # """Exibe o menu de opções na tela."""
    # Cabeçalho do sistema
    print("\n==Sistema de Gerenciamento de Alunos==")
    print("\n\n===  MENU INICIAL ===")

    # Lista as opções disponíveis para o usuário
    print("\n1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Média individual")
    print("4 - Buscar Aluno")
    print("5 - Deletar/alterar nota")                                                            
    print("6 - Média geral da turma")

    # Opção para encerrar o sistema
    print("\n0 - Sair")

# ---------------------------
# Execução do programa
# ---------------------------

def main(): 
    # """
    # Função principal do programa.

    # Controla o fluxo geral do sistema de gerenciamento de alunos:
    # - Exibe a tela de login e autentica o usuário.
    # - Após login bem-sucedido, exibe o menu principal.
    # - Permite acessar todas as funcionalidades do sistema, como cadastrar, listar, buscar,
    #   deletar/alterar notas e calcular médias.
    # - Finaliza o programa quando o usuário escolhe a opção de sair.
    # """                                                                                     
    # Loop infinito até que o usuário consiga efetuar login corretamente
    while True:                                                                                         
        menu_login()       # Exibe a tela de boas-vindas e instruções de login                                                                                     
        logado = login()   # Chama a função de login e recebe True se as credenciais forem válidas 

        if logado == True:
            # Loop principal do sistema após login bem-sucedido
            while True:
                # Mostra as opções do menu para o usuário
                exibir_menu()
                # Lê a opção escolhida pelo usuário                                                                    
                opcao = input("\nEscolha uma opção: ").strip() 

                # Executa a função correspondente à opção escolhida
                if opcao == "1":
                    # Chama a função para cadastrar um novo aluno
                    cadastrar_aluno()
                elif opcao == "2":
                    # Lista todos os alunos cadastrados
                    listar_alunos()
                elif opcao == "3":
                    # Mostra a média de cada aluno e status
                    media_individual()
                elif opcao == "4":
                    # Busca um aluno pelo nome ou ID
                    buscar_aluno()
                elif opcao == "5":
                    # Permite deletar um aluno ou alterar uma nota
                    deletar_aluno()
                elif opcao == "6":
                    # Calcula e exibe a média geral da turma
                    media_geral()
                elif opcao == "0":
                    # Mensagem de despedida
                    print(" Tchau, até mais!")
                    return # Encerra a função principal e finaliza o programa
                else:
                    # Mensagem para entradas inválidas
                    print(" Opção inválida. Tente novamente.")
            break


# Ponto de entrada do programa
# Chama a função main(), que inicia o sistema de gerenciamento de alunos
# e controla todo o fluxo do programa a partir do login até o encerramento.
main()
