# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:53:48 2018

@author: Fabrício
"""

import psycopg2 as psy

class BD():
    """Manuseie o banco de dados."""
    conn = None
    cur = None
    conectado = False
    senha = 'postgres'

    def database(self):
        """ Verifique a senha e crie o database."""
        try:
            self.conn = psy.connect(dbname='postgres', user='postgres',
                                    password=BD.senha)
        except psy.OperationalError:
            print('Senha do Postgres diferente da padrão ou não possui SGBD.')
            BD.senha = input('Insira a senha do Postgres: ')
            self.database()

    def conectar(self):
        """Conecte com o banco."""
        self.conn = psy.connect(dbname='postgres', user='postgres',
                                password=BD.senha)

        self.cur = self.conn.cursor()

        self.conectado = True

    def desconectar(self):
        """Desconecte do banco."""
        self.conn.close()
        self.conectado = False

    def executar(self, sql, parms=None):
        """Execute comandos SQL."""
        if self.conectado is True:
            if parms is None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, parms)
            return True
        else:
            return False

    def persistir(self):
        """Fixe as mudanças no banco."""
        if self.conectado is True:
            self.conn.commit()

    def fetchall(self):
        """Capta os dados de um SQL."""
        return self.cur.fetchall()


class BackendPaciente(BD):
    """Realize os comandos SQL da tabela Paciente."""
    def __init__(self):
        BD.__init__(self)

    def inserir_paciente(self, cpf, nome, idade, sexo, doenca, altura, peso,
                         cidade, bairro, rua, numero, complemento):
        """Insira na tabela Paciente as informações."""
        self.conectar()

        if idade == '':
            idade = 'NULL'
        if altura == '':
            altura = 'NULL'
        if peso == '':
            peso = 'NULL'

        self.executar("INSERT INTO paciente(cpf, nome, idade, sexo, doenca, \
                      altura, peso, cidade, bairro, rua, numero, complemento) \
                      VALUES('{}','{}',{},'{}','{}',{},{},'{}', '{}','{}', \
                      '{}','{}')".format(cpf, nome, idade, sexo, doenca,
                                         altura, peso, cidade, bairro, rua,
                                         numero, complemento))

        self.persistir()
        self.desconectar()

    def listar_paciente(self):
        """Busque informações de tudo da tabela Paciente."""
        self.conectar()

        self.executar("SELECT * FROM paciente")

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def selecionar_paciente(self, codigo, cpf, nome, idade, sexo, doenca,
                            altura, peso, cidade, bairro, rua, numero,
                            complemento):
        """Busque informações da tabela Paciente."""
        self.conectar()

        if idade == '':
            idade = 'NULL'
        if altura == '':
            altura = 'NULL'
        if peso == '':
            peso = 'NULL'

        self.executar("SELECT * FROM paciente WHERE codigo={} OR cpf='{}' OR \
                      nome= '{}' OR idade={} OR sexo='{}' OR doenca='{}' OR \
                      altura={} OR peso={} OR cidade='{}' OR bairro='{}' OR \
                      rua='{}' OR numero='{}' OR complemento='{}'".format(
                          codigo, cpf, nome, idade, sexo, doenca, altura,
                          peso, cidade, bairro, rua, numero, complemento))

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def atualizar_paciente(self, cpf, nome, idade, sexo, doenca, altura, peso,
                           cidade, bairro, rua, numero, complemento, codigo):
        """Atualize os campos de uma tupla da tabela Paciente."""
        self.conectar()

        if idade == '':
            idade = 'NULL'
        if altura == '':
            altura = 'NULL'
        if peso == '':
            peso = 'NULL'

        self.executar("UPDATE paciente SET cpf='{}', nome= '{}', idade={}, \
                      sexo='{}', doenca='{}', altura={}, peso={}, cidade='{}',\
                      bairro='{}', rua='{}', numero='{}', complemento='{}' \
                      WHERE codigo={} ".format(cpf, nome, idade, sexo, doenca,
                                               altura, peso, cidade, bairro,
                                               rua, numero, complemento, codigo
                                               ))

        self.persistir()
        self.desconectar()

    def deletar_paciente(self, codigo):
        """Remove uma tupla da tabela Paciente."""
        self.conectar()

        self.executar("DELETE FROM paciente WHERE codigo={}".format(codigo))

        self.persistir()
        self.desconectar()


class BackendProfissional(BD):
    """Realize os comandos SQL da tabela Profissional."""
    def __init__(self):
        BD.__init__(self)

    def inserir_profissional(self, cnpj, nome, salario, atuacao):
        """Insira na tabela Profissional as informações."""
        self.conectar()

        if salario == '':
            salario = 'NULL'

        self.executar("INSERT INTO profissional(cnpj,nome,salario,atuacao) \
                      VALUES('{}','{}',{},'{}')".format(cnpj, nome, salario,
                                                        atuacao))

        self.persistir()
        self.desconectar()

    def listar_profissional(self):
        """Busque informações de tudo da tabela Profissional."""
        self.conectar()

        self.executar("SELECT * FROM profissional")

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def selecionar_profissional(self, codigo, cnpj, nome, salario, atuacao):
        """Busque informações da tabela Profissional."""
        self.conectar()

        if salario == '':
            salario = 'NULL'

        self.executar("SELECT * FROM profissional WHERE codigo='{}' OR cnpj= \
                      '{}' OR nome='{}' OR salario={} OR atuacao='{}'".format(
                          codigo, cnpj, nome, salario, atuacao))

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def atualizar_profissional(self, cnpj, nome, salario, atuacao, codigo):
        """Atualize os campos de uma tupla da tabela Profissional."""
        self.conectar()

        if salario == '':
            salario = 'NULL'

        self.executar("UPDATE profissional SET cnpj='{}', nome='{}', \
                      salario={}, atuacao='{}' WHERE codigo={}".format(
                          cnpj, nome, salario, atuacao, codigo))

        self.persistir()
        self.desconectar()

    def deletar_profissional(self, codigo):
        """Remove uma tupla da tabela Profissional."""
        self.conectar()

        self.executar("DELETE FROM profissional WHERE codigo= \
                      {}".format(codigo))

        self.persistir()
        self.desconectar()


class BackendSala(BD):
    """Realize os comandos SQL da tabela Sala."""
    def __init__(self):
        BD.__init__(self)

    def inserir_sala(self, sigla, capacidade):
        """Insira na tabela Sala as informações."""
        self.conectar()

        if sigla == '':
            sigla = 'NULL'

        self.executar("INSERT INTO sala(sigla,capacidade) VALUES('{}',\
                      {})".format(sigla, capacidade))

        self.persistir()
        self.desconectar()

    def listar_sala(self):
        """Busque informações de tudo da tabela Sala."""
        self.conectar()

        self.executar("SELECT * FROM sala")

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def selecionar_sala(self, sigla, capacidade):
        """Busque informações da tabela Sala."""
        self.conectar()

        if sigla == '':
            sigla = 'NULL'

        self.executar("SELECT * FROM sala WHERE sigla='{}' OR \
                      capacidade={}".format(sigla, capacidade))

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def atualizar_sala(self, sigla, capacidade):
        """Atualize os campos de uma tupla da tabela Sala."""
        self.conectar()

        if sigla == '':
            sigla = 'NULL'
        if capacidade == '':
            capacidade = 'NULL'

        self.executar("UPDATE sala SET capacidade={} WHERE sigla= \
                      '{}'".format(capacidade, sigla))

        self.persistir()
        self.desconectar()

    def deletar_sala(self, sigla):
        """Remove uma tupla da tabela Sala."""
        self.conectar()

        if sigla == '':
            sigla = 'NULL'

        self.executar("DELETE FROM sala WHERE sigla='{}'".format(sigla))

        self.persistir()
        self.desconectar()


class BackendEquipamento(BD):
    """Realize os comandos SQL da tabela Equipamento."""
    def __init__(self):
        BD.__init__(self)

    def inserir_equipamento(self, nome):
        """Insira na tabela Equipamento as informações."""
        self.conectar()

        self.executar(
            "INSERT INTO equipamento(nome) VALUES('{}')".format(nome))

        self.persistir()
        self.desconectar()

    def listar_equipamento(self):
        """Busque informações de tudo da tabela Equipamento."""
        self.conectar()

        self.executar("SELECT * FROM equipamento")

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def selecionar_equipamento(self, codigo, nome):
        """Busque informações da tabela Equipamento."""
        self.conectar()

        self.executar("SELECT * FROM equipamento WHERE  codigo={} OR \
                      nome='{}'".format(codigo, nome))

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def atualizar_equipamento(self, nome, codigo):
        """Atualize os campos de uma tupla da tabela Equipamento."""
        self.conectar()

        self.executar("UPDATE equipamento SET nome='{}' WHERE codigo= \
                      {}".format(nome, codigo))

        self.persistir()
        self.desconectar()

    def deletar_equipamento(self, codigo):
        """Remove uma tupla da tabela Equipamento."""
        self.conectar()

        self.executar("DELETE FROM equipamento WHERE codigo={}".format(codigo))

        self.persistir()
        self.desconectar()


class BackendServico(BD):
    """Realize os comandos SQL da tabela Serviço."""
    def __init__(self):
        BD.__init__(self)

    def inserir_servico(self, nome, tipo, receita, hora, saida, data, sala,
                        paciente, profissional):
        """Insira na tabela Serviço as informações."""
        self.conectar()

        if receita == '':
            receita = 'NULL'
        if hora == '':
            hora = '000000'
        if saida == '':
            saida = '000000'
        if data == '':
            data = '0001-01-01'
        if sala == '':
            sala = 'NULL'
        if paciente == '':
            paciente = 'NULL'
        if profissional == '':
            profissional = 'NULL'

        self.executar("INSERT INTO servico(nome, tipo_consulta, receita, hora,\
                      saida, dia, sigla_sala, codigo_paciente, \
                      codigo_profissional) VALUES('{}','{}',{},'{}','{}','{}',\
                      '{}',{},{})".format(nome, tipo, receita, hora, saida,
                                          data, sala, paciente, profissional))

        self.persistir()
        self.desconectar()

    def listar_servico(self):
        """Busque informações de tudo da tabela Serviço."""
        self.conectar()

        self.executar("SELECT * FROM servico")

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def selecionar_servico(self, codigo, nome, tipo, receita, hora, saida,
                           data, sala, paciente, profissional):
        """Busque informações da tabela Serviço."""
        self.conectar()

        if receita == '':
            receita = 'NULL'
        if hora == '':
            hora = '000000'
        if saida == '':
            saida = '000000'
        if data == '':
            data = '0001-01-01'
        if sala == '':
            sala = 'NULL'
        if paciente == '':
            paciente = 'NULL'
        if profissional == '':
            profissional = 'NULL'

        self.executar("SELECT * FROM servico WHERE codigo='{}' OR nome='{}' OR\
                      tipo_consulta= '{}' OR receita={} OR hora='{}' OR \
                      saida='{}' OR dia='{}' OR sigla_sala='{}' OR \
                      codigo_paciente={} OR codigo_profissional={}".format(
                          codigo, nome, tipo, receita, hora, saida, data, sala,
                          paciente, profissional))

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def atualizar_servico(self, nome, tipo, receita, hora, saida, data, sala,
                          paciente, profissional, codigo):
        """Atualize os campos de uma tupla da tabela Serviço."""
        self.conectar()

        if receita == '':
            receita = 'NULL'
        if hora == '':
            hora = 'NULL'
        if saida == '':
            saida = 'NULL'
        if data == '':
            data = 'NULL'
        if sala == '':
            sala = 'NULL'
        if paciente == '':
            paciente = 'NULL'
        if profissional == '':
            profissional = 'NULL'

        self.executar("UPDATE servico SET nome='{}', tipo_consulta='{}', \
                      receita={}, hora='{}', saida='{}', dia='{}', sigla_sala=\
                      '{}', codigo_paciente={}, codigo_profissional={} WHERE \
                      codigo={}".format(nome, tipo, receita, hora, saida, data,
                                        sala, paciente, profissional, codigo))

        self.persistir()
        self.desconectar()

    def deletar_servico(self, codigo):
        """Remove uma tupla da tabela Serviço."""
        self.conectar()

        self.executar("DELETE FROM servico WHERE codigo={}".format(codigo))

        self.persistir()
        self.desconectar()


class BackendEquipSer(BD):
    """Realize os comandos SQL da tabela Equipamento-Serviço."""
    def __init__(self):
        BD.__init__(self)

    def inserir_equipser(self, servico, equipamento):
        """Insira na tabela Equipamento-Serviço as informações."""
        self.conectar()

        self.executar("INSERT INTO equipamento_servico(codigo_servico,\
                      codigo_equipamento) VALUES({},{})".format(servico,
                                                                equipamento))

        self.persistir()
        self.desconectar()

    def listar_equipser(self):
        """Busque informações de tudo da tabela Equipamento-Serviço."""
        self.conectar()

        self.executar("SELECT * FROM equipamento_servico")

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def selecionar_equipser(self, servico, equipamento):
        """Busque informações da tabela Equipamento-Serviço."""
        self.conectar()



        self.executar("SELECT * FROM equipamento_servico WHERE \
                      codigo_servico={} OR codigo_equipamento={}".format(
                          servico, equipamento))

        rows = self.fetchall()
        self.persistir()
        self.desconectar()
        for row in rows:
            print(row)
        print('')

    def deletar_equipser(self, servico, equipamento):
        """Remove uma tupla da tabela Equipamento-Serviço."""
        self.conectar()

        self.executar("DELETE FROM equipamento_servico WHERE codigo_servico={}\
                      AND codigo_equipamento={}".format(servico, equipamento))

        self.persistir()
        self.desconectar()

class BackendEstatistica(BD):
    """Realize os comandos SQL da tabela Estatistica."""
    def __init__(self):
        BD.__init__(self)

    def media_idade(self):
        """Busque a média das idades da tabela Paciente."""
        self.conectar()

        self.executar("SELECT AVG(idade)::DECIMAL(3,1) FROM paciente")

        media = self.fetchall()

        self.persistir()
        self.desconectar()
        return media

    def count_sexo(self):
        """Busque a contagem de cada sexo da tabela Paciente."""
        self.conectar()

        self.executar("SELECT sexo, COUNT(sexo) FROM paciente WHERE \
                      sexo='M' OR sexo='F' GROUP BY sexo;")

        count_sexo = self.fetchall()

        self.persistir()
        self.desconectar()
        return count_sexo

    def media_altura(self):
        """Busque a média das alturas da tabela Paciente."""
        self.conectar()

        self.executar("SELECT AVG(altura)::DECIMAL(3,1) FROM paciente")

        media = self.fetchall()

        self.persistir()
        self.desconectar()
        return media

    def media_peso(self):
        """Busque a média dos pesos da tabela Paciente."""
        self.conectar()

        self.executar("SELECT AVG(peso)::DECIMAL(3,1) FROM paciente")

        media = self.fetchall()

        self.persistir()
        self.desconectar()
        return media

    def media_salario(self):
        """Busque a média dos salários da tabela Profissional."""
        self.conectar()

        self.executar("SELECT AVG(salario)::DECIMAL(5,1) FROM profissional")

        media = self.fetchall()

        self.persistir()
        self.desconectar()
        return media

    def media_receita(self):
        """Busque a média das receitas da tabela Serviço."""
        self.conectar()

        self.executar("SELECT AVG(receita)::DECIMAL(5,1) FROM servico")

        media = self.fetchall()

        self.persistir()
        self.desconectar()
        return media

    def media_capacidade(self):
        """Busque a média das capacidades da tabela Sala."""
        self.conectar()

        self.executar("SELECT AVG(capacidade)::DECIMAL(4,1) FROM sala")

        media = self.fetchall()

        self.persistir()
        self.desconectar()
        return media
    
    def count_plano(self):
        self.conectar()
        
        self.executar("SELECT tipo_consulta, COUNT(tipo_consulta) FROM \
                      servico GROUP BY tipo_consulta")
        
        count_plano = self.fetchall()
        
        self.persistir()
        self.desconectar()
        return count_plano

def inicializar_database():
    """Crie as tabelas no banco de dados."""
    banco = BD()
    try:
        banco.conectar()
    except psy.OperationalError:
        banco.database()


    banco.executar('CREATE TABLE IF NOT EXISTS paciente (codigo SERIAL, cpf \
                   CHAR(11) UNIQUE NOT NULL, nome VARCHAR(50), idade INTEGER, \
                   sexo CHAR(1), doenca VARCHAR(50), altura DECIMAL(3,2), peso\
                   DECIMAL(4,1), cidade VARCHAR(30), bairro VARCHAR(20), rua \
                   VARCHAR(50), numero VARCHAR(5), complemento VARCHAR(10), \
                   PRIMARY KEY(codigo))')

    banco.executar('CREATE TABLE IF NOT EXISTS profissional (codigo SERIAL, \
                   cnpj CHAR(14) UNIQUE NOT NULL, nome VARCHAR(50), salario\
                   NUMERIC NOT NULL, atuacao VARCHAR(25), PRIMARY KEY(codigo))'
                   )

    banco.executar('CREATE TABLE IF NOT EXISTS sala (sigla VARCHAR(10) \
                   PRIMARY KEY, capacidade INTEGER)')

    banco.executar('CREATE TABLE IF NOT EXISTS equipamento (codigo SERIAL \
                   PRIMARY KEY, nome VARCHAR(30))')

    banco.executar('CREATE TABLE IF NOT EXISTS servico (codigo SERIAL, nome \
                   VARCHAR(30), tipo_consulta VARCHAR(15),  receita NUMERIC, \
                   hora TIME, saida TIME, dia DATE, sigla_sala VARCHAR(10) \
                   REFERENCES sala(sigla), codigo_paciente INTEGER REFERENCES \
                   paciente(codigo), codigo_profissional INTEGER REFERENCES \
                   profissional(codigo), PRIMARY KEY(codigo))')

    banco.executar('CREATE TABLE IF NOT EXISTS equipamento_servico \
                   (codigo_servico INTEGER REFERENCES servico(codigo), \
                   codigo_equipamento INTEGER REFERENCES equipamento(codigo),\
                   PRIMARY KEY (codigo_servico,codigo_equipamento))')

    banco.persistir()
    banco.desconectar()

inicializar_database()
