# Como enviar mensagens com a api do WhatsApp
___


1. Acesse [facebook developer](https://developers.facebook.com/)
2. Faça login
3. Crie uma conta de desenvolvedor Facebook

Voce sera redireconado para uma pagina onde voce vai criar um aplicativo
1. Dê o nome do seu aplicativo
2. Selecione o caso de uso **Outro**
3. Selecione o tipo de aplicativo **Empresa**
4. Clique em **Criar Aplicativo**

Voce sera redireconado para uma nova pagina onde voce vai configurar o aplicativo

1. Adicione o WhatsApp a sua aplicação clicando em configurar
2. Vai ser necessario configurar um portfólio empresarial, clique em **Continuar**

Voce sera redireconado para uma nova pagina onde voce vai configurar o portfólio empresarial

1. Clique em **Criar uma conta**
2. Preencha os dados ***O email tem que ser diferente da conta de desenvolvedor***
3. Clique em **enviar**

Voce sera redireconado para a pagina de configurar o aplicativo

1. Clique em **Continuar**
2. Clique em **Começar a usar a API**

Voce sera redireconado para a pagina de configurar a API do WhatsApp

1. clique no numero de telefone que vai enviar a mensagem
2. Clique em adicionar telefone

Configure o numero de WhatsApp ***Ele nao pode estar vinculado a nenhuma conta de whatsapp,<br> se ja estiver, delete a conta***

Com isso voce vai conseguir uma mensagem pela api do whatsapp
basta pegar gerar o token, colocar na .env e criar um template, pois o padrao de teste nao é possivel de enviar

***Como criar modelos***

Acesse [Whatsapp Manager](https://business.facebook.com/latest/whatsapp_manager/message_templates)

Caso não esteja no numero cadastrado, no canto superior direitro mude para seu numero do Whatsapp Business

- Clique em criar modelo

- Escolha o tipo de mensagem
- clique em avançar
- para colcar uma variavel no seu modelo de mensagem add ```{{``` que ele ja autocomplementa 
- apos configurar sua mensagem clique em enviar para analise e é so esperar
