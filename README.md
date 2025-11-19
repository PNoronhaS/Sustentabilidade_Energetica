# 🌱 Sustentabilidade Energética no Futuro do Trabalho

Este projeto acadêmico analisa dados de consumo energético em ambientes produtivos e propõe soluções sustentáveis.  
A iniciativa está alinhada com tendências do futuro do trabalho, promovendo eficiência, economia e responsabilidade ambiental.

---

## 📊 Dados utilizados

- **Fonte:** Dados simulados de consumo energético (`dados/consumo.csv`).  
- Cada linha representa o consumo diário em kWh.  
- Exemplo de conteúdo:

```csv
Dia,Consumo_kWh
2025-11-01,120
2025-11-02,115
2025-11-03,130
...
2025-11-30,118
```
Caso queira, você pode substituir por dados reais de consumo energético de sua instituição ou empresa.

## 💻 Código e Simulações
```text
- main.py → executa todo o fluxo (carregar dados, analisar, gerar gráficos e relatório).
- processamento.py → funções para leitura, análise e simulação de economia.
- graficos.py → gera gráficos de consumo e comparativo.
- relatorio.py → cria relatório em PDF com insights, recomendações e impacto ambiental.
- simulador.py → aplica reduções simuladas no consumo para estimar economia.
```
## 📝 Descrição da solução
```text
A solução consiste em:
- Ler dados de consumo energético.
- Identificar desperdícios e picos de consumo.
- Simular ajustes simples (ex.: desligar equipamentos fora do horário útil).
- Estimar economia em kWh e percentual.
- Calcular impacto ambiental (CO₂ evitado).
- Gerar gráficos comparativos e relatório em PDF com recomendações sustentáveis.

Impacto esperado:
- Redução de custos operacionais.
- Maior eficiência energética.
- Conexão com práticas sustentáveis no futuro do trabalho.
```
## ⚙️ Orientações de execução
```bash
# 1. Clone o repositório
git clone https://github.com/seuusuario/sustentabilidade_energetica.git
cd sustentabilidade_energetica

# 2. Crie ambiente virtual e instale dependências
python -m venv venv
venv\Scripts\activate   # Windows
pip install pandas matplotlib fpdf

# 3. Execute o projeto
python main.py
```
**Arquivos Gerados:**
```text
- grafico_consumo.png
- grafico_comparativo.png
- relatorio.pdf
```
## 🖼️ Demonstração
```text
Resultado da análise (terminal) → menu_analise.png
Gráfico de Consumo → grafico_consumo.png
Original vs Ajustado → grafico_comparativo.png
Relatório PDF → relatorio_pdf.png
```
## 🌍 Impacto ambiental
```text
- Fator de emissão utilizado: 0.10 kg CO₂/kWh (configurável em main.py).
- Cálculo:
   CO₂ evitado (kg) = economia de energia (kWh) × fator de emissão.
   Resultado também mostrado em toneladas no relatório.

Exemplo de saída no terminal:
Economia estimada: 120.00 kWh (10.00%)
CO2 evitado: 12.00 kg (0.012 t) com fator 0.100 kg/kWh
```
## 🎯 Conexão com o Futuro do Trabalho
```text
Este projeto mostra como práticas simples de análise e automação podem:
- Reduzir desperdícios energéticos
- Promover ambientes produtivos mais inteligentes
- Contribuir para a sustentabilidade econômica, ambiental e social
```
