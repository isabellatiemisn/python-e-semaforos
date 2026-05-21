import multiprocessing
import time 
import random 

pista = None
equipes = None

def init (p,e):
    global pista 
    global equipes

    pista = p
    equipes = e

def carro (dados):
    equipe, carro_id =  dados 
    with equipes[equipe]:
        with pista: 
            print("Carro",carro_id,"da equipe",equipe,"entrou na corrida")
            for volta in range (3):
                tempo = random.randint(1,3)
                time.sleep(tempo)
                print("Carro",carro_id,"equipe",equipe,"volta",volta + 1)
            print ("Carro",carro_id,"da equipe",equipe,"saiu")

def main ():
    with multiprocessing.Manager() as manager:
        pista_local = manager.Semaphore(5)
        equipes_local = [manager.Semaphore(1) for _ in range (7)]

        carros = [(equipe,carro_id)for equipe in range (7)for carro_id in range (2)]
        with multiprocessing.Pool(processes=14,initializer=init,initargs=(pista_local,equipes_local)) as pool:
                pool.map(carro,carros)



if __name__ == "__main__":
    main()

