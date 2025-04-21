def calcular_iof(dias):
    if dias <= 1:
        return 96
    elif dias <= 2:
        return 93
    elif dias <= 3:
        return 90
    elif dias <= 4:
        return 86
    elif dias <= 5:
        return 83
    elif dias <= 6:
        return 80
    elif dias <= 29:
        return 70 - (dias - 7)  # simplificado
    else:
        return 0

def calcular_ir(dias):
    if dias <= 180:
        return 22.5
    elif dias <= 360:
        return 20
    elif dias <= 720:
        return 17.5
    else:
        return 15

def calcular_investimento(valor_inicial, dias, taxa_rendimento=0.08):
    rendimento_bruto = valor_inicial * (taxa_rendimento / 30) * dias
    iof_percentual = calcular_iof(dias)
    iof_valor = rendimento_bruto * (iof_percentual / 100)
    
    rendimento_pos_iof = rendimento_bruto - iof_valor
    ir_percentual = calcular_ir(dias)
    ir_valor = rendimento_pos_iof * (ir_percentual / 100)

    valor_liquido = valor_inicial + rendimento_pos_iof - ir_valor

    return {
        "Rendimento Bruto": rendimento_bruto,
        "IOF": iof_valor,
        "IR": ir_valor,
        "Valor Líquido": valor_liquido
    }

# Exemplo de uso:
valor = float(input("Digite o valor inicial do investimento: R$ "))
dias = int(input("Digite o número de dias do investimento: "))

resultado = calcular_investimento(valor, dias)

for chave, valor in resultado.items():
    print(f"{chave}: R$ {valor:.2f}")
