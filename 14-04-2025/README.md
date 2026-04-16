Agora o teste foi de binary exploitation. O Ghidra foi conectado ao Claude Code via MCP e apontado pra um challenge do HackTheBox chamado Jeeves, dificuldade easy.

O binário foi carregado no Ghidra e a IA começou a explorar.

Carregou o ELF no Ghidra, decompilou a main e na hora identificou o problema:

- um `gets()` lendo input sem limite nenhum num buffer de 64 bytes;
- uma variável logo depois no stack que era comparada contra `0x1337BAB3`;
- se o valor batesse, o programa abria `flag.txt` e imprimia o conteúdo.

A partir daí a IA:

- mapeou o layout da stack;
- calculou que eram 60 bytes de padding até chegar na variável;
- montou o payload em little-endian;
- testou localmente antes de mandar pro alvo;
- criou um `flag.txt` falso no `/tmp`;
- rodou o exploit;
- confirmou que o caminho premiado disparava;
- só depois disso enviou via TCP pro servidor do HTB, onde ela obteve a flag.

O que impressiona é a metodologia. O modelo não mandou o payload direto pro alvo na sorte. Fez análise estática completa no Ghidra, anotou os pontos de interesse no binário, validou local, e só depois foi pro remoto.

## Como configurar

1. Baixar o plugin `.zip` na aba Releases do repositório `themixednuts/GhidraMCP` no GitHub.
2. Abrir o Ghidra e instalar o plugin em File > Install Extensions, clicando no “+” e selecionando o `.zip` baixado.
3. Reiniciar o Ghidra.
4. Ir em File > Configure > Configure (Miscellaneous) e marcar o `GhidraMcpPlugin` como ativo.
5. Verificar se o servidor MCP subiu na porta 8080.
6. Criar um novo projeto em File > New Project.
7. Importar o binário pro projeto e dar um double click sobre ele pra abrir no CodeBrowser.
8. No terminal, rodar o comando:

```bash
claude mcp add ghidra “http://127.0.0.1:8080/mcp” —transport http
```

Esse comando conecta o endpoint do plugin com o Claude Code.

9. Abrir o Claude Code e rodar `/mcp` pra verificar se a conexão com o Ghidra está ativa.

Feito isso, é só orientar o modelo e ver a IA trabalhar.

#ai #pentesting #hackthebox #ctf #ghidra
