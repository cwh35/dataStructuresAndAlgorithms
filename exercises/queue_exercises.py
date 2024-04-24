import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.queue import Queue
import time
import threading

# 1 - Design a food ordering system where the program will run two threads
# i - Place order --> place order and insert order into a queue, this thread places new order every 0.5 second (use time.sleep(0.5))
# ii - Serve order --> serve the order by popping the order out of the queue and print it, this thread serves an order every 2 seconds
# ^ start ii thread 1 second after i thread
food_queue = Queue()

def placeOrder(queue):
    for order in orders:
        print("Placing order:", order)
        food_queue.enqueue(order)
        time.sleep(0.5)

def serveOrder():
    time.sleep(1)
    while not food_queue.isEmpty():
        print("Serving:", food_queue.dequeue())
        time.sleep(2)

# 2 - Print binary numbers from 1 to 10 using Queue
# add a front() function to the queue class to return the front element in the queue
def binaryNumbers(num):
    queue = Queue()

    queue.enqueue("1")

    for i in range(num):
        front = queue.front()
        print("   ", front)
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")
        queue.dequeue()

if __name__ == "__main__":
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

    thread1 = threading.Thread(target=placeOrder, args=(orders,))
    thread2 = threading.Thread(target=serveOrder)

    thread1.start()
    thread2.start()


    binaryNumbers(10)