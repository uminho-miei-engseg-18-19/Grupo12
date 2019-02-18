# Aula TP - 11/Fev/2019 - Resolução

[tab:sha256]: imagens/keylength.256
[tab:sha1]: imagens/keylength.160

#### Pergunta P1.1

|                                                  | Tempo de Execução (ms) |
|:------------------------------------------------:|:----------------------:|
| head -c 32 /dev/random \| openssl enc -base64    |                     16 |
| head -c 64 /dev/random \| openssl enc -base64    |                 2.00e4 |
| head -c 1024 /dev/random \| openssl enc -base64  |                 3.72e5 |
| head -c 1024 /dev/urandom \| openssl enc -base64 |                     19 |

A primeira conclusão que podemos retirar da execução destes comandos é que, em `dev/random`, com o aumento do tamanho requerido de bytes aleatórios, existe também um aumento substancial do tempo necessário para que o mesmo seja gerado e apresentado. Esta conclusão baseia-se em dois factos:
1. A própria experiência na execução dos comandos, que apresentam um tempo bem mais elevado de retorno nos casos de geração de 1024 bytes, do que nos casos de geração de 32 e 64 bytes.
2. O facto de ser conhecido que a utilização de `dev/random` requer o bloqueio da operação de pedido de um número aleatório até que o sistema tenha conseguido coletar a entropia necessária para que o mesmo seja gerado, com segurança criptográfica forte.

A segunda conclusão que podemos retirar da execução do último comando é que, em `dev/urandom`, a geração do número pseudoaleatório, independentemente do tamanho, é feita de imediato, visto que o sistema não espera pela coleta da entropia necessária para gerar uma sequência de bytes pseudoaleatórios criptograficamente forte. Isto implica que, apesar de ser um método mais eficiente em termos de desempemho, pode por vezes não ser seguro logo, ser teoricamente suscetível a ataques criptográficos.

#### Pergunta P1.2

|                                                  | Tempo de Execução (ms) |
|:------------------------------------------------:|:----------------------:|
| head -c 1024 /dev/random \| openssl enc -base64  |                     13 |
| head -c 1024 /dev/urandom \| openssl enc -base64 |                      5 |

Após a execução dos comandos apresentados, é possível concluir que, com o _daemon_ do **haveged** ativo, a coleta da entropia necessária para a geração de bytes aleatórios é bastante mais rápida pelo que, mesmo pedindo a geração dos mesmos através de `/dev/random`, esta é feita de forma imediata. Esta conclusão pode ser retirada de dois factos:
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

2. A diferença entre os dois programas reside no facto de que um deles apenas precisa das componentes de um número de intervenientes definidos como o quorum (neste caso são 5) para conseguir recuperar o segredo (`recoverSecretFromComponents-app.py`), enquanto que o outro necessita das componentes de todos os intervenientes inicialmente definidos (neste caso são 8), para conseguir recuperar o segredo (`recoverSecretFromAllComponents-app.py`). Uma das situações em que poderemos precisar de todos os intervenientes será, por exemplo, se quisermos alterar o segredeo, visto que para esse efeito deve ser dada permissão de todos os intervenientes e, assim, o segredo alterar-se-ia e novas chaves seriam distribuídas pelo número de intervenientes necessários.

#### Pergunta P3.1
Para responder corretamente a esta pergunta, é necessário primeiro definir exatamente os parâmetros e funções que terão que existir, além das fornecidas pela API para que o algoritmo esteja correcto, com o objetivo de garantir as propriedades de confidencialidade, integridade e autenticidade tanto na segredo como na etiqueta. Assim, devemos determinar que existem estas funções:
- _todaysDate()_ , uma função que retorna o dia de hoje no formato "ano.mes.dia".
- _getUserID()_ , uma função que retorna o identificador do utilizador no sistema.
- _getKey(date)_ , uma função que recebe uma data no formato "ano.mes.dia" e retorna a chave a utilizar nesse dia.
- _verifyAnnuity(userID)_ , uma função que, dado o identificador de um utilizador no sistema, verifica se o mesmo tem a anuidade em dia e, assim, pode decifrar segredos.

Tendo estas funções em conta, bem como a própria API fornecida, podemos definir um algoritmo para a cifragem e outro para a decifragem dos conteúdos.
O algoritmo de cifra pode ser definido da seguinte forma:
1. Pedir ao utilizador o segredo que quer cifrar e a etiqueta que ficará anexada ao segredo.
2. verificar se o utilizador tem a anuidade paga invocando a função `verifyAnnuity(getUserID())`.
3. Em caso de resposta afirmativa prosseguir para o passo 4, caso contrário terminar a execução.
4. Invocar a função da API `cifra(segredo)`, onde o parâmetro segredo deverá ser o segredo que o utilizador indicou no início.
5. Invocar a função da API `cifra(etiqueta)`, onde o parâmetro etiqueta deverá ser a etiqueta indicada pelo utilizador para este segredo.
5. Invocar a função da API `hmac(k,str)`, onde o parâmetro k é a chave a ser utilizada na operação do _hmac_ e o parâmetro str é o segredo cifrado.
6. Invocar a função da API `hmac(k,str2)`, onde o parâmetro k é a chave a ser utilizada na operação do _hmac_ e o parâmetro str2 é a etiqueta cifrada.
7. Invocar a função `todaysDate()`.
8. Criar um objeto contendo 5 elementos como demonstrado em baixo e guardá-lo (A data tem que estar presente para que saibámos qual chave utilizar na decifragem).

        {
            "cryptogram": "...",
            "cryptogram_auth": "...",
            "tag": "...",
            "tag_auth": "...",
            "date": "..."
        }

O algoritmo de decifragem pode ser definido da seguinte forma:
1. Ir buscar o objeto correspondente ao segredo que o cliente pretende decifrar (object).
2. Verificar se o utilizador tem a anuidade paga invocando a função `verifyAnnuity(getUserID())`. Se sim, seguir para o passo 3, caso contrário, terminar execução.
3. Questionar cliente se pretende decifrar só a etiqueta ou se pretende decifrar a etiqueta e o segredo e guardar resposta.
4. Ir buscar a chave que deve ser utilizada neste segredo, invocando a função `getKey(object.date)`.
5. Calcular o código de autenticação da etiqueta, invocando a função `hmac(k,object.tag)`. Comparar o código obtido com object.tag_auth. Se forem iguais , seguir para o passo 5, caso contrário, terminar processo de decifragem.
6. Decifrar a etiqueta, invocando a função `decifra(object.tag,chave)`, onde o parâmetro chave é a chave que foi previamente obtida. Se o utilizador apenas escolheu decifrar a etiqueta, mostrar resultado e terminar execução, caso contrário, seguir para o passo 6.
7. Calcular o código de autenticação do segredo, invocando a função `hmac(k,object.cryptogram)`. Comparar o código obtido com object.cryptogram_auth. Se forem iguais, seguir para o passo 7, caso contrário, terminar execução.
8. Decifrar o segredo, invocando a função `decifra(object.cryptogram,chave)`, onde o parâmetro chave é a chave que foi previamente obtida.
9. Apresentar ao utilizador a etiqueta e o segredo decifrados.

        


#### Pergunta P4.1

Visto que somos o grupo 12 e recorrendo à [lista de entidades com serviços qualificados de confiança](https://webgate.ec.europa.eu/tl-browser/#/tl/NO), para o nosso caso, foi possível identificar o algoritmo e tamanho das chaves utilizados pelos seguintes serviços de emissão de certificados.

|                Entidade               |    Algoritmo   | Tamanho da Chave (bits) |
|:-------------------------------------|:--------------:|:-----------------------:|
| BankID Nordea Bank CA 2               | sha256 com RSA |                    4096 |
| Statoil Root CA                       | sha1 com RSA   |                    4096 |

![alt text][tab:sha256]
*Figura 1. https://www.keylength.com recomendações para sha256.*

![alt text][tab:sha1]
*Figura 2. https://www.keylength.com recomendações para sha1.*

De acordo com as imagens em cima (a primeira é referente ao sha256 e a segunda é referente ao sha1), podemos concluir que o algoritmo *sha1*, é desaconselhado para curto e longo prazo. Contudo, o algoritmo *sha256* continua a ser uma boa opção, para curtos e longos prazos, pelo que a entidade Statoil Root CA deveria alterar o seu algoritmo para sha256 com RSA.