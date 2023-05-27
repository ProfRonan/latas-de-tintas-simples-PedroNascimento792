print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
import math

def calculate_paint(metros_quadrados):
    litros_de_tinta = math.ceil(metros_quadrados / 3)  
    qtd_de_latas = math.ceil(litros_de_tinta / 18)  
    valor_total = qtd_de_latas * 80.00
    return qtd_de_latas, valor_total
qtd_de_latas, valor_total = calculate_paint(metros_quadrados)


print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")