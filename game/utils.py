
# ----------------------------------------------------------------------------

class Observable(object):
    def __init__(self):
        self.observers = []
    def subscribe(self, subscriber):
        self.observers.append(subscriber)
    def unsubscribe(self, subscriber):
        self.observers.remove(subscriber)
    def emit(self, *args):
        for subscriber in self.observers:
            subscriber(*args)

# ----------------------------------------------------------------------------

if __name__ == "__main__":
    def testObserver(o):
        def first(x):
            print("Subscription 1: %s" % x)
        def second(x):
            print("Subscription 2: %s" % x)
        o.subscribe( first )
        o.emit("LOLZ")
        o.subscribe( second )
        o.emit("ROFL")
        o.unsubscribe( second )
        o.emit("BONERZ")
    testObserver(Observable())

