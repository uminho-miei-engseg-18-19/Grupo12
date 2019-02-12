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
1. Após a análise dos 3 ficheiros indicados e a necessária geração da chave privada e do seu certificado, gerados numa diretoria criada para o propósito com o nome de `key_p21`, foi necessário executar o seguinte comando de forma a dividir o segredo com as propriedades definidas no enunciado:
`python2 createSharedSecret-app.py 8 5 g12 key_p21/mykey.pem`.
De seguida, introduzimos a palavra-chave definida no ato da criação da chave privada e inserimos o segredo indicado no enunciado. Para reconstruir o segredo a partir de um quorum de 5 intervenientes, foi necessário executar o seguinte comando:
`python2 recoverSecretFromComponents-app.py 5 g12 key_p21/mykey.crt`.
Como é possível ver no segundo comando mostrado, é necessário indicar ao programa o número de intervenientes necessários (quorum) para que seja possível recuperar o segredo. O programa de seguida, pede a inserção de 5 componentes das 8 previamente geradas ao criar o segredo.

2. A diferença entre os dois programas reside no facto de que um deles apenas precisa das componentes de um número de intervenientes definidos como o quorum (neste caso são 5) para conseguir recuperar o segredo (`recoverSecretFromComponents-app.py`), enquanto que o outro necessita das componentes de todos os intervenientes inicialmente definidos (neste caso são 8), para conseguir recuperar o segredo (`recoverSecretFromAllComponents-app.py`). **FALTA DIZER EM QUE SITUAÇÕES PODEREMOS PRECISAR DE UTILIZAR O RECOVER FROM ALL COMPONENTS**

#### Pergunta P3.1

#### Pergunta P4.1