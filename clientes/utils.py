from decimal import Decimal


def calcular_valor_total(tipo, quantidade_kg, valor_kg, valor_total):
    if tipo == 'S' and quantidade_kg:
        quantidade_kg = -quantidade_kg

    if valor_kg and quantidade_kg:
        if tipo == 'S':
            valor_total = -Decimal(quantidade_kg) * Decimal(valor_kg)
        else:
            valor_total = Decimal(quantidade_kg) * Decimal(valor_kg)
    elif valor_kg and valor_total:
        if tipo == 'S':
            quantidade_kg = -Decimal(valor_total) / Decimal(valor_kg)
        else:
            quantidade_kg = Decimal(valor_total) / Decimal(valor_kg)
    elif quantidade_kg and valor_total:
        if tipo == 'S':
            valor_kg = -Decimal(valor_total) / Decimal(quantidade_kg)
        else:
            valor_kg = Decimal(valor_total) / Decimal(quantidade_kg)

    return quantidade_kg, valor_kg, valor_total