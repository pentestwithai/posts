Mostrando esse teste autônomo na máquina Bastard (ambiente Windows de dificuldade média) do HackTheBox usando OpenCode com GPT-5.4 (iniciando com o 5.5) integrado ao Metasploit via MCP.

O teste começou com o GPT-5.5 e precisou de downgrade para o 5.4. As restrições do 5.5 pra atividades de segurança de alto risco estão mais rígidas que no modelo anterior, exatamente como a OpenAI prometeu no lançamento. Na prática, o modelo recusava comandos que o 5.4 executa sem problema.

A IA identificou Drupal 7.54 rodando em IIS 7.5, reconheceu que a versão é vulnerável ao Drupalgeddon2 (CVE-2018-7600, que permite RCE não autenticado), confirmou RCE via curl direto, enumerou privilégios, encontrou SeImpersonatePrivilege habilitado, baixou JuicyPotato no alvo via certutil, escalou pra SYSTEM e coletou as duas flags. Tudo no terminal.

Setup em 6 passos:

1. Clonar o repositório do MetasploitMCP
2. Instalar as dependências do projeto
3. Rodar opencode mcp add preenchendo as informações do servidor MCP
4. Iniciar o daemon RPC do Metasploit com: msfrpcd -P qualquersenha -S -a 127.0.0.1 -p 55553. Esse comando sobe o serviço RPC que permite o MCP se comunicar com o Metasploit. O -S desabilita SSL, o -a define o bind em localhost e o -p a porta
5. Atualizar o arquivo /home/<user>/.config/opencode/opencode.json
6. Verificar se o MCP conectou ao OpenCode com /mcps

A IA criou sozinha um shell script helper pra automatizar o Drupalgeddon2 usando o mcp. Identificou o vetor de escalada (SeImpersonate + JuicyPotato) sem dica. Testou CLSID válido pro Windows Server 2008 R2 e confirmou SYSTEM antes de disparar o payload.

O MCP do Metasploit deu timeout no run_exploit e nos comandos de sessão algumas vezes. PowerShell remoto não respondia, forçando fallback pra certutil e cmd.exe puro.

O GPT-5.5 é quase inutilizável pra CTFs hoje, teremos que pensar em mais maneiras de escapar dessas medidas.

#ai #cybersecurity #hacking #programming #hackthebox
