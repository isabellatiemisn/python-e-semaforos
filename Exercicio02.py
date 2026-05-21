import multiprocessing
import time
import random 

semaforo = None

def init(s):
    global semaforo
    semaforo = s

def corredor (id):
    total: int = 200
    distancia: int = 0 
    global semaforo
    while distancia < total:
        caminhada = random.randint(4,6)
        distancia += caminhada
        print ("Pessoa",id, "caminhou:",caminhada,"m. Com o total percorrido de:",distancia,"m\n")
        time.sleep(0.5)                           
    porta = random.randint(1,2)
    with semaforo:
        time.sleep(porta)
        print ("Pessoa",id,"passou pela porta\n")
  

def main ():
    i: int = 1
    pessoas: int = [0] * 4
    for i in range (4):
        pessoas[i] = i
    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4,initializer=init,initargs=(sem,)) as pool:
            pool.map(corredor, pessoas)



if __name__ == "__main__":
    main()
