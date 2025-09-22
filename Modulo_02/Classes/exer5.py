class ContaBancaria:

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
            
conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob", 500)
conta1.depositar(250)
conta2.depositar(300)
print(f"Saldo da conta de {conta1.titular}: R$ {conta1.saldo:.2f}")
print(f"Saldo da conta de {conta2.titular}: R$ {conta2.saldo:.2f}")
conta1.depositar(-50)  # Teste de depósito inválido