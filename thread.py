import threading

"""
Created on Sun Jun  3 16:05:35 2018

@author: Nikhil Bansal

 * Thread - a Sub process that can run independently
 * To create thread in python - 1. Import "threading" module.
                                2. create subclass of "threading.Thread" class and override "run()" method.
                                3. Call "start()" method on thread object. (start will call run() and make status of thread alive.


"""


class MyThread(threading.Thread):

    def __init__(self, name, purpose):
        threading.Thread.__init__(self, name=name)
        self.purpose = purpose

    def run(self):
        for _ in range(5):
            print(self.purpose)
            print(str(self.is_alive()) + " - " + self.name + " - " + str(
                self.ident) + " - " + threading.     ().name)


if __name__ == "__main__":
    t1 = MyThread(name="sender thread", purpose="I am sender")
    t2 = MyThread(name="receiver thread", purpose="I am receiver")

    # this line here will give "RuntimeError: cannot join current thread" as this line will create dead lock.
    # It block current thread  until current thread terminate
    #threading.current_thread().join()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
