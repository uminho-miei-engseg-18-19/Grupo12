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
Um centro comercial decide conduzir um estudo sobre os gostos e os interesses dos indivíduos que frequentam o estabelecimento, de modo a fornecer anúncios e publicidade, na infraestrutura, relevante para os consumidores. Para tal, era conduzida uma recolha sistemática de dados de navegação dos utilizadores que utilizassem a rede *wi-fi* pública do estabelecimento. Este projeto vai de encontro aos critérios de recolha sistemática de dados, provenientes de utilizadores que se encontram num local público, e em grande escala, assumindo que este é estabelecimento bastante populado diariamente.

3.

<center>

|              Submitting controller details              |        |
|:-------------------------------------------------------:|--------|
| Name of controller                                      | Merdas |
| Subject/title of DPO                                    | Merdas |
| Name of controller contact /DPO (delete as appropriate) | Merdas |

</center>

### 1º passo: Identificar a necessidade para um DPIA

Explain broadly what project aims to achieve and what type of processing it
involves. You may find it helpful to refer or link to other documents, such as a
project proposal. Summarise why you identified the need for a DPIA.

### 2º passo: Descrever o processamento

Describe the nature of the processing: how will you collect, use, store and
delete data? What is the source of the data? Will you be sharing data with anyone?
You might find it useful to refer to a flow diagram or other way of describing data
flows. What types of processing identified as likely high risk are involved?

Describe the scope of the processing: what is the nature of the data, and does
it include special category or criminal offence data? How much data will you be
collecting and using? How often? How long will you keep it? How many individuals
are affected? What geographical area does it cover?

Describe the context of the processing: what is the nature of your relationship
with the individuals? How much control will they have? Would they expect you to
use their data in this way? Do they include children or other vulnerable groups? Are
there prior concerns over this type of processing or security flaws? Is it novel in any
way? What is the current state of technology in this area? Are there any current
issues of public concern that you should factor in? Are you signed up to any
approved code of conduct or certification scheme (once any have been approved)?

Describe the context of the processing: what is the nature of your relationship
with the individuals? How much control will they have? Would they expect you to
use their data in this way? Do they include children or other vulnerable groups? Are
there prior concerns over this type of processing or security flaws? Is it novel in any
way? What is the current state of technology in this area? Are there any current
issues of public concern that you should factor in? Are you signed up to any
approved code of conduct or certification scheme (once any have been approved)?
Describe the purposes of the processing: what do you want to achieve? What is
the intended effect on individuals? What are the benefits of the processing – for
you, and more broadly?

### 3º passo: Processo de consulta

Consider how to consult with relevant stakeholders: describe when and how
you will seek individuals’ views – or justify why it’s not appropriate to do so. Who
else do you need to involve within your organisation? Do you need to ask your
processors to assist? Do you plan to consult information security experts, or any
other experts?

### 4º passo: Considerar a necessidade e proporcionalidade

Describe compliance and proportionality measures, in particular: what is
your lawful basis for processing? Does the processing actually achieve your
purpose? Is there another way to achieve the same outcome? How will you prevent
function creep? How will you ensure data quality and data minimisation? What
information will you give individuals? How will you help to support their rights?
What measures do you take to ensure processors comply? How do you safeguard
any international transfers?

### 5º passo: Identificar os riscos

### 6º passo: Identificar medidas que reduzem os riscos

### 7º passo: Sign off and record outcomes

## Pergunta P1.4

