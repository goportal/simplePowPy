import hashlib
import time 

class Block:
    
    def __init__(self, id, content, previous, nounce):
        self.id = id
        self.content = content
        self.previous = previous
        self.nounce = nounce

    def __str__(self):

        if self.nounce is None:
            return self.id +" "+self.content +" "+self.previous 
        else:
            return self.id +" "+self.content +" "+self.previous+" "+ self.nounce

    pass

def _main_():

    block = Block("1","lorenipsum","123456789",None)

    lock = True

    initialTime = time.time()
    for I in range(1000000000):
        block.nounce = str(I)

        frase = hashlib.sha256(block.__str__().encode('utf-8')).hexdigest()

        #print("o bloco: "+block.__str__())
        #print("o hash: "+frase[0])

        if frase[0]=="0" and frase[1]=="0" and frase[2]=="0" and frase[3]=="0" and frase[4]=="0" and frase[5]=="0":
            finalTime = time.time()
            print("achei o PoW: "+ frase)
            print("tempo de execução: "+str(finalTime-initialTime))
            lock = False
            break

        #if frase[0] == "0":
        #    print("achei o PoW: "+ frase)

        #print(block.__str__())
    if lock:
        print("acabou e nao achei :´(")

    #frase = "000123"

_main_()