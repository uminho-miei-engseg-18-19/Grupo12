# Aula 11 - Resolução

## Pergunta P1.1

O mesmo programa escrito em várias linguagens, neste caso Java, Python e C++, comporta-se de maneira diferente. Isto é, em todas as implementações do programa, primeiro todos alocam um pedaço de memória estática, com capacidade para armazenar 10 inteiros. De seguida, é solicitado ao utilizador que está a executar o programa, para indicar quantos números inteiros deseja armazenar. Posto isto, o utilizador pode inserir os elementos que pretende guardar, de acordo com o número máximo anteriormente referido.

Contudo, uma vez que o espaço alocado é estático, se o número de elementos que o utilizador desejar armazenar for superior ao número de elementos suportados, isto irá provocar um comportamento anormal de execução do programa, cujo tratamento depende da linguagem em que é implementado.

No caso da implementação em C++, executar o programa para armazenar um número de elementos superior ao que é suportado irá resultar *stack smashing*. Já no programa em Java, a execução deste será interrompida pelo lançamento de uma exceção: *Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10 at LOverflow2.main(LOverflow2.java:18)*. Finalmente, tal como na solução em java, a solução em Python também termina com uma exceção, mais concretamente: *IndexError: list assignment index out of range*.

 
## Pergunta P1.2

O programa *LOverflow3* implementado nas várias linguagens, permite ao utilizador especificar um número de elementos que pretende armazenar. De seguida, são armazenados por ordem decrescente os elementos com início no número especificado pelo utilizador. Posto isto, este pode especificar o elemento ao qual pretende aceder. Contudo, uma vez que não existe controlo sobre o número máximo de elementos que podem ser armazenados, e o espaço de memória é alocado estaticamente, o utilizador pode disputar um comportamento normal da aplicação, indicando um número de elementos que pretende armazenar superior ao que é suportado e previamente alocado, neste caso de 10.

Porém, a forma como este problema é tratado depende da linguagem em que o programa foi implementado. No caso do Java e do Python, é lançada uma exceção, que não permite aceder a posições de memória que não foram alocadas pelo progama. Já no programa em C++, ao introduzir um número máximo de elementos superior ao que é suportado irá deixar o programa a executar indefinidamente, possivelmente pelo valor da variável que é avaliada na condição de verificação do ciclo ser modificado, devido ao acesso a um espaço de endereçamento, que não deve ser usado para armazenar os valores da aplicação.

Para além disto, existe também outro controlo que deve existir para garantir um bom funcionamento da aplicação, que consiste no acesso a uma posição do vetor de elementos armazenados superior aquela que foi introduzida pelo utilizador, neste caso menor do que 10. Isto é, se um utiizador disser que pretende armazenar 2 valores e depois tentar aceder ao que está na posição 3, o resultado poderá variar de acordo com a linguagem em que foi implementada. No caso do C++, uma vez que este vetor não é inicializado, será devolvido o valor que estiver armazenado nesta posição de memória, seja ele qual for, produzindo um comportamento imprevisível. Contudo, uma vez que o Java e o Python inicializam estes vetores, no caso do Java será retornado o valor 0 e no caso do Python *None*.

## Pergunta P1.3



## Pergunta P1.4



## Pergunta P1.5



## Pergunta P2.1



## Pergunta P2.2

