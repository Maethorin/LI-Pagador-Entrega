# -*- coding: utf-8 -*-
import unittest
from pagador_retirada import cadastro


class FormularioRetirada(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(FormularioRetirada, self).__init__(*args, **kwargs)
        self.formulario = cadastro.FormularioRetirada()

    def test_deve_ter_bandeiras(self):
        self.formulario.tipos.nome.should.be.equal('json')
        self.formulario.tipos.ordem.should.be.equal(0)
        self.formulario.tipos.formato.should.be.equal(cadastro.cadastro.FormatoDeCampo.json)
        self.formulario.tipos.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.oculto)
        self.formulario.tipos.opcoes.should.be.equal(cadastro.TIPOS)
        self.formulario.tipos.validador.should.be.equal(cadastro.TiposValidador)

    def test_deve_ter_ativo(self):
        self.formulario.ativo.nome.should.be.equal('ativo')
        self.formulario.ativo.ordem.should.be.equal(1)
        self.formulario.ativo.label.should.be.equal(u'Pagamento ativo?')
        self.formulario.ativo.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.boleano)

    def test_deve_ter_valor_minimo_aceitado(self):
        self.formulario.valor_minimo_aceitado.nome.should.be.equal('valor_minimo_aceitado')
        self.formulario.valor_minimo_aceitado.ordem.should.be.equal(2)
        self.formulario.valor_minimo_aceitado.label.should.be.equal(u'Valor mínimo')
        self.formulario.valor_minimo_aceitado.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.decimal)

    def test_deve_ter_desconto(self):
        self.formulario.tem_desconto.nome.should.be.equal('desconto')
        self.formulario.tem_desconto.ordem.should.be.equal(3)
        self.formulario.tem_desconto.label.should.be.equal(u'Usar desconto?')
        self.formulario.tem_desconto.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.boleano)

    def test_deve_ter_desconto_valor(self):
        self.formulario.desconto_valor.nome.should.be.equal('desconto_valor')
        self.formulario.desconto_valor.ordem.should.be.equal(4)
        self.formulario.desconto_valor.label.should.be.equal(u'Desconto aplicado')
        self.formulario.desconto_valor.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.decimal)
        self.formulario.desconto_valor.validador.should.be.equal(cadastro.DescontoValidador)

    def test_deve_ter_aplicar_no_total(self):
        self.formulario.aplicar_no_total.nome.should.be.equal('aplicar_no_total')
        self.formulario.aplicar_no_total.ordem.should.be.equal(5)
        self.formulario.aplicar_no_total.label.should.be.equal(u'Aplicar no total?')
        self.formulario.aplicar_no_total.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.boleano)


class ValidadorBancos(unittest.TestCase):
    def test_deve_adicionar_erro_se_nao_for_lista(self):
        validador = cadastro.TiposValidador(valor='nao-eh-lista')
        validador.eh_valido.should.be.equal(False)
        validador.erros.should.contain('lista')
        validador.erros['lista'].should.be.equal('Os tipos devem ser uma lista.')

    def test_deve_adicionar_erro_para_atributos_faltando(self):
        validador = cadastro.TiposValidador(valor=['faltando'])
        validador.eh_valido.should.be.equal(False)
        validador.erros.should.be.equal({
            'atributos': [
                u'Não foi enviado o atributo ativo do tipo faltando',
                u'Não foi enviado o atributo id do tipo faltando',
                u'Não foi enviado o atributo nome do tipo faltando',
            ]
        })

    def test_deve_ser_valido_se_conter_todos_os_atributos(self):
        validador = cadastro.TiposValidador(valor=[cadastro.TIPO_BASE.copy()])
        validador.eh_valido.should.be.equal(True)
        validador.erros.should.be.empty


class ValidarDesconto(unittest.TestCase):
    def test_deve_validar_maior_que_100(self):
        validador = cadastro.DescontoValidador(valor='123.94')
        validador.eh_valido.should.be.equal(False)
        validador.erros.should.be.equal(u'Porcentagem inválida. Insira um valor entre 0% e 100%.')

    def test_deve_validar_menor_que_0(self):
        validador = cadastro.DescontoValidador(valor='-0.5')
        validador.eh_valido.should.be.equal(False)
        validador.erros.should.be.equal(u'Porcentagem inválida. Insira um valor entre 0% e 100%.')

    def test_deve_validar_none(self):
        validador = cadastro.DescontoValidador(valor=None)
        validador.eh_valido.should.be.equal(False)
        validador.erros.should.be.equal(u'Porcentagem inválida. Insira um valor entre 0% e 100%.')

    def test_deve_validar_se_valor_gerar_value_error(self):
        validador = cadastro.DescontoValidador(valor='asdds')
        validador.eh_valido.should.be.equal(False)
        validador.erros.should.be.equal(u'Porcentagem inválida. Insira um valor entre 0% e 100%.')

    def test_deve_retornar_ok_se_valor_for_certo(self):
        validador = cadastro.DescontoValidador(valor='50.43444')
        validador.eh_valido.should.be.equal(True)
        validador.erros.should.be.empty
