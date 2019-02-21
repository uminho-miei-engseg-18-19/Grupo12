# Aula TP 3 - 18/Fev/2019 - Resolução

## Exercício 1
Após a realização das experiências enunciadas, tendo , nas mesmas, criado um certificado baseado em algoritmo de curvas elípticas e experimentado o processo existente de assinatura cega, o grupo resolveu a pergunta 1.1 que consistia em alterar o código das componentes da assinatura cega para tornar mais simples o processo que a mesma envolve. Essa resolução encontra-se definida e explicada na próxima secção.

### Pergunta P1.1
Na pasta _BlindSignature_, encontra-se o código alterado como pedido nesta pergunta.

**Inicialização**

O módulo `init-app.py` deve agora, obrigatoriamente ser executado de uma das seguintes formas:
- `python init-app.py`, que devolve simplesmente as _pRDashComponents_.
- `python init-app.py -init`, que inicializa devidamente as componentes necessárias (_initComponents_ e _pRDashComponents_), guardando-as num ficheiro com o nome `signer_file`.

Qualquer outra forma de execução retornará uma mensagem informando como a aplicação deve ser executada. As imagens em baixo mostram o tipo de respostas possíveis nesta aplicação, excetuando erros ocorridos no próprio processo.

Execução utilizando o comando `python init-app.py`
![](imagens/init-app_alone.png)

Execução utilizando o comando `python init-app.py -init`
![](imagens/init-app_-init.png)

Execução utilizando o comando `python init-app.py -not` (erro)
![](imagens/init-app_error.png)

**Ofuscação**

O módulo `ofusca-app.py` deve agora, obrigatoriamente, ser executado da seguinte forma:
- `python ofusca-app.py -msg <mensagem_a_assinar> -RDash <pRDashComponents>`, devolvendo a _blind message_ e guardando as _blind components_ e as _pRComponents_ num ficheiro do requerente denominado de `req_file`.

Qualquer outra forma de execução retornará uma mensagem informando como a aplicação deve ser executada. As imagens em baixo mostram o tipo de respostas possíveis nesta aplicação, excetuando erros ocorridos no próprio processo.

Execução utilizando o comando correcto `python ofusca-app -msg <mensagem> -RDash <pRDashComponents>`.
![](imagens/ofusca-app.png)

Execução utilizando um exemplo de comando errado `python ofusca-app -msg <mensagem>`.
![](imagens/ofusca-app_errado.png)

**Assinatura**

O módulo `blindSignature-app.py` deve agora, obrigatoriamente, ser executado da seguinte forma:
- `python blindSignature-app.py -key <chave_privada> -bmsg <blind_message>`, devolvendo a _blind signature_ realizada.

Qualquer outra forma de execução retornará uma mensagem informando como a aplicação deve ser executada. As imagens em baixo mostram o tipo de respostas possíveis nesta aplicação, excetuando erros ocorridos no próprio processo.

Execução utilizando o comando correcto `python blindSignature-app.py -key <chave_privada> -bmsg <blind_message>`.
![](imagens/blindSignature-app.png)

Execução utilizando o comando errado `python blindSignature-app.py -bmsg <blind_message>`.
![](imagens/blindSignature-app_errado.png)

**Desofuscação**

O módulo `desofusca-app.py` deve agora, obrigatoriamente, ser executado da seguinte forma:
- `python desofusca-app.py -s <blind_signature> -RDash <pRDashComponents>`, devolvendo a assinatura retirada da _blind signature_.

Qualquer outra forma de execução retornará uma mensagem informando como a aplicação deve ser executada. As imagens em baixo mostram o tipo de respostas possíveis nesta aplicação, excetuando erros ocorridos no próprio processo.

Execução utilizando o comando correcto `python desofusca-app.py -s <blind_signature> -RDash <pRDashComponents>`.
![](imagens/desofusca-app.png)

Execução utilizando o comando errado `python desofusca-app.py -s <blind_signature>`.
![](imagens/desofusca-app_errado.png)

**Verificação**

O módulo `verify-app.py` deve agora, obrigatoriamente, ser executado da seguinte forma:
- `python verify-app.py -cert <certificado_assinante> -msg <mensagem_original_a_assinar> -sDash <signature> -f <ficheiro_requerente>`, retornando informação sobre a validade da assinatura.

Qualquer outra forma de execução retornará uma mensagem informando como a aplicação deve ser executada. As imagens em baixo mostram o tipo de respostas possíveis nesta aplicação, excetuando erros ocorridos no próprio processo.

Execução utilizando um comando correto e uma assinatura correcta.
![](imagens/verify-app_true.png)

Execução utilizando um comando correto e uma assinatura errada.
![](imagens/verify-app_false.png)

Execução utilizando um comando errado.
![](imagens/verify-app_errado.png)

**Conclusão exercício 1**

Após todas estas alterações, a simplificação do processo de assinatura cega está concluída, como demonstrado pelas imagens anteriormente referidas. Um exemplo do `req_file` e `signer_file`, bem como o código alterado e a chave e certificado utilizados encontram-se também neste repositório dentro da pasta `Aula3`. Os ficheiros encontram-se na pasta `BlindSignature`. A chave e certificado encontram-se na pasta `q1`.



## Exercício 2

### Pergunta P2.1

## Exercício 3

### Pergunta P3.1

#### P3.1.1 - Resultados ssh-audit

#### P3.1.2 - software e versão servidores ssh

#### P3.1.3 - Análise de vulnerabilidades

#### P3.1.4 - Gravidade de vulnerabilidades

#### P3.1.5 - Análise da gravidade de uma vulnerabilidade

