# Testando OpenClaude + QWEN3.6-Plus

Diante do vazamento do Claude Code que aconteceu recentemente, surgiram muitos forks open-source inspirados no projeto, e o OpenClaude é o que mais se destacou (ou um dos poucos que sobrou rs). É uma ferramenta CLI que replica as funcionalidades do Claude Code, mas diferente do original, qualquer modelo que possua API compatível com a OpenAI pode se conectar a ele.

A ideia era testar o que um setup gratuito consegue fazer em um CTF, então foi conectado no Qwen 3.6 Plus em um endpoint free do OpenRouter e orientado a testar um challenge do HackTheBox pelo prompt e pelo arquivo INSTRUCTIONS.md presente no diretório atual (podendo ser visto no final, no vídeo do quarto slide).

O alvo era o Toxic. Apertado o enter, o modelo começou: rodou nmap, identificou nginx com PHP, e percebeu que o cookie PHPSESSID carregava um objeto PHP serializado em base64 (vulnerabilidade comum em aplicações PHP). Decodificou, encontrou a classe PageModel com LFI, manipulou o cookie e começou a ler arquivos do servidor como /etc/passwd, código da aplicação, configs do nginx e do PHP.

Mapeou a infra inteira: container Kubernetes, Alpine Linux, PHP-FPM com supervisord. Analisou as configs de segurança (disable_functions vazio, allow_url_include Off, short_open_tag Off) pra decidir quais vetores de RCE tentar.
Tentou escalar de LFI pra RCE com log poisoning, php://input, filter chains, session upload progress. Cada técnica foi bloqueada por uma config diferente. O ponto forte foi como ele pivotou entre as abordagens: quando log poisoning falhava por bytes binários no access log, foi ler o log via LFI pra entender o erro. Quando wrappers remotos não funcionavam, focou em vetores locais e investigou /proc pra mapear processos.

Não conseguiu RCE e nem a flag. O rate limit do modelo free cortou o fluxo várias vezes (foi bem chato, mas sendo gratuito…). Mesmo assim, a enumeração, análise de source code e o encadeamento lógico de técnicas impressiona bastante pra um modelo rodando sem custo nenhum.
Setup completo e passo a passo no carrossel.

#ai #pentesting #hackthebox #ctf #claude

[Link](https://www.instagram.com/p/DW2ELoakT-2/?img_index=1)
