# Aula TP - 11/Fev/2019 - Resolução

#### Pergunta P1.1
A primeira conclusão que podemos retirar da execução destes comandos é que, em `dev/random`, com o aumento do tamanho requerido de bytes aleatórios, existe também um aumento substancial do tempo necessário para que o mesmo seja gerado e apresentado. Esta conclusão baseia-se em dois factos:
1. A própria experiência na execução dos comandos, que apresentam um tempo bem mais elevado de retorno nos casos de geração de 1024 bytes do que nos casos de geração de 32 e 64 bytes.
2. O facto de ser conhecido que a utilização de `dev/random` requer o bloqueio da operação de pedido de um número aleatório até que o sistema tenha conseguido coletar a entropia necessária para que o mesmo seja gerado, com segurança criptográfica forte.

A segunda conclusão que podemos retirar da execução do último comando é que, em `dev/urandom`, a geração do número pseudoaleatório, independentemente do tamanho, é feita de imediato, visto que o sistema não espera pela coleta da entropia necessária para gerar um número pseudoaleatório criptograficamente forte, o que implica que, apesar de ser um método mais veloz pode, por vezes, não ser seguro e, logo, ser teoricamente suscetível a ataques criptográficos.

#### Pergunta P1.2
Após a execução dos comandos apresentados, é possível concluir que, com o _daemon_ do **haveged** ligado, a coleta da entropia necessária para a geração de bytes aleatórios é bastante mais rápida pelo que, mesmo pedindo a geração dos mesmos através de `/dev/random`, esta é feita de forma imediata. Esta conclusão pode ser retirada de dois factos:
1. O **haveged** é um _daemon_ que coleta entropia apartir de efeitos indiretos que ocorrem no sistema, ou seja, é capaz de coletar bastante mais entropia do que seria normalmente o caso, o que permite gerar mais rapidamente os bytes aleatórios.
2. A realização de uma experiência feita pelo grupo, ao executar o comando `head -c 10000000 /dev/random | openssl enc -base64`, pedindo a geração de dez milhões de bytes aleatórios, que resultou apenas no tempo de geração dos número necessário de bytes e não uma espera excessiva pela coleta de entropia. Servindo como indicador, a execução completa deste comando, desde a geração do primeiro byte ao último demorou cerca de 6 segundos apenas, o que para números desta grandeza é compreensível.

#### Pergunta P1.3
1. Após execução do programa _generateSecret-app.py_ e respetiva análise do seu código bem como do código da função `generateSecret(length)` do módulo **shamirsecret** importado da _package_ **eVotUM.Cripto**, podemos afirmar que a razão pela qual o _output_ produzido pela execução do programa apresenta apenas letras e dígitos deve-se ao facto da função anteriormente referida(`generateSecret(length)`) apenas imprimir bytes _ascii_ e dígitos, o que faz com que apenas letras e números sejam apresentadas no resultado final.
2. Para que o _output_ gerado também apresentasse outro tipo de caratéres, a função `generateSecret(length)` deveria ser alterada de forma a que codificasse os bytes aleatórios gerados em `base64`, tal como era feito na primeira e segunda perguntas deste enunciado.

#### Pergunta P2.1

#### Pergunta P3.1

#### Pergunta P4.1