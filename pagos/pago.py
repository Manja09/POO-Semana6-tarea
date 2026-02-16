class Pago:
    def __init__(self, total: float):
        self.total = total

    def procesar(self) -> tuple[bool, str]:
        raise NotImplementedError("Implementa procesar() en la clase hija")
