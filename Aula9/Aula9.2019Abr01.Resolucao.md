# Aula 9 - Resolução

## Pergunta P1.1

### Pergunta P1.1.1

Tendo em conta que usualmente se utiliza a estimativa de que um software desenvolvido com métodos rigorosos de segurança contém cerca de 5 _bugs_ por 1000 linhas de código fonte e software desenvolvido normalmente pode conter até 50 _bugs_ por 1000 linhas de código fonte, podemos realizar as seguintes estimativas:
- Assumindo que o _facebook_ terá sido uma aplicação desenvolvida, à partida, com métodos normais de desenvolvimento, deverá apresentar um limite superior de _bugs_ de 50 * (62000000/1000), ou seja, de 3 milhões e 100 mil _bugs_, apesar de que esse número poderá ser bastante exagerado.
- Assumindo que o _Linux3.1_ deverá ter sido um software desenvolvido com métodos mais rigorosos do que, por exemplo, o _facebook_ podemos estimar que tenha um limite inferior de _bugs_ de 5 * (15000000/1000), ou seja de 75000 _bugs_, apesar de que esse número pode ser superior.
- O _software_ construído para automóveis tem que ser, certamente, desenvolvido com métodos rigorosos de _software_, pelo que podemos estimar que tenha um limite inferior de _bugs_ de 5 *(100000000/1000), ou seja, de 500000 _bugs_, o que mesmo assim seria um número elevado.
- Assumindo que todos os serviços _Google_ são desenvolvidos com métodos normais, com raras excepções, podemos estimar que estes serviços tenham um limite superior de _bugs_ de 50 * (2000000000/1000), ou seja de 100000000 de _bugs_, apesar de que o número pode ser inferior. 


### Pergunta P1.1.2

É praticamente impossível dizer quantas vulnerabilidades existem nos _bugs_ estimados, visto que num número muito grande de _bugs_ podem existir muito poucas vulnerabilidades e num número muito pequeno de _bugs_ podem existir muitas vulnerabilidades, dependerá sempre do tipo de _bug_ que é.

## Pergunta P1.2

Para as vulnerabilidades de projeto podemos apresentar, por exemplo:
- **Insufficient UI Warning of Dangerous Operations**, que acontece quando, na fase de _design_, se ignoram situações em que, avisos de operações perigosas devem ser postos, de uma forma clara, à atenção do utilizador, o que pode resultar numa quebra de segurança.
- **Improperly Implemented Security Check For Standard**, que acontece quando, na fase de _design_, não se tem em conta que um _software_ não está a implementar completamente um algoritmo ou técnica standardizada, o que pode resultar numa quebra de segurança, visto que sem o passo em falta, existe a possibilidade desse algoritmo ou técnica ser vulnerável.

Para as vulnerabilidades de codificação podemos apresentar, por exemplo:
- **Improper Input Validation** , que acontece quando um programador nega o facto de que um atacante consegue modificar o _input_ de campos escondidos ou de _cookies_, quando recorre a _proxies_, por exemplo.
- **Path traversal:'../filedir'**,  que acontece quando o _software_ usa _input_ externo para construir um nome de caminho para um ficheiro que devia estar dentro de uma diretoria restrita, mas que não neutraliza sequências de **'../'** que podem direccionar para diretorias fora da diretoria restrita.

Para as vulnerabilidades operacionais podemos apresentar, por exemplo:
- **ASP.NET Misconfiguration: Password in Configuration File**, que acontece quando, ao configurar um _software_, se guarda uma _password_ sem ser cifrada, num ficheiro de configuração, permitindo que qualquer pessoa que ganhe acesso a esse ficheiro consiga ler a mesma.
- **ASP.NET Misconfiguration: Creating Debug Binary**, que acontece quando, após a fase de desenvolvimento e testes, são mantidas mensagens de debug detalhadas, o que é um risco de segurança para o _software_.



## Pergunta P1.3

A diferença entre estes dois tipos de vulnerabilidades reside no facto de que, enquanto que as vulnerabilidades de dia zero são vulnerabilidades conhecidas apenas em meio restrito, não sendo divulgadas para a comunidade que lida com segurança informática, as vulnerabilidades de codificação não dia-zero são vulnerabilidades que, normalmente, possuem um ciclo de vida, ou seja, são criadas através da codificação, são posteriormente descobertas e, finalmente, são corrigidas através de _patches_ fornecidos pela empresa que desenvolveu o código que possui a vulnerabilidade.