def calcular_iof(dias):
    tabela_iof = {
        1: 96, 2: 93, 3: 90, 4: 86, 5: 83, 6: 80,
        7: 76, 8: 73, 9: 70, 10: 66, 11: 63, 12: 60,
        13: 56, 14: 53, 15: 50, 16: 46, 17: 43, 18: 40,
        19: 36, 20: 33, 21: 30, 22: 26, 23: 23, 24: 20,
        25: 16, 26: 13, 27: 10, 28: 6, 29: 3, 30: 0
    }
    return tabela_iof.get(dias, 0)
    ## O IOF é cobrado apenas para investimentos com prazo inferior a 30 dias.
def calcular_ir(dias):
    if dias <= 180:
        return 22.5
    elif dias <= 360:
        return 20
    elif dias <= 720:
        return 17.5
    else:
        return 15
#
def calcular_investimento(valor_inicial, dias, taxa_rendimento=0.1415):  # 14,15% ao ano
    rendimento_diario = (1 + taxa_rendimento) ** (1 / 365) - 1
    rendimento_bruto = valor_inicial * rendimento_diario * dias

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

valor = float(input("Digite o valor inicial do investimento: R$ "))
dias = int(input("Digite o número de dias do investimento: "))
#O IR é cobrado apenas para investimentos com prazo superior a 180 dias.  
#O rendimento é de 14,15% ao ano, o que equivale a aproximadamente 0,0387% ao dia.
resultado = calcular_investimento(valor, dias)

for chave, valor in resultado.items():
    print(f"{chave}: R$ {valor:.2f}")
