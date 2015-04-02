# -*- coding: utf-8 -*-
from pagador import entidades
from pagador_entrega import cadastro

CODIGO_GATEWAY = 13


class ConfiguracaoMeioPagamento(entidades.ConfiguracaoMeioPagamento):
    def __init__(self, loja_id, codigo_pagamento=None, eh_listagem=False):
        self.campos = ['ativo', 'valor_minimo_aceitado', 'desconto', 'desconto_valor', 'aplicar_no_total', 'json']
        self.codigo_gateway = CODIGO_GATEWAY
        self.eh_gateway = True
        self.tipos = cadastro.TIPOS
        super(ConfiguracaoMeioPagamento, self).__init__(loja_id, codigo_pagamento, eh_listagem=eh_listagem)

        if not self.json:
            self.json = []

        if not self.eh_listagem:
            self.formulario = cadastro.FormularioEntrega()
