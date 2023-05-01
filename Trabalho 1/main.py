# Trabalho de Arquitetura e Organização de Computadores 2
# Gabriel de Melo Osorio – 107862
# Henrique Shiguemoto Felizardo – 115207
# Matheus Augusto Schiavon Parise – 107115

# imports 
from collections import deque
import sys
import copy

# Algumas constantes

SEM_IMEDIATOS = 0
COM_IMEDIATOS = 1

# Definindo a variavel de ciclo de clock
Ciclo = 0

# Definindo o program counter
PC = 0

# Contador de Instrução
Contador_Instrucao = 0

# Contador Estação de Reserva
Contador_Estacao_Reserva = 0

# Classe que representa os registradores
class Registrador:
    def __init__(self, valor: int, qi: int):
        self.valor: int = valor
        self.qi: int = qi
        self.tipo_er : str = ""

# Definindo a memória de dados
Memoria_Dados = [0]*512

# Classes que representam uma instrução
class Instrucao:
    def __init__(self, qtd_ciclos: int, operacao: str):
        global Contador_Instrucao
        self.qtd_ciclos = qtd_ciclos
        self.operacao: str = operacao
        self.destino: Registrador = None
        self.primeiro_arg_reg: Registrador = None
        self.segundo_arg_reg: Registrador = None
        self.segundo_arg_imm: int = 0
        self.ordem_geral: int = Contador_Instrucao
        Contador_Instrucao += 1
        self.estacao_reserva : Estacao_Reserva = None

class Instrucao_Soma(Instrucao):
    def __init__(self, qtd_ciclos: int, operacao: str):
        super().__init__(qtd_ciclos, operacao)

class Instrucao_Mult(Instrucao):
    def __init__(self, qtd_ciclos: int, operacao: str):
        super().__init__(qtd_ciclos, operacao)

class Instrucao_Load(Instrucao):
    def __init__(self, qtd_ciclos: int, operacao: str):
        super().__init__(qtd_ciclos, operacao)

# Todas as instruções que nosso simulador suporta (quantidade de ciclos e operacao já estão setadas)
Instrucao_add = Instrucao_Soma(5, "add")
Instrucao_addi = Instrucao_Soma(5, "addi")
Instrucao_sub = Instrucao_Soma(5, "sub")
Instrucao_subi = Instrucao_Soma(5, "subi")
Instrucao_mul = Instrucao_Mult(15, "mul")
Instrucao_div = Instrucao_Mult(25, "div")
Instrucao_and = Instrucao_Soma(5, "and")
Instrucao_or = Instrucao_Soma(5, "or")
Instrucao_not = Instrucao_Soma(5, "not")
Instrucao_lw = Instrucao_Load(5, "lw")
Instrucao_sw = Instrucao_Load(5, "sw")
Instrucao_blt = Instrucao_Soma(5, "blt")
Instrucao_bgt = Instrucao_Soma(5, "bgt")
Instrucao_beq = Instrucao_Soma(5, "beq")
Instrucao_bne = Instrucao_Soma(5, "bne")
Instrucao_j = Instrucao_Soma(5, "j")

# Definindo uma classe que será usada para a fila de instruções
class Fila:
    def __init__(self):
        self.elem = deque[Instrucao]()
    def estaVazia(self) -> bool:
        return len(self.elem) == 0
    def insere(self, item : Instrucao):
        self.elem.append(item)
    def remove(self) -> Instrucao:
        if len(self.elem) == 0:
            return None
        return self.elem.popleft()

fila_de_instrucoes = Fila()

# Definindo a memória de instruções
Memoria_Instrucao: list[Instrucao] = [None]*128

# Classes que representam as estações de reserva
class Estacao_Reserva:
    def __init__(self):
        global Contador_Estacao_Reserva
        self.busy: bool = False
        self.instrucao: Instrucao = None
        self.vj: int = 0
        self.vk: int = 0
        self.qj: int = -1
        self.qk: int = -1
        self.endereco = 0 # Apenas instruções de Load e Store que utilizam o campo Endereço, por isso a variável endereco existe apenas nesse construtor
        self.id: int = Contador_Estacao_Reserva
        self.instrucao_esta_em_uf: bool = False
        Contador_Estacao_Reserva += 1
    
class Estacao_Reserva_Soma(Estacao_Reserva):
    def __init__(self):
        super().__init__()

class Estacao_Reserva_Mult(Estacao_Reserva):
    def __init__(self):
        super().__init__()

class Estacao_Reserva_Load(Estacao_Reserva):
    def __init__(self):
        super().__init__()
        
# Classes que representam as unidades funcionais
class Unidade_Funcional:
    def __init__(self):
        self.busy: bool = False
        self.ciclos_para_termino_execucao = 0
        self.instrucao: Instrucao = None

class Unidade_Funcional_Soma(Unidade_Funcional):
    def __init__(self):
        super().__init__()

class Unidade_Funcional_Mult(Unidade_Funcional):
    def __init__(self):
        super().__init__()

class Unidade_Funcional_Load(Unidade_Funcional):
    def __init__(self):
        super().__init__()

# Definindo os 32 registradores de uso geral
r0 = Registrador(0, -1)
r1 = Registrador(10, -1)
r2 = Registrador(0, -1)
r3 = Registrador(0, -1)
r4 = Registrador(0, -1)
r5 = Registrador(0, -1)
r6 = Registrador(0, -1)
r7 = Registrador(0, -1)
r8 = Registrador(0, -1)
r9 = Registrador(0, -1)
r10 = Registrador(0, -1)
r11 = Registrador(0, -1)
r12 = Registrador(0, -1)
r13 = Registrador(0, -1)
r14 = Registrador(0, -1)
r15 = Registrador(0, -1)
r16 = Registrador(0, -1)
r17 = Registrador(0, -1)
r18 = Registrador(0, -1)
r19 = Registrador(0, -1)
r20 = Registrador(0, -1)
r21 = Registrador(0, -1)
r22 = Registrador(0, -1)
r23 = Registrador(0, -1)
r24 = Registrador(0, -1)
r25 = Registrador(0, -1)
r26 = Registrador(0, -1)
r27 = Registrador(0, -1)
r28 = Registrador(0, -1)
r29 = Registrador(0, -1)
r30 = Registrador(0, -1)
r31 = Registrador(0, -1)

# Definindo as 48 estações de reserva
estacoes_reserva_soma: list[Estacao_Reserva_Soma] = []
estacoes_reserva_mult: list[Estacao_Reserva_Mult] = []
estacoes_reserva_load: list[Estacao_Reserva_Load] = []
for i in range(0, 16):
    estacoes_reserva_soma.append(Estacao_Reserva_Soma())
    estacoes_reserva_mult.append(Estacao_Reserva_Mult())
    estacoes_reserva_load.append(Estacao_Reserva_Load())

# Defininco as unidades funcionais
uf_soma: list[Unidade_Funcional_Soma] = []
uf_mult: list[Unidade_Funcional_Mult] = []
uf_load: list[Unidade_Funcional_Load] = []
for i in range(0, 3):
    uf_soma.append(Unidade_Funcional_Soma())
    uf_mult.append(Unidade_Funcional_Mult())
    uf_load.append(Unidade_Funcional_Load())

def verificar_uf_livre(uf_soma : list[Unidade_Funcional_Soma]):
    for uf in uf_soma:
        if uf.busy == False:
            return True

# Função que além de incrementar a variável global Ciclo, também diminui os contadores de ciclos restantes em Unidades Funcionais
def incrementaCiclo():
    global Ciclo
    Ciclo += 1
    for i in range(0, len(uf_soma)):
        if uf_soma[i].busy == True:
            uf_soma[i].ciclos_para_termino_execucao -= 1
            if uf_soma[i].ciclos_para_termino_execucao == 0:
                uf_soma[i].busy = False
                Execucao_Instrucoes(uf_soma[i].instrucao)
                for j in range(0, len(estacoes_reserva_soma)):
                    if estacoes_reserva_soma[j].busy == True:
                        if estacoes_reserva_soma[j].instrucao_esta_em_uf == False:
                            uf_soma[i].instrucao = estacoes_reserva_soma[j].instrucao 
                            uf_soma[i].ciclos_para_termino_execucao = estacoes_reserva_soma[j].instrucao.qtd_ciclos
                            uf_soma[i].busy = True
                            estacoes_reserva_soma[j].instrucao_esta_em_uf = True  
                            break        
        if uf_mult[i].busy == True:
            uf_mult[i].ciclos_para_termino_execucao -= 1
            if uf_mult[i].ciclos_para_termino_execucao == 0:
                uf_mult[i].busy = False
                Execucao_Instrucoes(uf_mult[i].instrucao)
                for j in range(0, len(estacoes_reserva_mult)):
                    if estacoes_reserva_mult[j].busy == True:
                        if estacoes_reserva_mult[j].instrucao_esta_em_uf == False:
                            uf_mult[i].instrucao = estacoes_reserva_mult[j].instrucao 
                            uf_mult[i].ciclos_para_termino_execucao = estacoes_reserva_mult[j].instrucao.qtd_ciclos
                            uf_mult[i].busy = True
                            estacoes_reserva_mult[j].instrucao_esta_em_uf = True  
                            break
        if uf_load[i].busy == True:
            uf_load[i].ciclos_para_termino_execucao -= 1
            if uf_load[i].ciclos_para_termino_execucao == 0:
                uf_load[i].busy = False
                Execucao_Instrucoes(uf_load[i].instrucao)
                for j in range(0, len(estacoes_reserva_load)):
                    if estacoes_reserva_load[j].busy == True:
                        if estacoes_reserva_load[j].instrucao_esta_em_uf == False:
                            uf_load[i].instrucao = estacoes_reserva_load[j].instrucao 
                            uf_load[i].ciclos_para_termino_execucao = estacoes_reserva_load[j].instrucao.qtd_ciclos
                            uf_load[i].busy = True
                            estacoes_reserva_load[j].instrucao_esta_em_uf = True  
                            break

def Busca_Instrucao() -> Instrucao:
    if Memoria_Instrucao[PC] != None:
        fila_de_instrucoes.insere(Memoria_Instrucao[PC]) # Busca de Instrução
    return Memoria_Instrucao[PC]

def Despacho_Instrucao(instrucao: Instrucao): 
    global estacoes_reserva_soma
    global estacoes_reserva_mult
    global estacoes_reserva_load
    tinha_estacao_livre: bool = False
    if instrucao.operacao in ["add", "addi", "sub", "subi", "and", "or", "not", "blt", "bgt", "beq", "bne", "j"]:
        for i in range(0, len(estacoes_reserva_soma)):
            estacao = estacoes_reserva_soma[i]
            if estacao.busy == False:
                tinha_estacao_livre = True
                if instrucao.primeiro_arg_reg.qi != -1:
                    estacao.qj = instrucao.primeiro_arg_reg.qi
                else:
                    estacao.vj = instrucao.primeiro_arg_reg.valor
                    estacao.qj = -1
                # Verificando se o segundo argumento é um registrador
                if instrucao.segundo_arg_reg != None:
                    if instrucao.segundo_arg_reg.qi != -1:
                        estacao.qk = instrucao.segundo_arg_reg.qi
                    else:
                        estacao.vk = instrucao.segundo_arg_reg.valor
                        estacao.qk = -1
                # Verificar se o segundo argumento é um valor imediato
                else:
                    estacao.vk = instrucao.segundo_arg_imm
                estacao.busy = True
                estacao.instrucao = instrucao
                estacao.instrucao.operacao = instrucao.operacao 
                instrucao.destino.qi = estacao.id
                instrucao.destino.tipo_er = "soma"
                instrucao.estacao_reserva = estacao
                break
    elif instrucao.operacao in ["mul", "div"]:
        for i in range(0, len(estacoes_reserva_mult)):
            estacao = estacoes_reserva_mult[i]
            if estacao.busy == False:
                if instrucao.primeiro_arg_reg.qi != -1:
                    estacao.qj = instrucao.primeiro_arg_reg.qi
                else:
                    estacao.vj = instrucao.primeiro_arg_reg.valor
                    estacao.qj = -1
                if instrucao.segundo_arg_reg.qi != -1:
                    estacao.qk = instrucao.segundo_arg_reg.qi
                else:
                    estacao.vk = instrucao.segundo_arg_reg.valor
                    estacao.qk = -1
                estacao.busy = True
                estacao.instrucao = instrucao
                estacao.instrucao.operacao = instrucao.operacao
                instrucao.destino.qi = estacao.id
                instrucao.destino.tipo_er = "mul"
                instrucao.estacao_reserva = estacao
                break
    elif instrucao.operacao in ["lw", "sw"]:
        for i in range(0, len(estacoes_reserva_load)):
            estacao = estacoes_reserva_load[i]
            if estacao.busy == False:
                if instrucao.primeiro_arg_reg.qi != -1:
                    estacao.qj = instrucao.primeiro_arg_reg.qi
                else:
                    estacao.vj = instrucao.primeiro_arg_reg.valor
                    estacao.qj = -1
                
                estacao.endereco = instrucao.segundo_arg_imm
                estacao.busy = True
                estacao.instrucao = instrucao
                estacao.instrucao.operacao = instrucao.operacao
                instrucao.destino.qi = estacao.id
                instrucao.destino.tipo_er = "load"
                instrucao.estacao_reserva = estacao
                break
    Aloca_Unidade_Funcional(instrucao)
    return tinha_estacao_livre, instrucao

def Aloca_Unidade_Funcional(instrucao: Instrucao):
    contador_uf_busy = 0
    
    # Se a operação for executada em uma Unidade Funcional de Soma e Subtração
    if instrucao.operacao in ["add", "addi", "sub", "subi", "and", "or", "not", "blt", "bgt", "beq", "bne", "j"]:
        for i in range(0, len(uf_soma)):
            if uf_soma[i].busy == False:
                uf_soma[i].busy = True
                uf_soma[i].instrucao = instrucao
                uf_soma[i].ciclos_para_termino_execucao = instrucao.qtd_ciclos
                instrucao.estacao_reserva.instrucao_esta_em_uf = True
                break
            else:
                contador_uf_busy += 1
                if contador_uf_busy == len(uf_soma):
                    print("Unidades Funcionais de Soma e Subtração Cheias")
    elif instrucao.operacao in ["mul", "div"]:
        for i in range(0, len(uf_mult)):
            if uf_mult[i].busy == False:
                uf_mult[i].busy = True
                uf_mult[i].instrucao = instrucao
                uf_mult[i].ciclos_para_termino_execucao = instrucao.qtd_ciclos
                break
            else:
                contador_uf_busy += 1
                if contador_uf_busy == len(uf_mult):
                    print("Unidades Funcionais de Multiplicação e Divisão Cheias")
    else:
        for i in range(0, len(uf_load)):
            if uf_load[i].busy == False:
                uf_load[i].busy = True
                uf_load[i].instrucao = instrucao
                uf_load[i].ciclos_para_termino_execucao = instrucao.qtd_ciclos
                break
            else:
                contador_uf_busy += 1
                if contador_uf_busy == len(uf_load):
                    print("Unidades Funcionais de Load e Store Cheias")

def Execucao_Instrucoes(instrucao: Instrucao):
    global Ciclo, PC
    resultado = 0
    pode_executar: bool = False

    if instrucao.estacao_reserva.qj == -1 and instrucao.estacao_reserva.qk == -1:
        pode_executar = True

    if pode_executar:
        # Instruções aritmeticas
        if instrucao.operacao == "add":
            resultado = instrucao.primeiro_arg_reg.valor + instrucao.segundo_arg_reg.valor
        elif instrucao.operacao == "addi":
            resultado = instrucao.primeiro_arg_reg.valor + instrucao.segundo_arg_imm
        elif instrucao.operacao == "sub":
            resultado = instrucao.primeiro_arg_reg.valor - instrucao.segundo_arg_reg.valor
        elif instrucao.operacao == "subi":
            resultado = instrucao.primeiro_arg_reg.valor - instrucao.segundo_arg_imm
        elif instrucao.operacao == "mul":
            resultado = instrucao.primeiro_arg_reg.valor * instrucao.segundo_arg_reg.valor
        elif instrucao.operacao == "div":
            if instrucao.segundo_arg_reg.valor == 0:
                raise Exception("Divisão por zero!")
            resultado = int(instrucao.primeiro_arg_reg.valor / instrucao.segundo_arg_reg.valor)

        # Instruções logicas
        elif instrucao.operacao == "and":
            resultado = instrucao.primeiro_arg_reg.valor and instrucao.segundo_arg_reg.valor
        elif instrucao.operacao == "or":
            resultado = instrucao.primeiro_arg_reg.valor or instrucao.segundo_arg_reg.valor
        elif instrucao.operacao == "not":
            resultado = not instrucao.primeiro_arg_reg.valor

        # Instruções de Desvio
        elif instrucao.operacao == "blt":
            # MUDAR DE ACORDO COM A IMPLEMENTAÇÃO
            if instrucao.primeiro_arg_reg.valor > instrucao.segundo_arg_reg.valor:
                PC = instrucao.segundo_arg_imm
        elif instrucao.operacao == "bgt":
            # MUDAR DE ACORDO COM A IMPLEMENTAÇÃO
            if instrucao.primeiro_arg_reg.valor < instrucao.segundo_arg_reg.valor:
                PC = instrucao.segundo_arg_imm
        elif instrucao.operacao == "beq":
            # MUDAR DE ACORDO COM A IMPLEMENTAÇÃO
            if instrucao.primeiro_arg_reg.valor == instrucao.segundo_arg_reg.valor:
                PC = instrucao.segundo_arg_imm
        elif instrucao.operacao == "bne":
            # MUDAR DE ACORDO COM A IMPLEMENTAÇÃO
            if instrucao.primeiro_arg_reg.valor != instrucao.segundo_arg_reg.valor:
                PC = instrucao.segundo_arg_imm
        elif instrucao.operacao == "j":
            PC = instrucao.segundo_arg_imm

        # Instruções de Memoria
        elif instrucao.operacao == "lw":
            # MUDAR DE ACORDO COM A IMPLEMENTAÇÃO
            posicao = instrucao.primeiro_arg_reg.valor + instrucao.segundo_arg_imm
            resultado = Memoria_Instrucao[posicao]
        elif instrucao.operacao == "sw":
            # MUDAR DE ACORDO COM A IMPLEMENTAÇÃO
            posicao = instrucao.primeiro_arg_reg.valor + instrucao.segundo_arg_imm
            Memoria_Instrucao[posicao] = instrucao.primeiro_arg_reg.valor
        else:
            raise Exception('Operação não é suportada')
        
        Escrever_Instrucoes(instrucao, resultado)
 
def Escrever_Instrucoes(instrucao: Instrucao, resultado):
    if instrucao.operacao in ["add", "addi", "sub", "subi", "mul", "div", "and", "or", "not", "lw"]:
        for i in range(0, 32):
            reg = getattr(sys.modules[__name__], "r" + str(i))
            if reg.qi == instrucao.estacao_reserva.id:
                reg.valor = resultado
                reg.qi = -1
        #Passar por todas as estações de reserva e atualizar os campos que dependem de instrucao.estacao_reserva
        for i in range(0, len(estacoes_reserva_soma)):
            if estacoes_reserva_soma[i].qj == instrucao.estacao_reserva.id:
                estacoes_reserva_soma[i].vj = resultado
                estacoes_reserva_soma[i].qj = -1
            if estacoes_reserva_mult[i].qj == instrucao.estacao_reserva.id:
                estacoes_reserva_mult[i].vj = resultado
                estacoes_reserva_mult[i].qj = -1
            if estacoes_reserva_load[i].qj == instrucao.estacao_reserva.id:
                estacoes_reserva_load[i].vj = resultado
                estacoes_reserva_load[i].qj = -1
            if estacoes_reserva_soma[i].qk == instrucao.estacao_reserva.id:
                estacoes_reserva_soma[i].vk = resultado
                estacoes_reserva_soma[i].qk = -1
            if estacoes_reserva_mult[i].qk == instrucao.estacao_reserva.id:
                estacoes_reserva_mult[i].vk = resultado
                estacoes_reserva_mult[i].qk = -1
            if estacoes_reserva_load[i].qk == instrucao.estacao_reserva.id:
                estacoes_reserva_load[i].vk = resultado
                estacoes_reserva_load[i].qk = -1
        instrucao.estacao_reserva.busy = False
        instrucao.estacao_reserva.instrucao_esta_em_uf = False
    elif instrucao.operacao == "sw":
        Memoria_Dados[instrucao.estacao_reserva.endereco] = instrucao.estacao_reserva.vj
        instrucao.estacao_reserva.busy = False
        instrucao.estacao_reserva.instrucao_esta_em_uf = False

def se_estacoes_estão_busy() -> bool:
    estacoes_em_uso = False
    for i in range(0, len(estacoes_reserva_soma)):
        if estacoes_reserva_soma[i].busy == True:
            estacoes_em_uso = True
    for i in range(0, len(estacoes_reserva_mult)):
        if estacoes_reserva_mult[i].busy == True:
            estacoes_em_uso = True
    for i in range(0, len(estacoes_reserva_load)):
        if estacoes_reserva_load[i].busy == True:
            estacoes_em_uso = True
    return estacoes_em_uso

def imprimir_Resultados():
    global estacoes_reserva_soma
    global estacoes_reserva_mult
    global estacoes_reserva_load

    print("/////// PC = " + str(PC) + " Ciclo = " + str(Ciclo) + "///////")

    # Imprimir o estado das estações de reserva
    print("-------------------------------------------------------------------------------------------------------")
    print("Estado das Estações de Reserva de Soma e Subtração: ")
    for i in range(0, len(estacoes_reserva_soma)):
        er = estacoes_reserva_soma[i]
        if er.instrucao != None:
            operacao = er.instrucao.operacao
        else:
            operacao = "None"
        print("Estação de Reserva " + str(i) + ": busy = " + str(er.busy) + ", OP = " + operacao
                + ", vj = " + str(er.vj) + ", vk = " + str(er.vk) + ", qj = " + str(er.qj) 
                + ", qk = " +  str(er.qk))
    print("-------------------------------------------------------------------------------------------------------")
    print("Estado das Estações de Reserva de Multiplicação e Divisão: ")
    for i in range(0, len(estacoes_reserva_mult)):
        er = estacoes_reserva_mult[i]
        if er.instrucao != None:
            operacao = er.instrucao.operacao
        else:
            operacao = "None"
        print("Estação de Reserva " + str(i) + ": busy = " + str(er.busy) + ", OP = " + operacao
                + ", vj = " + str(er.vj) + ", vk = " + str(er.vk) + ", qj = " + str(er.qj) 
                + ", qk = " +  str(er.qk))
    print("-------------------------------------------------------------------------------------------------------")
    print("Estado das Estações de Reserva de Load e Store: ")
    for i in range(0, len(estacoes_reserva_load)):
        er = estacoes_reserva_load[i]
        if er.instrucao != None:
            operacao = er.instrucao.operacao
        else:
            operacao = "None"
        print("Estação de Reserva " + str(i) + ": busy = " + str(er.busy) + ", OP = " + operacao
                + ", vj = " + str(er.vj) + ", vk = " + str(er.vk) + ", qj = " + str(er.qj) 
                + ", qk = " +  str(er.qk) + ", endereço = " + str(er.endereco))
    # Imprimir o estado da memória de dados
    print("-------------------------------------------------------------------------------------------------------")
    print("Estado da Memória de Dados: ")
    for i in range(0, len(Memoria_Dados)):
        print("Posição " + str(i) + ": " + str(Memoria_Dados[i]))
    
    # Imprimir o estado dos registradores
    for i in range(0, 32):
        reg = getattr(sys.modules[__name__], "r" + str(i))
        print("Registrador r" + str(i) + ": valor = " + str(reg.valor) + ", qi = " + str(reg.qi) + ", tipo da estação = " + reg.tipo_er)

def separar_argumentos(lista: list[str]) -> list[str]:
    if lista[0] == "lw" or lista[0] == "sw":
        #Pegamos o último argumento de lista e substituímos os parênteses por " " e 
        # depois separamos o valor imediato do registrador
        result = lista[2].replace("(", " ").replace(")", " ").split()
        #Retiramso o último elemento
        lista.pop(2)
        #Recolocamos o valor imediato
        lista.append(result[0])
        #Recolocamos o registrador
        lista.append(result[1])
    return lista

def incrementarPC():
    global PC
    PC += 1

def main():
    global PC
    # Leitura de um arquivo
    # Inserir todas as instruções em Memoria_Instrucao
    arquivo = open("testeload", "r")
    linha = arquivo.readline()
    
    # Leitura de todas as instruções no arquivo .txt e armazenamos os objetos Instrução correspondente na Memória de Instruções
    while linha != "":
        separacao_linha = linha.replace(",", " ").split()
        argumentos = separar_argumentos(separacao_linha)
        # Verificando se a instrução possui argumento imediato 
        if separacao_linha[0] in ["addi", "subi", "blt", "bgt", "beq", "bne", "j", "lw", "sw"]:
            if separacao_linha[0] == "addi":
                instrucao = Instrucao_addi
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_imm = int(argumentos[3]) #Assumindo que seja possível sempre realizar essa conversão
            elif separacao_linha[0] == "subi":
                instrucao = Instrucao_subi
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_imm = int(argumentos[3]) #Assumindo que seja possível sempre realizar essa conversão
            elif separacao_linha[0] == "blt":
                instrucao = Instrucao_blt
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_imm = int(argumentos[3]) #Assumindo que seja possível sempre realizar essa conversão
            elif separacao_linha[0] == "bgt":
                instrucao = Instrucao_bgt
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_imm = int(argumentos[3]) #Assumindo que seja possível sempre realizar essa conversão
            elif separacao_linha[0] == "beq":
                instrucao = Instrucao_beq
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_imm = int(argumentos[3]) #Assumindo que seja possível sempre realizar essa conversão
            elif separacao_linha[0] == "bne":
                instrucao = Instrucao_bne
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_imm = int(argumentos[3]) #Assumindo que seja possível sempre realizar essa conversão
            elif separacao_linha[0] == "j":
                instrucao = Instrucao_j
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_imm = int(argumentos[3]) #Assumindo que seja possível sempre realizar essa conversão
            elif separacao_linha[0] == "lw":
                instrucao = Instrucao_lw
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[3])
                instrucao.segundo_arg_imm = int(argumentos[2]) #Assumindo que seja possível sempre realizar essa conversão
            elif separacao_linha[0] == "sw":
                instrucao = Instrucao_sw
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[3])
                instrucao.segundo_arg_imm = int(argumentos[2]) #Assumindo que seja possível sempre realizar essa conversão
        #Verificando se a instrução não possui argumento imediato
        else:
            if separacao_linha[0] == "add":
                instrucao = Instrucao_add
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_reg = getattr(sys.modules[__name__], argumentos[3])
            elif separacao_linha[0] == "sub":
                instrucao = Instrucao_sub
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_reg = getattr(sys.modules[__name__], argumentos[3])
            elif separacao_linha[0] == "mul":
                instrucao = Instrucao_mul
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_reg = getattr(sys.modules[__name__], argumentos[3])
            elif separacao_linha[0] == "div":
                instrucao = Instrucao_div
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_reg = getattr(sys.modules[__name__], argumentos[3])
            elif separacao_linha[0] == "and":
                instrucao = Instrucao_and
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_reg = getattr(sys.modules[__name__], argumentos[3])
            elif separacao_linha[0] == "or":
                instrucao = Instrucao_or
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
                instrucao.segundo_arg_reg = getattr(sys.modules[__name__], argumentos[3])
            elif separacao_linha[0] == "not":
                instrucao = Instrucao_not
                instrucao.primeiro_arg_reg = getattr(sys.modules[__name__], argumentos[2])
        
        instrucao.destino = getattr(sys.modules[__name__], argumentos[1])
        Memoria_Instrucao[PC] = copy.copy(instrucao)
        PC = PC + 1
        linha = arquivo.readline()
    PC = 0 # Resetando PC
    
    estacao_livre: bool = True
    instrucao_buscada = Busca_Instrucao()
    incrementarPC()
    incrementaCiclo() #Ciclo 0 -> Ciclo 1

    # Loop que faz o Algoritmo de Tomasulo
    while len(fila_de_instrucoes.elem) > 0 or se_estacoes_estão_busy():
        if len(fila_de_instrucoes.elem) > 0:
            if Ciclo == 1:
                if estacao_livre:
                    instrucao_buscada = fila_de_instrucoes.remove()
                Despacho_Instrucao(instrucao_buscada)
                instrucao_buscada = Busca_Instrucao()
                incrementarPC()
            elif Ciclo >= 2:
                if estacao_livre:
                    instrucao_buscada = fila_de_instrucoes.remove()
                if instrucao_buscada != None:
                    Despacho_Instrucao(instrucao_buscada)
                
                instrucao_buscada = Busca_Instrucao()
                incrementarPC()
        incrementaCiclo()  
        imprimir_Resultados()

if __name__ == '__main__':
    main()