
import random
import time
from threading import Thread

class No:
    def __init__(self, id_no):
        self.id_no = id_no
        self.estado = "ocioso"  # Estados: ocioso, propondo, aceitando, rejeitando
        self.valor_proposto = None
        self.valor_aceito = None
        self.historico = []

    def propor_valor(self, valor, nos):
        print(f"Nó {self.id_no} está propondo o valor: {valor}")
        self.valor_proposto = valor
        for no in nos:
            if no.id_no != self.id_no:
                resposta = no.receber_proposta(self.id_no, valor)
                self.historico.append((no.id_no, resposta))

    def receber_proposta(self, id_proponente, valor):
        # Simula um cenário onde há 10% de chance de falha no nó
        if random.random() < 0.1:
            print(f"Nó {self.id_no} falhou ao processar a proposta do nó {id_proponente}.")
            return "falha"

        # Decide aceitar ou rejeitar a proposta
        decisao = random.choice(["aceitar", "rejeitar"])
        if decisao == "aceitar":
            self.valor_aceito = valor
            print(f"Nó {self.id_no} ACEITOU a proposta do nó {id_proponente}.")
        else:
            print(f"Nó {self.id_no} REJEITOU a proposta do nó {id_proponente}.")
        return decisao

class SimuladorPaxos:
    def __init__(self, quantidade_nos):
        self.nos = [No(i) for i in range(quantidade_nos)]
        self.logs = []

    def simular(self, valor_para_propor):
        # Seleciona um nó aleatório como proponente
        proponente = random.choice(self.nos)
        print(f"Nó {proponente.id_no} foi escolhido como proponente.")
        self.logs.append(f"Nó {proponente.id_no} foi escolhido como proponente.")
        proponente.propor_valor(valor_para_propor, self.nos)

    def exibir_resultados(self):
        print("
--- Resultados da Simulação ---")
        for no in self.nos:
            print(f"Nó {no.id_no}: Valor Aceito = {no.valor_aceito} | Histórico = {no.historico}")

if __name__ == "__main__":
    # Configuração da simulação
    simulador = SimuladorPaxos(quantidade_nos=5)
    simulador.simular(valor_para_propor="Bloco_1")
    simulador.exibir_resultados()
