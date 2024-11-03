#queries
queries = [
    {
        "question": "Qual é o total de vendas por mês deste ano?",
        "sql": """
            SELECT TO_CHAR(DATA_PEDIDO, 'YYYY-MM') AS MES, SUM(VALOR_TOTAL) AS TOTAL_VENDAS
            FROM Pedido
            WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE)
            GROUP BY TO_CHAR(DATA_PEDIDO, 'YYYY-MM')
            ORDER BY MES
        """
    },
    {
        "question": "Qual é o valor médio das vendas por loja?",
        "sql": """
            SELECT l.NOME_LOJA, AVG(p.VALOR_TOTAL) AS VALOR_MEDIO_VENDA
            FROM Pedido p
            JOIN Loja l ON p.ID_LOJA = l.ID_LOJA
            GROUP BY l.NOME_LOJA
            ORDER BY VALOR_MEDIO_VENDA DESC
        """
    },
    {
        "question": "Qual é a quantidade total de produtos em estoque por tipo?",
        "sql": """
            SELECT TIPO_PRODUTO, SUM(QUANTIDADE) AS TOTAL_ESTOQUE
            FROM Estoque
            GROUP BY TIPO_PRODUTO
            ORDER BY TOTAL_ESTOQUE DESC
        """
    },
    {
        "question": "Qual é o total de pedidos e o valor total de vendas por vendedor?",
        "sql": """
            SELECT v.NOME_VENDEDOR, COUNT(p.ID_PEDIDO) AS NUM_PEDIDOS, SUM(p.VALOR_TOTAL) AS TOTAL_VENDAS
            FROM Pedido p
            JOIN Vendedor v ON p.ID_VENDEDOR = v.ID_VENDEDOR
            GROUP BY v.NOME_VENDEDOR
            ORDER BY TOTAL_VENDAS DESC
        """
    },
    {
        "question": "Qual é o valor total das vendas e o número de pedidos por tipo de pedido?",
        "sql": """
            SELECT TIPO_PEDIDO, COUNT(ID_PEDIDO) AS NUM_PEDIDOS, SUM(VALOR_TOTAL) AS VALOR_TOTAL
            FROM Pedido
            GROUP BY TIPO_PEDIDO
            ORDER BY VALOR_TOTAL DESC
        """
    },
    {
        "question": "Qual é o total de vendas por loja?",
        "sql": """
            SELECT l.NOME_LOJA, SUM(p.VALOR_TOTAL) AS TOTAL_VENDAS
            FROM Pedido p
            JOIN Loja l ON p.ID_LOJA = l.ID_LOJA
            GROUP BY l.NOME_LOJA
            ORDER BY TOTAL_VENDAS DESC
        """
    },
    {
        "question": "Qual é o total de vendas por cliente?",
        "sql": """
            SELECT c.NOME_CLIENTE, SUM(p.VALOR_TOTAL) AS TOTAL_VENDAS
            FROM Pedido p
            JOIN Cliente c ON p.ID_CLIENTE = c.ID_CLIENTE
            GROUP BY c.NOME_CLIENTE
            ORDER BY TOTAL_VENDAS DESC
        """
    },
    {
        "question": "Qual é a quantidade total vendida de cada produto?",
        "sql": """
           SELECT TIPO_PRODUTO, SUM(QUANTIDADE) AS TOTAL_VENDIDO
           FROM PEDIDOPRODUTO
           GROUP BY TIPO_PRODUTO
           ORDER BY TOTAL_VENDIDO DESC;
        """
    },
    {
        "question": "Qual é o número total de pedidos por tipo de produto?",
        "sql": """
            SELECT e.TIPO_PRODUTO, COUNT(p.ID_PEDIDO) AS NUM_PEDIDOS
            FROM Pedido p
            JOIN Estoque e ON p.ID_LOJA = e.ID_LOJA
            GROUP BY e.TIPO_PRODUTO
            ORDER BY NUM_PEDIDOS DESC
        """
    },
    {
        "question": "Qual é o total de pedidos cancelados, devolvidos e reembolsos por vendedor?",
        "sql": """
            SELECT v.NOME_VENDEDOR,
                   COUNT(DISTINCT pc.ID_CANCELAMENTO) AS NUM_CANCELAMENTOS,
                   COUNT(DISTINCT pd.ID_DEVOLUCAO) AS NUM_DEVOLUCOES,
                   COUNT(DISTINCT pr.ID_REEMBOLSO) AS NUM_REEMBOLSOS
            FROM Vendedor v
            LEFT JOIN PedidoCancelamento pc ON v.ID_VENDEDOR = pc.ID_PEDIDO
            LEFT JOIN PedidoDevolucao pd ON v.ID_VENDEDOR = pd.ID_PEDIDO
            LEFT JOIN PedidoReembolso pr ON v.ID_VENDEDOR = pr.ID_PEDIDO
            GROUP BY v.NOME_VENDEDOR
            ORDER BY NUM_REEMBOLSOS DESC, NUM_DEVOLUCOES DESC, NUM_CANCELAMENTOS DESC
        """
    }
]

