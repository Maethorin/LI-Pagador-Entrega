# -*- coding: utf-8 -*-
from pagador import entidades
from pagador_entrega import cadastro

CODIGO_GATEWAY = 13

TIPOS = [
    {'id': 1, 'value': 'dinheiro', 'label': 'Dinheiro'},
    {'id': 2, 'value': 'cheque', 'label': 'Cheque'},
    {'id': 3, 'value': 'cartao_debito_mastercard', 'label': 'Cartão de débito MasterCard'},
    {'id': 4, 'value': 'cartao_debito_visa', 'label': 'Cartão de débito Visa'},
    {'id': 5, 'value': 'cartao_debito_elo', 'label': 'Cartão de débito Elo'},
    {'id': 6, 'value': 'cartao_debito_cabal', 'label': 'Cartão de débito Cabal'},
    {'id': 7, 'value': 'cartao_credito_mastercard', 'label': 'Cartão de crédito MasterCard'},
    {'id': 8, 'value': 'cartao_credito_visa', 'label': 'Cartão de crédito Visa'},
    {'id': 9, 'value': 'cartao_credito_elo', 'label': 'Cartão de crédito Elo'},
    {'id': 10, 'value': 'cartao_credito_cabal', 'label': 'Cartão de crédito Cabal'},
    {'id': 11, 'value': 'cartao_credito_hipercard', 'label': 'Cartão de crédito Hipercard'},
    {'id': 12, 'value': 'cartao_credito_diners', 'label': 'Cartão de crédito Diners'},
    {'id': 13, 'value': 'cartao_credito_americanexpress', 'label': 'Cartão de crédito American Express'},
    {'id': 14, 'value': 'cartao_sodexo_refeicao', 'label': 'Cartão Sodexo Refeição'},
    {'id': 15, 'value': 'cartao_sodexo_alimentacao', 'label': 'Cartão Sodexo Alimentação'},
    {'id': 16, 'value': 'cartao_alelo_refeicao', 'label': 'Cartão Alelo Refeição'},
    {'id': 17, 'value': 'cartao_alelo_alimentacao', 'label': 'Cartão Alelo Alimentação'},
]


class Malote(entidades.Malote):
    def __init__(self, configuracao):
        super(Malote, self).__init__(configuracao)
        self.tipo_pagamento = None
        self.valor_troco = None

    def monta_conteudo(self, pedido, parametros_contrato=None, dados=None):
        self.tipo_pagamento = dados['tipo_pagamento']
        self.valor_troco = dados['valor_troco']


class ConfiguracaoMeioPagamento(entidades.ConfiguracaoMeioPagamento):
    modos_pagamento_aceitos = {
        #'outros': ['entrega'],
    }

    def __init__(self, loja_id, codigo_pagamento=None, eh_listagem=False):
        self.campos = ['ativo', 'valor_minimo_aceitado', 'desconto', 'desconto_valor', 'aplicar_no_total', 'json']
        self.codigo_gateway = CODIGO_GATEWAY
        self.eh_gateway = True
        self.tipos = TIPOS
        super(ConfiguracaoMeioPagamento, self).__init__(loja_id, codigo_pagamento, eh_listagem=eh_listagem)

        if not self.json:
            self.json = []

        if not self.eh_listagem:
            self.formulario = cadastro.FormularioEntrega()
