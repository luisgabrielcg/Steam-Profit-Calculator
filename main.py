import sys
continuar = "1" 

while continuar == "1":
    try:    
        valor = float(input("Preço do item (em R$): ").replace(',', '.')) 
        #Coloquei R$, mas você pode utilizar qualquer outra moeda.
        lucrodesejado = input("Insira a porcentagem desejada de lucro: ").replace(',', '.') 
        porcentagem = valor * 1.15 * (1 + float(lucrodesejado) / 100)  
        #Dependendo do valor do item, a taxa pode acabar sendo um pouco acima de 13%. Por isso, coloquei 15% para cobrir qualquer diferença que possa surgir.

        print()
        print(f"Para um item de R${round(valor, 2)} com lucro de {lucrodesejado}%, você deve vender por: R${round(porcentagem, 2)}.")
        print()

    except ValueError:
        print("Por favor, insira apenas números.")

    continuar = ""
    while continuar not in ["1", "2"]:
        continuar = input("Gostaria de inserir um novo valor? Digite 1 para SIM ou 2 para NÃO: ")
       
if continuar == "2":
    sys.exit()