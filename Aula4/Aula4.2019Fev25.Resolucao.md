# Aula 4 - Resolução do Trabalho

## Pergunta 1

### Pergunta 1.1

#### Pergunta 1.1.1

Tendo em conta a protecção de privacidade e do anonimato do protocolo **TOR**, não.

#### Pergunta 1.1.2

A ferramenta _anonsurf_ utiliza o protocolo **TOR** para garantir o anonimato, visto que todo o tráfego é encaminhado utilizando esse protocolo, o que faz com que o utilizador que execute esse comando irá garantir o anonimato, devido ao facto de o seu verdadeiro IP estar protegido por outros nodos. O que impede que seja possível garantir que o IP pertenceça aos EUA é o facto de que, ao utilizar o comando `sudo anonsurf start` não temos qualquer tipo de controlo sobre o IP que nos irá "representar".

### Pergunta 1.2

#### Pergunta 1.2.1

O circuito apresentado no _browser_ **TOR**, após acesso à _The Hidden Wiki_, é o seguinte:

1. This browser
2. Czech Republic
3. Germany
4. Russia
5. Relay
6. Relay
7. Relay
8. zqktlwi4fecvo6ri.onion (_The Hidden Wiki_)

#### Pergunta 1.2.2

A razão pela qual são realizados 6 saltos até ao site deve-se ao facto de o nosso _browser_ se conectar a um ponto de _rendezvous_ , o que faz com que tenha que ser estabelecido um circuito de 3 _Onion Routers_ (incluindo o ponto de _rendezvous_), assim como o circuito já existente entre o ponto de _rendezvous_ e o _website_ ao qual queremos aceder (após conexão), sendo que este circuito é composto por 3 _onion routers_ escolhidos pelo servidor ao qual nos estámos a tentar conectar. 3 dos nodos apresentados na informação acima descrita são do tipo "Relay", visto que estes são os nodos escolhidos pelo servidor, dos quais nós não possuímos informação, sabendo apenas que eles estão lá para garantir o anonimato do servidor, bem como a transmissão dos dados enviados e recebidos.

