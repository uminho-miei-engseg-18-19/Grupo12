# Aula 7 - Resolução

## Pergunta P1.1

Para esta pergunta, o grupo escolheu analisar o documento _Handbook on european data protection law_, especificamente, a secção 6.1.5 que define o direito à portabilidade de dados (_right to data portability_).
Na definição do direito à portabilidade de dados, podemos definir duas entidades existentes em dada altura de um processo respeitante ao mesmo:

- O controlador, entidade que processa os dados pessoais de um sujeito.
- O sujeito, que é identificado pelos dados pessoais possuídos e processados pelo controlador.

Este direito é aplicável em qualquer situação onde exista um consentimento ou um contrato entre o sujeito e o controlador. Além disso, o direito aplica-se, obviamente, ao sujeito, sendo que, do lado do controlador, se torna num dever de providenciar ferramentas para que o sujeito possa exercer esse direito.

O direito à portabilidade de dados define-se, sumariamente, como sendo o direito de um sujeito ter a possibilidade de existir uma transmissão dos seus dados pessoais de um controlador para o outro.

Este direito é definido por 4 _guidelines_:

- O sujeito tem o direito de receber os seus dados pessoais, processados por um controlador, numa forma estruturada, num formato comum e legíveis por uma máquina.
- O sujeito tem o direito de transmitir os seus dados pessoais de um controlador para o outro, sem obstáculos técnicos à possibilidade de o fazer.
- O controlador não é responsável pela conformidade com a lei de protecção de dados do destinatário dos dados pessoais de um sujeito, após pedido de portabilidade realizado pelo mesmo.
- O exercício deste direito não influencia qualquer outro direito declarado no RGPD.

Tendo tudo isto em conta, é fácil verificar que estas _guidelines_ fazem com que tenham que, obrigatoriamente, existir preocupações adicionais ao desenvolver _software_, visto que este tem que estar conforme a lei de protecção de dados, o que inclui o direito à portabilidade de dados.
O _software_ construído deve, nesse sentido, ser capaz de produzir uma espécie de relatório de todos os dados pessoais de qualquer um dos sujeitos que são utilizadores do mesmo num formato que seja utilizável por outros controladores.
Em suma, o desenvolvimento de um _software_ deve sempre ter em conta que os dados recolhidos de um dado sujeito devem sempre estar disponíveis e preparados para serem recolhidos e reunidos num formato que permita a transmissão dos mesmos para outro controlador, que poderá à partida, ter outro tipo de _software_, pelo que o formato utilizado deve ser um que é utilizado de forma comum.

## Pergunta P1.2

No documento _Privacy and Data protection by design - from policy to engineering_ estão descritas e detalhadas 8 estratégias de _privacy design_ sendo que estas estão separadas em duas categorias, da forma que se segue:

- Orientadas aos dados:
    - MINIMISE
    - HIDE
    - SEPARATE
    - AGGREGATE
- Orientadas ao processo:
    - INFORM
    - CONTROL
    - ENFORCE
    - DEMONSTRATE

A estratégia _MINIMISE_ estabelece que os dados pessoais que são processados devem ser limitados ao mínimo possível, ou seja, aos dados que são estritamente necessários para o funcionamento do serviço com o qual o utilizador interage. Para aplicar esta estratégia podemos aplicar um padrão de _design_, por exemplo, do tipo _select before collect_, ou seja, escolher o tipo de dados a processar antes de os coletar.

A estratégia _HIDE_ estabelece que os dados pessoais e as relações entre os mesmos não devem estar imediatamente visíveis, ou seja, não deve ser fácil "abusar" dos dados mesmo que sejam visualizados na sua forma de armazenamento. Para aplicar esta estratégia podemos aplicar cifras aos dados, escondendo-os.

A estratégia _SEPARATE_ estabelece que os dados pessoais devem ser ser processados de forma distribuída e compartimentada, sempre que possível, de forma a evitar a construção de um perfil do utilizador. A ideia principal é que, ao processar dados de um dado utilizador, de forma compartimentada, fica mais difícil coletar toda a informação sobre o mesmo.

A estratégia _AGGREGATE_ estabelece que os dados pessoais devem ser processados num nível alto de agregação e com o mínimo possível de detalhe, ou seja, os dados devem ser agregados por grupos de atributo ou indivíduos, restringindo a quantidade de detalhe de informação pessoal de um único indivíduo. A aplicação desta estratégia funciona bem em casos de coleta da mesma informação ao longo do tempo (_aggregation over time_) ou em casos de coleta extensiva de localização do indivíduo (_dynamic location granularity_).

A estratégia _INFORM_ estabelece que os sujeitos dos dados processados devem ser sempre informados sobre a informação que vai ser processada, para qual propósito vai ser processada e por que meios esse processamento vai ocorrer. Isto inclui a informação sobre os meios de protecção desses dados. Além disso, esta estratégia também estabelece que o utilizador deve ser notificado em qualquer situação de fuga de privacidade ou de alteração em formas de processamento.
Esta estratégia pode ser aplicada recorrenda a, por exemplo, notificações de fugas de dados ou a plataformas de preferências de privacidade.

A estratégia _CONTROL_ estabelece que a um indivíduo deve ser dada a capacidade de controlar qual informação sua é processada ou utilizada. Além disso, também lhe deve ser fornecida a capacidade de atualizar ou remover a sua informação, quando aplicável. Esta estratégia pode ser aplicada utilizando, por exemplo, uma gestão de identidade centrada no utilizador ou cifragem ponto-a-ponto nos dados escolhidos pelo indíviduo, ou até uma combinação das duas.

A estratégia _ENFORCE_ estabelece que deve ser aplicada uma política de privacidade pelo controlador dos dados, que seja compatível com os requisitos legais. Além disso, esta estratégia define também que devem ser implementados mecanismos que previnam a violação dessa política de privacidade. Esta estratégia pode ser implementada recorrendo, por exemplo, a técnicas de controlo de acesso.

A estratégia _DEMONSTRATE_ estabelece que um controlador de dados deve conseguir demonstrar que cumpre a política de privacidade e os requisitos legais, ou seja, o controlador de dados deve provar que tem, de facto, controlo dos dados. Este também deve conseguir determinar a gravidade de uma fuga de privacidade que ocorra, se aplicar esta estratégia. Esta estratégia pode ser implementada recorrendo a ferramentas de _logging_ e _auditing_, por exemplo.

## Pergunta P1.3

1. O GDPR não requer que seja efetuado um DPIA para qualquer operação de processamento de dados pessoais, que pode representar um risco para a liberdade dos sujeitos. Apenas se torna obrigatório, quando o processamento pode resultar num risco elevado, para os direitos e liberdade das pessoas.

    De modo a estabelecer uma distinção entre estes conjuntos de operações, foram desenvolvidos nove critérios, que devem ser considerados, devido ao seu elevado risco inerente. Esses são os seguintes:

    1. **Avaliação ou classificação**, incluindo desenhar um perfil ou prever, aspetos relativos ao desempenho laboral, estado económico, saúde, gostos pessoais ou interesses, confiabilidade ou comportamento, localização ou deslocamentos.
    
    2. Processamento que envolve a **tomada de decisões com efeitos legais ou semelhantes significativamente**. Isto envolve que, durante o processamento, sejam tomadas decisões no lugar do utilizador, com os efeitos já referidos. Um exemplo disto seria o processamento de dados, que leva à exclução ou discriminação de certos indivíduos.

    3. **Monitorização sistemática**, ou seja, processamento que envolve observação, monitorização ou controlo de dados sobre indivíduos. Isto inclui dados coletados de redes ou monitorização sistemática em locais públicos. Isto é importante considerar, uma vez que podem ser adquiridos dados pessoais, em circunstâncias onde os indivíduos não estejam cientes de tal. Pior ainda, por vezes pode ser impossível que os indivíduos se apercebam que estão a ser coletados dados sobre eles, em locais públicos.

    4. **Dados sensíveis ou de num carater pessoal elevado**, isto inclui algumas categorias em específico definidas no *Artigo 9* (por exemplo, informação sobre ideias políticas dos indivíduos), como também dados pessoais relativos a convicções criminosas ou ofenças definidas no *Artigo 10*.

    5. **Dados coletados numa grande escala**. O GDPR não define o que consituiu uma grande escala. No entanto, o *WP29* recomenda ter em conta os seguintes fatores, para determinar se um processamento é feito em grande escala. São os seguintes:

        1. O número de indivíduos, cujos dados estão a ser recolhidos, quer seja um número em específico, ou uma proporção de população relevante;
        2. O volume de dados e/ou o alcance dos diferentes tipos de dados, que estão a ser processados;
        3. A duração, ou permanência, atividade de processamento de dados.
        4. A extensão geográfica da atividade de processamento.

    6. Coincidir ou combinar *datasets*, por exemplo, de duas or mais operações de processamento, realizadas com propósitos diferentes e/ou por donos dos mesmos difrentes.

    7. **Dados relativos a indivíduos vulneráveis**. Este tipo de processamento é um fator a ter em conta, uma vez que existe um desequilíbrio evidente entre a pessoa recolhe os dados, e o indivíduo cujos dados foram coletados. O que significa que, a decisão dos indivíduos, sobre o acordo ou oposição ao processamento, pode ser afetada mediante a sua posição. Este tipo de sujeitos inclui crianças, operadores, elementos da população que se encontrem debilitados e em qualquer outro caso, onde seja verificada uma relação desiquilibrada entre os intervenientes.

    8. **Aplicaçâo tecnológica ou soluções organizacionais**, que combinam o uso de impressão digital e reconhecimento facial, para melhorar o acesso físico.

    9. **Quando o processamento em si** restringe o indivíduo de exercer um direito ou usufruir de um serviço ou contrato. O que inclui operações de processamento que envolvem permitir, modificar ou refutar o acesso ou acordo com um contrato, por parte do indivíduo.

    O DPIA deverá ser levado a cabo, sempre que pelo menos dois destes critérios, sejam encontrados.

2. Um exemplo de um projeto que envolve a utilização de dados de risco elevado, sujeito a um DPIA, seria:
Um centro comercial decide conduzir um estudo sobre os gostos e os interesses dos indivíduos que frequentam o estabelecimento, de modo a fornecer anúncios e publicidade, na infraestrutura, relevante para os consumidores. Para tal, era conduzida uma recolha sistemática de dados de navegação dos utilizadores que utilizassem a rede *wi-fi* pública do estabelecimento. Este projeto vai de encontro aos critérios de recolha sistemática de dados, provenientes de utilizadores que se encontram num local público, e em grande escala assumindo que este é estabelecimento bastante populado diariamente.

3.

### 1º passo: Identificar a necessidade para um DPIA

O objetivo deste projeto passa por tentar fornecer uma melhor experiência aos visitantes de um centro comercial, fornecendo-lhes conteúdo relevante, para uma maioria, com base nos seus gostos, beneficiando não só os consumidores, como os agentes lucrativos. Desta forma, seriam analisados os pacotes trocados na rede pública da infraestrutura, de modo a recolher informação sobre os gostos e preferências dos utilizadores.

Por isso, torna-se necessário conduzir um DPIA, uma vez que é realizada uma coleta em grande escala de dados, num local público, sem que os indivíduos estejam, por vezes, completamente inconscientes da situação.

### 2º passo: Descrever o processamento

Desta forma, a recolha e processamento dos dados seria feita através da captura dos pacotes que são trocados, na rede pública. Uma vez capturados, seria possível determinar o domínio requisitado e, consequentemente, o tipo de conteúdo acedido. De seguida, isto será armazenado, de maneira a que seja possível criar um *dataset* adequado, para que a sua análise seja conclusiva.

Contudo, uma vez que se trata de um projeto interno, ou seja, que não envolve nenhuma entidade exterior à organização da empresa, os dados recolhidos não serão partilhados com nenhum indivíduo do exterior.

Posto isto, é possível garantir que os dados recolhidos serão apenas relativos ao tipo de conteúdo acedido pelos consumidores, pelo que não terá qualquer tipo de incriminatório. Para além disso, serão recolhidas tantas informações, quanto possível, durante as horas mais movimentadas do estabelecimento e abrangirá todo o terreno coberto pela rede. O estudo irá prolongar-se ao longo do ano, estando a estratégia de *markting*, desenvolvida com base nos resultados obtidos com a análise, continuamente em funcionamento, durante esse período.

Também no tempo decorrido do estudo, o tipo de relacionamento entre os sujeitos e os condutores do projeto manter-se-á como vendedor e consumidor apenas. Todavia, o indivíduo consciente da coleta dos dados, poderá eventualmente requisitar o acesso aos dados respetivos à sua pessoa, e que os mesmos sejam apagados, se tal for o seu desejo. 

### 3º passo: Processo de consulta

As opinião de utilizadores informados será recolhida aquando da sua conexão, onde este irá ser interrogado se concorda com os termos de utilização impostos. Não serão envolvidas quaisquer entidades exteriores, neste processo.

### 4º passo: Considerar a necessidade e proporcionalidade

Apenas depois de recolhidos, processados e analisados os dados, será possível dizer se o procedimento realmente consegue cumprir o seu propósito. Contudo, caso isto não se verifique, serão analisados outros tipos de procedimento, para atingir os objetivos pretendidos.

## Pergunta P1.4

Depois de preenchidas todas as secções propostas pela ferramenta, colocou-se o PIA nesta diretoria. Este pode ser encontrado como *pia.pdf*.