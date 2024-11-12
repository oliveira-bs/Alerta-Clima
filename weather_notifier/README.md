# Saiba mais

## Fluxo de Funcionamento do Projeto

1. **Consulta à API de Clima (HG Brasil)**:
   - O projeto faz requisições à **API da HG Brasil**, que fornece dados meteorológicos de várias cidades, incluindo as principais cidades do Vale do Café e o Rio de Janeiro.
   - A API retorna informações detalhadas sobre o clima, como a descrição do tempo (ensolarado, nublado, etc.), temperatura, sensação térmica, umidade, e outros parâmetros.

2. **Processamento dos Dados Climáticos**:
   - Os dados recebidos pela API são processados e formatados para serem entendidos facilmente pelos usuários. O projeto busca consolidar a informação relevante para cada cidade solicitada.
   - As informações são preparadas de maneira que facilite a leitura em e-mails, incluindo o nome da cidade, descrição do clima e a temperatura atual.

3. **Envio de Notificações por E-mail**:
   - O sistema envia e-mails automaticamente para os destinatários configurados.
   - O e-mail contém as previsões climáticas personalizadas de acordo com a localidade do destinatário (se ele está em uma das cidades do Vale do Café relacionadas ou no Rio de Janeiro).
   - O conteúdo do e-mail inclui informações sobre o clima atual e uma breve previsão para o dia ou próximo período.

4. **Automação e Personalização**:
   - O sistema pode ser configurado para enviar notificações diariamente ou em intervalos personalizados (por exemplo, apenas nos dias com previsão de clima adverso ou para horários específicos do dia).
   - Além disso, ele pode ser facilmente escalado para incluir mais cidades no futuro ou modificar a frequência das notificações conforme a necessidade dos usuários.

## Cidades do Vale do Café

As principais cidades que pertencem ao Vale do café no Rio de Janeiro são:

- Vassouras – Considerada a "Capital do Café", com várias fazendas históricas.
- Barra do Piraí – Importante cidade histórica com várias fazendas e um rico patrimônio cultural.
- Valença – Conhecida pelas fazendas coloniais e pelo turismo rural.
- Rio das Flores – Cidade tranquila, com muitas fazendas antigas preservadas.
- Paraíba do Sul – Local de importância histórica e também conhecida por suas fazendas.
- Miguel Pereira – Destino de turismo rural e ecológico.
- Paty dos Alferes – Famosa pelo Festival do Tomate e pelas fazendas históricas.

## Componentes do Sistema

1. **Requisição de Dados Climáticos**:
   - A aplicação faz uma requisição à API da HG Brasil usando uma chave de API e a cidade desejada. O projeto é configurado para acessar múltiplas cidades, sendo possível personalizar as cidades do Vale do Café e a cidade do Rio de Janeiro.
   
2. **Processamento e Formatação dos Dados**:
   - O módulo que consome a API de clima recebe os dados e os formata para criar uma mensagem compreensível, por exemplo: *"O clima em Campos dos Goytacazes está parcialmente nublado com temperatura de 28°C."*

3. **Envio de E-mails**:
   - Utiliza-se o protocolo SMTP para enviar os e-mails para os usuários com as previsões. O sistema é configurado para conectar-se a servidores como o **Gmail** ou outro servidor SMTP.
   - O e-mail é enviado com um título e um corpo que contém os dados meteorológicos para cada cidade da lista.

## Exemplo de Funcionamento

1. **Usuário** (agricultor, morador ou empresário) se cadastra para receber previsões.
2. A cada **manhã**, o sistema consulta a **API da HG Brasil** para obter as previsões para o **Vale do Café** e o **Rio de Janeiro**.
3. O sistema **formata** os dados e prepara uma mensagem de e-mail como:

   - **Assunto**: Notificação do Clima – dd/mm/aaaa
   - **Corpo do E-mail**:
   
      Olá, [Nome],
      
      Previsão do clima para hoje, dd/mm/aaaa:

      ![alt text](image.png)

      ...


4. O **e-mail é enviado automaticamente** para os usuários cadastrados, permitindo que eles se planejem adequadamente com base nas condições climáticas.

## Benefícios do Funcionamento

- **Planejamento eficiente**: Agricultores podem ajustar suas atividades, como plantio ou colheita, com base no clima.
- **Segurança pública**: Em caso de previsões de tempestades ou eventos climáticos extremos, a comunidade pode se preparar com antecedência.
- **Facilidade e conveniência**: Ao automatizar a coleta e o envio das informações, os usuários economizam tempo e não precisam se preocupar em verificar manualmente as previsões.

Esse funcionamento é altamente adaptável e pode ser expandido para cobrir mais cidades, enviar previsões em outros formatos (como SMS ou notificações push) e até adicionar funcionalidades como alertas de clima severo.