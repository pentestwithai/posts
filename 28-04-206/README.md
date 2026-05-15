Máquina Administrator (Windows) do Hack The Box resolvida com OpenClaude + BloodHound MCP.

Ambiente Windows, Active Directory, dificuldade medium. Cenário de assumed breach partindo de um usuário low-privilege (Olivia) com o objetivo de chegar em Domain Admin.

O ponto central desse writeup é como o BloodHound MCP mudou o fluxo. Normalmente você coleta os dados via bloodhound-python ou SharpHound, importa no BloodHound, e fica navegando manualmente pelo grafo tentando encontrar attack paths entre milhares de relações. Com o MCP integrado ao OpenClaude, o modelo consulta o banco Neo4j direto e interpreta as relações em linguagem natural. Você pergunta “qual o caminho mais curto até Domain Admin partindo da Olivia?” e ele mapeia a cadeia inteira.

Foi assim que o modelo traçou o path completo: Olivia com GenericAll sobre Michael, permitindo reset de senha. Michael com ForceChangePassword sobre Benjamin. Benjamin com acesso ao FTP onde havia um backup .psafe3. Vault crackado, credenciais da Emily expostas. Emily tinha GenericWrite sobre Ethan, abrindo espaço pra Targeted Kerberoasting, foi solicitado ao modelo usar a ferramenta targetedKerberoast.py. Hash crackado, e o Ethan com DCSync rights entregando o hash do Administrator. Domain compromise completo.

5 pivots, tudo mapeado pelo modelo antes de executar um único comando. O BloodHound MCP não substitui o pentest, ele acelera a parte mais demorada que é a análise do grafo e a identificação de attack paths viáveis. O resto continua sendo execução técnica.

Setup:
Passo 1: Clonar o repositório bloodhound_mcp
Passo 2: Rodar o comando uv sync para instalar dependências
Passo 3: Criar o arquivo .env
Passo 4: Adquirir token ID e token Key do BloodHound e preencher o .env
Passo 5: Conectar o MCP server ao OpenClaude via openclaude mcp add

#pentesting #hackthebox #activedirectory #hacking #code
