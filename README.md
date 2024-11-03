---

# Cloud.IA - Vanna.AI e OpenAI App

## Sumário

1. [Visão Geral](#visão-geral)
2. [Objetivo do Projeto](#objetivo-do-projeto)
3. [Arquitetura da Solução](#arquitetura-da-solução)
4. [Tecnologias e Bibliotecas Utilizadas](#tecnologias-e-bibliotecas-utilizadas)
5. [Diferença entre a Proposta Atual e Inicial](#diferença-entre-a-proposta-atual-e-inicial)
6. [Funcionamento dos Recursos](#funcionamento-dos-recursos)
7. [Como Funciona o Sistema](#como-funciona-o-sistema)
8. [Treinamento do Vanna](#treinamento-do-vanna)
9. [Instalação e Configuração](#instalação-e-configuração)
10. [Execução](#execução)
11. [Link da Aplicação Mobile](#link-da-aplicação-mobile)
12. [Link do Video](#link-do-video)

---

## Visão Geral

Este projeto une a tecnologia de geração de queries SQL da **Vanna.AI** com a interface **Streamlit** para análise de dados na web, e inclui uma aplicação mobile que expande essa funcionalidade ao integrar a **API da OpenAI**. Na versão web, a interface em **Streamlit** permite ao usuário interagir com o banco de dados Oracle e visualizar dados automaticamente com gráficos e dashboards. Já na versão mobile, a **API da OpenAI** complementa o Vanna, permitindo que o usuário faça perguntas contextuais sobre os resultados obtidos para gerar insights mais detalhados.

---

## Objetivo do Projeto

O projeto visa:
- **Facilitar o acesso e a visualização de dados** por meio de queries automáticas geradas pelo Vanna.AI a partir de perguntas em linguagem natural.
- **Permitir uma exploração aprofundada dos insights** na versão mobile, onde a OpenAI responde perguntas adicionais sobre os resultados gerados, ajudando o usuário a compreender o contexto e a tirar conclusões.

---

## Arquitetura da Solução

A aplicação é dividida em duas partes principais:

1. **Aplicação Web em Streamlit**: Conecta-se ao banco de dados Oracle e gera consultas SQL automaticamente usando a API Vanna. Os dados retornados são exibidos em tabelas e gráficos interativos, proporcionando uma experiência de análise dinâmica.
  
2. **Aplicação Mobile com OpenAI**: Integra a OpenAI para fornecer respostas mais detalhadas e insights adicionais com base nos resultados de consulta SQL do Vanna.

### Fluxo de Funcionamento:
1. O usuário faz uma pergunta em linguagem natural.
2. O Vanna.AI interpreta a pergunta e gera uma consulta SQL.
3. O resultado da consulta SQL é exibido em um gráfico no Streamlit.
4. No aplicativo mobile, a OpenAI oferece insights adicionais sobre o resultado, respondendo perguntas de acompanhamento.

---

## Tecnologias e Bibliotecas Utilizadas

- **Streamlit**: Framework para visualização de dados em tempo real na web.
- **Vanna.AI**: Tecnologia de geração de SQL a partir de perguntas em linguagem natural.
- **API da OpenAI**: Para perguntas contextuais sobre os resultados dos dados, melhorando a interpretação dos insights.
- **Banco de Dados Oracle**: Usado para armazenar e consultar dados.

---

## Diferença entre a Proposta Atual e Inicial

Na versão inicial, o projeto utilizava o **Streamlit** apenas para a visualização de dados baseada em SQL estática. A nova proposta integrou o **Vanna.AI** para geração dinâmica de queries SQL a partir de linguagem natural e expandiu o uso da **API da OpenAI** para perguntas contextualizadas no aplicativo mobile, proporcionando uma experiência mais interativa e personalizada ao usuário.

---

## Funcionamento dos Recursos

### Perguntas e Geração de SQL
O Vanna.AI interpreta perguntas em linguagem natural e gera a SQL necessária para consulta no banco de dados Oracle. Isso permite que o usuário explore os dados sem precisar entender SQL.

### Visualização de Dados
As consultas SQL retornadas pelo Vanna são exibidas em tabelas e gráficos interativos criados com Plotly, integrados ao Streamlit. A interface permite uma análise visual e detalhada das respostas.

### Perguntas Contextuais na Aplicação Mobile
A aplicação mobile permite que o usuário faça perguntas adicionais com base nos resultados, usando a API da OpenAI. Isso fornece insights contextuais mais aprofundados e ajuda o usuário a entender melhor os dados apresentados.

---

## Como Funciona o Sistema

### Interação do Usuário
1. **Entrada do Usuário**: O usuário insere uma pergunta em linguagem natural em um campo de texto da interface.
2. **Processamento da Pergunta**: Quando a pergunta é submetida, o sistema utiliza a API do Vanna.AI para entender a intenção do usuário e determinar a query SQL adequada.
  
### Geração da Consulta SQL
- **Modelagem de Linguagem Natural**: O Vanna.AI utiliza modelos de aprendizado de máquina treinados para converter perguntas em linguagem natural em consultas SQL válidas. O modelo analisa a estrutura da pergunta, identificando entidades, ações e contextos relevantes.
- **Criação da Query**: O sistema então gera a consulta SQL correspondente, utilizando parâmetros e condições extraídos da pergunta do usuário.

### Execução da Query
- **Conexão com o Banco de Dados**: A consulta SQL é enviada ao banco de dados Oracle, onde é executada. O sistema espera a resposta que contém os dados solicitados.
- **Retorno de Dados**: Os dados retornados pelo banco são processados e formatados para serem apresentados ao usuário.

### Visualização dos Resultados
- **Exibição no Streamlit**: Os dados são exibidos na interface do Streamlit em tabelas e gráficos interativos, permitindo que o usuário visualize facilmente as informações.
- **Insights Contextuais**: O aplicativo mobile permite ao usuário fazer perguntas adicionais, utilizando a API da OpenAI para fornecer respostas mais profundas e contextuais, enriquecendo a experiência de análise.

### Feedback e Melhoria Contínua
O sistema é projetado para aprender com o uso. As interações dos usuários e o feedback recebido podem ser utilizados para melhorar os modelos de linguagem e a precisão da geração de SQL, otimizando continuamente a experiência do usuário.

---

## Treinamento do Vanna

O desempenho do Vanna.AI depende principalmente da qualidade dos dados de treinamento, especificamente dos pares corretos de pergunta-SQL. Esses pares servem como referência para o modelo, permitindo que ele entenda o contexto das perguntas e gere queries SQL precisas. Aqui estão algumas orientações para otimizar o treinamento:

- **Qualidade dos Pares Pergunta-SQL**: O modelo Vanna usa uma camada de recuperação aumentada treinada com exemplos de pergunta-SQL. Quanto mais precisos e variados forem esses exemplos, melhor será o desempenho do modelo na geração de queries.

- **Uso de DDL e Consultas**: Durante o treinamento, utilizamos o DDL (Data Definition Language) para definir a estrutura do banco de dados, garantindo que as colunas e tabelas estejam bem descritas e documentadas. As consultas SQL que usamos foram extraídas de práticas recomendadas e de exemplos reais, o que ajudou a modelar perguntas em linguagem natural de forma mais eficaz.

- **Documentação**: Também seguimos as sugestões fornecidas pela documentação do Vanna para o treinamento. Isso incluiu a criação de uma base de dados de exemplos que refletissem uma ampla gama de possíveis perguntas e seus respectivos comandos SQL. A documentação ajudou a identificar quais parâmetros e condições poderiam ser mais relevantes para os usuários, orientando a seleção dos pares de dados.

- **Contexto e Estrutura**: Pares de pergunta-SQL que utilizam nomes de colunas específicos (em vez de consultas genéricas como `SELECT * FROM tabela`) ajudam o sistema a entender melhor o contexto e a estrutura dos dados.

- **Sugestões para Melhorar o Treinamento**:
  - Usar instruções SQL que sejam ricas em contexto, mencionando colunas específicas e condições claras.
  - Começar com um notebook Jupyter permite controlar melhor os dados de treinamento e realizar operações em massa, como extrair o esquema do banco de dados.

Para uma explicação mais visual sobre o funcionamento do Vanna, veja a imagem a seguir:

![Imagem explicativo sobre o Vanna](https://vanna.ai/docs/img/how-vanna-works.gif)

---

## Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- Streamlit
- Credenciais de acesso para Vanna e OpenAI
- Banco de dados Oracle configurado

### Passo a Passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/Viannaana/Cloud.IA---IOT-V_Final-.git
   cd Cloud.IA---IOT-V_Final-
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as credenciais no arquivo `config.json`:
   ```json
   {
     "vanna_api_key": "YOUR_VANNA_API_KEY",
     "openai_api_key": "YOUR_OPENAI_API_KEY",
     "oracle": {
       "user": "youruser",
       "password": "yourpassword",
       "host": "yourhost"
     }
   }
   ```

4. Configure o banco de dados Oracle e execute o script `setup.sql` para criar as tabelas.

---

## Execução

1. Inicie

 a aplicação Streamlit:
   ```bash
   streamlit run app.py
   ```

2. Acesse a aplicação pelo navegador em `http://localhost:8501`.

---

## Link da Aplicação Mobile

A aplicação mobile está disponível [aqui](https://github.com/Rminoro/ClaudiANext).

---

## Link do Video 

O vídeo da explicação do projto [aqui](https://youtu.be/50whnZ2u0Rk).

---
