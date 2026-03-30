class Pago:
    def __init__(self, monto):
        self.monto = monto

    def procesar_pago(self):
        raise NotImplementedError
