from pydispatch import dispatcher
SIGNAL = 'my-first-signal'

first_sender = object()
second_sender = {}
def main( ):
    dispatcher.send( signal=SIGNAL, sender=first_sender )
    dispatcher.send( signal=SIGNAL, sender=second_sender )
