""" Chain is like a composite, for example handler will find a handler that can handle the request """
class Handler:
    def __init__(self, successor) -> None:
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle(request)
        
    def _handle(self):
        raise NotImplementedError('There is no implementation to this request')
    

class ConcreteHandler(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print('{} is successfully handled'.format(request))
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print('End of chain. There is no handler for {}'.format(request))
        return True


class Client:
    def __init__(self,) -> None:
        self._handler = ConcreteHandler(DefaultHandler(None))
    
    def delegate(self, requests):
        for request in requests:
            self._handler.handle(request)


c = Client()

requests = [1, 3, 5, 50]

c.delegate(requests)
