# Testando o MCP Burp Integrado ao Claude Code

Conectei o MCP Server do Burp Suite no Claude Code pra ver como a IA se comporta usando o Burp como proxy de ataque, em vez de simplesmente rodar curl pelo terminal (ferramenta nativa que o Claude Code possui).

O challenge era o Spookifier. Dei só o IP e a porta, a única instrução foi para o modelo utilizar o MCP do burp como ferramenta, sem arquivo de instrução adicional. A IA mandou o primeiro request pelo Burp, leu os headers de resposta e já mapeou a stack: Flask, Werkzeug 2.0, Python 3.8, com um parâmetro ?text= que aceitava input do usuário. Suspeitou de SSTI na hora.
Foi testar Jinja2 primeiro — {{7*7}} voltou cru, sem avaliar. Não insistiu. Trocou pra sintaxe Mako, mandou ${7*7}, e a resposta veio com 49. Confirmado.

Daí pra frente foi rápido: injetou os.popen(‘id’) dentro do template e o servidor devolveu uid=0(root). Quando foi ler a flag, o payload quebrou por causa de caracteres especiais no request. Sem hesitar, URL-encodou tudo e mandou de novo. Aqui ja era flag na mão!
O que me chamou atenção não foi o SSTI, isso é básico. Foi a IA trocar de Jinja2 pra Mako sem ninguém pedir, e resolver o problema de encoding sem travar o fluxo. Parece pouco, mas é o tipo de adaptação que diferencia um scan automatizado de um “raciocínio” real.

E o fato de tudo passar pelo Burp faz diferença: cada request fica no Proxy History, tudo documentado, pronto pra virar relatório. É diferente de rodar pelo terminal e perder o histórico quando resetar a sessão. Apesar da viabilidade é importante perceber que isso pode acumular muitos tokens, então é preciso ser feito com acompanhamento (ou seja, não ativar o modo —dangerously-skip-permissions por preguiça.)

Como configurar:
Passo 1 — Instale a extensão MCP Server no Burp Suite pela BApp Store.
Passo 2 — Acesse a nova aba MCP que vai aparecer e certifique-se de que o Server Configuration está marcado como Enabled.
Passo 3 — Extraia o arquivo mcp-proxy.jar clicando no botão “Extract server proxy” dentro da mesma aba MCP.
Passo 4 — No terminal, rode: claude mcp add burp — java -jar /tmp/mcp-proxy.jar —sse-url http://127.0.0.1:9876 (esse é o comando que integra os dois).

#ai #pentesting #hackthebox #ctf #burpsuite

[Link](https://www.instagram.com/p/DW7QoK7kQ-I/?img_index=1)
