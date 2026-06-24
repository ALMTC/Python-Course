class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        self.caminho = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print("Abrindo arquivo")
        self._arquivo = open(self.caminho, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, trcebakc_):
        print("Fechando arquivo")
        self._arquivo.close()


#inst = MyContextManager('Aula242.txt', 'w')


with MyContextManager('Aula242.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print("WITH", arquivo)