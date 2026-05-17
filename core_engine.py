import ollama

class EwaAiEngine:
    """
    Engine de IA Soberana diseñado por Manuel Beltran para el análisis local
    de metadatos de SAP extraídos de reportes EarlyWatch Alerts.
    """
    def __init__(self, model_name="llama3"):
        self.model_name = model_name

    def generate_summary(self, ewa_text: str) -> str:
        prompt = f"""
        Actúa como un Consultor Senior de SAP Basis y Operaciones Técnicas.
        Analiza el siguiente extracto de un reporte EarlyWatch Alert (EWA) y genera:
        1. Un resumen ejecutivo en español del estado del sistema.
        2. Alertas críticas identificadas (Rojo/Amarillo).
        3. Plan de acción inmediato con sus respectivos T-Codes de SAP para mitigación.

        Texto del EWA:
        {ewa_text[:2000]} 
        """
        try:
            response = ollama.generate(model=self.model_name, prompt=prompt)
            return response['response']
        except Exception as e:
            return f"Error conectando con el motor local de Ollama: {str(e)}"
