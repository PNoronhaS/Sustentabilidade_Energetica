import matplotlib.pyplot as plt

def grafico_consumo(df, caminho_png='grafico_consumo.png'):
    plt.figure(figsize=(10,4))
    plt.plot(df['Dia'], df['Consumo_kWh'], marker='o', label='Consumo')
    plt.title('Consumo diário (kWh)')
    plt.xlabel('Dia')
    plt.ylabel('kWh')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(caminho_png)
    plt.close()

def grafico_comparativo(df, caminho_png='grafico_comparativo.png'):
    plt.figure(figsize=(10,4))
    plt.plot(df['Dia'], df['Consumo_kWh'], marker='o', label='Original')
    plt.plot(df['Dia'], df['Consumo_Ajustado'], marker='o', label='Ajustado')
    plt.title('Original vs Ajustado (kWh)')
    plt.xlabel('Dia')
    plt.ylabel('kWh')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(caminho_png)
    plt.close()
