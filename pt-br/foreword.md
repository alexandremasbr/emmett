
Préfácio
========


>- Nota do Tradutor: Trabalhei com web2py por 10 anos e compartilho muitas das percepções do autor. Também fiz a tradução do livro do web2py  para o Português. Os motivos que fizeram interessar pelo Emmett (antes weppy): 1) a evolução do web2py, o py4web, seguiu por um caminho de usar Vue.js, limitando as opções para quem trabalhava com o template antigo, e sua interface administrativa é um lixo. 2) O Emmett está buscando se tornar totalmente async, o que pode trazer resultados muito bons. 

Quando eu começei a programar aplicações web, a primeira grande decisão que enfrentei foi a escolha da linguagem de programação. 

Como um programador, não é um grande problema trabalhar com diversas linguagens, e mudar de uma linguagem para outra, não deve ser tão difícil, além de aprender um pouco de sintaxe; ao mesmo tempo todo mundo escolhe uma linguagem para usar como um *hábito diário*. Nós somos humanos, apesar de tudo. 

Eu queria uma linguagem dinâmica para escrever minhas aplicações, uma linguagem com uma sintaxe mais fácil do que PHP, e mais estruturada que o Javascript. Eu queria algo que me permitiria escrever aquela *pequena mágica* que cada programador faz atrás das cenas de uma maneira prática. E eu finalmente escolhi Python. Ruby estava na lista (e parece bastante popular para desenvolvimento web na época), mas achei sua sintaxe, em algumas situações, menos imediata (no sentido que precisa escrever código desnecessário para chegar onde se quer); além disso Python é um pouco mais sólido que Ruby, talvez até muito sólido. Penso que Python pode levar vantagem por uma comunidade mais dinâmica: apenas pense sobre o status da adoção do Python3. 

Eu realmente apreciei escrever código em python, e após ganhar alguma confiança, eu enfrentei a segunda "grande decisão": que framework usar para escrever minhas aplicações. Olhando o cenário do Python, eu (obviamente) começei olhando o *django*, o mais famos, mas logo eu descobri que eu não gostava dele. Ele não era tão amigo do usuário quanto eu esperava. Então eu encontrei *web2py* e eu amei desde a primeira linha do livro de documentação: era simples, cheio de recursos, e a curva de aprendizagem era muito mais rápida que o django.  

Mesmo assim, após alguns anos usando *web2py*, inspecionando profundamente o código e a lógica, e contribuindo, eu comecei a ter um sentimento. Uma necessidade cresceu em minha mente enquanto eu escrevia aplicações, para escrever as coisas de forma diferente. Me encontrei pensando "Por quê eu devo escrever isto *desse jeito? Isso não é legal ou prático em absoluto," e eu tive que encarar o problema que fazer o que eu queria envolvia redesenhar o framework inteiro. 

Com este sentimento ranzinza em minha mente, comecei olhando em volta e encontrei um monte de syntax e lógica em *Flask* que eram a resposta para o que eu estava procurando. Infelizmente, ao mesmo tempo, *Flask* não tinha muitos dos recursos que estava acostumado a ter abrindo a caixa com *web2py*, e nem mesmo usando extensões poderia ser o suficiente para cobrir aquilo tudo. 

Eu naturalmente cheguei à conclusão que eu estava *naquele ponto* da minha vida de código onde eu precisava de uma *ferramenta de design personalizado*.

Porquê não? 
--------

> – Oi cara. o que você está fazendo?   
> – *escrevendo um novo framework python*   
> – Uai! Porque você faz isso?   
> – *...Porquê não?*

Essa foi minha resposta quando um amigo meu perguntou as razões por trás da minha intenção de desenvolver um novo framework. Esta era uma questão legítima: Há tantos frameworks no cenário. É realmente um bom movimento construir uma nova ferramenta ao invés de escolhar uma das disponíveis?

Eu gostaria de responder esta dúvida com uma definição de *ferramenta* que eu realmente amo: 


> **ferramenta:** *alguma coisa* que pretende fazer uma tarefa mais fácil.

Então um framework, que é uma ferramenta, tem que deixar você escrever sua aplicação **de forma mais fácil** que sem ele. Agora, eu encontrei muitos frameworks, e estou certo que você pode encontrá-los também - onde você tem que lidar com aprender *bastante* de como "como fazer isto" com o framework primeiro ao invés de focar na aplicação. 

Este é o primeiro princípio sobre o qual eu baseei o *Emmett*:   **É fácil para usar e aprender, então você pode focar no *seu* produto.** 

Outro princípio chave do *Emmett* é a **preservação do seu  controle** sobre o fluxo. O que eu quero dizer? Há vários frameworks que fazem muita mágica por trás das cenas. Eu sei que isso pode parecer esquisito porque eu acabei de falar sobre simplicidade, mas se você pensar sobre isso, você vai descobrir que um framework que é simples para usar não é necessáriamente aquele que esconde muito do seu fluxo. 


Como desenvolvedores, nós temos que admitir que quando nós usamos frameworks ou libraries (bibliotecas) para o nosso projeto, muitas vezes é difícil fazer alguma coisa fora do seu esquema pronto. Eu posso pensar sobre vários frameworks - mesmo o famoso *Ruby on Rails* - que 
de tempos em tempos, forçam você a usar um monte de formalismos mesmo quando  isto não é realmente necessário. Você se encontra escrevendo código seguindo regras desnecessárias que você não gosta. 

> NT: Eu concordo com autor, pois deixei de usar muitos frameworks pelo modo de fazer as coisas e serem muito prolixos. 

Em outras palavras: Eu gosto de mágica também, mas **não é melhor quando você realmente *controla* a mágica?**

Com esses princípios em mente, eu tentei construi uma ferramenta completa, alguma coisa para fazer sua tarefa mais fácil, com um conjunto rico de recursos na caixa. O resultado da minha receita é um framework que tem uma sintaxe fácil, similar ao *Flask*, mas que também inclui alguns dos amados recursos do *web2py*.

Eu espero que você goste. 


Agradecimentos
---------------
Eu gostaria de agradecer:


* Todos os  **contribuidores do Emmett**
* **Guido Van Rossum**, pela linguagem Python
* **Massimo Di Pierro** e os  **desenvolvidores do web2py**, pelo que eu aprendi deles e pelo seu framework no qual eu baseei Emmett
* **Armin Ronacher**, que realmente me inspirou com o framework Flask 
* **Marco Stagni**, **Michael Genesini** e **Filippo Zanella** por seus conselhos e suporte contínuo 

[próximo](instalattion.md)

[índice](README.md)
