# Aula 11 - Resolução

## Pergunta P1.1

O mesmo programa escrito em várias linguagens, neste caso Java, Python e C++, comporta-se de maneira diferente. Isto é, em todas as implementações do programa, primeiro todos alocam um pedaço de memória estática, com capacidade para armazenar 10 inteiros. De seguida, é solicitado ao utilizador que está a executar o programa, para indicar quantos números inteiros deseja armazenar. Posto isto, o utilizador pode inserir os elementos que pretende guardar, de acordo com o número máximo anteriormente referido.

Contudo, uma vez que o espaço alocado é estático, se o número de elementos que o utilizador desejar armazenar for superior ao número de elementos suportados, isto irá provocar um comportamento anormal de execução do programa, cujo tratamento depende da linguagem em que é implementado.

No caso da implementação em C++, executar o programa para armazenar um número de elementos superior ao que é suportado irá resultar *stack smashing*. Já no programa em Java, a execução deste será interrompida pelo lançamento de uma exceção: *Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10 at LOverflow2.main(LOverflow2.java:18)*. Finalmente, tal como na solução em java, a solução em Python também termina com uma exceção, mais concretamente: *IndexError: list assignment index out of range*.

 
## Pergunta P1.2

O programa *LOverflow3* implementado nas várias linguagens, permite ao utilizador especificar um número de elementos que pretende armazenar. De seguida, são armazenados por ordem decrescente os elementos com início no número especificado pelo utilizador. Posto isto, este pode especificar o elemento ao qual pretende aceder. Contudo, uma vez que não existe controlo sobre o número máximo de elementos que podem ser armazenados, e o espaço de memória é alocado estaticamente, o utilizador pode dispoletar um comportamento anormal da aplicação, indicando um número de elementos que pretende armazenar superior ao que é suportado e previamente alocado, neste caso de 10.

Porém, a forma como este problema é tratado depende da linguagem em que o programa foi implementado. No caso do Java e do Python, é lançada uma exceção, que não permite aceder a posições de memória que não foram alocadas pelo progama. Já no programa em C++, ao introduzir um número máximo de elementos superior ao que é suportado irá deixar o programa a executar indefinidamente, possivelmente pelo valor da variável que é avaliada na condição de verificação do ciclo ser modificado, devido ao acesso a um espaço de endereçamento, que não deve ser usado para armazenar os valores da aplicação.

Para além disto, existe também outro controlo que deve existir para garantir um bom funcionamento da aplicação, que consiste no acesso a uma posição do vetor de elementos armazenados superior aquela que foi introduzida pelo utilizador, neste caso menor do que 10. Isto é, se um utiizador disser que pretende armazenar 2 valores e depois tentar aceder ao que está na posição 3, o resultado poderá variar de acordo com a linguagem em que foi implementada. No caso do C++, uma vez que este vetor não é inicializado, será devolvido o valor que estiver armazenado nesta posição de memória, seja ele qual for, produzindo um comportamento imprevisível. Contudo, uma vez que o Java e o Python inicializam estes vetores, no caso do Java será retornado o valor 0 e no caso do Python *None*.

## Pergunta P1.3

A vulnerabilidade de *Buffer Overflow* presente nestas aplicações é conhecida como *Stack-based buffer overflow*. Esta acontece porque, quando um *array* é declaro em C, o espaço para ele é reservado e o *array* é manipulado através do seu apontador, para o primeiro byte. Contudo, a função `gets` não é segura porque não verifica se os limites do *array* são ultrapassados. Por isso, quando o compilador gera código máquina, para ser executado, o código gerado permite que o programa copie informação, para além dos limites do *array*, alterando o conteúdo das posições de memória adjacentes a este.

Posto isto, para o caso do programa *RootExplooit*, poderá ser usada uma string com mais de 4 caracteres, que corresponde ao espaço reservado para a password introduzida, de modo alterar a informação nas posições de memória adjacentes. Neste caso, alterando o valor da variável `pass` e obter as permissões de root/admin.

Para o caso da aplicação *0-simple*, já será necessário que a string introduzida possua um número máximo de caracteres superior a 64. Desta forma, é possível alterar o valor da variável `control` e consequentemente obter a mensagem "YOU WIN!!!".

## Pergunta P1.4

Após testar e executar o programa `ReadOverflow.c`, podemos concluir que, facilmente, se extrai conhecimento remanescente da memória, executando este programa de forma a que o mesmo seja quebrado. Um exemplo disto é indicar ao programa que pretendemos escrever 20 caratéres, mas quando escrevermos a frase, escrevemos uma que tenha apenas 9 caratéres, por exemplo. O programa ao percorrer o ciclo sem validar se o tamanho da frase é, de facto, igual ao tamanho inicialmente indicado, para além de imprimir os caratéres inseridos, também vai imprimir os restantes que faltam até atingir o número indicado, de posições sucessivas da memória, que ficaram como dados remanescentes.



## Pergunta P1.5



## Pergunta P2.1



## Pergunta P2.2

