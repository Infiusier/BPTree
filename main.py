DEBUG=0



class no_arvore_b_plus:
    def __init__(self, size):
        self.init_valores_no_b_plus()
        self.folha_status = False
        if DEBUG:
            self.debug_no_b_plus()
        self.tamanho_arvore_b_plus = size
        self.no_esta_vazio=True
        self.quant_folhas=0
    
    def debug_no_b_plus(self):
        print(self.quant_folhas)
        print(self.folha_status)
        print(self.tamanho_arvore_b_plus)
        
        if self.tamanho_arvore_b_plus>1:
            print("NO criado com sucesso")
    def inserir_valor_na_folha(self, folha, valor_att, chave_valor):
        if (self.valores_listados):
            x = self.valores_listados
            tamanho=len(x)
            for index in range(tamanho):
                if (valor_att == x[index]):
                    if DEBUG:
                        print("sucesso ao inserir 1")
                    self.chaves_correspondentes[index].append(chave_valor)
                    break
                elif (valor_att < x[index]):
                    if DEBUG:
                        print("sucesso ao inserir 2")
                    self.valores_listados = self.valores_listados[:index] + [valor_att] + self.valores_listados[index:]
                    self.chaves_correspondentes = self.chaves_correspondentes[:index] + [[chave_valor]] + self.chaves_correspondentes[index:]
                    break
                elif (index + 1 == tamanho):
                    if DEBUG:
                        print("sucesso ao inserir 3")
                    self.valores_listados.append(valor_att)
                    self.chaves_correspondentes.append([chave_valor])
                    break
        else:
            self.valores_listados = [valor_att]
            self.chaves_correspondentes = [[chave_valor]]
            if DEBUG:
                print("passei pro aqui")
            
    
            
    def init_valores_no_b_plus(self):
        self.valores_listados = []
        self.proxima_chave = None
        self.pai_arvore_b_plus = None
        self.chaves_correspondentes = []



class arvore_b_plus_principal:
    def __init__(self, tamanho):
        self.raiz_arvore_b_plus = no_arvore_b_plus(tamanho)
        self.init_valores_classe()
    def procura_no_especifico(self, value):
        if DEBUG:
            print("procurando por chave/valor")
        no_atual = self.raiz_arvore_b_plus
        while(no_atual.folha_status == False):
            a = no_atual.valores_listados
            for i in range(len(a)):
                if (value == a[i]):
                    no_atual = no_atual.chaves_correspondentes[i + 1]
                    if DEBUG:
                        print("etapa1")
                    break
                elif (value < a[i]):
                    no_atual = no_atual.chaves_correspondentes[i]
                    if DEBUG:
                        print("etapa2")
                    break
                elif (i + 1 == len(no_atual.valores_listados)):
                    no_atual = no_atual.chaves_correspondentes[i + 1]
                    if DEBUG:
                        print("etapa3")
                    break
        return no_atual
    def imprime_arvore_b_plus(self):
        y = [self.raiz_arvore_b_plus]
        while (len(y) != 0):
            x = y.pop(0)     
            for nada, item in enumerate(x.chaves_correspondentes):
                print(item.valores_listados)
            
    def inserir_em_no_pai(self, valor1, valor2, valor3):
        if (self.raiz_arvore_b_plus == valor1):
            no_raiz = no_arvore_b_plus(valor1.tamanho_arvore_b_plus)
            no_raiz.valores_listados = [valor2]
            no_raiz.chaves_correspondentes = [valor1, valor3]
            self.raiz_arvore_b_plus = no_raiz
            valor1.pai_arvore_b_plus = no_raiz
            valor3.pai_arvore_b_plus = no_raiz
            return

        no_original = valor1.pai_arvore_b_plus
        valor4 = no_original.chaves_correspondentes
        for i in range(len(valor4)):
            if (valor4[i] == valor1):
                no_original.valores_listados = no_original.valores_listados[:i] + \
                    [valor2] + no_original.valores_listados[i:]
                no_original.chaves_correspondentes = no_original.chaves_correspondentes[:i +
                                                  1] + [valor3] + no_original.chaves_correspondentes[i + 1:]
                if (len(no_original.chaves_correspondentes) > no_original.tamanho_arvore_b_plus):
                    parentdash = no_arvore_b_plus(no_original.tamanho_arvore_b_plus)
                    parentdash.pai_arvore_b_plus = no_original.pai_arvore_b_plus
                    import math
                    mid = int(math.ceil(no_original.tamanho_arvore_b_plus / 2)) - 1
                    parentdash.valores_listados = no_original.valores_listados[mid + 1:]
                    parentdash.chaves_correspondentes = no_original.chaves_correspondentes[mid + 1:]
                    value_ = no_original.valores_listados[mid]
                    if (mid == 0):
                        no_original.valores_listados = no_original.valores_listados[:mid + 1]
                    else:
                        no_original.valores_listados = no_original.valores_listados[:mid]
                    no_original.chaves_correspondentes = no_original.chaves_correspondentes[:mid + 1]
                    for j in no_original.chaves_correspondentes:
                        j.pai_arvore_b_plus = no_original
                    for j in parentdash.chaves_correspondentes:
                        j.pai_arvore_b_plus = parentdash
                    self.inserir_em_no_pai(no_original, value_, parentdash)

    def insere_valor_chave_arvore(self, valor_entrada, chave_valor):
        valor_entrada = str(valor_entrada)
        no_anterior = self.procura_no_especifico(valor_entrada)
        no_anterior.inserir_valor_na_folha(no_anterior, valor_entrada, chave_valor)
        if DEBUG:
            print("inserindo valor")
        if (len(no_anterior.valores_listados) == no_anterior.tamanho_arvore_b_plus):
            import math
            no_init = no_arvore_b_plus(no_anterior.tamanho_arvore_b_plus)
            no_init.folha_status = True
            no_init.pai_arvore_b_plus = no_anterior.pai_arvore_b_plus
            meio_arvore = int(math.ceil(no_anterior.tamanho_arvore_b_plus / 2)) - 1
            no_init.valores_listados = no_anterior.valores_listados[meio_arvore + 1:]
            no_init.chaves_correspondentes = no_anterior.chaves_correspondentes[meio_arvore + 1:]
            no_init.proxima_chave = no_anterior.proxima_chave
            no_anterior.valores_listados = no_anterior.valores_listados[:meio_arvore + 1]
            no_anterior.chaves_correspondentes = no_anterior.chaves_correspondentes[:meio_arvore + 1]
            no_anterior.proxima_chave = no_init
            self.inserir_em_no_pai(no_anterior, no_init.valores_listados[0], no_init)
    
        
    
    
    def verificar_chave_lista(self,item,valor_entrada,chave_valor,lista,index):
        if item == valor_entrada:
                if chave_valor in lista.chaves_correspondentes[index]:
                    return True
                else:
                    return False

    def encontrar_chave_valor(self, valor_entrada, chave_valor):
        lista = self.procura_no_especifico(valor_entrada)
        for index, item in enumerate(lista.valores_listados):
            return self.verificar_chave_lista(item,valor_entrada,chave_valor,lista,index)
        return "False"

    
    
    def init_valores_classe(self):
        self.valor_raiz=0
        self.raiz_arvore_b_plus.folha_status = True
        self.no_inicial=True

def main():
    
    arvore_b_plus = arvore_b_plus_principal(4)
    
    arvore_b_plus.insere_valor_chave_arvore('1', 'key1')
    arvore_b_plus.insere_valor_chave_arvore('2', 'key2')
    arvore_b_plus.insere_valor_chave_arvore('3', 'key3')
    arvore_b_plus.insere_valor_chave_arvore('4', 'key4')
    arvore_b_plus.insere_valor_chave_arvore('5', 'key5')
    arvore_b_plus.insere_valor_chave_arvore('6', 'key6')
    arvore_b_plus.insere_valor_chave_arvore('7', 'key7')
    arvore_b_plus.insere_valor_chave_arvore('8', 'key8')
    arvore_b_plus.insere_valor_chave_arvore('9', 'key9')
    arvore_b_plus.imprime_arvore_b_plus()
    print(arvore_b_plus.encontrar_chave_valor('1', 'key1'))
    
main()

    
