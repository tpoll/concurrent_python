from queue import Queue
from threading import Thread
import requests


def main():
    UrlQ = Queue()

    for x in xrange(1, 100):
        UrlQ.add("http://www.reddit.com/")
        UrlQ.add("http://www.nytimes.com/")
        UrlQ.add("http://www.theatlantic.com/")
        UrlQ.add("https://github.com/tpoll")
        UrlQ.add("http://arstechnica.com/")
        UrlQ.add("http://www.amazon.com/")
        UrlQ.add("http://www.newyorker.com/")

    RequestURls(UrlQ, Requester, 15)



def RequestURls(UrlQ, fun, NumberOfThreads=10):
    threads = []
    HtmlQ = Queue()

    for x in xrange(0, NumberOfThreads):
        threads.append(Thread(target=fun, args=(UrlQ, HtmlQ)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def Requester(UrlQ, HtmlQ):
    while not UrlQ.is_empty():
        try:
            Url = UrlQ.remove()
            HtmlQ.add(requests.get(Url))
        except:
            print "Request Failed: " + Url



if __name__ == '__main__':
        main()
