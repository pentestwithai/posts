# Tipo MCP com Gemini

Semana passada nós comentamos sobre servidores de Model Context Protocol ou MCP em nossos stories, então resolvemos fazer um post básico desse tipo de estrutura, mas diferente.

A simplicidade do código abaixo mostra como é possível aplicar o conceito de MCP, usando `SERVIDOR → HOST → CLIENT` de forma bem dinâmica e sem complicações.

Mas antes de entrar no código, vale entender a diferença entre:

- usar o conceito de MCP de forma informal, como fizemos aqui;
- implementar o MCP de forma formal e padronizada.

No nosso exemplo:

- tudo roda dentro de um único processo Python;
- as ferramentas são funções locais;
- o schema é inferido automaticamente pelo SDK do Gemini;
- a comunicação acontece internamente.

É rápido, funciona, e já aplica a lógica de Server → Host → Client na prática.

Já no MCP formal:

- cada ferramenta roda em um processo separado;
- se comunica via JSON-RPC;
- expõe um schema explícito;
- pode ser conectada a qualquer LLM compatível: Claude, GPT, Gemini, não importa.

A estrutura é mais robusta, plugável e portável. O espírito é o mesmo. A diferença está na padronização e na escalabilidade.

Para o nosso exemplo, a primeira coisa que devemos ter é uma assinatura free tier do Gemini. Essa assinatura já vai nos permitir utilizar o SDK do Google para nossas consultas — e é aqui que entra a biblioteca `google-generativeai`.

Essa lib é o SDK oficial do Google para acessar os modelos Gemini via Python. Com ela dá pra fazer bastante coisa:

- enviar prompts simples;
- manter conversas com histórico;
- configurar instruções de sistema;
- trabalhar com imagens e documentos;
- registrar funções Python como ferramentas que o modelo pode chamar automaticamente.

Esse último ponto é o mais importante pro nosso contexto. É exatamente isso que permite o Gemini decidir, por conta própria, quando rodar o `subfinder` ou o `nuclei` com base no que o usuário pediu.

Além disso, ela suporta:

- streaming de respostas;
- embeddings;
- geração de código.

Tudo com poucas linhas.

Acesse https://aistudio.google.com/api-keys e gera sua chave através de sua conta Google, simples e rápido.

#mcp #python #gemini #googleai #ia #fastapi #infosec #devtools #llm #agentes

## Instale as ferramentas necessárias

```bash
brew install nuclei
brew install subfinder
```

## Instale as dependências

```bash
pip install -r requirements.txt
```

## Execute o script

```bash
python mcp-test.py
```

[Link](https://www.instagram.com/p/DWyk3I7EcDr/?img_index=1)
