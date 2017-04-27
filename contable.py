def iva(neto):
    return neto*0.21


def descuento(neto, descuento):
    return neto * descuento


def total(neto, descuento):
    return neto * 1.21 * (1-descuento)

