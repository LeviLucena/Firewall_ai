import openai

openai.api_key = "API OPENAI AQUI"

def explain_vulnerability(port, service):
    """Gera uma explicação sobre os riscos e mitigação usando IA."""
    prompt = f"O serviço {service} na porta {port} pode ter vulnerabilidades. Explique os riscos e como mitigar."
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]
