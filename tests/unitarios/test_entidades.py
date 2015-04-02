# -*- coding: utf-8 -*-
import unittest
import mock
from pagador_entrega import cadastro, entidades


class EntregaConfiguracaoMeioPagamento(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(EntregaConfiguracaoMeioPagamento, self).__init__(*args, **kwargs)
        self.campos = ['ativo', 'valor_minimo_aceitado', 'desconto', 'desconto_valor', 'aplicar_no_total', 'json']
        self.codigo_gateway = 13

    @mock.patch('pagador_entrega.entidades.ConfiguracaoMeioPagamento.preencher_gateway', mock.MagicMock())
    def test_deve_ter_os_campos_especificos_na_classe(self):
        entidades.ConfiguracaoMeioPagamento(234).campos.should.be.equal(self.campos)

    @mock.patch('pagador_entrega.entidades.ConfiguracaoMeioPagamento.preencher_gateway', mock.MagicMock())
    def test_deve_ter_codigo_gateway(self):
        entidades.ConfiguracaoMeioPagamento(234).codigo_gateway.should.be.equal(self.codigo_gateway)

    @mock.patch('pagador_entrega.entidades.ConfiguracaoMeioPagamento.preencher_gateway', autospec=True)
    def test_deve_definir_gateway_na_inicializacao(self, preencher_mock):
        configuracao = entidades.ConfiguracaoMeioPagamento(234)
        preencher_mock.assert_called_with(configuracao, self.codigo_gateway, self.campos)

    @mock.patch('pagador_entrega.entidades.ConfiguracaoMeioPagamento.preencher_gateway', mock.MagicMock())
    def test_deve_definir_formulario_na_inicializacao(self):
        configuracao = entidades.ConfiguracaoMeioPagamento(234)
        configuracao.formulario.should.be.a('pagador_entrega.cadastro.FormularioEntrega')

    @mock.patch('pagador_entrega.entidades.ConfiguracaoMeioPagamento.preencher_gateway', mock.MagicMock())
    def test_deve_definir_tipos_na_inicializacao(self):
        configuracao = entidades.ConfiguracaoMeioPagamento(234)
        configuracao.tipos.should.be.equal(cadastro.TIPOS)

    @mock.patch('pagador_entrega.entidades.ConfiguracaoMeioPagamento.preencher_gateway', mock.MagicMock())
    def test_deve_ser_aplicacao(self):
        configuracao = entidades.ConfiguracaoMeioPagamento(234)
        configuracao.eh_aplicacao.should.be.falsy

