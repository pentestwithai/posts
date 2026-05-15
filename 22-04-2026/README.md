Rodando Gemma 4 de 4 bilhões de parâmetros (modelo local) no VSCode pra fazer whitebox em um challenge do HackTheBox, o C.O.P. Sem API, sem nuvem, sem gastar token, somente hardware local. Modelo enxuto fazendo análise de código fonte real.

Setup em 4 passos:

1. Instalar o modelo: ollama pull gemma4:e4b
2. Instalar o plugin Continue no VSCode
3. Atualizar o config.yaml apontando pro modelo local (config que mostrei no vídeo)
4. Importar o código fonte do challenge no VSCode

Feito isso, abra a aba do Continue, selecione os arquivos como contexto e manda o prompt.

O Gemma 4 sozinho achou SQL Injection no parâmetro product_id da rota /view/<id>, com query montada em f-string sem sanitização. E Pickle Deserialization no filtro pickle_loads do app.py, RCE clássico quando pickle.loads() recebe input não confiável.

Onde ele não teve avanço: o Gemma identificou as duas vulnerabilidades separadamente, mas não enxergou que elas precisam ser encadeadas pra resolver o challenge.

A solução correta do C.O.P é usar o SQLi com UNION SELECT pra injetar um payload pickle malicioso direto no resultado da query, fazendo o template renderizar esse dado e triggerar o pickle.loads() com código arbitrário do atacante.

O modelo sugeriu injetar payload no fluxo de dados que chega ao product.data, mas não conectou que o próprio SQLi é o vetor de entrega do payload pickle. Descreveu as vulnerabilidades isoladamente, não em cadeia.

Modelo de 4B rodando local é legal pra recon e identificação de vulnerabilidades isoladas em código. Mas pra raciocínio de attack chain encadeada, ainda precisa de modelo maior, (por exemplo o Opus 4.7 ou GPT-5.4) ou um prompt mais guiado (sempre avaliando o tamanho da janela de contexto). Boa ferramenta pra velocidade em achar findings, ajuda muito, mas não substitui uma análise humana ainda.
