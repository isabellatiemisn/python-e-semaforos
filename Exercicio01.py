import multiprocessing
import time

semaforo = None

def init(s):
    global semaforo
    semaforo = s

def cruzamento(id):
    global semaforo
    with semaforo:
        time.sleep(0.5)
        print ("Carro do sentido",id,"passou")
  

def main ():
    sentido = ["Norte","Sul","Leste","Oeste"]
    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4,initializer=init,initargs=(sem,)) as pool:
            pool.map(cruzamento, sentido)



if __name__ == "__main__":
    main()



