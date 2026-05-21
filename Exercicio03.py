import multiprocessing
import time
import random

semaforo = None
posicao = None

def init(s, p):
    global semaforo
    global posicao
    posicao = p
    semaforo = s

def corrida (id):
    global posicao
    total: int = 50
    distancia: int = 0
    print("Sapo",id, "iniciou a corrida\n")
    while distancia < total:
        salto = random.randint(0,5)
        distancia += salto
        print ("Sapo:",id, "saltou:",salto,"cm. Com o total percorrido de:",distancia,"cm!\n")
        time.sleep(0.5)
    with semaforo:
        posicao.value+=1
        time.sleep(0.5)
        print ("Sapo",id,"chegou em",posicao.value,"° lugar\n")
        

def main ():

    sapos = [1,2,3,4,5]
    with multiprocessing.Manager() as manager:
        pos = multiprocessing.Value("i",0)
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=5,initializer=init,initargs=(sem,pos)) as pool:
            pool.map(corrida, sapos)

if __name__ == "__main__":
    main()