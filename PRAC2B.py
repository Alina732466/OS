from multiprocessing import Process, Queue
import time
import random


def baker(queue):
    cakes = ["Chocolate Cake", "Vanilla Cake", "Red Velvet Cake",
             "Black Forest Cake", "Pineapple Cake", "Strawberry Cake"]

    for cake in cakes:
        print(f"Baker prepared: {cake}")

        
        queue.put(cake)

        print(f"{cake} placed on the shelf.")
        time.sleep(random.uniform(0.5, 1.5))



def customer(queue):
    for i in range(3):
      
        cake = queue.get()

        print(f"Customer bought: {cake}")
        time.sleep(random.uniform(1, 2))


if __name__ == "__main__":
   
    q = Queue(maxsize=3)

    p1 = Process(target=baker, args=(q,))
    p2 = Process(target=customer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Bakery is closed.")
