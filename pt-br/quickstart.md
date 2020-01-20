Começando
===============

Pronto para começar com Emmett? Este guia apresenta uma boa introdução ao framework. 


Uma aplicação 'Olá Mundo!'
----------------------------
Como seria um aplicativo mínimo em Emmett?


```python
from emmett import App

app = App(__name__)

@app.route("/")
async def hello():
    return "Olá mundo!"
```

Aqui está. Salve-o como * hello.py * e execute-o com Emmett:

```bash
> emmett -a hello.py develop
App running on 127.0.0.1:8000
```
Agora, se você for para [http://127.0.0.1:8000](https://127.0.0.1:8000), deverá ver sua mensagem
'Olá Mundo!' mensagem.

Routing (Roteamento)
-------
Como você viu no exemplo 'Olá mundo!' nós *roteamos* a função `hello()`. O que isso significa?

Na verdade, é bastante simples: o decorador de rota do objeto de aplicativo é usado para
definir o roteamento do seu aplicativo.

>NT: Route(rota) no desenvolvimento web é o mapeamento do caminho da URL (meusite/pagina1) até o código que irá fazer o tratamento da solicitação e preparar a resposta. Routing é execução da rota. 

> – Espere, você quer dizer que não há necessidade de uma tabela de roteamento?   
> – *Não.*   
> – E como eu devo definir variáveis da URL, métodos HTTP, etc.?   
> – *Apenas use o decorador de rota e seus parametros.*   

De fato, `route()` aceita parametros diferentes. Mas vamos em ordem, começando com regras de váriáveis para rotear suas funcões

### Regras de variáveis 

Para adicionar partes variáveis a um URL, você pode marcar essas seções especiais como
`<type: variable_name>` e as variáveis serão passadas como argumentos de palavra-chave para suas
funções. Vamos ver alguns exemplos:



```python
@app.route('/user/<str:username>')
async def user(username):
    return "Olá %s" % username

@app.route('/double/<int:number>')
async def double(number):
    return "%d * 2 = %d" % (number, number*2)
```

É bem simples, não é? Que tipos de variáveis você pode usar? Aqui está a lista completa:

| tipo | especificação
| --- | --- |
| int | aceita números inteiros |
| float | aceita flutuadores em notação de ponto |
| str | aceita strings |
| date | aceita seqüências de datas no formato * AAAA-MM-DD * |
| alpha | aceita cadeias contendo apenas letras|
| any | aceita qualquer caminho (também com barras) |


Então, basicamente, se tentarmos abrir a URL para a função `double` do último exemplo
com uma string, como '/double/foo', ela não corresponderá e Emmett retornará um erro 404.

> - Tudo bem. Mas, e se eu quiser um argumento condicional para minha função?

Basta escrever a URL colocando a parte condicional entre parênteses e um ponto de interrogação
no fim:


```python
@app.route("/profile(/<int:user_id>)?")
async def profile(user_id):
    if user_id:
        # pega o usuário solicitado
    else:
        # tenta? carregar o perfil usuário logado
```

> NT: user = usuario e profile = perfil. Mantive o original porque em muitos casos a prática é manter o nome das funções e estruturas de dados em inglês. 

Como você pensou, quando argumentos condicionais não são fornecidos no URL solicitado, seus parâmetros da função serão "None".

Agora, é hora de ver o parâmetro `methods` de `route()`


### Métodos HTTP (methods)

O HTTP tem métodos diferentes para acessar URLs. Por padrão, uma rota responde apenas a
Solicitações GET e POST, mas isso pode ser alterado fornecendo o argumento de métodos para o
o decorador `route ()`. Por exemplo:

```python
@app.route("/onlyget", methods="get")
async def f():
    # code

@app.route("/post", methods=["post", "delete"])
async def g():
    # code
```

Se você não tem idéia do que é um método HTTP - não se preocupe -
[A Wikipedia possui boas informações] (http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods) sobre eles.

> - OK, entendi. O que mais posso fazer com a rota?

Como esta é uma * visão geral rápida * de Emmett, você deve verificar o
[Capítulo de roteamento](routing.md) da documentação para obter a lista completa dos parâmetros
aceito pelo decorador `route()`.

Vamos ver como criar URLs com nossas regras de roteamento.


### Construindo URLs


Emmett provides a useful method to create URLs.

```python
from emmett import App, url

app = App(__name__)

@app.route("/")
async def index():
    # code

@app.route("/anotherurl")
async def g():
    #code

@app.route("/find/<str:a>/<str:b>")
async def f(a, b):
    # code

@app.route("/post/<int:id>/edit")
async def edit(id):
    # code

a = url('index')
b = url('g', params={'u': 2})
c = url('f', ['foo', 'bar'])
d = url('edit', 123)
```
As URLs acima `a`,` b`, `c` e` d` serão respectivamente convertidos em:

- /
- /anotherurl?u=2
- /find/foo/bar
- /post/123/edit

o que é bastante útil em vez de lembrar de todas as regras e escrever manualmente
os links.


#### Arquivos estáticos (Static files)

Muitas vezes, você precisará vincular conteúdo estático (imagens, CSS, JavaScript) ao seu
inscrição. Você pode criar uma pasta chamada *static* no seu package ou ao lado do seu
módulo e estará disponível em */static* na aplicação.

Para gerar URLs para arquivos estáticos, use o primeiro argumento especial `static`:


```python
url('static', 'js/common.js')
```
que apontará para o arquivo em *static/js/common.js *

> - Mas talvez eu possa escrever diretamente */static/js/common.js* em vez de usar
a função `url ()`?

Obviamente, você pode. No entanto, o Emmett fornece alguns recursos úteis para arquivos estáticos
URLs, como idiomas e controle de versão, que são aplicados automaticamente com base no seu
configuração de aplicativo. Você pode encontrar mais informações no
[Capítulo de roteamento] (routing.md) da documentação.


Renderizando a saída
--------------------
Agora que você descobriu como o núcleo de Emmett funciona, vamos descobrir como renderizar nosso
conteúdo. Vamos ver como gerar uma resposta HTML com um modelo e como gerar uma resposta JSON.

### O template engine
Emmett fornece o templating engine *Renoir*, o que significa que você pode usar o cógido Python
diretamente em seus arquivos HTML. Vamos ver com um exemplo.
Podemos fazer uma nova aplicação com esta estrutura:

>NT - o Web2py usa o mesmo template engine 


```
/myapp.py
/templates
    echo.html
```

com  *myapp.py* ficando assim:

```python
from emmett import App
app = App(__name__)

@app.route("/<str:msg>")
async def echo(msg):
    return dict(message=msg)
```

e *echo.html*:

```html
<html>
  <body>
    {{=message}}
  </body>
</html>
```

> - Então, a mensagem que eu coloquei no modelo é o valor retornado da minha função `echo ()`?
> - * você pegou! *

O dicionário retornado por suas funções é o * contexto * do modelo, no qual
você pode inserir os valores definidos no código Python. Além disso, já que tudo o que você
escreve dentro de colchetes `{{}}` é avaliado como código Python normal, você pode facilmente
gerar HTML com condições e ciclos:

```html
<div class="container">
{{for post in posts:}}
  <div class="post">{{=post.text}}</div>
{{pass}}
</div>
{{if user_logged_in:}}
<div class="cp">User cp</div>
{{pass}}
```

Como você pode ver a única diferença entre o modelo Renoir e um código Python puro
é que você deve escrever `pass 'após as instruções para dizer a Renoir onde o Python
termina de bloco - normalmente temos recuo no Python, mas não podemos usá-lo no HTML.

O sistema de modelos tem muitos outros recursos: explore-os no
[Capítulo Templates] (./templates.md) da documentação.

### Outras opções de renderização
Muitas vezes, você precisará renderizar suas funções em formatos diferentes de
HTML, como JSON.

Emmett pode ajudá-lo com o decorador * service *


```python
from emmett import App
from emmett.tools import service

app = App(__name__)

@app.route("/json")
@service.json
async def f():
    l = [1, 2, {'foo': 'bar'}]
    return dict(status="OK", data=l)
```

A saída será um objeto JSON com o conteúdo convertido do seu dicionário Python.

O módulo `service` possui outros auxiliares, como o formato * XML *: vá além no
[Capítulo Serviços] (./ serviços) da documentação.


Lidar com requests (solicitações)
---------------------

Agora vamos tentar ir a algum lugar mais profundo na lógica central de Emmett.

> - Como meu aplicativo pode reagir às solicitações do cliente?
> - * você pode começar com o objeto `request` *

### O objeto request
Você pode acessar o objeto `request` do Emmett usando um import:


```python
from emmett import request
```

Ele contém informações úteis sobre a solicitação de processamento atual, vamos ver
alguns deles:

| atributo | descrição
| --- | --- |
| scheme | pode ser * http * ou * https * |
| method | o método HTTP de solicitação |
| now | um objeto de data e hora do pêndulo criado com solicitação |
| query_params | um objeto que contém parâmetros de URL |

Vamos nos concentrar no objeto `request.query_params` e entendê-lo com um exemplo:


```python
from emmett import App, request

app = App(__name__)

@app.route("/post/<int:id>")
async def post(id):
    editor = request.params.editor
    if editor == "markdown":
        # code
    elif editor == "html":
        # code
    #..
```

Agora, quando um cliente chama a URL */post/123?editor=markdown*, o parâmetro `editor`
será mapeado para `request.query_params` e podemos acessar seu valor simplesmente chamando
o nome do parâmetro como um atributo.

> - Espere, o que acontece se o cliente chamar */post/123* e meu aplicativo tentar acessar * request.params.editor *, que não está no URL?

Simples! O atributo será "Nenhum", portanto é totalmente seguro chamá-lo. Não vai
crie qualquer exceção.

Mais informações sobre o objeto `request` podem ser encontradas no
[Capítulo request](request.md) da documentação.


### Pipeline: fazendo operações com requests

> NT A tradução literal de pipeline é tubulação, mas vamos deixar o termo em inglês, porque o sentido é figurado mesmo. Pipe é tubo. 

> - E se eu quiser fazer algo antes e depois da solicitação?
> - * Você pode usar o pipeline. *

Emmett usa o pipeline para executar operações antes e depois de executar as funções
definido com suas regras de roteamento.

O pipeline é uma lista de * pipes *, objetos da classe `Pipe`.
Vamos ver como criar um deles:


```python
from emmett import Pipe

class MyPipe(Pipe):
    async def open(self):
        # code
    async def close(self):
        # code
    async def on_pipe_success(self):
        # code
    async def on_pipe_failure(self):
        # code
```

Como você pode ver, o `Pipe` fornece métodos para executar seu código antes que a solicitação seja processada por sua função (com o método `open`) e depois que sua função foi executada,
fornecendo métodos diferentes, dependendo do que aconteceu em sua função: se ocorrer uma exceção, Emmett chamará o método `on_pipe_failure`, caso contrário, o método `on_pipe_success`. O método `close` é ** sempre ** chamado após cada solicitação ter sido processada, * após * a resposta foi criada e * antes * de enviá-la ao cliente.

Para registrar seu pipe em uma função, basta escrever:


```python
@app.route("/url", pipeline=[MyPipe()])
async def f():
    #code
```

E se você precisar registrar seu pipe em todas as funções de seu aplicativo, poderá omitir
o pipe do decorador `route ()` escrevendo:


```python
app.pipeline = [MyPipe()]
```

Emmett também fornece um pip `Injector`, projetado para adicionar métodos de ajuda a
os modelos. Explore o [capítulo Pipeline] (request.md#pipeline) da documentação
para mais informações.

### Redirects (Redirecionamentos) e erros

Tomando novamente o exemplo dado para `request.query_params`, podemos adicionar um redirecionamento no parâmetro de URL ausente:


```python
from emmett import redirect, url

@app.route("/post/<int:id>")
async def post(id):
    editor = request.query_params.editor
    if editor == "markdown":
        # code
    elif editor == "html":
        # code
    else:
        redirect(url('post', id, params={'editor': 'markdown'}))
```

o que significa que, quando o var do `editor` está ausente, forçamos o usuário a
remarcação um.

Outra maneira seria retornar um erro 404 (page not found - página não encontrada):


```python
from emmett import abort

@app.on_error(404)
async def not_found():
    #code

@app.route("/post/<int:id>")
async def post(id):
    editor = request.params.editor
    if editor == "markdown":
        # code
    elif editor == "html":
        # code
    else:
        abort(404)
```

Como você pode ver, os aplicativos Emmett podem lidar com ações específicas em erros de HTTP.
Para mais informações, consulte o [Capítulo Tratamento de erros] (./request.md#errors_and_redirects) da documentação.

Sessions(Sessões)
--------
Um recurso essencial para um aplicativo da web é a capacidade de armazenar
informações sobre o cliente entre várias solicitações. Assim, Emmett fornece
outro objeto além do `request`, chamado` session`.

O conteúdo da sessão pode ser armazenado de várias maneiras, como o uso de arquivo ou redis. Nesse início rápido, veremos como usar a `session` e armazenar seu conteúdo diretamente nos cookies do cliente.

Vamos usar a classe `SessionManager` fornecida por Emmett e escrever uma
rota simples que interage com a sessão:

```python
from emmett import App, session
from emmett.sessions import SessionManager

app = App(__name__)
app.pipeline = [SessionManager.cookies('minhachavesupersecreta-me-troque')]

@app.route("/")
async def count():
    session.counter = (session.counter or 0) + 1
    return "Você visitou %d vezes" % session.counter
```

O código acima é bastante simples: o aplicativo incrementa o contador toda vez que o usuário
visita a página e retorna esse número ao usuário. Basicamente, você pode armazenar um valor para
a sessão do usuário e recupere-a sempre que a sessão for mantida.

> - e se eu tentar acessar um atributo não existente na sessão?
> - * o mesmo que `request.query_params`: o atributo será` None` e você não precisará capturar nenhuma exceção *

Mais informações sobre o armazenamento de sistemas estão disponíveis no
[Capítulo da sessão] (./sessions.md) da documentação.

Criando formulários
--------------
Você provavelmente precisará criar formulários para o seu aplicativo da Web frequentemente. Emmett fornece a classe `Form` para ajudá-lo a fazer isso.

Vamos ver como usá-lo com um exemplo:


```python
from emmett import Field, Form

# create a form
@app.route('/form')
async def a():
    simple_form = await Form({
        'name': Field(),
        'number': Field.int(),
        'type': Field(
            validation={'in': ['type1', 'type2']}
        )
    })
    if simple_form.accepted:
        #do something
    return dict(form=simple_form)
```

Como você pode ver, a classe `Form` aceita uma lista de campos para a entrada, e você
pode adicionar validação aos seus campos. A classe `Form` vem com muitas opções. Por exemplo, você pode definir um método `onvalidation` para executar validação adicional, além dos requisitos dos campos.

Você também pode personalizar a renderização e o estilo do formulário ou gerar formulários a partir de tabelas de banco de dados criadas com o [ORM] (/orm.md) integrado. Confira o [capítulo Forms] (./forms.md) da documentação e as [Extensão BS3?] (#) que adiciona o estilo do Bootstrap 3 aos seus formulários.

Línguas e internacionalização (i18n)
----------------------------------

O Emmett fornece o * Severus * como seu mecanismo de internacionalização integrado, o que ajuda você a escrever aplicativos com suporte a diferentes idiomas.
Mas como isso funciona?


```python
from emmett import App, T
app = App(__name__)

@app.route("/")
async def index():
    hello = T('Hello, my dear!')
    return dict(hello=hello)
```

Como você pode ver, Emmett expõe um tradutor de idiomas com o objeto `T`. Então, o que você deve fazer com os idiomas? Você pode escrever sua tradução em um arquivo * json * ou * yaml * dentro da pasta * languages * do aplicativo, nomeando-o para o código do idioma que deseja usar. Isso é "pt" para portugues e "pt-br", então nosso arquivo *pt-br.json * será semelhante a:


```json
{
    "Hello, my dear!": "Olá, meu amigo!"
}
```

A mensagem "olá" será traduzida quando o usuário solicitar o idioma português brasileiro.

Nas configurações padrão, o idioma solicitado pelo usuário é determinado pelo campo "Accept-Language" no cabeçalho HTTP, mas o mecanismo de tradução tem outra maneira de se comportar, na verdade, se colocarmos essa linha no exemplo anterior:

```python
app.language_force_on_url = True
```

Emmett usa a URL para determinar o idioma em vez do cabeçalho HTTP "Accept-Language". Isso significa que o Emmett adicionará automaticamente o suporte ao idioma nas suas regras de roteamento.

Para saber mais sobre idiomas e explorar os recursos do tradutor, leia o
documentação disponível no [capítulo Idiomas] (./languages.md).

Continue
--------

Parabéns! Você leu tudo o que precisa para executar um simples, mas funcional
Aplicação Emmett. Use este * guia de início rápido * como seu manual e consulte a
[documentação completa] (./README.md) para todos os aspectos detalhados que você possa encontrar.



[próximo](tutorial.md)

[índice](README.md)