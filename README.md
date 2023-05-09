# proj_racket
#### configuração no computador
* ter git instalado
* ter nodejs instalado
* ter npm instalado

##### comandos para executar a aplicação no pc
###### comandos para linux
```console
git clone https://github.com/marcosfnsc/proj_racket.git &&
cd proj_racket/racket_ui &&
npm install
```

#### configuração no celular
* ter  o aplicativo [termux](https://f-droid.org/en/packages/com.termux/) instalado
* ter  o aplicativo [termux-api](https://f-droid.org/en/packages/com.termux.api/) instalado


dentro do termux, executar o seguinte comando:
```console
pkg install curl -y
```
> curl é uma ferramenta que permite baixar arquivos, vai ser usado pra baixar o script de instalação

##### copie e cole o comando abaixo no termux e aperte a tecla enter
```console
curl https://raw.githubusercontent.com/marcosfnsc/proj_racket/main/setup_termux.sh?token=GHSAT0AAAAAABVYGR6EG4YSVZMGOPEVG43YZC2Z5KA | bash
```
> quando o script terminar de configurar, aparecerá a mensagem `configuração concluida`
