BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "version" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "version_db" TEXT,
    "version_system" TEXT
);

CREATE TABLE IF NOT EXISTS "SCRIPTS" (
    "idSCRIPT" INTEGER PRIMARY KEY AUTOINCREMENT,
    "DESCRICAO" TEXT,
    "SCRIPT_TEXT" TEXT
);

CREATE TABLE IF NOT EXISTS "INSTALADORES" (
    "idARQUIVO" INTEGER PRIMARY KEY AUTOINCREMENT,
    "DESCRICAO" VARCHAR(150),
    "LINK_ARQUIVO" TEXT
);

CREATE TABLE IF NOT EXISTS "DRIVERS" (
    "idDRIVER" INTEGER PRIMARY KEY AUTOINCREMENT,
    "DESCRICAO" VARCHAR(150),
    "LINK_DRIVER" TEXT
);



INSERT INTO "version" ("id","version_db","version_system") VALUES (1,'0.0.2','4.0.2');
COMMIT;

INSERT INTO "SCRIPTS" ("idSCRIPT","DESCRICAO","SCRIPT_TEXT") VALUES (1,'Banco de Dados Suspeito','-- Passo 1

ALTER DATABASE Hiper SET EMERGENCY

ALTER DATABASE Hiper SET SINGLE_USER WITH ROLLBACK IMMEDIATE



-- Passo 2

DBCC CheckDB (Hiper, REPAIR) -- Tentar este comando, se der erro, tentar o debaixo

--DBCC CheckDB (Hiper, REPAIR_ALLOW_DATA_LOSS)



-- Passo 3

ALTER DATABASE Hiper SET MULTI_USER

ALTER DATABASE Hiper SET ONLINE



-- Passo 4

USE Hiper EXEC sp_msforeachtable ALTER TABLE ? WITH CHECK CHECK CONSTRAINT ALL

'),
 (2,'CONSULTA DE PEDIDOS','select * from pedido_venda where codigo = ''L3204''

select * from pedido_venda_operacao_pdv where id_pedido_venda = 28706

select * from operacao_pdv where id_operacao = 11126

select * from operacao_pdv'),
 (3,'FORÇAR SINCRONIZAÇÃO','DELETE HIPERLOJA_SYNC_PROTOCOLO_SINCRONIZACAO
DELETE HIPERLOJA_SYNC_PROTOCOLO_SINCRONIZACAO_ARQUIVOS
DELETE HIPERLOJA_SYNC_PROTOCOLO_SINCRONIZACAO_OBJETOS
DELETE HIPERLOJA_SYNC_PROTOCOLO_SINCRONIZACAO_OBJETOS_ALERTAS
DELETE HIPERLOJA_SYNC_PROTOCOLO_SINCRONIZACAO_OBJETOS_ENTIDADES
DELETE HIPERLOJA_SYNC_PROCESSAMENTO

3°
SELECT * FROM HIPERLOJA_SYNC_AUDITORIA
SELECT * FROM HIPERLOJA_SYNC_PRODUTO

4º
DELETE HIPERLOJA_SYNC_AUDITORIA
DELETE HIPERLOJA_SYNC_PRODUTO

5º
SELECT * FROM HIPERLOJA_SYNC_PROCESSAMENTO
UPDATE HIPERLOJA_SYNC_PROCESSAMENTO SET DATAEHORADAULTIMASOLICITACAO = GETDATE() - 1'),
 (4,'IMPRESSORA ERRO 0X0000709','
Passo 1>
	Ativar o Recurso LPD Printer Service
	Ativar o Recurso LPR Port Monitor
	
Acessar o Painel de Controle, em baixo do nome Programas escolher a opção ''Desinstalar um Programa''.
	No lado esquerdo, escolher a opção ''Ativar ou desativar recursos do Windows'';
	Procurar por ''Serviços de Impressão e Documentos''
	Clicar no + para expandir
	Selecionar Monitor de Porta LPR e Serviço de Impressão LPD e depois clicar em ''OK'';
	
Passo 2>
	Abri o Editor de ''Editor de Política de Grupo Local''
	Para isso. aperta a tecla ''Windows + R'' ou então pesquisar na barra de pesquisa pelo nome ''Executar'';
	Na tela que aparece, digite o nome ''gpedit.msc'' e aperte enter ou então clique em ok;
	Na nova tela procure por ''Modelos Administrativos''--> Impressoras;
	Selecione a opção ''Definir configurações de conexão RCP'' -- Voce pode abrir essa opção dando 2 cliques ou 
	clicar em ''configuração de Politicia''.
		Na tela que abre, na opção ''Definir configurações de conexão RPC'' marque a opção ''habilitado''.
		Na opçao ''Protocolo a ser usado para conexoes RPC de saida" marque ''RCP sobre pipes nomeados;
		Na opçao ''Use a autenticação para conexões RPC de saida'' marque ''Padrão''
		Em seguida, clique em aplicar e ok
		
Definir configurações de ouvinte RCP
Configurar RCP sobre porta TCP

Abrir editor de registro
	Computador\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Printers\RPC
	RpcOverNamedPipes(1) dword 32
	RpcOverTcp(0) dword 32
	RpcUseNamedPipeProtocol(1)
	
Dar permissoes
	Computador\HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows
	dar permissões sobre a pasta Windows (Full control)

Habilitar o RpcAuthnLevelPrivacyEnabled
	Computador\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print
	 
	 REINICIAR O SERVIÇO DE SPOOLER
	
	
	====================
	
	
	Step - 1
Turn Windows Features On or Off
Printer and Document Service
LPD Printer Service
LPR Port Monitor

Step - 2
Local Group Policy Editor
Administrative Templetes
Printer
Configure RPC Connection - Enabled- RPC over named pipes
Configure RPC Listener - Enabled- RPC over named pipes and TCP
Configure RPC over TCP - Enabled

Step - 3
[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows NT\Printers\RPC]
There are 2 values that can be configured:
RpcUseNamedPipeProtocol REG_DWORD
0: RpcOverTcp  Value - 0
1: RpcOverNamedPipes Value - 1

Step - 4
[HKEY_LOCAL_MACHINE\SYSTEM|CurrentControlSet\Control\Print
RpcAuthnLevelPrivacyEnabled REG_DWORD

Step - 5
HKEY_CURRENT_USER\Software\Microsoft\WindowsNT\CurrentVersion\Windows
Then Right-click on Windows key and select Permissions.

Step - Final
Print Spooler
	'),
 (5,'LIBERA FILA DE SYNC TRAVADA','Rodar ele sempre com o HiperSync Fechado

delete hiperloja_sync_protocolo_sincronizacao
delete hiperloja_sync_protocolo_sincronizacao_arquivos
delete hiperloja_sync_protocolo_sincronizacao_objetos
delete hiperloja_sync_protocolo_sincronizacao_objetos_alertas
delete hiperloja_sync_protocolo_sincronizacao_objetos_entidades
delete hiperloja_sync_processamento

Roda até parar de aparecer os erros vermelhos e 0 linhas alteradas

select * from hiperloja_sync_auditoria - roda este select se tiver algo
delete from hiperloja_sync_auditoria - roda este dai

update hiperloja_sync_processamento
set DataEHoraDaUltimaSolicitacao = GETDATE() - 1'),
 (6,'OPERAÇÕES PARADAS','select * from (
select ''devoluca'' coluna, count( *) qtd from hiper..devolucao_venda (nolock) where status_integracao <> 0
union all select ''documento_estoque'', count( *) from hiper..documento_estoque (nolock) where status_integracao <> 0
union all select ''entidade'', count( *) from hiper..entidade (nolock) where status_integracao <> 0
union all select ''hierarquia_produto'', count( *) from hiper..hierarquia_produto (nolock) where status_integracao <> 0
union all select ''lancamento_devolucao_venda'', count( *) from hiper..lancamento_devolucao_venda (nolock) where status_integracao <> 0
union all select ''marca_produto'', count( *) from hiper..marca_produto (nolock) where status_integracao <> 0
union all select ''nota_fiscal'', count( *) from hiper..nota_fiscal nf (nolock) where status_integracao <> 0 AND ((nf.situacao_registro <> 1 and nf.situacao_registro is not null) or (nf.status_nfe not in (0,1,2,7) and nf.status_nfe is not null))
union all select ''nota_fiscal_log_email'', count( *) from hiper..nota_fiscal_log_email (nolock) where status_integracao <> 0
union all select ''operacao_pdv'', count( *) from hiper..operacao_pdv (nolock) where status_integracao <> 0
union all select ''pedido_venda'', count( *) from hiper..pedido_venda (nolock) where status_integracao <> 0 AND situacao <> 1 AND situacao <> 7 --tira em cadastramento
union all select ''produto '', count( *) from hiper..produto (nolock) where status_integracao <> 0
union all select ''tabela_preco_produto'', count( *) from hiper..tabela_preco_produto (nolock) where status_integracao <> 0
union all select ''unidade_medida'' , count( *) from hiper..unidade_medida (nolock) where status_integracao <> 0
) dados where qtd > 0--select * from produto (nolock) where status_integracao <> 0
'),
 (7,'Portas Usadas Pelo Hiper','Portas Usadas Pelo Hiper

443,1433,8080,9090,9095,9096,9097,9098,9099'),
 (10,'QUERYS HIPER','
--Produto SEM estoque (COM estoque SE arrumar o GROUP BY)
SELECT 
	t1.codigo,
    COALESCE(t2.codigo_barras, '''') AS codigo_barras,
    t1.referencia_interna_produto,
	t1.nome AS nome_produto,
    t9.codigo AS codigo_fornecedor,
	t4.sigla as sigla_unidade_medida,
	--CASE WHEN t6.quantidade > ''-1'' THEN SUM(t6.quantidade) END AS estoque   
	t1.preco_aquisicao AS precoFornecedor,
	t1.preco_custo AS preço_de_custo,
	t1.preco_minimo_venda,
	t1.preco_venda,
	t3.id_ncm AS NCM,
	isnull(cast(t5.id_situacao_tributaria_icms AS VARCHAR), '''') AS Codigo_situacao_tributaria_ICMS,
	isnull(cast(t5.id_situacao_tributaria_simples_nacional AS VARCHAR), '''') AS CSOSN,
	isnull(cast(t5.aliquota_icms AS VARCHAR), '''') AS AliquotaICMS,
	isnull(cast(t5.percentual_reducao_base_icms AS VARCHAR), '''') AS ReducaoICMS,
	isnull(cast(t5.mva AS VARCHAR), '''') AS MVA
FROM produto t1
	LEFT JOIN produto_sinonimo t2 ON t1.id_produto = t2.id_produto
	LEFT JOIN ncm t3 ON t1.id_ncm = t3.id_ncm
	LEFT JOIN unidade_medida t4 ON t1.id_unidade_medida = t4.id_unidade_medida
	LEFT JOIN regra_tributacao_icms_personalizada t5 ON t1.id_produto = t5.id_produto
	--LEFT JOIN saldo_estoque t6 ON t1.id_produto = t6.id_produto
	LEFT JOIN entidade t9 ON t1.id_entidade_fornecedor = t9.id_entidade
WHERE t1.codigo <> 1
	--GROUP BY t6.id_produto, t1.codigo, t2.codigo_barras, t1.referencia_interna_produto, t1.nome, t9.codigo, t4.sigla, t6.quantidade --t1.codigo, t2.codigo_barras, t1.referencia_interna_produto, t1.nome, t9.codigo, t4.sigla, t6.quantidade, 
	ORDER BY t1.codigo

--Estoque
SELECT
	t1.id_produto,
	t2.codigo,
	SUM(t1.quantidade) as estoque
FROM saldo_estoque t1
	LEFT JOIN produto t2 ON t1.id_produto = t2.id_produto
	GROUP BY t1.id_produto, t2.codigo
	ORDER BY t1.id_produto


--Clientes e Fornecedores
SELECT
	CASE WHEN t1.flag_cliente = ''1'' THEN ''SIM'' ELSE ''NAO'' END AS eh_cliente,
	CASE WHEN t1.flag_fornecedor = ''1'' THEN ''SIM'' ELSE ''NAO'' END AS eh_fornecedor,
	CASE WHEN t1.flag_transportadora = ''1'' THEN ''SIM'' ELSE ''NAO'' END AS eh_transportadora,
	t1.codigo,
	t1.nome,
	CASE WHEN t1.tipo_entidade = ''2'' THEN t4.cnpj ELSE t3.cpf END AS cpf_ou_cnpj,
	CASE WHEN t1.tipo_entidade = ''2'' THEN t4.nome_fantasia ELSE '''' END AS nome_fantasia,
	CASE WHEN t1.tipo_entidade = ''2'' THEN t4.ie ELSE t3.ie END AS inscricao_estadual,
	t3.rg,
	t1.logradouro,
	t1.numero_endereco,
	t1.bairro,
	t1.complemento,
	t1.cep,
	t2.nome as cidade,
	t2.uf,
	t1.fone_primario_ddd + fone_primario_numero as telefone_principal,
	t1.fone_secundario_ddd + fone_secundario_ddd as telefone_secundario,
	t1.email
FROM entidade t1
	LEFT JOIN cidade t2 ON t1.id_cidade = t2.id_cidade
	LEFT JOIN pessoa_fisica t3 ON t1.id_entidade = t3.id_entidade
	LEFT JOIN pessoa_juridica t4 ON t1.id_entidade = t4.id_entidade


--Ordem Producao
SELECT 
        t1.id_ordem_producao AS "codigo Ordem Producao",
        COALESCE(LEFT(t2.nome,80),'''') AS Produto,
        t1.quantidade AS "quantidade utilizada",
        t1.quantidade_produzida AS "quantidade produzida",
        t1.quantidade_desperdicio AS "quantidade Desperdicio",
    CASE
        WHEN t3.situacao = 4 THEN ''Producao Concluida''
        WHEN t3.situacao = 3 THEN ''Producao Parcial''
        WHEN t3.situacao = 2 THEN ''Producao Pendente''
        WHEN t3.situacao = 1 THEN ''Em cadastramento''
        END AS "Status Ordem Producao",
    t3.observacao,
    t4.razao_social AS "Nome Empresa",
    t3.data_hora_cadastro,
    t5.nome AS "Usuario de cadastro",
    t3.data_hora_alteracao,
    CASE
        WHEN t3.id_usuario_alteracao IS NULL THEN ''Não Alterado''
        ELSE (SELECT nome 
                FROM usuario 
                    WHERE t3.id_usuario_alteracao = id_usuario) 
                        END AS "Nome usuario Alteracao"
    FROM item_ordem_producao t1 (NOLOCK)
        LEFT JOIN produto t2  (NOLOCK) ON t1.id_produto = t2.id_produto
        LEFT JOIN ordem_producao t3 (NOLOCK) ON t1.id_ordem_producao = t3.id_ordem_producao
        LEFT JOIN filial t4 (NOLOCK)ON t3.id_filial_ordem = t4.id_filial
        LEFT JOIN usuario t5 (NOLOCK) ON t3.id_usuario_cadastro = t5.id_usuario

--Pedido de venda
use Hiper

DECLARE @datainicial date
SET @datainicial = ''2020-01-01'' -- pode estar informando a data que inicial desejada (ANO / DIA / MES)
DECLARE @datafinal  date
SET @datafinal = ''2021-12-31''-- pode estar informando a data que final desejada (ANO / DIA / MES)

SELECT 
    t2.codigo AS "Codigo Pedido de Venda",
    t3.nome AS "Nome do Produto",
    t1.valor_unitario AS "Preço Unitario",
    t2.observacao,
    t4.nome AS "Nome Cliente",
    CASE
        WHEN t4.tipo_entidade = 1 THEN t6.cpf
        WHEN t4.tipo_entidade = 2 THEN t7.cnpj
        ELSE '''' END AS "CPF ou CNPJ Cliente",
    t8.nome AS "usuario Geração Pedido de Venda",
    left(t2.data_hora_geracao,11) AS "Data Abertura",
    CASE
        WHEN CAST(t2.situacao AS VARCHAR(20)) = 1 THEN ''Em cadastramento'' 
        WHEN CAST(t2.situacao AS VARCHAR(20)) = 2 THEN ''Não Faturado''
        WHEN CAST(t2.situacao AS VARCHAR(20)) = 5 THEN ''Faturado''
        WHEN CAST(t2.situacao AS VARCHAR(20)) = 6 THEN ''Cancelado''
        WHEN CAST(t2.situacao AS VARCHAR(20)) = 7 THEN ''Em Faturamento''
         END AS "Status"

    FROM item_pedido_venda t1 (NOLOCK)
    LEFT JOIN pedido_venda t2 (NOLOCK) ON t1.id_pedido_venda = t2.id_pedido_venda
    LEFT JOIN produto t3 (NOLOCK) ON t1.id_produto = t3.id_produto
    LEFT JOIN entidade t4 (NOLOCK) ON t2.id_entidade_cliente = t4.id_entidade
    LEFT JOIN filial t5 (NOLOCK) ON t2.id_filial_venda = t5.id_filial
    LEFT JOIN pessoa_fisica t6 (NOLOCK) ON t4.id_entidade = t6.id_entidade 
    LEFT JOIN pessoa_juridica t7 (NOLOCK) ON t4.id_entidade = t7.id_entidade
    LEFT JOIN usuario t8 (NOLOCK) ON t2.id_usuario_geracao = t8.id_usuario
    WHERE 
    -- ira pegar somente os pedido que não foram excluidos, caso queira os excluidos também altera o 1 por 99
    t2.excluido <> 1
    and t2.data_hora_geracao BETWEEN @dataInicial AND  @dataFinal

    ORDER BY t2.codigo



'),
 (11,'SISTEMA PERSEU - QUERY ESTOQUE','--ESSA QUERY IRÁ TRAZER TODOS OS DADOS DO PRODUTO NO SISTEMA PERSEU

select t1.codigo, t1.codbarra, t1.produto,t1.unidade, t2.atual as estoque,
       t1.precocusto as CUSTO, t1.precovenda as P_VENDA,t1.cst,
       t1.classificacao_fiscal as NCM, t1.alicota,t1.IPI,t1.reducao,
       t1.situacao,t1.piscofins,t1.incidencia_piscofins,
       t1.situacao_tributaria,t1.csosn
from c000025 as t1
inner join estoque_produto as t2
on t1.codigo = t2.cod_produto
order by codigo asc;'),
 (13,'HIPER - IMPORTAÇÃO DE CLIENTES','--PARA OBTER DADOS DA PESSOA FÍSICA ORDENADOS:

--NOVA QUERY

/*
SELECT
DISTINCT
CASE
WHEN tipo_entidade = 1 THEN ''Pessoa física''
WHEN tipo_entidade = 2 THEN ''Pessoa jurídica''
WHEN tipo_entidade = 3 THEN ''Pessoa simplificada''
END AS ''Tipo cliente'',
E.NOME,E.LOGRADOURO,E.NUMERO_ENDERECO,
	   E.BAIRRO,E.COMPLEMENTO,E.CEP,
	   E.FONE_PRIMARIO_DDD,E.FONE_PRIMARIO_NUMERO,
	   F.CPF,F.RG,J.CNPJ,J.IE,J.NOME_FANTASIA,
	   C.NOME AS CIDADE,C.UF	   
FROM ENTIDADE E
LEFT JOIN PESSOA_FISICA F
ON E.ID_ENTIDADE = F.ID_ENTIDADE
LEFT JOIN PESSOA_JURIDICA J
ON E.ID_ENTIDADE = J.ID_ENTIDADE
LEFT JOIN CIDADE C
ON E.ID_CIDADE = C.ID_CIDADE
ORDER BY  [Tipo cliente] DESC
-----------------------------------------------------------------------

SELECT E.NOME,E.LOGRADOURO,E.NUMERO_ENDERECO,
	   E.BAIRRO,E.COMPLEMENTO,E.CEP,
	   E.FONE_PRIMARIO_DDD,E.FONE_PRIMARIO_NUMERO,
	   F.CPF,F.RG,J.CNPJ,J.IE,J.NOME_FANTASIA,
	   C.NOME AS CIDADE,C.UF
	   
FROM ENTIDADE E
INNER JOIN PESSOA_FISICA F
ON E.ID_ENTIDADE = F.ID_ENTIDADE
INNER JOIN PESSOA_JURIDICA J
ON E.ID-ENTIDADE = J.ID_ENTIDADE
INNER JOIN CIDADE C
ON E.ID_CIDADE = C.ID_CIDADE
ORDER BY E.NOME ASC
GO


--PARA OBTER DADOS DA PESSOA JURIDICA ORDENADOS:


SELECT E.NOME,E.LOGRADOURO,E.NUMERO_ENDERECO,
	   E.BAIRRO,E.COMPLEMENTO,E.CEP,
	   E.FONE_PRIMARIO_DDD,E.FONE_PRIMARIO_NUMERO,
	   J.CNPJ,J.IE,J.NOME_FANTASIA,
	   C.NOME AS CIDADE,C.UF
FROM ENTIDADE E
INNER JOIN PESSOA_JURIDICA J
ON E.ID_ENTIDADE = J.ID_ENTIDADE
INNER JOIN CIDADE C
ON E.ID_CIDADE = C.ID_CIDADE
ORDER BY E.NOME ASC
GO
*/'),
 (14,'HIPER - IMPORTAÇÃO DE FORNECEDORES','--ESSA QUERY IRÁ TRAZER TODOS OS DADOS DOS FORNECEDORES DO BANCO DE DADOS HIPER

SELECT
        t1.nome AS ''Nome fornecedor'',
        CASE
        WHEN t3.ie <> '''' THEN t3.ie
        WHEN t4.ie <> '''' THEN t4.ie
        WHEN t3.ie = '' '' AND t1.tipo_entidade = 1 THEN ''Sem I.E''
        WHEN t4.ie = '' '' AND t1.tipo_entidade = 2 THEN ''Sem I.E''
        WHEN t1.tipo_entidade = 3 THEN ''Sem I.E''
        END AS ''Inscrição estadual'',
        codigo AS ''Código'',
        CASE
        WHEN fone_primario_ddd IS NOT NULL THEN ''('' + fone_primario_ddd + '')'' +'' ''+
        fone_primario_numero
        WHEN fone_secundario_ddd IS NOT NULL THEN ''('' + fone_secundario_ddd + '')'' +'' ''+
        fone_secundario_numero
        WHEN fone_secundario_ddd IS NULL AND fone_primario_ddd IS NULL THEN ''Sem telefone
        cadastrado''
        END AS ''Telefone'',
        ISNULL(t2.nome + '' - '' + t2.uf, ''Sem cidade/UF cadastrada'') AS ''Localidade'',
        CASE
        WHEN t1.logradouro = '''' THEN ''Sem logradouro cadastrado''
        WHEN t1.logradouro <> '''' THEN t1.logradouro
        END AS ''Logradouro'',
        CASE
        WHEN ISNUMERIC(t1.numero_endereco) = 0 THEN ''Sem número cadastrado''
        WHEN ISNUMERIC(t1.numero_endereco) = 1 THEN t1.numero_endereco
        END AS ''Número endereço'',
        CASE
        WHEN t1.bairro = '' '' THEN ''Sem bairro cadastrado''
        WHEN t1.bairro <> '''' THEN t1.bairro
        END AS ''Bairro'',
        CASE
        WHEN tipo_entidade = 1 THEN t3.cpf + '' - '' +''CPF''
        WHEN tipo_entidade = 2 THEN t4.cnpj + '' - '' + ''CNPJ''
        WHEN tipo_entidade NOT IN (1,2) THEN ''Sem CPF ou CNPJ''
        END AS ''CPF/CNPJ'',
        CASE
        WHEN flag_fornecedor = 1 THEN ''É fornecedor''
        END AS ''Tipo''
        FROM entidade t1
        LEFT JOIN cidade t2 ON t1.id_cidade = t2.id_cidade
        LEFT JOIN pessoa_fisica t3 ON t1.id_entidade = t3.id_entidade
        LEFT JOIN pessoa_juridica t4 ON t1.id_entidade = t4.id_entidade
        WHERE t1.flag_fornecedor = 1 AND t1.excluido = 0'),
 (15,'HIPER - IMPORTAÇÃO DE PRODUTOS','

--ESSA QUERY  TRAZ TODOS OS DADOS DOS PRODUTOS DO BANCO DE DADOS HIPER.

SELECT
        t1.codigo,
        COALESCE(t2.codigo_barras, '''') AS codigo_barras,
        t1.referencia_interna_produto,
        t1.nome AS nome_produto,
        t9.codigo AS codigo_fornecedor,
        t4.sigla as sigla_unidade_medida,
        t6.quantidade as Estoque,
        t1.preco_aquisicao AS precoFornecedor,
        t1.preco_custo AS preço_de_custo,
        t1.preco_minimo_venda,
        t1.preco_venda,
        t3.id_ncm AS NCM,
        isnull(cast(t5.id_situacao_tributaria_icms AS VARCHAR), '''') AS Codigo_situacao_tributaria_ICMS,
        isnull(cast(t5.id_situacao_tributaria_simples_nacional AS VARCHAR), '''') AS CSOSN,
        isnull(cast(t5.aliquota_icms AS VARCHAR), '''') AS AliquotaICMS,
        isnull(cast(t5.percentual_reducao_base_icms AS VARCHAR), '''') AS ReducaoICMS,
        isnull(cast(t5.mva AS VARCHAR), '''') AS MVA
        FROM produto t1
        LEFT JOIN produto_sinonimo t2 ON t1.id_produto = t2.id_produto
        LEFT JOIN ncm t3 ON t1.id_ncm = t3.id_ncm
        LEFT JOIN unidade_medida t4 ON t1.id_unidade_medida = t4.id_unidade_medida
        LEFT JOIN regra_tributacao_icms_personalizada t5 ON t1.id_produto = t5.id_produto
        LEFT JOIN saldo_estoque t6 ON t1.id_produto = t6.id_produto
        LEFT JOIN entidade t9 ON t1.id_entidade_fornecedor = t9.id_entidade
        WHERE t1.codigo <> 1
        --GROUP BY t6.id_produto, t1.codigo, t2.codigo_barras, t1.referencia_interna_produto, t1.nome, t9.codigo, t4.sigla, t6.quantidade --t1.codigo, t2.codigo_barras, t1.referencia_interna_produto, t1.nome, t9.codigo, t4.sigla, t6.quantidade,
        ORDER BY t1.codigo'),
 (16,'Grupo de Permissões (Padrão) para operadores de Caixa','SET IDENTITY_INSERT PERMISSAO_GRUPO ON
INSERT INTO PERMISSAO_GRUPO (IDE, ID, CODIGO, NOME, SUPERUSUARIO, PADRAO, DATA_ALTERACAO, STATUS, ACESSA_TODAS_FILIAIS) VALUES (''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''2'',''2'',''CAIXA'',''0'', ''0'', ''2020-12-17 15:44:32.430'',''0'',''1'')
SET IDENTITY_INSERT PERMISSAO_GRUPO OFF

SET IDENTITY_INSERT PERMISSAO ON
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''C5511E04-029E-4D51-BC6B-A5E41E31AEA2'', ''1'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''87'', ''8'', ''2020-12-17 15:44:32.510'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''B9FC01F8-00F0-4ABB-93F5-CD407E6D4AB7'', ''2'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''251'', ''8'', ''2020-12-17 15:44:32.510'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''7253D998-2ED7-437C-91C8-70E0ECD93A1E'', ''3'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''84'', ''8'', ''2020-12-17 15:44:32.510'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''0AEDED35-FE66-44FA-8469-D8A1941E19A1'', ''4'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''51'', ''8'', ''2020-12-17 15:44:32.510'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''7739FE08-364D-47A4-8CB9-6963DF05C29E'', ''5'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''168'', ''8'', ''2020-12-17 15:44:32.510'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''B2BC83B7-66D0-442A-A4DE-4B025F046AEC'', ''6'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''89'', ''1'', ''2020-12-17 15:44:32.510'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''A0260331-F4BE-4FA1-832A-972C60FA9CC7'', ''7'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''90'', ''1'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''CBC943A3-85AF-4133-AA10-C9FC3E106705'', ''8'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''47'', ''1'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''B18A6503-2EC0-4B15-A95F-D532C3581693'', ''9'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''6'', ''3'', ''2020-12-17 15:44:32.463'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''C3FBB675-CCB4-4857-B4E7-058ACC706951'', ''10'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''33'', ''1'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''1E0C0F05-A323-430D-888D-14907EC02F08'', ''11'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''214'', ''1'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''9D659B9C-CBCB-4F60-9E71-E0BAF20E097D'', ''12'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''244'', ''8'', ''2020-12-17 15:44:32.510'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''A2E6DEF7-1DB8-44E1-8B6D-57F750663DDA'', ''13'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''49'', ''8'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''D63E6F0E-BE12-4F14-A59F-0F5ED7C7C673'', ''14'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''50'', ''8'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''06229A6E-7651-4CCF-93D6-5F6DD23668BB'', ''15'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''75'', ''8'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''C9A2AC74-8DF4-4D7A-BF7D-DFA92B08E288'', ''16'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''188'', ''8'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''E58570E3-3C20-4891-A697-D6E52FE17722'', ''17'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''189'', ''8'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''8DA01641-B605-4324-9407-F83FBC6EF556'', ''18'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''93'', ''8'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''2402B80B-A3D8-48B3-9193-3BC03B37A61F'', ''19'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''92'', ''8'', ''2020-12-17 15:44:32.527'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''ABB40693-D0CB-4307-9266-D314576B3A99'', ''20'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''243'', ''8'', ''2020-12-17 15:44:32.477'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''A4008D9C-2835-4AC7-B184-981101BBF8B0'', ''21'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''182'', ''1'', ''2020-12-17 15:44:32.463'', ''0'')
INSERT INTO PERMISSAO (IDE, ID, GRUPO__IDE, PERMISSAO_ID, PERMISSAO_TIPO, DATA_ALTERACAO, STATUS) VALUES (''AA4B89C0-60F3-4ED6-A395-036BDA6151A9'', ''22'', ''3FB37922-53CB-48DA-9166-2AB974E0F303'', ''120'', ''1'', ''2020-12-17 15:44:32.447'', ''0'')

SET IDENTITY_INSERT PERMISSAO OFF'),
 (17,'VR - SENHAS DE ACESSO À CONFIGURAÇÕES','SENHAS DE ACESSO À CONFIGURAÇÕES--------------------------------------------------
1º) Gourmet Droid: 
	Qual o filho(a) preferido(a) da Big Mom?  = "katakuri"


2º) E-Trade Partner:
	Qual foi o Shichibukai que recebeu o título de Yonkou durante a Guerra dos 	Melhores? = "teach"


3º) Bridge:
Eles são conhecidos como Promotores da Guerra, são os mercenários do submundo e estavam envolvidos no Golpe das Quatro Nações, eles são...?
	"germa66"


'),
 (18,'SCRIPTS - VERIFICAÇÃO DE VÍRUS','Para realizar uma verificação de vírus usando o PowerShell, você pode utilizar o cmdlet Get-MpComputerStatus, que é específico para o Windows Defender (ou Microsoft Defender, dependendo da versão do Windows). Este comando exibe o status da proteção contra vírus no computador.


1º - Abra o PowerShell como administrador.

2º - Digite o seguinte comando:
	Get-MpComputerStatus

Este comando exibirá informações sobre o status da proteção contra vírus, incluindo se há alguma ameaça detectada ou não no seu sistema.

Atenção!
Se você quiser realizar uma verificação completa do sistema em busca de vírus, pode usar o seguinte comando:

	Start-MpScan -ScanType FullScan

O comando Start-MpScan -ScanType FullScan inicia uma verificação completa do sistema em busca de ameaças. Este comando não fornece resultados imediatos no PowerShell; em vez disso, inicia a verificação, que pode levar um tempo para ser concluída, dependendo do tamanho e da quantidade de arquivos no seu sistema.
'),
 (19,'COMANDO DESEMPENHO DE ENERGIA','powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61'),
 (20,'ETrade - EXPORTA PRODUTOS.CSV','SELECT P.CODIGO,
P.NOME,
ISNULL(P.TIPO,''N'')[TIPO],
ISNULL(CI.CODIGO,1) [CLASSE DE IMPOSTO],
P.NCM,
UN.CODIGO,
ISNULL((SELECT  TOP 1 CAST(PP.PRECO AS NUMERIC(15,2)) FROM PRODUTOPRECO AS PP WHERE PP.PRODUTO__CODIGO = P.CODIGO AND PP.TABELAPRECO__IDE = ''1D05193A-5045-4592-AA17-E2C1EA4D9260''),0) [CUSTO], 
ISNULL((SELECT TOP 1 CAST(PP1.PRECO AS NUMERIC(15,2)) FROM PRODUTOPRECO AS PP1 WHERE PP1.PRODUTO__CODIGO = P.CODIGO AND PP1.TABELAPRECO__IDE = ''11627049-F321-42DE-A3ED-4101BADDBC32''),0) [PRECO],
MARGEM [LUCRO],
CODIGO_FABRICANTE1 [FABRICANTE 1],
CODIGO_FABRICANTE2 [FABRICANTE 2],
ISNULL(IIF(CS.NOME = ''NÃƒÆ’O ESPECIFICADO'', '''',CS.NOME),'''') [CLASSE],
ISNULL(IIF(SB.NOME = ''NÃƒÆ’O ESPECIFICADO'', '''',SB.NOME),'''') [SUBCLASSE],
P.LOCALIZACAO,
P.CODIGO_EAN,
ISNULL(IIF(MC.NOME = ''NÃƒÆ’O ESPECIFICADO'', '''',MC.NOME),0) [MARCA], 
ISNULL((SELECT TOP 1 CAST(QTDE AS NUMERIC) FROM ESTOQUE_ATUAL EA WHERE EA.PRODUTO = P.CODIGO AND FILIAL = 1),0) [ESTOQUE],
P.MEDABC [ABC FARMA], 
MEDNEGPOS [LISTA NEGATIVA POSITIVA],
MEDCODIGOANVISA [COD. ANVISA],
MEDPRINCIPIOATIVO,
ISNULL(CE.CODIGO,0) [CEST],
P.MEDPRECOMAXIMOCONSUMIDOR [PREÃƒâ€¡O MAXIMO], 
P.EXPORTAR_BALANCA [BALANÃƒâ€¡A], 
P.INATIVO,
ISNULL(IIF(FM.NOME = ''NÃƒÆ’O ESPECIFICADO'', '''',FM.NOME),'''') [FAMILIA],
ISNULL(IIF(GP.NOME = ''NÃƒÆ’O ESPECIFICADO'', '''',GP.NOME),'''') [GRUPO]
FROM PRODUTO P 
JOIN UNIDADEMEDIDA UN ON P.UNIDADE_VENDA__IDE=UN.IDE
LEFT JOIN CLASSES AS CS ON CS.CODIGO = P.CLASSE
LEFT JOIN CLASSEIMPOSTO CI ON P.CLASSEIMPOSTO__IDE = CI.IDE
LEFT JOIN SUBCLASSES AS SB ON SB.CODIGO = P.SUBCLASSE
LEFT JOIN MARCA AS MC ON MC.IDE = P.MARCA
LEFT JOIN CEST CE ON CE.IDE = P.CEST
LEFT JOIN FAMILIAS FM ON FM.CODIGO = P.FAMILIA
LEFT JOIN GRUPO GP ON GP.CODIGO = P.GRUPO
ORDER BY P.CODIGO_ORDENACAO'),
 (21,'ETrade - EXPORTA CLIENTES.CSV','SELECT CODIGO,
NOME,
CNPJ,
INSCRICAO,
ENDERECO,
NUMERO,
COMPLEMENTO,
BAIRRO,
CIDADE,
UF,
CEP,
FONE1,
FONE2,
NASCIMENTO,
ISNULL(TIPO,''C'') [TIPO],
ISNULL(FISICAJURIDICA,''F'') [FISICAJURIDICA],
FANTASIA,
EMAIL,
CONTATO,
OBS,
EMAILNFE,
NOMECONTADOR,
EMAILCONTADOR,
LIMITE_CREDITO 
FROM CLI_FOR'),
 (22,'ETrade - CONTAS A RECEBER.CSV','SELECT PAGAR_RECEBER,
CLIENTE__CODIGO,
VENCIMENTO,
VALOR,
'''' [PAGAMENTO],
'''' [VALOR PAGO],
DESCRICAO, 
PLANO_CONTA__CODIGO 
FROM FINANCEIRO_CONTA 
WHERE PAGAR_RECEBER= /*COLOCAR ''P'' PARA CONTAS A PAGAR E ''R'' PARA RECEBIVEIS*/ 
AND SITUACAO=''A'' 
AND STATUS <> -1'),
 (23,'Hiper - REDUÇÃO DE BANCO DE DADOS','Verificar se não existe operação pendente de sincronizar
    Realizar backup das bases (Todas)
    Rodar os scripts 


Fazer um backup das bases antes!




--Excluir XML
update hiperpdv_operacao_pdv set xml_nfce = null
where id_modelo_documento_fiscal = 8 and xml_nfce is not null
and situacao_replicacao = 10


--Reduzir Hiper
USE Hiper;
GO
ALTER DATABASE Hiper
SET RECOVERY SIMPLE;
GO
DBCC SHRINKFILE (Hiper, 1);
GO
ALTER DATABASE Hiper
SET RECOVERY FULL;
GO


--Em seguida deve ser executado o comando de shrink na base do Hiper.log (Roda na base Hiper)
USE Hiper;
GO
ALTER DATABASE Hiper
SET RECOVERY SIMPLE;
GO
DBCC SHRINKFILE (Hiper_log, 1);
GO
ALTER DATABASE Hiper
SET RECOVERY FULL;
GO'),
 (24,'ALTERA ALÍQUOTA DE ICMS EM MASSA','
/*verifica a quantidade de sincronização que está acontecendo no momento*/
select count(*) from produto where status_integracao = 2

--select * from hiperloja_sync_processamento
--update hiperloja_sync_processamento set DataEHoraDaUltimaSolicitacao = getdate() - 1



--1º
select  id_produto into #tempprod from regra_tributacao_icms_personalizada where id_situacao_tributaria_icms = 0 and aliquota_icms = 18

select *from regra_tributacao_icms_personalizada where id_situacao_tributaria_icms = 0 and aliquota_icms = 18



--2º
BEGIN TRAN
update t1
	set t1.aliquota_icms = 20.5

	from regra_tributacao_icms_personalizada t1
	where id_situacao_tributaria_icms = 0 and aliquota_icms = 18

--3º
begin tran
update produto set status_integracao = 2 where id_produto in (select id_produto from #tempprod where id_produto = id_produto)

select count(*) from produto where status_integracao = 2

/* puxa nova sincronização */
select * from hiperloja_sync_processamento
update hiperloja_sync_processamento set DataEHoraDaUltimaSolicitacao = getdate() - 1



/* força a sincronização com o gestão */
--4º
cd "C:\Hiper\Hiper.Sync.Loja\Logs"
Get-Content Hiper.Sync.Loja_$((Get-Date).tostring("ddMMyyyy")).log -wait
'),
 (25,'ENCONTRAR CHAVE DE ATIVAÇÃO','1º OPÇÃO
(Get-WmiObject -query ''select * from SoftwareLicensingService'').OA3xOriginalProductKey

2º OPÇÃO
wmic path SoftwareLicensingService get OA3xOriginalProductKey'),
 (26,'BACKUP BASES HIPER','DECLARE @name VARCHAR(50) -- database name
DECLARE @path VARCHAR(256) -- path for backup files
DECLARE @fileName VARCHAR(256) -- filename for backup
DECLARE @fileDate VARCHAR(20) -- used for file name
-- specify database backup directory
SET @path = ''C:\Hiper\''
-- specify filename format
SELECT @fileDate = CONVERT(VARCHAR(20),GETDATE(),112)
DECLARE db_cursor CURSOR READ_ONLY FOR
SELECT name
FROM master.dbo.sysdatabases
WHERE name NOT IN (''master'',''model'',''msdb'',''tempdb'') -- exclude these databases
OPEN db_cursor
FETCH NEXT FROM db_cursor INTO @name
WHILE @@FETCH_STATUS = 0
BEGIN
SET @fileName = @path + @fileDate + ''_'' + @name + ''.bak''
BACKUP DATABASE @name TO DISK = @fileName
FETCH NEXT FROM db_cursor INTO @name
END
CLOSE db_cursor
DEALLOCATE db_cursor'),
 (27,'BASE SUSPEITA HIPER','-- Passo 1
ALTERDATABASE Hiper SETEMERGENCY
ALTERDATABASE Hiper SETSINGLE_USERWITHROLLBACKIMMEDIATE

-- Passo 2
DBCC CheckDB (''Hiper'', REPAIR)

-- Passo 3
ALTERDATABASE Hiper SETMULTI_USER
ALTERDATABASE Hiper SETONLINE

-- Passo 4
USE Hiper EXECsp_msforeachtable''ALTER TABLE ? WITH CHECK CHECK CONSTRAINT ALL'''),
 (28,'HIPER - PYTHON(ACRECENTA PORCENTAGEM PRECO CUST. E VENDA)','import pandas as pd
from io import StringIO

path = ''precos.csv''

# Lista para armazenar linhas válidas do arquivo
lines = []

# Abrir o arquivo com encoding e ignorar linhas com problemas
with open(path, ''r'', encoding=''ISO-8859-1'', errors=''ignore'') as file:
    # Ler cada linha do arquivo
    for line in file:
        lines.append(line)

# Criar um DataFrame a partir das linhas válidas usando ponto e vírgula como delimitador
df = pd.read_csv(StringIO(''\n''.join(lines)), delimiter='';'', decimal='','')

# Exibir os nomes das colunas
print(df.columns)

# Converter a coluna ''PRECO_MINIMO_VENDA'' e ''PRECO_VENDA'' para numérica
df[''PRECO_MINIMO_VENDA''] = pd.to_numeric(df[''PRECO_MINIMO_VENDA''], errors=''coerce'')
df[''PRECO_VENDA''] = pd.to_numeric(df[''PRECO_VENDA''], errors=''coerce'')

# Adicionar 2,5% aos preços
df[''PRECO_MINIMO_VENDA''] = df[''PRECO_MINIMO_VENDA''] * 1.025
df[''PRECO_VENDA''] = df[''PRECO_VENDA''] * 1.025

# Salvar de volta no arquivo CSV
df.to_csv(''preco_atualizado.csv'', index=False, sep='';'', decimal='','')
');
INSERT INTO "INSTALADORES" ("idARQUIVO","DESCRICAO","LINK_ARQUIVO") VALUES (1,'Hiper.Setup','https://downloads.hiper.com.br/Hiper.Setup.exe'),
 (2,'E-Trade instalador','https://vrsystem.info/files/Install_ETrade.exe'),
 (3,'E-Trade versão stable','https://vrsystem.info/files/Stable_ETrade.exe'),
 (4,'Bancos de Dados dos Estados','https://drive.google.com/drive/folders/1hvI1N9nA7PSZx-5HV53qjzI7ekTcJcTf'),
 (5,'SQL Server 2014 + SSMS x86','https://download.microsoft.com/download/0/1/5/015567C0-E851-4AC6-964F-9BBA9B31D6BC/ExpressAndTools%2032BIT/SQLEXPRWT_x86_PTB.exe'),
 (6,'SQL Server 2014 + SSMS x64','https://download.microsoft.com/download/0/1/5/015567C0-E851-4AC6-964F-9BBA9B31D6BC/ExpressAndTools%2064BIT/SQLEXPRWT_x64_PTB.exe'),
 (7,'SQL Server® 2019 Express','https://www.microsoft.com/pt-br/download/confirmation.aspx?id=101064'),
 (8,'teste_teste','teste.com'),
 (9,'Setup TechTools','https://drive.google.com/drive/my-drive'),
 (14,'Reset de impressoras AdjProgram','https://arquivos.blogdainformatica.com.br/resets/Epson-L455-Resetter.zip'),
 (15,'Tutorial Reseat Adj Program','https://www.baixesoft.com/download/resetter-da-impressora-epson-l455');
INSERT INTO "DRIVERS" ("idDRIVER","DESCRICAO","LINK_DRIVER") VALUES (1,'Bematech MP-100S TH 32bits','https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_100_SpoolerDrivers_x86_v4.4.0.3.rar'),
 (2,'Bematech MP-100S TH 64bits','https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_100_SpoolerDrivers_x64_v4.4.0.3.rar'),
 (3,'Bematech MP-2800 TH 32 bits','https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_2800_SpoolerDrivers_x86_v1.3.rar'),
 (4,'Bematech MP-2800 TH 64 bits','https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_2800_SpoolerDrivers_x64_v1.3.rar'),
 (5,'Bematech MP-4200 TH 32 bits','https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_4200_SpoolerDrivers_x86_v4.3.1.0.rar'),
 (6,'Bematech MP-4200 TH 64 bits','https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_4200_SpoolerDrivers_x64_v4.3.1.0.rar'),
 (7,'Diebold Todos os Drivers','https://dieboldnixdorf.com.br/wp-content/uploads/2021/04/4900c52a69e4dd711601380202f91e8b-1.zip'),
 (8,'Daruma DR-800','https://drive.google.com/drive/folders/17nZFyaAZsFN-Ub3-kaj2Qg6TSqaIDROf'),
 (9,'Epson TM-T20','https://download.epson-biz.com/modules/pos/index.php?page=single_soft&cid=6888&scat=31&pcat=3'),
 (10,'Epson TM-T20X','https://ftp.epson.com/latin/drivers/pos/APD_601_T20X_WM.zip'),
 (11,'Epson TM-T70II','https://encr.pw/vhaRp'),
 (12,'Epson Térmica TM-T88VII','https://epson.com.br/Suporte/Ponto-de-venda/Impressoras-térmicas/Epson-TM-T88VII-Series/s/SPT_C31CJ57052'),
 (13,'Epson L375','https://ftp.epson.com/latin/drivers/inkjet/L375_Lite_LA.exe'),
 (14,'Epson L1250','https://ftp.epson.com/latin/drivers/inkjet/L1250_Lite_LA.exe'),
 (15,'Epson L3110','https://ftp.epson.com/latin/drivers/Multi/l3110/L3110_Lite_LA.exe'),
 (16,'Epson L3210','https://ftp.epson.com/latin/drivers/inkjet/L3210_Lite_LA.exe'),
 (17,'Epson L3250','https://ftp.epson.com/latin/drivers/inkjet/L3250_L3251_Lite_LA.exe'),
 (18,'Epson L3251','https://epson.com.br/c/Epson-L3251/s/SPT_C11CJ67302'),
 (19,'Epson L3252','https://www.epson.co.in/Support/Printers/All-In-One/L-Series/Epson-L3252/s/SPT_C11CJ67511'),
 (20,'Epson L4160','https://ftp.epson.com/latin/drivers/inkjet/L4160_Lite_LA.exe'),
 (21,'Epson L4260','https://ftp.epson.com/latin/drivers/inkjet/L4260_Lite_LA.exe'),
 (22,'Elgin i7/i9','https://www.elgin.com.br/assets/arquivos/imgCard_4ce638a5-22e5-4a0d-a820-0108152ced91_imgCard_3969ab8d-70ab-4b53-ac90-d84cc55ddd70_ELGIN%20i9%20Printer%20Driver_v-1.7.3.rar'),
 (23,'HP DeskJet 2774','https://arquivos.blogdainformatica.com.br/drivers/impressoras/hp/hp-deskjet-ink-2770/HPEasyStart-13.6.5-DJ2700_51_4_4865_1_Webpack.exe?md5=7Rcm0COquWIQHQax9e1pLA&expires=1681620578'),
 (24,'HP Ink Tank Wireless 416','https://ftp.ext.hp.com/pub/softlib/software13/printers/ITW410/Full_Webpack-45.4.2608-ITW410_Full_Webpack.exe'),
 (25,'Samsung ML-2160','https://ftp.hp.com/pub/softlib/software13/printers/SS/SL-M3370FD/SamsungUniversalPrintDriver3.exe'),
 (26,'Xerox Phaser 3020','https://www.support.xerox.com/pt-br/product/phaser-3020/downloads?language=pt_BR#'),
 (27,'Zebra Z800','https://www.zebra.com/br/pt/support-downloads/eula/unrestricted-eula.7b8a235653193b4c72c440110c25661656f56f5180957c98e7c0bc2144149cd156a1bc6e684725abae8eaa3b64ee1090a63134434792cf7fe7ebd953120a60cd367633fe9f513f4ae43f722b47f328b04e84f768a150ebe0.html#'),
 (28,'Argox All Driver','https://drive.google.com/uc?id=134HjCgrHHWQ9CArgcSUUowsK0H3nrxR6&export=download'),
 (29,'Elgin L42 PRO FULL','https://l1nq.com/N6Ju1'),
 (30,'Zebra ZD420','https://l1nq.com/lS9Ok'),
 (31,'Zebra ZD421','https://l1nq.com/lS9Ok'),
 (32,'Zebra ZD621','https://l1nq.com/lS9Ok'),
 (33,'Zebra ZD621R RFID','https://l1nq.com/lS9Ok'),
 (34,'Zebra GK420T','https://l1nq.com/xSIlz'),
 (35,'Bematech LB-1000','https://l1nq.com/6ASQV'),
 (36,'POS-58 ou POS-80','https://baixar.programanex.com.br/extras/impressoras/POS58/POS_58_Driver-11.3.0.0.zip'),
 (37,'Epson L1250','https://ftp.epson.com/latin/drivers/inkjet/L1250_Lite_LA.exe'),
 (38,'Epson L455','https://epson.com.br/Suporte/Impressoras/Impressoras-multifuncionais/Epson-L/Epson-EcoTank-L455/s/SPT_C11CE24301?review-filter=Windows+8+64-bit');

