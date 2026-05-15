Dessa vez um pouco diferente. Comparando o DeepSeek V4 Pro e Claude Opus 4.6 na resolução da máquina Nocturnal do Hack The Box usando Burp MCP.
Ambos os modelos foram testados no mesmo cenário, com o mesmo prompt e as mesmas dicas quando necessário. A máquina exige encadear IDOR, leitura de arquivos, command injection e dump de banco de dados (sqlite).
Primeiro ponto em comum, os dois se perderam no início. Nenhum identificou o IDOR no parâmetro username do view.php de forma autônoma. Ambos precisaram de direcionamento para fazer fuzzing de usernames antes de partir para técnicas mais avançadas. AI parece ainda priorizar complexidade sobre metodologia básica.
Na leitura do arquivo privacy.odt, o Opus resolveu rapidamente, extraindo o conteúdo sem dificuldade. O DeepSeek travou nessa etapa e precisou de ajuda para tratar o arquivo binário corretamente.
Na fase de command injection, o DeepSeek surpreendeu criando scripts automatizados para interagir com o endpoint vulnerável, mostrando criatividade na exploração. O Opus foi mais autônomo no fluxo geral, precisando de menos intervenções para manter o raciocínio no caminho certo.
Dados da sessão:
DeepSeek V4 Pro: $1.76 de custo, 102k tokens consumidos, 35 minutos de execução
Claude Opus 4.6: $3.83 de custo, 158k tokens consumidos, 21 minutos de execução
O DeepSeek custou menos da metade do Opus, mas foi mais lento. O Opus foi mais consistente e autônomo, mas consumiu mais tokens, apesar da velocidade. A escolha depende do que se prioriza, custo ou estabilidade no raciocínio.
Ambos precisaram de direcionamento humano em alguns momentos.
#pentesting #hacking #ai #claude #deepseek
