O experimento da vez foi com escalação de privilégios em Linux usando IA. O setup foi o GPT-5.3 Codex (modelo acessível no plano gratuito) rodando no agente OpenAI Codex CLI, integrado a um MCP Server próprio pra agilizar o privesc, disponível em github.com/pentestwithai/LinuxPrivescMCP. O alvo foi a máquina Admirer do HackTheBox, começando já autenticado como waldo via SSH. A intenção era ver como a IA performava sozinha da conta comum até root.
Com o prompt enviado, a IA abriu sessão SSH pelo MCP, confirmou que estava como usuário comum (waldo) e disparou a enumeração chamando o MCP Server. Coletou binários SUID, grupos do usuário, permissões de diretórios sensíveis e rodou sudo -l. Foi ali que achou o ponto de entrada: waldo podia executar /opt/scripts/admin_tasks.sh como root com a flag SETENV ativa.
O script foi aberto e analisado. A IA percebeu que ele chamava /opt/scripts/backup.py internamente, e esse Python fazia import shutil. Com SETENV liberado, a conclusão foi imediata: dava pra sequestrar a importação do shutil manipulando a variável PYTHONPATH. Um /tmp/shutil.py falso foi criado contendo uma função make_archive que copiava o bash pra /tmp e aplicava o bit SUID. O comando sudo PYTHONPATH=/tmp /opt/scripts/admin_tasks.sh 6 fez o Python carregar o shutil adulterado antes do real, e saiu um bash SUID root no /tmp pronto pra executar.
Um /tmp/rootbash -p depois, a sessão virou root. Root flag capturada.
O detalhe interessante é que a IA não ficou chutando exploits conhecidos ou gastando token lendo output do LinPEAS. Seguiu uma cadeia lógica partindo do output do sudo: quem tem SETENV, o que esse script chama, como o Python resolve imports, como influenciar esse resolve. Python library hijacking é bem conhecido, mas chegar nele sem gargalo e de foma direta é impressionante.
Como configurar:
Passo 1: Clonar o repositório github.com/pentestwithai/LinuxPrivescMCP.
Passo 2: Criar e ativar ambiente virtual do Python e Instalar as dependências listadas com pip install -r requirements.txt.
Passo 3: Registrar o MCP Server no Codex apontando pro LinuxPrivescMCP.

Tendo isso, agora é só dar início à brincadeira!
