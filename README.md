
# Simulação do Algoritmo Paxos 

Este projeto simula o algoritmo de consenso Paxos em um ambiente distribuído, com foco em demonstrar como os nós alcançam consenso, mesmo em cenários de falhas.

## Descrição do Projeto
O Paxos é um algoritmo clássico de consenso distribuído, projetado para garantir que múltiplos nós em um sistema distribuído concordem sobre um único valor. Este projeto implementa uma versão simplificada do Paxos, simulando as fases principais e incluindo:

- Propostas de valores feitas por nós (proponentes).
- Aceitação ou rejeição de propostas pelos nós participantes.
- Registro detalhado das interações e decisões.
- Simulação de falhas, com nós falhando aleatoriamente.

## Instruções de Configuração e Execução
### Requisitos
- Python 3.8 ou superior.

### Passos para Configuração
1. Clone o repositório ou extraia os arquivos fornecidos.
2. Certifique-se de ter Python instalado em seu ambiente.
3. Navegue até o diretório do projeto no terminal.

### Para Executar a Simulação
1. Execute o arquivo principal:
   ```bash
   python main.py
   ```
2. Acompanhe os logs no terminal para observar as interações entre os nós.
3. No final, o sistema exibirá os resultados da simulação, incluindo o estado de cada nó.

## Explicação das Fases do Algoritmo
### Fase 1: Proposta
Um nó é selecionado como proponente e envia uma proposta de valor para os outros nós da rede. Este valor pode representar uma decisão a ser aceita pelos participantes.

### Fase 2: Aceitação ou Rejeição
Cada nó participante analisa a proposta recebida e decide se irá aceitá-la ou rejeitá-la com base em critérios aleatórios (simulação).

### Fase 3: Consenso
Se a maioria dos nós aceitar a proposta, o valor é considerado aceito pela rede. Caso contrário, o consenso não é alcançado.

## Falhas Simuladas e Respostas do Sistema
### Falhas Simuladas
1. **Falha no Processamento:** Nós podem falhar ao processar propostas (10% de chance por nó).
2. **Rejeições Aleatórias:** Nós podem rejeitar propostas por decisão própria.

### Resposta do Sistema
- Se um nó falhar ao processar uma proposta, ele não participa da decisão.
- O histórico de cada nó é registrado para rastrear como cada decisão foi tomada.

## Melhorias Futuras
- Implementação de lógica para recuperação de nós após falhas.
- Suporte para múltiplos rounds de propostas.
- Expansão para tolerância a falhas bizantinas.

## Exemplos de Uso
Esta simulação é útil para estudantes e desenvolvedores que desejam entender os princípios básicos do consenso distribuído e como o Paxos pode ser aplicado em sistemas reais.
