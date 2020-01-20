
Instalação
============


Então, como instalar Emmett no seu computador rapidamente? Há muitos modos de fazer, mas o modo mais prático é usar o virtualenv, então vamos olhá-lo primeiro. 

Você irá precisar do Python versão 3.7 ou superior para fazer o Emmett funcionar. 



virtualenv
----------

virtualenv é provavelmente o que você quer usar durante o desenvolvimento (development), e se você tiver acesso shell às suas máquinas de produção, você irá provavelmente querer usá-lo lá também. 

Qual o problema que virtualvenv resolve? Se você usa Python um pouco, você irá provavelmente querer usá-lo para outros projetos além de suas aplicações baseadas no Emmett. Entretanto, quanto mais projetos você tiver, é mais provável que você irá trabalhar com diferentes versões de Python em si, ou ao menos diferentes versões de bibliotecas Python. Vamos encarar: com frequência, bibliotecas quebram a compatibilidade para trás, e é improvável que qualquer aplicação séria terá zero dependências. Então o que você irá fazer se dois ou mais projetos têm dependências conflitantes? 

Virtualenv para o resgate! Virtualenv habilita múltiplas instalações paralelas de Python, uma para cada projeto. Ele não instala realmente  cópias separadas do Python, mas permite um modo esperto de manter diversos ambientes de projeto isolados. 

Vamos ver como virtualenv trabalha.   

#### virtualenv no Python 3

Você pode iniciar seu ambiente na pasta *.venv* usando:



```bash
$ mkdir -p meuprojeto
$ cd meuprojeto
$ python3 -m venv .venv
```

### Instalando o Emmet no virtualenv

Agora, se você quer trabalhar no projeto, você precisa apenas ativar o ambiente respectivo. No OS X  e Linux, você pode fazer o seguinte:



```bash
$ source .venv/bin/activate
```

Vocẽ deve agora estar usando seu virtualenv (perceba que o prompt do seu shell mudou para mostrar o ambiente ativo).

Agora você pode digitar o seguinte comando para instlar o Emmet no seu virtualenv:

```bash
$ pip install emmett
```

E agora você está pronto para ir. 

Você pode ler mais sobre o virtualenv em [seu site de documentação](https://docs.python.org/3/library/venv.html).

[pŕoximo](quickstart.md)

[índice](README.md)