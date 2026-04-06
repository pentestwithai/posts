import os, re, subprocess
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from fastapi.responses import HTMLResponse

os.environ["GEMINI_API_KEY"] = "SUA_CHAVE_AQUI"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

app = FastAPI()

def is_safe(text: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9.-]+$", text)) and not text.startswith("-")

def executar_subfinder(dominio: str):
    if not is_safe(dominio): return "Erro: Alvo inválido."
    print(f"[*] Determinando subdominios em: {dominio}")
    cmd = ["subfinder", "-d", dominio]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout

def executar_nuclei(alvo: str):
    if not is_safe(alvo): return "Erro: Alvo inválido."
    print(f"[*] Rodando scan de vulnerabilidades em: {alvo}")
    cmd = ["nuclei", "-u", alvo, "-severity", "critical,high", "-silent"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout if res.stdout else "Nenhum risco crítico encontrado."

instrucoes = """
Sempre formate as respostas de vulnerabilidades com os campos:
- Descricao
- Risco
- Evidencias
- Recurso Afetado
- Nunca fale o nome das ferramentas que você executa, somente a funcionalidade delas
"""

model = genai.GenerativeModel(
    model_name='gemini-2.5-flash', # Flash é mais rápido para testes
    tools=[executar_subfinder, executar_nuclei],
    system_instruction=instrucoes
)

class Prompt(BaseModel):
    text: str

@app.post("/hunt")
async def hunt(p: Prompt):
    chat = model.start_chat(enable_automatic_function_calling=True)
    response = chat.send_message(p.text)
    return {"analise": response.text}

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <body style="font-family:sans-serif; background:#121212; color:white; padding:50px;">
        <h1>🛡️ Threat Hunter Standalone</h1>
        <input id="p" style="width:70%; padding:10px;" placeholder="Ex: Analise o dominio testasp.vulnweb.com">
        <button onclick="enviar()">Caçar</button>
        <pre id="r" style="margin-top:20px; white-space:pre-wrap;"></pre>
        <script>
            async function enviar() {
                document.getElementById('r').innerText = 'Buscando...';
                const res = await fetch('/hunt', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({text: document.getElementById('p').value})
                });
                const data = await res.json();
                document.getElementById('r').innerText = data.analise;
            }
        </script>
    </body>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
