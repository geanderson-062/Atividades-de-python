# README: Exibindo a Data e Hora Atual com PyScript em HTML

Este documento oferece instruções e informações sobre um script HTML que utiliza PyScript para exibir a data e hora atual. PyScript é uma estrutura que permite executar Python no navegador da web.

## Descrição

O script HTML apresentado usa PyScript, uma tecnologia que permite incorporar e executar código Python diretamente em uma página HTML. Neste exemplo específico, o script exibe a data e hora atual, atualizando a cada 5 segundos.

## Estrutura do Código

O código HTML consiste em várias partes:

- **Doctype e Língua**: Define o documento como HTML e especifica o idioma como inglês.
- **Meta Tags**: Inclui a codificação de caracteres, a configuração da viewport para responsividade e uma meta tag para atualizar a página a cada 5 segundos.
- **Título**: Define o título da página como "PyScript".
- **Link para PyScript CSS**: Inclui o arquivo CSS para PyScript.
- **Script PyScript**: Importa o script PyScript, que é necessário para executar Python no HTML.
- **Corpo e PyScript**: Contém uma seção `pyscript` onde o código Python é escrito.

O código Python dentro da tag `<py-script>` faz o seguinte:

- Importa o módulo `datetime`.
- Obtém a data e hora atuais.
- Exibe a data e hora no formato `MM/DD/YYYY, HH:MM:SS`.

## Pré-requisitos

Não há pré-requisitos especiais para executar este script, além de um navegador da web moderno que suporte JavaScript, pois PyScript é executado inteiramente no navegador.

## Executando o Script

1. Copie o código HTML fornecido para um arquivo com a extensão `.html`.
2. Abra o arquivo em um navegador da web.
3. A data e hora atuais serão exibidas na página.
4. A página será atualizada automaticamente a cada 5 segundos, mostrando a nova hora.

## Código

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta http-equiv="refresh" content="5" />
    <title>PyScript</title>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
  </head>
  <body>
    <section class="pyscript">
      <py-script>
        from datetime import datetime now = datetime.now()
        display(now.strftime("%m/%d/%Y, %H:%M:%S"))
      </py-script>
    </section>
  </body>
</html>
```

## Conclusão

Este script é uma demonstração básica do uso de PyScript para integrar Python em HTML. Ele oferece uma maneira simples e eficaz de exibir informações atualizadas, como a data e hora atuais, em uma página web.
