# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:09:58 2018

@author: Fabrício
"""

import tkinter as tk

from tkinter import Tk, Toplevel

class MenuPrincipal(Tk):
    """Opere a estrutura tkinter do Menu Principal."""
    def __init__(self):
        Tk.__init__(self)
        self.wm_title('Menu')
        self.resizable(False, False)
        self.frame_menu = tk.Frame(self)
        self.frame_paciente = tk.Frame(self)
        self.frame_profissional = tk.Frame(self)
        self.frame_sala = tk.Frame(self)
        self.frame_equipamento = tk.Frame(self)
        self.frame_servico = tk.Frame(self)
        self.frame_equip_serv = tk.Frame(self)
        self.frame_menu.grid(row=0, column=0)
        self.button_paciente = tk.Button(self.frame_menu, text='Pacientes')
        self.button_profissional = tk.Button(self.frame_menu,
                                             text='Profissionais')
        self.button_sala = tk.Button(self.frame_menu, text='Salas')
        self.button_equipamento = tk.Button(self.frame_menu,
                                            text='Equipamentos')
        self.button_servico = tk.Button(self.frame_menu, text='Serviços')
        self.button_equip_serv = tk.Button(self.frame_menu,
                                           text='Equipamentos e Serviços')
        self.button_paciente.grid(row=0, column=0, padx=5,
                                  pady=5, sticky='we')
        self.button_profissional.grid(row=1, column=0, padx=5,
                                      pady=5, sticky='we')
        self.button_sala.grid(row=2, column=0, padx=5,
                              pady=5, sticky='we')
        self.button_equipamento.grid(row=0, column=1, padx=5,
                                     pady=5, sticky='we')
        self.button_servico.grid(row=1, column=1, padx=5,
                                 pady=5, sticky='we')
        self.button_equip_serv.grid(row=2, column=1, padx=5,
                                    pady=5, sticky='we')


class GUIPaciente(Toplevel):
    """Opere a estrutura tkinter do Menu Paciente."""
    def __init__(self, parent):
        Toplevel.__init__(self, master=parent)
        self.wm_title('Pacientes')
        self.resizable(False, False)
        self.frame_paciente = tk.Frame(self)
        self.frame_paciente.grid(row=0, column=0)

        self.txt_codigo = tk.IntVar()
        self.txt_cpf = tk.StringVar()
        self.txt_nome = tk.StringVar()
        self.txt_idade = tk.StringVar()
        self.txt_sexo = tk.StringVar()
        self.txt_doenca = tk.StringVar()
        self.txt_altura = tk.StringVar()
        self.txt_peso = tk.StringVar()
        self.txt_cidade = tk.StringVar()
        self.txt_bairro = tk.StringVar()
        self.txt_rua = tk.StringVar()
        self.txt_numero = tk.StringVar()
        self.txt_complemento = tk.StringVar()

        self.lbl_codigo = tk.Label(self.frame_paciente, text='Código')
        self.lbl_cpf = tk.Label(self.frame_paciente, text='CPF')
        self.lbl_nome = tk.Label(self.frame_paciente, text='Nome')
        self.lbl_idade = tk.Label(self.frame_paciente, text='Idade')
        self.lbl_sexo = tk.Label(self.frame_paciente, text='Sexo')
        self.lbl_doenca = tk.Label(self.frame_paciente, text='Doenca')
        self.lbl_altura = tk.Label(self.frame_paciente, text='Altura')
        self.lbl_peso = tk.Label(self.frame_paciente, text='Peso')
        self.lbl_cidade = tk.Label(self.frame_paciente, text='Cidade')
        self.lbl_bairro = tk.Label(self.frame_paciente, text='Bairro')
        self.lbl_rua = tk.Label(self.frame_paciente, text='Rua')
        self.lbl_numero = tk.Label(self.frame_paciente, text='Número')
        self.lbl_complemento = tk.Label(self.frame_paciente, text=
                                        'Complemento')

        self.ent_codigo = tk.Entry(self.frame_paciente,
                                   textvariable=self.txt_codigo)
        self.ent_cpf = tk.Entry(self.frame_paciente,
                                textvariable=self.txt_cpf)
        self.ent_nome = tk.Entry(self.frame_paciente,
                                 textvariable=self.txt_nome)
        self.ent_idade = tk.Entry(self.frame_paciente,
                                  textvariable=self.txt_idade)
        self.ent_sexo = tk.Entry(self.frame_paciente,
                                 textvariable=self.txt_sexo)
        self.ent_doenca = tk.Entry(self.frame_paciente,
                                   textvariable=self.txt_doenca)
        self.ent_altura = tk.Entry(self.frame_paciente,
                                   textvariable=self.txt_altura)
        self.ent_peso = tk.Entry(self.frame_paciente,
                                 textvariable=self.txt_peso)
        self.ent_cidade = tk.Entry(self.frame_paciente,
                                   textvariable=self.txt_cidade)
        self.ent_bairro = tk.Entry(self.frame_paciente,
                                   textvariable=self.txt_bairro)
        self.ent_rua = tk.Entry(self.frame_paciente,
                                textvariable=self.txt_rua)
        self.ent_numero = tk.Entry(self.frame_paciente,
                                   textvariable=self.txt_numero)
        self.ent_complemento = tk.Entry(self.frame_paciente,
                                        textvariable=self.txt_complemento)


        self.btn_inserir = tk.Button(self.frame_paciente, text='Inserir')
        self.btn_selecionar = tk.Button(self.frame_paciente, text='Selecionar')
        self.btn_atualizar = tk.Button(self.frame_paciente, text='Atualizar')
        self.btn_deletar = tk.Button(self.frame_paciente, text='Deletar')
        self.btn_retornar = tk.Button(self.frame_paciente, text='Retornar')

        self.lbl_codigo.grid(row=0, column=0, padx=5, pady=3)
        self.lbl_cpf.grid(row=1, column=0, padx=5, pady=3)
        self.lbl_nome.grid(row=2, column=0, padx=5, pady=3)
        self.lbl_idade.grid(row=3, column=0, padx=5, pady=3)
        self.lbl_sexo.grid(row=0, column=2, padx=5, pady=3)
        self.lbl_doenca.grid(row=1, column=2, padx=5, pady=3)
        self.lbl_altura.grid(row=2, column=2, padx=5, pady=3)
        self.lbl_peso.grid(row=3, column=2, padx=5, pady=3)
        self.lbl_cidade.grid(row=4, column=2, padx=5, pady=3)
        self.lbl_bairro.grid(row=5, column=2, padx=5, pady=3)
        self.lbl_rua.grid(row=6, column=2, padx=5, pady=3)
        self.lbl_numero.grid(row=7, column=2, padx=5, pady=3)
        self.lbl_complemento.grid(row=8, column=2, padx=5, pady=3)

        self.ent_codigo.grid(row=0, column=1, padx=5, pady=3)
        self.ent_cpf.grid(row=1, column=1, padx=5, pady=3)
        self.ent_nome.grid(row=2, column=1, padx=5, pady=3)
        self.ent_idade.grid(row=3, column=1, padx=5, pady=3)
        self.ent_sexo.grid(row=0, column=3, padx=5, pady=3)
        self.ent_doenca.grid(row=1, column=3, padx=5, pady=3)
        self.ent_altura.grid(row=2, column=3, padx=5, pady=3)
        self.ent_peso.grid(row=3, column=3, padx=5, pady=3)
        self.ent_cidade.grid(row=4, column=3, padx=5, pady=3)
        self.ent_bairro.grid(row=5, column=3, padx=5, pady=3)
        self.ent_rua.grid(row=6, column=3, padx=5, pady=3)
        self.ent_numero.grid(row=7, column=3, padx=5, pady=3)
        self.ent_complemento.grid(row=8, column=3, padx=5, pady=3)

        self.btn_inserir.grid(row=4, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_selecionar.grid(row=5, column=0, columnspan=2, padx=5,
                                 pady=3, sticky='WE')
        self.btn_atualizar.grid(row=6, column=0, columnspan=2, padx=5,
                                pady=3, sticky='WE')
        self.btn_deletar.grid(row=7, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_retornar.grid(row=8, column=0, columnspan=2, padx=5,
                               pady=3, sticky='WE')


class GUIProfissional(Toplevel):
    """Opere a estrutura tkinter do Menu Profissional."""
    def __init__(self, parent):
        Toplevel.__init__(self, master=parent)
        self.wm_title('Profissionais')
        self.frame_profissional = tk.Frame(self)
        self.frame_profissional.grid(row=1, column=0)

        self.txt_codigo = tk.IntVar()
        self.txt_cnpj = tk.StringVar()
        self.txt_nome = tk.StringVar()
        self.txt_salario = tk.DoubleVar()
        self.txt_atuacao = tk.StringVar()

        self.lbl_codigo = tk.Label(self.frame_profissional, text='Código')
        self.lbl_cnpj = tk.Label(self.frame_profissional, text='CNPJ')
        self.lbl_nome = tk.Label(self.frame_profissional, text='Nome')
        self.lbl_salario = tk.Label(self.frame_profissional, text='Salário')
        self.lbl_atuacao = tk.Label(self.frame_profissional, text='Atuação')

        self.ent_codigo = tk.Entry(self.frame_profissional,
                                   textvariable=self.txt_codigo)
        self.ent_cnpj = tk.Entry(self.frame_profissional,
                                 textvariable=self.txt_cnpj)
        self.ent_nome = tk.Entry(self.frame_profissional,
                                 textvariable=self.txt_nome)
        self.ent_salario = tk.Entry(self.frame_profissional,
                                    textvariable=self.txt_salario)
        self.ent_atuacao = tk.Entry(self.frame_profissional,
                                    textvariable=self.txt_atuacao)

        self.btn_inserir = tk.Button(self.frame_profissional, text='Inserir')
        self.btn_selecionar = tk.Button(self.frame_profissional,
                                        text='Selecionar')
        self.btn_atualizar = tk.Button(self.frame_profissional, text=
                                       'Atualizar')
        self.btn_deletar = tk.Button(self.frame_profissional, text='Deletar')
        self.btn_retornar = tk.Button(self.frame_profissional, text='Retornar')

        self.lbl_codigo.grid(row=0, column=0, padx=5, pady=3)
        self.lbl_cnpj.grid(row=1, column=0, padx=5, pady=3)
        self.lbl_nome.grid(row=2, column=0, padx=5, pady=3)
        self.lbl_salario.grid(row=3, column=0, padx=5, pady=3)
        self.lbl_atuacao.grid(row=4, column=0, padx=5, pady=3)

        self.ent_codigo.grid(row=0, column=1, padx=5, pady=3)
        self.ent_cnpj.grid(row=1, column=1, padx=5, pady=3)
        self.ent_nome.grid(row=2, column=1, padx=5, pady=3)
        self.ent_salario.grid(row=3, column=1, padx=5, pady=3)
        self.ent_atuacao.grid(row=4, column=1, padx=5, pady=3)

        self.btn_inserir.grid(row=5, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_selecionar.grid(row=6, column=0, columnspan=2, padx=5,
                                 pady=3, sticky='WE')
        self.btn_atualizar.grid(row=7, column=0, columnspan=2, padx=5,
                                pady=3, sticky='WE')
        self.btn_deletar.grid(row=8, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_retornar.grid(row=9, column=0, columnspan=2, padx=5,
                               pady=3, sticky='WE')


class GUISala(Toplevel):
    """Opere a estrutura tkinter do Menu Sala."""
    def __init__(self, parent):
        Toplevel.__init__(self, master=parent)
        self.wm_title('Sala')
        self.frame_sala = tk.Frame(self)
        self.frame_sala.grid(row=2, column=0)

        self.txt_sigla = tk.StringVar()
        self.txt_capacidade = tk.IntVar()

        self.lbl_sigla = tk.Label(self.frame_sala, text='Sigla')
        self.lbl_capacidade = tk.Label(self.frame_sala, text='Capacidade')

        self.ent_sigla = tk.Entry(self.frame_sala, textvariable=self.txt_sigla)
        self.ent_capacidade = tk.Entry(self.frame_sala,
                                       textvariable=self.txt_capacidade)

        self.btn_inserir = tk.Button(self.frame_sala, text='Inserir')
        self.btn_selecionar = tk.Button(self.frame_sala, text='Selecionar')
        self.btn_atualizar = tk.Button(self.frame_sala, text='Atualizar')
        self.btn_deletar = tk.Button(self.frame_sala, text='Deletar')
        self.btn_retornar = tk.Button(self.frame_sala, text='Retornar')

        self.lbl_sigla.grid(row=0, column=0, padx=5, pady=3)
        self.lbl_capacidade.grid(row=1, column=0, padx=5, pady=3)

        self.ent_sigla.grid(row=0, column=1, padx=5, pady=3)
        self.ent_capacidade.grid(row=1, column=1, padx=5, pady=3)

        self.btn_inserir.grid(row=2, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_selecionar.grid(row=3, column=0, columnspan=2, padx=5,
                                 pady=3, sticky='WE')
        self.btn_atualizar.grid(row=4, column=0, columnspan=2, padx=5,
                                pady=3, sticky='WE')
        self.btn_deletar.grid(row=5, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_retornar.grid(row=6, column=0, columnspan=2, padx=5,
                               pady=3, sticky='WE')


class GUIEquipamento(Toplevel):
    """Opere a estrutura tkinter do Menu Equipamento."""
    def __init__(self, parent):
        Toplevel.__init__(self, master=parent)
        self.wm_title('Equipamentos')
        self.frame_equipamento = tk.Frame(self)
        self.frame_equipamento.grid(row=0, column=1)

        self.txt_codigo = tk.IntVar()
        self.txt_nome = tk.StringVar()

        self.lbl_codigo = tk.Label(self.frame_equipamento, text='Código')
        self.lbl_nome = tk.Label(self.frame_equipamento, text='Nome')

        self.ent_codigo = tk.Entry(self.frame_equipamento,
                                   textvariable=self.txt_codigo)
        self.ent_nome = tk.Entry(self.frame_equipamento,
                                 textvariable=self.txt_nome)

        self.btn_inserir = tk.Button(self.frame_equipamento, text='Inserir')
        self.btn_selecionar = tk.Button(self.frame_equipamento, text=
                                        'Selecionar')
        self.btn_atualizar = tk.Button(self.frame_equipamento, text=
                                       'Atualizar')
        self.btn_deletar = tk.Button(self.frame_equipamento, text='Deletar')
        self.btn_retornar = tk.Button(self.frame_equipamento, text='Retornar')

        self.lbl_codigo.grid(row=0, column=0, padx=5, pady=3)
        self.lbl_nome.grid(row=1, column=0, padx=5, pady=3)

        self.ent_codigo.grid(row=0, column=1, padx=5, pady=3)
        self.ent_nome.grid(row=1, column=1, padx=5, pady=3)

        self.btn_inserir.grid(row=2, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_selecionar.grid(row=3, column=0, columnspan=2, padx=5,
                                 pady=3, sticky='WE')
        self.btn_atualizar.grid(row=4, column=0, columnspan=2, padx=5,
                                pady=3, sticky='WE')
        self.btn_deletar.grid(row=5, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_retornar.grid(row=6, column=0, columnspan=2, padx=5,
                               pady=3, sticky='WE')


class GUIServico(Toplevel):
    """Opere a estrutura tkinter do Menu Serviço."""
    def __init__(self, parent):
        Toplevel.__init__(self, master=parent)
        self.wm_title('Serviços')
        self.frame_servico = tk.Frame(self)
        self.frame_servico.grid(row=1, column=1)

        self.txt_codigo = tk.IntVar()
        self.txt_nome = tk.StringVar()
        self.txt_tipo = tk.StringVar()
        self.txt_receita = tk.DoubleVar()
        self.txt_hora = tk.StringVar()
        self.txt_saida = tk.StringVar()
        self.txt_data = tk.StringVar()
        self.txt_sala = tk.StringVar()
        self.txt_paciente = tk.StringVar()
        self.txt_profissional = tk.StringVar()

        self.lbl_codigo = tk.Label(self.frame_servico, text='Código')
        self.lbl_nome = tk.Label(self.frame_servico, text='Nome')
        self.lbl_tipo = tk.Label(self.frame_servico, text='Tipo Consulta')
        self.lbl_receita = tk.Label(self.frame_servico, text='Receita')
        self.lbl_hora = tk.Label(self.frame_servico, text='Hora')
        self.lbl_saida = tk.Label(self.frame_servico, text='Saída')
        self.lbl_data = tk.Label(self.frame_servico, text='Data')
        self.lbl_sala = tk.Label(self.frame_servico, text='Sigla Sala')
        self.lbl_paciente = tk.Label(self.frame_servico, text=
                                     'Código Paciente')
        self.lbl_profissional = tk.Label(self.frame_servico,
                                         text='Código Profissional')

        self.ent_codigo = tk.Entry(self.frame_servico,
                                   textvariable=self.txt_codigo)
        self.ent_nome = tk.Entry(self.frame_servico,
                                 textvariable=self.txt_nome)
        self.ent_tipo = tk.Entry(self.frame_servico,
                                 textvariable=self.txt_tipo)
        self.ent_receita = tk.Entry(self.frame_servico,
                                    textvariable=self.txt_receita)
        self.ent_hora = tk.Entry(self.frame_servico,
                                 textvariable=self.txt_hora)
        self.ent_saida = tk.Entry(self.frame_servico,
                                  textvariable=self.txt_saida)
        self.ent_data = tk.Entry(self.frame_servico,
                                 textvariable=self.txt_data)
        self.ent_sala = tk.Entry(self.frame_servico,
                                 textvariable=self.txt_sala)
        self.ent_paciente = tk.Entry(self.frame_servico,
                                     textvariable=self.txt_paciente)
        self.ent_profissional = tk.Entry(self.frame_servico,
                                         textvariable=self.txt_profissional)

        self.btn_inserir = tk.Button(self.frame_servico, text='Inserir')
        self.btn_selecionar = tk.Button(self.frame_servico, text='Selecionar')
        self.btn_atualizar = tk.Button(self.frame_servico, text='Atualizar')
        self.btn_deletar = tk.Button(self.frame_servico, text='Deletar')
        self.btn_retornar = tk.Button(self.frame_servico, text='Retornar')

        self.lbl_codigo.grid(row=0, column=0, padx=5, pady=3)
        self.lbl_nome.grid(row=1, column=0, padx=5, pady=3)
        self.lbl_tipo.grid(row=2, column=0, padx=5, pady=3)
        self.lbl_receita.grid(row=3, column=0, padx=5, pady=3)
        self.lbl_hora.grid(row=0, column=2, padx=5, pady=3)
        self.lbl_saida.grid(row=1, column=2, padx=5, pady=3)
        self.lbl_data.grid(row=2, column=2, padx=5, pady=3)
        self.lbl_sala.grid(row=0, column=4, padx=5, pady=3)
        self.lbl_paciente.grid(row=1, column=4, padx=5, pady=3)
        self.lbl_profissional.grid(row=2, column=4, padx=5, pady=3)

        self.ent_codigo.grid(row=0, column=1, padx=5, pady=3)
        self.ent_nome.grid(row=1, column=1, padx=5, pady=3)
        self.ent_tipo.grid(row=2, column=1, padx=5, pady=3)
        self.ent_receita.grid(row=3, column=1, padx=5, pady=3)
        self.ent_hora.grid(row=0, column=3, padx=5, pady=3)
        self.ent_saida.grid(row=1, column=3, padx=5, pady=3)
        self.ent_data.grid(row=2, column=3, padx=5, pady=3)
        self.ent_sala.grid(row=0, column=5, padx=5, pady=3)
        self.ent_paciente.grid(row=1, column=5, padx=5, pady=3)
        self.ent_profissional.grid(row=2, column=5, padx=5, pady=3)

        self.btn_inserir.grid(row=4, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_selecionar.grid(row=5, column=0, columnspan=2, padx=5,
                                 pady=3, sticky='WE')
        self.btn_atualizar.grid(row=6, column=0, columnspan=2, padx=5,
                                pady=3, sticky='WE')
        self.btn_deletar.grid(row=7, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_retornar.grid(row=8, column=0, columnspan=2, padx=5,
                               pady=3, sticky='WE')


class GUIEquiSer(Toplevel):
    """Opere a estrutura tkinter do Menu Equipamento-Serviço."""
    def __init__(self, parent):
        Toplevel.__init__(self, master=parent)
        self.wm_title('Equipamentos e Serviços')
        self.frame_equip_serv = tk.Frame(self)
        self.frame_equip_serv.grid(row=2, column=1)

        self.txt_servico = tk.IntVar()
        self.txt_equipamento = tk.IntVar()

        self.lbl_servico = tk.Label(self.frame_equip_serv, text='Serviço')
        self.lbl_equipamento = tk.Label(self.frame_equip_serv, text=
                                        'Equipamento')

        self.ent_servico = tk.Entry(self.frame_equip_serv,
                                    textvariable=self.txt_servico)
        self.ent_equipamento = tk.Entry(self.frame_equip_serv,
                                        textvariable=self.txt_equipamento)

        self.btn_inserir = tk.Button(self.frame_equip_serv, text='Inserir')
        self.btn_selecionar = tk.Button(self.frame_equip_serv, text=
                                        'Selecionar')
        self.btn_deletar = tk.Button(self.frame_equip_serv, text='Deletar')
        self.btn_retornar = tk.Button(self.frame_equip_serv, text='Retornar')

        self.lbl_servico.grid(row=0, column=0, padx=5, pady=3)
        self.lbl_equipamento.grid(row=1, column=0, padx=5, pady=3)
        self.ent_servico.grid(row=0, column=1, padx=5, pady=3)
        self.ent_equipamento.grid(row=1, column=1, padx=5, pady=3)

        self.btn_inserir.grid(row=2, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_selecionar.grid(row=3, column=0, columnspan=2, padx=5,
                                 pady=3, sticky='WE')
        self.btn_deletar.grid(row=5, column=0, columnspan=2, padx=5,
                              pady=3, sticky='WE')
        self.btn_retornar.grid(row=6, column=0, columnspan=2, padx=5,
                               pady=3, sticky='WE')
 