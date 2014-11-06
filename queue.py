import threading
import sys

'''Thread safe python Queue implementation '''
class Queue():
    def __init__(self):
        self.__q = []
        self.__lock = threading.Lock()
        self.__len = 0
        self.__done = False
        self.__has_items = threading.Semaphore(0)

    ''' Add object to queue after acquiring lock '''
    def add(self, obj):
        with self.__lock:
            self.__q.append(obj)
            self.__has_items.release()
            self.__len += 1


    ''' Removes object start of queue after acquiring lock and returns
        A call to remove if nothing on the queue has the queue wait until the
        the next object is placed on the queue. The thread is then woken up '''
    def remove(self):
        self.__has_items.acquire()
        with self.__lock:        
            obj = self.__q.pop(0)
            self.__len -= 1
        return obj

    ''' Acquires lock and returns queue length '''
    def length(self):
        with self.__lock:
            length = self.__len
        return length

    ''' Acquires lock and returns true if queue is is_empty '''
    def is_empty(self):
        with self.__lock:
            length = self.__len
        
        if length == 0:
            return True
        else:
            return False

                
