# Aula TP - 25/Mar/2019 - Resolução

Respostas às perguntas dos exercícios propostos na aula prática de 25 de março de 2019.

## Resolução dos Exercícios



### 1. Blockchain



#### Pergunta 1.1

Nesta implementação de uma blockchain, a classe *Block* é definida mediante as seguintes propriedades:

1. index - Esta é uma propriedade opcional, que pode ser passada ao construtor para indicar a posição do bloco instanciado, na blockchain;
2. timestamp - Tal como o nome indica, esta propriedade atribui um timestamp sobre quando é que o bloco foi criado;
3. data - Este parâmetro, armazena qualquer tipo de informação relevante para os utilizadores, por exemplo uma descrição de uma transação;
4. previousHash - Consiste numa string que contém o valor do hash do bloco anterior.

Posto isto, a classe *Blockchain* é implementada com base na classe anterior. Esta é inicializada pelo seu construtor, que por sua vez usa o construtor da classe *Block*, para criar o primeiro bloco da cadeia (**genesis block**).

Tendo isto em conta, o grupo alterou o método `createGenesisBlock`, de modo a que o timestamp seja a data atual e a informação para ser armazenada seja: "Bloco inicial da koreCoin". Para tal, definiu-se uma função `formatDate`, para formatar uma instância do objeto *Date* e convertê-lo para string. A informação que é passada ao construtor, foi também alterada para o que é pretendido. O código modificado pode ser encontrado na respetiva diretoria.

#### Pergunta 1.2

Tal como foi visto anteriormente, a propriedade **data** permite armazenar informação de todo o tipo, podendo ser uma descrição para uma determinada transação. Contudo, pode também descrever várias transações. Por isso, foram também adicionados alguns exemplos de blocos, que contêm várias transações em cada um deles.

Ao testar a validade da cadeia, facilmemte se verifica que esta é válida, para todos os blocos adicionados.

### 2\. Proof of Work Consensus Model



#### Pergunta P2.1

2 - 0.245s
3 - 0.645s
4 - 3.127s
5 - 31.154s

#### Pergunta P2.2

1. O algoritmo de _proof of work_ consiste no incremento de uma variável dada pelo último _proof of work_ até que esta seja divisível por 9 e seja também divisível pelo último _proof of work_.

2. 