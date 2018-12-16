# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:12:24 2018

@author: Fabrício
"""

import tkinter

import psycopg2

import frontend

import backend


class MainMenu(frontend.MenuPrincipal):
    """Atribua comandos aos botões do menu principal"""
    def __init__(self):
        frontend.MenuPrincipal.__init__(self)
        self.button_paciente["command"] = self.get_paciente
        self.button_profissional["command"] = self.get_profissional
        self.button_sala["command"] = self.get_sala
        self.button_equipamento["command"] = self.get_equipamento
        self.button_servico["command"] = self.get_servico
        self.button_servico["command"] = self.get_servico
        self.button_equip_serv["command"] = self.get_equip_ser
        self.button_estatistica["command"] = self.get_estatistica

    def get_paciente(self):
        """Invoque a GUI Paciente."""
        MainPaciente(self)

    def get_profissional(self):
        """Invoque a GUI Profissional"""
        MainProfissional(self)

    def get_sala(self):
        """Invoque a GUI Sala."""
        MainSala(self)

    def get_equipamento(self):
        """Invoque a GUI Equipamento."""
        MainEquipamento(self)

    def get_servico(self):
        """Invoque a GUI Serviço."""
        MainServico(self)

    def get_equip_ser(self):
        """Invoque a GUI Equipamento-Serviço."""
        MainEquipSer(self)

    def get_estatistica(self):
        """Invoque a GUI Estatistica."""
        MainEstatistica(self)


class MainPaciente(backend.BackendPaciente):
    """Atribua comandos aos botões da GUI Paciente."""
    def __init__(self, main):
        backend.BackendPaciente.__init__(self)
        self.gui = frontend.GUIPaciente(main)
        self.gui.btn_inserir["command"] = self.comando_inserir
        self.gui.btn_listar["command"] = self.comando_listar
        self.gui.btn_selecionar["command"] = self.comando_selecionar
        self.gui.btn_atualizar["command"] = self.comando_atualizar
        self.gui.btn_deletar["command"] = self.comando_deletar
        self.gui.btn_retornar["command"] = self.gui.destroy

    def comando_inserir(self):
        """Realize o comando INSERT na tabela Paciente."""
        try:
            self.inserir_paciente(self.gui.txt_cpf.get(),
                                  self.gui.txt_nome.get(),
                                  self.gui.txt_idade.get(),
                                  self.gui.txt_sexo.get(),
                                  self.gui.txt_doenca.get(),
                                  self.gui.txt_altura.get(),
                                  self.gui.txt_peso.get(),
                                  self.gui.txt_cidade.get(),
                                  self.gui.txt_bairro.get(),
                                  self.gui.txt_rua.get(),
                                  self.gui.txt_numero.get(),
                                  self.gui.txt_complemento.get())
        except psycopg2.IntegrityError:
            print('CPF já utilizado.')
        except psycopg2.ProgrammingError:
            print('Inseriu letras em campos númericos.')
        except psycopg2.DataError:
            print('Ultrapassou o limite de caracteres ou números de '
                  'um campo.\n'
                  '(OBS: Altura deve ser colocada em metros ex.: 1.75)')

    def comando_listar(self):
        """Realize o comando SELECT de tudo na tabela Paciente."""
        self.listar_paciente()

    def comando_selecionar(self):
        """Realize o comando SELECT na tabela Paciente."""
        try:
            self.selecionar_paciente(self.gui.txt_codigo.get(),
                                     self.gui.txt_cpf.get(),
                                     self.gui.txt_nome.get(),
                                     self.gui.txt_idade.get(),
                                     self.gui.txt_sexo.get(),
                                     self.gui.txt_doenca.get(),
                                     self.gui.txt_altura.get(),
                                     self.gui.txt_peso.get(),
                                     self.gui.txt_cidade.get(),
                                     self.gui.txt_bairro.get(),
                                     self.gui.txt_rua.get(),
                                     self.gui.txt_numero.get(),
                                     self.gui.txt_complemento.get())
        except tkinter.TclError:
            print('Insira um número no campo Código (não vazio).')
        except psycopg2.ProgrammingError:
            print('Inseriu letras em campos númericos.')

    def comando_atualizar(self):
        """Realize o comando UPDATE na tabela Paciente."""
        try:
            self.atualizar_paciente(self.gui.txt_cpf.get(),
                                    self.gui.txt_nome.get(),
                                    self.gui.txt_idade.get(),
                                    self.gui.txt_sexo.get(),
                                    self.gui.txt_doenca.get(),
                                    self.gui.txt_altura.get(),
                                    self.gui.txt_peso.get(),
                                    self.gui.txt_cidade.get(),
                                    self.gui.txt_bairro.get(),
                                    self.gui.txt_rua.get(),
                                    self.gui.txt_numero.get(),
                                    self.gui.txt_complemento.get(),
                                    self.gui.txt_codigo.get())
        except tkinter.TclError:
            print('Insira um número no campo Código (não vazio).')
        except psycopg2.ProgrammingError:
            print('Inseriu letras em campos númericos.')
        except psycopg2.DataError:
            print('Ultrapassou o limite de caracteres ou números de '
                  'um campo.\n'
                  '(OBS: Altura deve ser colocada em metros ex.: 1.75)')

    def comando_deletar(self):
        """Realize o comando DELETE na tabela Paciente."""
        try:
            self.deletar_paciente(self.gui.txt_codigo.get())
        except tkinter.TclError:
            print('Insira um número no campo Código (não vazio).')


class MainProfissional(backend.BackendProfissional):
    """Atribua comandos aos botões da GUI Profissional."""
    def __init__(self, main):
        backend.BackendProfissional.__init__(self)
        self.gui = frontend.GUIProfissional(main)
        self.gui.btn_inserir["command"] = self.comando_inserir
        self.gui.btn_listar["command"] = self.comando_listar
        self.gui.btn_selecionar["command"] = self.comando_selecionar
        self.gui.btn_atualizar["command"] = self.comando_atualizar
        self.gui.btn_deletar["command"] = self.comando_deletar
        self.gui.btn_retornar["command"] = self.gui.destroy

    def comando_inserir(self):
        """Realize o comando INSERT na tabela Profissional."""
        try:
            self.inserir_profissional(self.gui.txt_cnpj.get(),
                                      self.gui.txt_nome.get(),
                                      self.gui.txt_salario.get(),
                                      self.gui.txt_atuacao.get())
        except tkinter.TclError:
            print('Insira um valor no campo Salário (não vazio).')
        except psycopg2.DataError:
            print('Ultrapassou o limite de caracteres ou números de um campo.')

    def comando_listar(self):
        """Realize o comando SELECT de tudo na tabela Profissional."""
        self.listar_profissional()

    def comando_selecionar(self):
        """Realize o comando SELECT na tabela Profissional."""
        try:
            self.selecionar_profissional(self.gui.txt_codigo.get(),
                                         self.gui.txt_cnpj.get(),
                                         self.gui.txt_nome.get(),
                                         self.gui.txt_salario.get(),
                                         self.gui.txt_atuacao.get())
        except tkinter.TclError:
            print('Insira um número nos campos numéricos (não vazio).')

    def comando_atualizar(self):
        """Realize o comando UPDATE na tabela Profissional."""
        try:
            self.atualizar_profissional(self.gui.txt_cnpj.get(),
                                        self.gui.txt_nome.get(),
                                        self.gui.txt_salario.get(),
                                        self.gui.txt_atuacao.get(),
                                        self.gui.txt_codigo.get())
        except tkinter.TclError:
            print('Insira um número nos campos numéricos (não vazio).')
        except psycopg2.DataError:
            print('Ultrapassou o limite de caracteres ou números de um campo.')

    def comando_deletar(self):
        """Realize o comando DELETE na tabela Profissional."""
        try:
            self.deletar_profissional(self.gui.txt_codigo.get())
        except tkinter.TclError:
            print('Insira um número no campo Código (não vazio).')


class MainSala(backend.BackendSala):
    """Atribua comandos aos botões da GUI Sala."""
    def __init__(self, main):
        backend.BackendSala.__init__(self)
        self.gui = frontend.GUISala(main)
        self.gui.btn_inserir["command"] = self.comando_inserir
        self.gui.btn_listar["command"] = self.comando_listar
        self.gui.btn_selecionar["command"] = self.comando_selecionar
        self.gui.btn_atualizar["command"] = self.comando_atualizar
        self.gui.btn_deletar["command"] = self.comando_deletar
        self.gui.btn_retornar["command"] = self.gui.destroy

    def comando_inserir(self):
        """Realize o comando INSERT na tabela Sala."""
        try:
            self.inserir_sala(self.gui.txt_sigla.get(),
                              self.gui.txt_capacidade.get())
        except tkinter.TclError:
            print('Insira um número no campo Capacidade (não vazio).')
        except psycopg2.DataError:
            print('Ultrapassou o limite de caracteres ou números de um campo.')

    def comando_listar(self):
        """Realize o comando SELECT de tudo na tabela Sala."""
        self.listar_sala()

    def comando_selecionar(self):
        """Realize o comando SELECT na tabela Sala."""
        try:
            self.selecionar_sala(self.gui.txt_sigla.get(),
                                 self.gui.txt_capacidade.get())
        except tkinter.TclError:
            print('Insira um número no campo Capacidade (não vazio).')

    def comando_atualizar(self):
        """Realize o comando UPDATE na tabela Sala."""
        try:
            self.atualizar_sala(self.gui.txt_sigla.get(),
                                self.gui.txt_capacidade.get())
        except tkinter.TclError:
            print('Insira um número no campo Capacidade (não vazio).')

    def comando_deletar(self):
        """Realize DELETE na tabela Sala."""
        self.deletar_sala(self.gui.txt_sigla.get())



class MainEquipamento(backend.BackendEquipamento):
    """Atribua comandos aos botões da GUI Equipamento."""
    def __init__(self, main):
        backend.BackendEquipamento.__init__(self)
        self.gui = frontend.GUIEquipamento(main)
        self.gui.btn_inserir["command"] = self.comando_inserir
        self.gui.btn_listar["command"] = self.comando_listar
        self.gui.btn_selecionar["command"] = self.comando_selecionar
        self.gui.btn_atualizar["command"] = self.comando_atualizar
        self.gui.btn_deletar["command"] = self.comando_deletar
        self.gui.btn_retornar["command"] = self.gui.destroy

    def comando_inserir(self):
        """Realize o comando INSERT na tabela Equipamento."""
        try:
            self.inserir_equipamento(self.gui.txt_nome.get())
        except psycopg2.DataError:
            print('Ultrapassou o limite de caracteres ou números de um campo.')

    def comando_selecionar(self):
        """ Realize o comando SELECT na tabela Equipamento."""
        try:
            self.selecionar_equipamento(self.gui.txt_codigo.get(),
                                        self.gui.txt_nome.get())
        except tkinter.TclError:
            print('Insira um número no campo Código (não vazio).')

    def comando_listar(self):
        """Realize o comando SELECT de tudo na tabela Equipamento."""
        self.listar_equipamento()

    def comando_atualizar(self):
        """Realize o comando UPDATE na tabela Equipamento."""
        try:
            self.atualizar_equipamento(self.gui.txt_nome.get(),
                                       self.gui.txt_codigo.get())
        except tkinter.TclError:
            print('Insira um número no campo Código (não vazio).')
        except psycopg2.DataError:
            print('Ultrapassou o limite de caracteres ou números de um campo.')

    def comando_deletar(self):
        """Realize o comando DELETE na tabela Equipamento."""
        try:
            self.deletar_equipamento(self.gui.txt_codigo.get())
        except tkinter.TclError:
            print('Insira um número no campo Código (não vazio).')


class MainServico(backend.BackendServico):
    """Atribua comandos aos botões da GUI Serviço."""
    def __init__(self, main):
        backend.BackendServico.__init__(self)
        self.gui = frontend.GUIServico(main)
        self.gui.btn_inserir["command"] = self.comando_inserir
        self.gui.btn_listar["command"] = self.comando_listar
        self.gui.btn_selecionar["command"] = self.comando_selecionar
        self.gui.btn_atualizar["command"] = self.comando_atualizar
        self.gui.btn_deletar["command"] = self.comando_deletar
        self.gui.btn_retornar["command"] = self.gui.destroy

    def comando_inserir(self):
        """Realize o comando INSERT na tabela Serviço."""
        try:
            self.inserir_servico(self.gui.txt_nome.get(),
                                 self.gui.txt_tipo.get(),
                                 self.gui.txt_receita.get(),
                                 self.gui.txt_hora.get(),
                                 self.gui.txt_saida.get(),
                                 self.gui.txt_data.get(),
                                 self.gui.txt_sala.get(),
                                 self.gui.txt_paciente.get(),
                                 self.gui.txt_profissional.get())
        except tkinter.TclError:
            print('Insira um número nos campos numéricos (não vazio).')
        except psycopg2.IntegrityError:
            print('Erro de integridade, chave estrangeira inexistente.')
        except psycopg2.DataError:
            print('Ultrapassou o limite de caracteres ou números de um campo '
                  'ou \ninsira uma data ou hora valida.\n'
                  'Data: 21/06/2018 = 2018-06-21\nHora: 13:45 (Exemplo)')

    def comando_listar(self):
        """Realize o comando SELECT de tudo na tabela Serviço."""
        self.listar_servico()

    def comando_selecionar(self):
        """Realize o comando SELECT na tabela Serviço."""
        try:
            self.selecionar_servico(self.gui.txt_codigo.get(),
                                    self.gui.txt_nome.get(),
                                    self.gui.txt_tipo.get(),
                                    self.gui.txt_receita.get(),
                                    self.gui.txt_hora.get(),
                                    self.gui.txt_saida.get(),
                                    self.gui.txt_data.get(),
                                    self.gui.txt_sala.get(),
                                    self.gui.txt_paciente.get(),
                                    self.gui.txt_profissional.get())
        except tkinter.TclError:
            print('Insira um número nos campos numéricos (não vazio).')
        except psycopg2.DataError:
            print('Insira uma data ou hora valida.\n'
                  'Data: 21/06/2018 = 2018-06-21\nHora: 13:45 (Exemplo)')

    def comando_atualizar(self):
        """Realize o comando UPDATE na tabela Serviço."""
        try:
            self.atualizar_servico(self.gui.txt_nome.get(),
                                   self.gui.txt_tipo.get(),
                                   self.gui.txt_receita.get(),
                                   self.gui.txt_hora.get(),
                                   self.gui.txt_saida.get(),
                                   self.gui.txt_data.get(),
                                   self.gui.txt_sala.get(),
                                   self.gui.txt_paciente.get(),
                                   self.gui.txt_profissional.get(),
                                   self.gui.txt_codigo.get())
        except tkinter.TclError:
            print('Insira um número nos campos numéricos (não vazio).')
        except psycopg2.IntegrityError:
            print('Essa ação viola a integridade da chave estrangeira, '
                  'chave pode estar ligada com a tabela Equipamento-Serviço')
        except psycopg2.DataError:
            print('Ultrapassou o limite de caracteres ou números de um campo '
                  'ou \ninsira uma data ou hora valida.\n'
                  'Data: 21/06/2018 = 2018-06-21\nHora: 13:45 (Exemplo)')

    def comando_deletar(self):
        """Realize o comando DELETE na tabela Serviço."""
        try:
            self.deletar_servico(self.gui.txt_codigo.get())
        except tkinter.TclError:
            print('Insira um número no campo Código (não vazio).')
        except psycopg2.IntegrityError:
            print('Essa ação viola a integridade da chave estrangeira, '
                  'chave pode estar ligada com a tabela Equipamento-Serviço')


class MainEquipSer(backend.BackendEquipSer):
    """Atribua comandos aos botões da GUI Equipamento-Serviço."""
    def __init__(self, main):
        backend.BackendEquipSer.__init__(self)
        self.gui = frontend.GUIEquiSer(main)
        self.gui.btn_inserir["command"] = self.comando_inserir
        self.gui.btn_listar["command"] = self.comando_listar
        self.gui.btn_selecionar["command"] = self.comando_selecionar
        self.gui.btn_deletar["command"] = self.comando_deletar
        self.gui.btn_retornar["command"] = self.gui.destroy

    def comando_inserir(self):
        """Realize o comando INSERT na tabela Equipamento-Serviço."""
        try:
            self.inserir_equipser(self.gui.txt_servico.get(),
                                  self.gui.txt_equipamento.get())
        except tkinter.TclError:
            print('Insira um número nos campos numéricos (não vazio).')
        except psycopg2.IntegrityError:
            print('Erro de integridade, chave estrangeira inexistente.')

    def comando_listar(self):
        """Realize o comando SELECT de tudo na tabela Equipamento-Serviço."""
        self.listar_equipser()

    def comando_selecionar(self):
        """Realize o comando SELECT na tabela Equipamento-Serviço."""
        try:
            self.selecionar_equipser(self.gui.txt_servico.get(),
                                     self.gui.txt_equipamento.get())
        except tkinter.TclError:
            print('Insira um número nos campos numéricos (não vazio).')

    def comando_deletar(self):
        """Realize o comando DELETE na tabela Equipamento-Serviço."""
        try:
            self.deletar_equipser(self.gui.txt_servico.get(),
                                  self.gui.txt_equipamento.get())
        except tkinter.TclError:
            print('Insira um números nos campos numéricos (não vazio).')

class MainEstatistica(backend.BackendEstatistica):
    """Atribua comandos aos botões da GUI Estatistica."""
    def __init__(self, main):
        backend.BackendEstatistica.__init__(self)
        self.gui = frontend.GUIEstatistica(main)
        self.gui.btn_atualizar["command"] = self.comando_atualizar
        self.gui.btn_retornar["command"] = self.gui.destroy

    def comando_atualizar(self):
        """Atualize os Labels após realizar cálculos."""
        self.comando_media_idade()
        self.comando_count_sexo()
        self.comando_media_altura()
        self.comando_media_peso()
        self.comando_media_salario()
        self.comando_media_capacidade()
        self.comando_media_receita()
        self.comando_count_plano()

    def comando_media_idade(self):
        """Realize o cálculo da média da idade dos Pacientes."""
        media = self.media_idade()
        self.gui.lbl_media_idade["text"] = media

    def comando_count_sexo(self):
        """Realize a contagem de pessoas do sexo F e M."""
        countsexo = self.count_sexo()
        self.gui.lbl_countsexo["text"] = countsexo

    def comando_media_altura(self):
        """Realize o cálculo da média da altura dos Pacientes."""
        media = self.media_altura()
        self.gui.lbl_media_altura["text"] = media

    def comando_media_peso(self):
        """Realize o cálculo da média do peso dos Pacientes."""
        media = self.media_peso()
        self.gui.lbl_media_peso["text"] = media

    def comando_media_salario(self):
        """Realize o cálculo da média do salário dos Profissionais."""
        media = self.media_salario()
        self.gui.lbl_media_salario["text"] = media

    def comando_media_capacidade(self):
        """Realize o cálculo da média da capacidade das Salas."""
        media = self.media_capacidade()
        self.gui.lbl_media_capacidade["text"] = media

    def comando_media_receita(self):
        """Realize o cálculo da média da receita dos Serviços."""
        media = self.media_receita()
        self.gui.lbl_media_receita["text"] = media
    
    def comando_count_plano(self):
        countplano = self.count_plano()
        self.gui.lbl_countplano["text"] = countplano


PROGRAMA = MainMenu()
PROGRAMA.mainloop()
