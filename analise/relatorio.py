from fpdf import FPDF

def gerar_relatorio(insights: dict, economia: dict, caminho_pdf='relatorio.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Relatorio de Eficiencia Energetica', ln=True)

    pdf.set_font('Arial', '', 12)
    pdf.ln(4)
    pdf.cell(0, 8, f"Consumo total: {insights['total_kwh']:.2f} kWh", ln=True)
    pdf.cell(0, 8, f"Consumo medio: {insights['media_kwh']:.2f} kWh/dia", ln=True)
    pdf.cell(0, 8, f"Pico: {insights['pico_kwh']:.2f} kWh em {insights['dia_pico']}", ln=True)

    pdf.ln(4)
    pdf.cell(0, 8, f"Economia estimada: {economia['economia_kwh']:.2f} kWh ({economia['economia_percent']:.2f}%)", ln=True)
    pdf.cell(0, 8, f"Fator de emissao: {economia['fator_emissao_kg_por_kwh']:.3f} kg CO2/kWh", ln=True)
    pdf.cell(0, 8, f"CO2 evitado: {economia['co2_evitable_kg']:.2f} kg ({economia['co2_evitable_ton']:.3f} t)", ln=True)

    pdf.ln(6)
    pdf.multi_cell(0, 8, (
        "Recomendacoes:\n"
        "- Desligar equipamentos fora do horario util.\n"
        "- Automatizar iluminacao com sensores de presenca.\n"
        "- Revisar picos de consumo e ajustar rotinas.\n"
        "- Considerar fontes renovaveis para cargas base."
    ))

    pdf.output(caminho_pdf)
