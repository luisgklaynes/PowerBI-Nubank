# Dashboard de Gastos no Cartão de Crédito - Nubank

## Descrição

Este projeto é um **dashboard de Power BI** que permite visualizar métricas de gastos categorizados das faturas do cartão de crédito do **Nubank**. O objetivo principal é fornecer uma visão detalhada sobre os gastos mensais, permitindo ao usuário identificar categorias de maior despesa e acompanhar padrões de consumo ao longo do tempo.

A grande vantagem deste dashboard é que o usuário pode baixar o arquivo `.pbix` (Power BI), ajustar a fonte de dados para sua própria pasta e salvar as faturas no diretório definido sem precisar manipular ou unifcar os arquivos.

## Funcionalidades

- Visualização de gastos mensais por **categoria**.
- Acompanhamento de **tendências** de consumo.
- Insights sobre **padrões de gastos** em diferentes períodos de tempo.
- **Personalização fácil** da fonte de dados para uso com faturas pessoais.

## Pré-requisitos

Antes de começar, você vai precisar:

- **Power BI Desktop** instalado no seu computador.
- Faturas do cartão de crédito Nubank exportadas para `.csv`.

## Configuração

Siga os passos abaixo para configurar o dashboard com os seus próprios dados:

### 1. Faça o Download do Arquivo

Baixe o arquivo do projeto (`.pbix`) a partir deste repositório.  

<img src="https://github.com/luisgklaynes/PowerBI-Nubank/blob/main/Tutorial/Download.png?raw=true" alt="Download" width="350"/>  

### 2. Baixe Suas Faturas do Nubank

1. Acesse sua conta Nubank através do [site oficial](https://nubank.com.br/).
2. No menu de **Cartão de Crédito**, baixe as faturas mensais no formato `.csv` para um diretório no seu computador. Exemplo: `C:\minhas_faturas\`
<img src="https://github.com/luisgklaynes/PowerBI-Nubank/blob/main/Tutorial/Baixando%20faturas%20nubank.png?raw=true" alt="Download_fatura" width="750"/>  

### 3. Ajuste a Fonte de Dados no Power BI

1. Abra o arquivo `.pbix` no **Power BI Desktop**.
2. No menu superior, selecione a opção **Transformar Dados**.
<img src="https://github.com/luisgklaynes/PowerBI-Nubank/blob/main/Tutorial/Alterar%20fonte%20de%20dados.png?raw=true" alt="Logo do Projeto" width="500"/>

3. Atualize o caminho da pasta para apontar para o local onde você salvou suas faturas. Exemplo: `C:\minhas_faturas\`
   
5. Após ajustar o caminho da fonte, clique em **Atualizar** para carregar os novos dados.

### 4. Atualize e Visualize

Depois de configurar a nova fonte de dados, o Power BI atualizará automaticamente os gráficos e as visualizações com os seus gastos pessoais. Agora, você poderá explorar suas métricas de despesas categorizadas!

## Dicas Úteis

- **Atualização Automática**: Sempre que adicionar novas faturas à pasta configurada, basta clicar em **Atualizar** no Power BI para carregar os novos dados.
- **Filtros Personalizados**: Use os filtros do Power BI para visualizar dados específicos por período, categoria ou valor de gasto.
  
## Contribuições

Este projeto foi criado para uso pessoal e educativo. Sugestões de melhorias ou novos recursos são bem-vindas! Sinta-se à vontade para baixar adicionar dashboards ou personalizar.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
