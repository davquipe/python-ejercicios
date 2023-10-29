# Definimos nuestra excepción personalizada
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_actual, cantidad_retirada):
        super().__init__(f"Saldo insuficiente. Saldo actual: ${saldo_actual}. Intento de retiro: ${cantidad_retirada}.")
        self.saldo_actual = saldo_actual
        self.cantidad_retirada = cantidad_retirada

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(self.saldo, cantidad)
        self.saldo -= cantidad
        return self.saldo

# Crear una cuenta y realizar algunas operaciones
try:
    cuenta_de_juan = CuentaBancaria("Juan", 100)
    print(f"Saldo inicial: ${cuenta_de_juan.saldo}")
    cuenta_de_juan.depositar(50)
    print(f"Saldo después del depósito: ${cuenta_de_juan.saldo}")
    cuenta_de_juan.retirar(200)  # Esto debería lanzar nuestra excepción personalizada
except SaldoInsuficienteError as e:
    print(f"Error: {e}")

