from pydispatch import dispatcher

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

SIGNAL = 'my-first-signal'


def tick():
    print('Tick! The time is: %s' % datetime.now())
    dispatcher.send( signal=SIGNAL, sender='tick' )

def handle_event( sender ):
    """Simple event handler"""
    print 'Signal was sent by', sender

if __name__ == '__main__':
    dispatcher.connect( handle_event, signal=SIGNAL, sender=dispatcher.Any )
    #scheduler = BackgroundScheduler()

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=5)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

#    scheduler.start()
#    try:
#        # This is here to simulate application activity (which keeps the main thread alive).
#        while True:
#            time.sleep(2)
#    except (KeyboardInterrupt, SystemExit):
#        scheduler.shutdown()
