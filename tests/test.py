import urllib2
import simplejson
import random
import time
from threading import Thread
import threadpool
import os
PUBLISHER_URL = 'http://localhost:8080/publish/?channel=232'
SUBSCRIBER_URL = 'http://localhost:8080/activity/?channel=232'
import logging
logging.basicConfig(level = logging.DEBUG)
log = logging.getLogger('test.py')

def publish():
    res = urllib2.urlopen(PUBLISHER_URL, \
                              data = simplejson.dumps(\
            {'message': 'hello world %d' % random.randint(1, 100)}))
    return 

def subscribe(dummy):
    res = urllib2.urlopen(SUBSCRIBER_URL)
    log.info('pid::'+str(os.getpid()))
    log.info('msg:: '+res.read()+'\n')


if __name__ == '__main__':
    pool = threadpool.ThreadPool(2)
    requests = threadpool.makeRequests(subscribe, [1]*20)
    while True:
        t = Thread(target = publish)
        t.run()
        [pool.putRequest(request) for request in requests]
        pool.wait()
        #time.sleep(random.randint(3, 4))    