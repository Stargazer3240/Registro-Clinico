## Nível Descritivo
* O paciente possui código (identificador único), cpf, nome, idade, sexo, doença, altura, peso, cidade, bairro, rua e complemento.
* Um paciente pode receber um ou mais serviços e um serviço só pode possuir um paciente.
* Um profissional possui código (identificador único), CNPJ, nome, salário e atuação.
* Um profissional pode prestar um ou mais serviços e um serviço só pode ser prestado por um profissional.
* As salas possuem sigla (primary key) e capacidade. Cada serviço só utiliza uma sala, mas uma sala pode ser usada por mais de um serviço.
* Os equipamentos têm código (identificador) e nome. Um equipamento pode ser usado por um ou mais serviços e um serviço pode utilizar nenhum ou mais equipamentos.

## Diagrama Entidade-Relacionamento

![projetoconceitual](/images/projetoconceitual.png)

## Esquema Relacional

![projeto](/images/projeto.png)