from analise.processamento import carregar_dados, analisar_consumo, simular_economia
from analise.graficos import grafico_consumo, grafico_comparativo
from analise.relatorio import gerar_relatorio

def main():
    caminho_csv = 'dados/consumo.csv'

    df = carregar_dados(caminho_csv)
    insights = analisar_consumo(df)

    # Ajuste aqui o fator de emissao conforme a sua referencia
    fator_emissao = 0.10  # kg CO2 por kWh
    economia = simular_economia(df, reducao_percentual=10, fator_emissao_kg_por_kwh=fator_emissao)

    grafico_consumo(df)
    grafico_comparativo(economia['df_ajustado'])

    gerar_relatorio(insights, economia)

    print("Analise concluida!")
    print(f"Total: {insights['total_kwh']:.2f} kWh | Media: {insights['media_kwh']:.2f} kWh/dia")
    print(f"Economia estimada: {economia['economia_kwh']:.2f} kWh ({economia['economia_percent']:.2f}%)")
    print(f"CO2 evitado: {economia['co2_evitable_kg']:.2f} kg ({economia['co2_evitable_ton']:.3f} t) com fator {fator_emissao:.3f} kg/kWh")
    print("Arquivos gerados: grafico_consumo.png, grafico_comparativo.png, relatorio.pdf")

if __name__ == '__main__':
    main()
