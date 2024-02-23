from time import sleep as SLP
import os
import random
logoprojeto=("""
 bbbbbbbbb                                                                                                             
LLLLLLLLLLL               iiii b::::::b                                                             tttt                                            
L:::::::::L              i::::ib::::::b                                                          ttt:::t                                            
L:::::::::L               iiii b::::::b                                                          t:::::t                                            
LL:::::::LL                     b:::::b                                                          t:::::t                                            
  L:::::L               iiiiiii b:::::bbbbbbbbb        eeeeeeeeeeee    rrrrr   rrrrrrrrr   ttttttt:::::ttttttt      aaaaaaaaaaaaa      ssssssssss   
  L:::::L               i:::::i b::::::::::::::bb    ee::::::::::::ee  r::::rrr:::::::::r  t:::::::::::::::::t      a::::::::::::a   ss::::::::::s  
  L:::::L                i::::i b::::::::::::::::b  e::::::eeeee:::::eer:::::::::::::::::r t:::::::::::::::::t      aaaaaaaaa:::::ass:::::::::::::s 
  L:::::L                i::::i b:::::bbbbb:::::::be::::::e     e:::::err::::::rrrrr::::::rtttttt:::::::tttttt               a::::as::::::ssss:::::s
  L:::::L                i::::i b:::::b    b::::::be:::::::eeeee::::::e r:::::r     r:::::r      t:::::t              aaaaaaa:::::a s:::::s  ssssss 
  L:::::L                i::::i b:::::b     b:::::be:::::::::::::::::e  r:::::r     rrrrrrr      t:::::t            aa::::::::::::a   s::::::s      
  L:::::L                i::::i b:::::b     b:::::be::::::eeeeeeeeeee   r:::::r                  t:::::t           a::::aaaa::::::a      s::::::s   
  L:::::L         LLLLLL i::::i b:::::b     b:::::be:::::::e            r:::::r                  t:::::t    tttttta::::a    a:::::assssss   s:::::s 
LL:::::::LLLLLLLLL:::::Li::::::ib:::::bbbbbb::::::be::::::::e           r:::::r                  t::::::tttt:::::ta::::a    a:::::as:::::ssss::::::s
L::::::::::::::::::::::Li::::::ib::::::::::::::::b  e::::::::eeeeeeee   r:::::r                  tt::::::::::::::ta:::::aaaa::::::as::::::::::::::s 
L::::::::::::::::::::::Li::::::ib:::::::::::::::b    ee:::::::::::::e   r:::::r                    tt:::::::::::tt a::::::::::aa:::as:::::::::::ss  
LLLLLLLLLLLLLLLLLLLLLLLLiiiiiiiibbbbbbbbbbbbbbbb       eeeeeeeeeeeeee   rrrrrrr                      ttttttttttt    aaaaaaaaaa  aaaa sssssssssss    
                                                                                                                                                    """)#logo principal!


logoaula = str("""
               AAA                              lllllll                             000000000       1111111   
              A:::A                             l:::::l                           00:::::::::00    1::::::1   
             A:::::A                            l:::::l                         00:::::::::::::00 1:::::::1   
            A:::::::A                           l:::::l                        0:::::::000:::::::0111:::::1   
           A:::::::::A        uuuuuu    uuuuuu   l::::l   aaaaaaaaaaaaa        0::::::0   0::::::0   1::::1   
          A:::::A:::::A       u::::u    u::::u   l::::l   a::::::::::::a       0:::::0     0:::::0   1::::1   
         A:::::A A:::::A      u::::u    u::::u   l::::l   aaaaaaaaa:::::a      0:::::0     0:::::0   1::::1   
        A:::::A   A:::::A     u::::u    u::::u   l::::l            a::::a      0:::::0 000 0:::::0   1::::l   
       A:::::A     A:::::A    u::::u    u::::u   l::::l     aaaaaaa:::::a      0:::::0 000 0:::::0   1::::l   
      A:::::AAAAAAAAA:::::A   u::::u    u::::u   l::::l   aa::::::::::::a      0:::::0     0:::::0   1::::l   
     A:::::::::::::::::::::A  u::::u    u::::u   l::::l  a::::aaaa::::::a      0:::::0     0:::::0   1::::l   
    A:::::AAAAAAAAAAAAA:::::A u:::::uuuu:::::u   l::::l a::::a    a:::::a      0::::::0   0::::::0   1::::l   
   A:::::A             A:::::Au:::::::::::::::uul::::::la::::a    a:::::a      0:::::::000:::::::0111::::::111
  A:::::A               A:::::Au:::::::::::::::ul::::::la:::::aaaa::::::a       00:::::::::::::00 1::::::::::1
 A:::::A                 A:::::Auu::::::::uu:::ul::::::l a::::::::::aa:::a        00:::::::::00   1::::::::::1
AAAAAAA                   AAAAAAA uuuuuuuu  uuuullllllll  aaaaaaaaaa  aaaa          000000000     111111111111""")#logo
print(logoprojeto)#imprime a logo!

def script_aula1():#Define uma função par ser usada para ser acessado o script da aula 1.
    print(str("Escolha de número 1"))#Print normal!
    #Lógica do Script
    print("Neste Script você irá escolher um número de 0 a 3 e irá competir com o computador para ver se consegue advinhar o número em que ele está pensando. Boa Sorte")#Explicação
    while True:#um loop de condição (enquanto for verdadeiro ira continuar executando)
        escolha_pc = random.randint(0,3)#O computador sorteia um número de 0 a 3.
        escolha_player = int(input("Escolha um Número:"))#Aqui proponho uma entrada convertendo ela a um numero inteiro para usar como a "aposta" do usuario.
        print("[4] Sair") #Print normal!
        if escolha_player == escolha_pc:# Se a escolha do pc for igual ao usuario ira executar o bloco de código abaixo.
            print("Parabéns você me venceu!",f"O número era {escolha_pc}.") #Print com formatação (chamando variaveis)
        elif escolha_player == 4:#Se a escolha for 4 ira encerrar o script da aula 01
            print("Saindo...")#Print de uma string normal!
            print(logoprojeto)#Imprime a ASCII imposta na variavel (logoprojeto)
            menu()#Chama a função do menu!
def script_aula2():#Define uma função para executar o segundo script.
    print(str("Escolha de número 2"))#Print de uma string normal
    
def exibição_menu():#Define uma função para ser o HUB de opções (menu), somente exibição sem nenhuma interação!
    print(str("Script [1]"))#Print de uma string normal
    print(str("Script [2]"))#Print de uma string normal
    print(str("Script [3]"))#Print de uma string normal
    print(str("Script [4]"))#Print de uma string normal
    print(str("Sair [0]")) #Print de uma string normal
#O bloco abaixo é a função do menu sendo definida!
def menu():#DEFININDO
    escolha = None #Define uma variavel para armazenar as escolhas do usuario.
    exibição_menu()#Chama a função para exibir as opções do menu.
    while escolha != "0": #Um loop simples (Enquanto a escolha do usuario não for 0, ele ira continuar em execução.)
        escolha = input("Escolha algum Script:")#Aqui definimos um input(entrada) que ira captar qual opção do menu o usuario ira escolher.
        if escolha == "1":#Se a escolha for 1 no formato de (string) ira executar a função que chama o script de numero 1.
            script_aula1()#chama a função do script!
        elif escolha == "0":#Define que se a escolha do usuário for 0 (string) irá encerrar o código.
            print("Saindo em 3.")
            SLP(1)#O comando serve para dar um atraso antes da proxima função ou impressão.(Sleep)
            print("Saindo em 2..")
            SLP(1)#O comando serve para dar um atraso antes da proxima função ou impressão.(Sleep)
            print("Saindo em 1...")
            SLP(1)#O comando serve para dar um atraso antes da proxima função ou impressão.(Sleep)
            break#Para o codigo!
#O bloco abaixo serve para definir uma função de limpar o terminal
def clear():#definie clear como função para limpar o terminal de forma automatico.
    if os.name == 'posix':# Verifica se o sistema operacional é tipo Unix (Linux, macOs)
        os.system('clear')# Se sim irá executar o comando para limpar o terminal!
    elif os.name == 'nt':# Verifica se o sistema operacional é Windows!
        os.system("cls") #Se sim irá executar o comando para limpar o terminal!
print("Um momento estamos limpando a interface...")#Executa um print no terminal!
SLP(3)#O comando serve para dar um atraso antes da proxima função ou impressão.(Sleep)
#O comando abaixo nada mais é que a função menu criada acima sendo chamada.
menu()



