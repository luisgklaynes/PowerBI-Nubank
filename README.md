# Dashboard de Gastos no Cartão de Crédito - Nubank

## Descrição

Este projeto é um **dashboard de Power BI** que permite visualizar métricas de gastos categorizados das faturas do cartão de crédito do **Nubank**. O objetivo principal é fornecer uma visão detalhada sobre os gastos mensais, permitindo ao usuário identificar categorias de maior despesa e acompanhar padrões de consumo ao longo do tempo.

A grande vantagem deste dashboard é que o usuário pode baixar o arquivo `.pbix` (Power BI), ajustar a fonte de dados para sua própria pasta, e fazer o download de suas faturas do Nubank diretamente do site para visualização e análise.

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

### 2. Baixe Suas Faturas do Nubank

1. Acesse sua conta Nubank através do [site oficial](https://nubank.com.br/).
2. No menu de **Cartão de Crédito**, baixe as faturas mensais no formato `.csv`.

### 3. Ajuste a Fonte de Dados no Power BI

1. Abra o arquivo `.pbix` no **Power BI Desktop**.
2. No menu superior, selecione a opção **Transformar Dados**.
<img src="https://github.com/luisgklaynes/PowerBI-Nubank/blob/main/Tutorial/Alterar%20fonte%20de%20dados.png?raw=true" alt="Logo do Projeto" width="500"/>

3. No painel de **Consultas**, você verá a consulta que carrega os dados das faturas. Clique nela e, em seguida, clique no botão **Fonte** no painel superior.
4. Atualize o caminho da pasta para apontar para o local onde você salvou suas faturas.
   
   - Exemplo:
     ```plaintext
     C:\meu_diretorio\minhas_faturas\
     ```
5. Após ajustar o caminho da fonte, clique em **Fechar e Aplicar** para carregar os novos dados.

### 4. Atualize e Visualize

Depois de configurar a nova fonte de dados, o Power BI atualizará automaticamente os gráficos e as visualizações com os seus gastos pessoais. Agora, você poderá explorar suas métricas de despesas categorizadas!

## Dicas Úteis

- **Atualização Automática**: Sempre que adicionar novas faturas à pasta configurada, basta clicar em **Atualizar** no Power BI para carregar os novos dados.
- **Filtros Personalizados**: Use os filtros do Power BI para visualizar dados específicos por período, categoria ou valor de gasto.
  
## Contribuições

Este projeto foi criado para uso pessoal e educativo. Sugestões de melhorias ou novos recursos são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
