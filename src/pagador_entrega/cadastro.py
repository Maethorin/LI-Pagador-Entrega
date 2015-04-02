# -*- coding: utf-8 -*-
from li_common.padroes import cadastro

TIPOS = [
    (1, 'dinheiro', 'Dinheiro'),
    (2, 'cheque', 'Cheque'),
    (3, 'cartao_debito_mastercard', 'Cartão de débito MasterCard'),
    (4, 'cartao_debito_visa', 'Cartão de débito Visa'),
    (5, 'cartao_debito_elo', 'Cartão de débito Elo'),
    (6, 'cartao_debito_cabal', 'Cartão de débito Cabal'),
    (7, 'cartao_credito_mastercard', 'Cartão de crédito MasterCard'),
    (8, 'cartao_credito_visa', 'Cartão de crédito Visa'),
    (9, 'cartao_credito_elo', 'Cartão de crédito Elo'),
    (10, 'cartao_credito_cabal', 'Cartão de crédito Cabal'),
    (11, 'cartao_credito_hipercard', 'Cartão de crédito Hipercard'),
    (12, 'cartao_credito_diners', 'Cartão de crédito Diners'),
    (13, 'cartao_credito_americanexpress', 'Cartão de crédito American Express'),
    (14, 'cartao_sodexo_refeicao', 'Cartão Sodexo Refeição'),
    (15, 'cartao_sodexo_alimentacao', 'Cartão Sodexo Alimentação'),
    (16, 'cartao_alelo_refeicao', 'Cartão Alelo Refeição'),
    (17, 'cartao_alelo_alimentacao', 'Cartão Alelo Alimentação'),
]

TIPO_BASE = {
    'id': None,
    'nome': None,
    'ativo': False,
}


class TiposValidador(cadastro.ValidadorBase):
    @property
    def eh_valido(self):
        valido = True
        if type(self.valor) is not list:
            valido = False
            self.erros['lista'] = 'Os tipos devem ser uma lista.'
        for tipo in self.valor:
            erros = []
            for chave in TIPO_BASE:
                if chave not in tipo:
                    valido = False
                    erros.append(u'Não foi enviado o atributo {} do tipo {}'.format(chave, tipo))
            if erros:
                self.erros['atributos'] = erros
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
    tipos = cadastro.CampoFormulario('json', ordem=0, tipo=cadastro.TipoDeCampo.oculto, formato=cadastro.FormatoDeCampo.json, opcoes=TIPOS, validador=TiposValidador)
    ativo = cadastro.CampoFormulario('ativo', u'Pagamento ativo?', ordem=1, tipo=cadastro.TipoDeCampo.boleano)
    valor_minimo_aceitado = cadastro.CampoFormulario('valor_minimo_aceitado', u'Valor mínimo', requerido=False, decimais=2, ordem=2, tipo=cadastro.TipoDeCampo.decimal, texto_ajuda=u'Informe o valor mínimo para exibir esta forma de pagamento.')
    tem_desconto = cadastro.CampoFormulario('desconto', u'Usar desconto?', requerido=False, ordem=3, tipo=cadastro.TipoDeCampo.boleano, texto_ajuda=u'Define se esta forma de pagamento usará desconto.')
    desconto_valor = cadastro.CampoFormulario('desconto_valor', u'Desconto aplicado', requerido=False, ordem=4, tipo=cadastro.TipoDeCampo.decimal, validador=DescontoValidador)
    aplicar_no_total = cadastro.CampoFormulario('aplicar_no_total',  u'Aplicar no total?', requerido=False, ordem=5, tipo=cadastro.TipoDeCampo.boleano, texto_ajuda=u'Aplicar desconto no total da compra (incluir por exemplo o frete).')
