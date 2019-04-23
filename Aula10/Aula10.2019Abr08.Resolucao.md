# Aula 10 - Resolução

## Pergunta P1.1

O que está exposto a um maior risco é o serviço de _homebanking_ visto que, pela fórmula do risco podemos destacar três fatores a ter em conta no cálculo do mesmo:

- O impacto de um ataque bem sucedido.
- O nível da ameaça.
- O grau de vulnerabilidade.

Um PC doméstico terá, com certeza, um grau de vulnerabilidade mais elevado do que o serviço de _homebanking_ mas, o serviço de _homebanking_ terá um nível de ameaça mais elevado do que o PC doméstico. Além disso, o impacto de um ataque bem sucedido num serviço de _homebanking_ é muito mais elevado do que o impacto de um ataque bem sucedido num PC doméstico.

Assim e , tendo em conta que, a fórmula do risco multiplica os 3 fatores acima mencionados, parece-nos óbvio que existe muito mais risco para um serviço de _homebanking_ do que existe para um PC doméstico.

## Pergunta P2.1

O regulamento europeu RGPD deve ser tido em conta, durante a fase de requisitos, uma vez que nesta fase são definidos os requisitos minímos de segurança, com base na legislação em vigor (por exemplo o RGPD) e as recomendações e normas internacionais, para o software a desenvolver.

## Pergunta P2.2

Os controlos de segurança consistem em salvaguardas ou medidas que permitem evitar, detetar, contrariar ou minimizar os riscos de segurança de informação ou outro tipo de recursos.

Os controlos criptográficos podem ser aplicados para conseguir determinados objetivos de segurança, garantindo propriedades essenciais de segurança tais como a confidencialidade, integridade e autenticidade.

No caso do projeto que o nosso grupo está a desenvolver, os controlos criptográficos utilizados passam por disponibilizar uma funcionalidade de assinatura digital, extensão de assinatura digital e validação da assinatura de documento através de uma _API_ já definida, o que permite garantir a integridade e autenticidade da informação bem como a propriedade de não-repúdio.

O controlo de segurança seguinte, consiste no processo de desenvolvimento e apoio do software. O seu objetivo principal passa por garantir que a segurança da informação seja desenhada e implementada, durante o ciclo de desenvolvimento do sistema, ou seja, que em qualquer estágio do ciclo de desenvolvimento de software, a segurança da informação seja discutida e levada em conta.

No caso do projeto que o nosso grupo está a desenvolver, estes controlos de segurança podem-se definir, por exemplo, numa fase de declaração da política de desenvolvimento, no facto de utilizarmos ou não um repositório privado e seguro onde se encontra o código resultado do desenvolvimento e, neste caso, utilizámos um repositório pertence a uma organização, mas que é público em relação aos outros grupos da mesma organização. Na fase de desenvolvimento, por exemplo, devem ser aplicadas diretrizes de desenvolvimento seguro, o que, neste momento ainda não é aplicado, visto que apenas concluímos a fase de _deploy_ da aplicação que fornece a _API_, tendo agora que desenvolver a aplicação que comunica com essa _API_. Em suma, estes controlos dizem respeito a todo um conjunto de boas práticas e processos que permitem garantir a segurança da informação ao longo de todo o ciclo de desenvolvimento do projeto, em situações como os exemplos referidos anteriormente.

## Pergunta P3.1

As 3 práticas de segurança que escolhemos, que também são utilizadas no desenvolvimento do projeto da UC de Engenharia de segurança são:

- **Education & Guidance**, visto que esta prática de segurança diz respeito ao treino que os desenvolvedores têm treino em questões de segurança e se as aplicam, o que se tem verificado no projeto, visto que tem sido desenvolvido de forma incremental, cuidada e com testes extensivos a novas funcionalidades adicionadas. O grau de maturidade calculado desta prática é de 2.6.
- **Security Testing**, visto que a ideia do grupo será testar que, a aplicação desenvolvida, além de implementar corretamente a parte funcional, seja capaz de lidar com erros de forma a que isso não influencie o comportamento da aplicação ou de outras aplicações do sistema, principalmente, no que diz respeito ao input de opções por parte do utilizador. O grau de maturidade calculado desta prática é de 2.33.
- **Issue Management**, visto que pelo que o grupo entendeu desta prática de segurança, ele refere-se à gestão das tarefas a realizar na aplicação, incluindo aquelas que dizem respeito à segurança da mesma, peloq eu se adequa ao que tem sido e irá continuar a ser feito no projeto da UC. O grau de maturidade calculado desta prática é de 1.82.

## Pergunta P3.2

Em relação às três práticas de segurança previamente identificadas, o objetivo, em termos de grau de maturidade, é:

- Para a prática **Education & Guidance** o grupo é da opinião que o grau de maturidade calculado já é aceitável.
- Para a prática **Security Testing**, o grupo pretende atingir um grau de maturidade de 2.5.
- Para a prática **Issue Management**, o grupo pretende atingir um grau de maturidade de 2.5.

## Pergunta P3.3

Notas: na práticas de **educaiton & guidance** o plano será manter o que está definido no cálculo do grau de maturidade atual.
nas outras será melhorar um outro ponto provavelmente dos que estão na interview.

