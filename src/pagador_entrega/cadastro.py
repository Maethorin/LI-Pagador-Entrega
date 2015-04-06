# -*- coding: utf-8 -*-
from li_common.padroes import cadastro


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
