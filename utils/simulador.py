def aplicar_ajuste(consumo_kwh, reducao_percentual=10):
    """Aplica uma redução percentual ao consumo (ex.: desligar fora do horário)."""
    fator = 1 - (reducao_percentual / 100)
    return consumo_kwh * fator
