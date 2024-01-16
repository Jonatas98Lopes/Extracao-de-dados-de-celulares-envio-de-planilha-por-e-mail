# Automação de planilhas

***

## Descrição:

Neste projeto, nós vamos extrair os dados de marca e preço de celulares de um site. Feito isso, nós salvá-los numa planilha e enviá-la por e-mail ao usuário.


Esse é o [site](https://telefonesimportados.netlify.app/) de onde vamos extrair os dados.
***

## Requisitos:

* Ter o Python 3 instalado no seu computador. 

* Ter habilitado a opção  **Add to Path** na instalação do Python

* Possuir o navegador **Google Chrome** instalado.

* Possuir uma **Gmail** para envio de e-mails como saída do programa.

* Possuir um arquivo chamado **token_email.txt** no mesmo diretório da aplicação, contendo o endereço de e-mail rementente que enviará o e-mail de saída ao usuário de destino e o token de acesso(MELHOR EXPLICADO ABAIXO).

* Para visualização da planilha gerada, você deve ter um programa visualizador de planilhas como Excel ou LibreOffice. 

***


## Como rodar o projeto?

### Obtendo o token de acesso:

Como especificado nos requisitos, você precisa de uma conta Gmail para poder enviar os e-mail, isso é um dos requisitos da aplicação. Por isso, a primeira coisa que você vai precisar é obter o seu token de acesso para aplicações poderem acessar o seu Gmail. Normalmente, você acessa o seu e-mail através de usuário e senha, mas como vamos precisar que o **programa** acesse o seu e-mail, ao invés de usar a sua senha padrão de usuário, precisamos de um token de acesso para aplicações. Siga os passoa abaixo para obter o seu token de acesso:
<details>
  <summary><strong>Como obter o seu token de acesso no Gmail:</strong></summary>
  
  - Esteja logado no seu Gmail e na página Home.
  - Clique na sua foto de perfil à direita superior.
  - Depois, clique em "Manage your Google Account"  ou“Gerenciar sua conta do Google”.
  - Quando a página carregar, clique em "Security" ou “Segurança” à esquerda.
  - Role a página para baixo e clique em "2-Step Verification" ou “Verificação em duas etapas”.
  - Quando a página carregar, clique em  “Get started” ou “Iniciar”. -> **PODE NÃO APARECER ESSA PÁGINA**
  - Sua senha de usuário será requisitada novamente. Insira e clique para continuar.
  - Role até o final da página e clique em 'Senha de App' ou 'App password'.
  - Defina um nome para o seu app. Ex: 'primeira aplicacao' e clique em 'Gerar'.
  - Uma tela aparecerá com uma sequência de letras aleatórioas. Esse é o seu token.
  - Salve-o em um local seguro, pois este é o único momento que você o verá.
  - Feito isso, clique em 'Concluído'.
</details>

***

### Criando ambiente virtual com Python:

Assim que clonar este código, sugiro que você crie um arquivo chamado: **token_email.txt()**(EXATAMENTE DESSE JEITO) no diretório da aplicação. Dentro dele, você deve inserir o seu gmail na **PRIMEIRA LINHA** do arquivo e o token de acesso, na **SEGUNDA LINHA DO ARQUIVO**. 
Exemplo:
```
seuemail@gmail.com <- SEU GMAIL
ijfirjewfief <- SEU TOKEN DE ACESSO
```
***

Feito isso, crie um ambiente virtual isolando os arquivos que estão no seu computador do diretório do projeto.


#### Passo a passo

1. Clone o projeto.

2. Estando dentro da pasta do projeto, abra o seu terminal.

CASO ESTEJA NO **WINDOWS**, RODE O COMANDO ABAIXO E AGUARDE A CRIAÇÃO:

```
python -m venv nome_do_ambiente_virtual
```

**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

CASO ESTEJA NO LINUX OU NO MAC, RODE O COMANDO ABAIXO E A AGUARDE A CRIAÇÃO:

```
python3 -m venv nome_do_ambiente_virtual
```
**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

3. Ative o ambiente virtual através do seu terminal:

NO CASO DO **WINDOWS**, RODE:
```
nome_do_ambiente_virtual\Scripts\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

NO CASO DO **LINUX** OU **MAC**, RODE:

```
source nome_do_ambiente_virtual\bin\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

***

### Instalando bibliotecas necessárias:


Feito isso, vamos instalar as bibliotecas necessárias através do arquivo requirements.txt:
No **Windows**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip install -r requirements.txt
```
No **Linux** ou **MAC**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip3 install -r requirements.txt
```
Pronto! Você está apto para rodar o projeto.

***

### Gerando executável:

**OBS: PARA GERAR O EXECUTÁVEL VOCÊ PRECISA BAIXAR O CONTEÚDO DO ARQUIVO requirements.txt. COMO FAZER ISSO FOI EXPLICADO ACIMA.**

Caso você queira um executável do projeto. Você deve ter executado as etapas anteriores. - ATÉ A PARTE DE INSTALAR AS BIBLIOTECAS DO ARQUIVO requirements.txt.

Feito isso, você deve estar com o seu ambiente virtual ativado e abrir o seu terminal na pasta raiz do projeto.

Estando lá, digite o seguinte comando

NO **WINDOWS**:
```
python setup.py build
```

NO **LINUX** OU NO **MAC**:
```
python3 setup.py build
```

Uma pasta **build**, com um arquivo **app.exe** deve ser gerada.
O ARQUIVO **app.exe** será o seu executável.

***

## Arquivos:

* **app.py** - Arquivo principal que contém a **execução** da criação da planilha, extração de dados do site e o envio de e-mail.
* **acesso_site.py** - Arquivo que contém as **funções** que abrem o navegador, criam uma nova planilha e extraem os dados do site. 
* **enviar_email.py** - Contém as funções que são necessários para criar o e-mail, anexar uma nova planilha e enviar o e-mail. 
* **inicializar.py** - Contém as configurações de abertura do navegador Chrome.
* **interface.py** - Contém a lógica da interface gráfica usada para interagir com o usuário.
* **icone.ico** - Ícone que é utilizado como imagem do executável.
* **icon_atribuicao.html** - Referência para o criador do ícone usado.
* **setup.py** - Arquivo contém a lógica para geração de executável.
* **requirements.txt** - Arquivo que contém as bibliotecas necessárias para rodar o programa.