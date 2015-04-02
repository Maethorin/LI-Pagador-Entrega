# -*- coding: utf-8 -*-
from li_common.padroes import cadastro

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


class TiposValidador(cadastro.ValidadorBase):
    @property
    def eh_valido(self):
        valido = True
        if type(self.valor) is not list:
            valido = False
            self.erros['lista'] = 'Os tipos devem ser uma lista.'
        return valido


class DescontoValidador(cadastro.ValidadorBase):
    @property
    def eh_valido(self):
        try:
            valor = float(self.valor)
            if valor > 100.0 or valor < 0.0:
                self.erros = u'Porcentagem inválida. Insira um valor entre 0% e 100%.'
        except (TypeError, ValueError):
            self.erros = u'Porcentagem inválida. Insira um valor entre 0% e 100%.'
        return not self.erros


class FormularioEntrega(cadastro.Formulario):
    tipos = cadastro.CampoFormulario('json', ordem=0, tipo=cadastro.TipoDeCampo.oculto, formato=cadastro.FormatoDeCampo.json, validador=TiposValidador)
    ativo = cadastro.CampoFormulario('ativo', u'Pagamento ativo?', ordem=1, tipo=cadastro.TipoDeCampo.boleano)
    valor_minimo_aceitado = cadastro.CampoFormulario('valor_minimo_aceitado', u'Valor mínimo', requerido=False, decimais=2, ordem=2, tipo=cadastro.TipoDeCampo.decimal, texto_ajuda=u'Informe o valor mínimo para exibir esta forma de pagamento.')
    tem_desconto = cadastro.CampoFormulario('desconto', u'Usar desconto?', requerido=False, ordem=3, tipo=cadastro.TipoDeCampo.boleano, texto_ajuda=u'Define se esta forma de pagamento usará desconto.')
    desconto_valor = cadastro.CampoFormulario('desconto_valor', u'Desconto aplicado', requerido=False, ordem=4, tipo=cadastro.TipoDeCampo.decimal, validador=DescontoValidador)
    aplicar_no_total = cadastro.CampoFormulario('aplicar_no_total', u'Aplicar no total?', requerido=False, ordem=5, tipo=cadastro.TipoDeCampo.boleano, texto_ajuda=u'Aplicar desconto no total da compra (incluir por exemplo o frete).')
