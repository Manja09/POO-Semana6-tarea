class Pago:
    def __init__(self, monto: float):
        self.monto = monto

    def procesar_pago(self):
        raise NotImplementedError("Las subclases deben implementar procesar_pago().")
