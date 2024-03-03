# Chain of Responsibility Pattern

1. What is it?

   The Chain of Responsibility (CoR) pattern is a design pattern where a series of objects (handlers) are linked together. Each handler can process a request or pass it to the next handler in the chain.

2. What is its purpose?

   The purpose of the Chain of Responsibility pattern is to create a chain of handlers for a request, allowing the request to be processed by any handler in the chain. This promotes flexibility and avoids coupling between the sender of a request and its receivers.

3. When to use this?

   Use the Chain of Responsibility pattern when:

   You have multiple objects that can handle a request.
   The set of handlers and their order may change dynamically.
   You want to decouple the sender and receiver objects.

4. Small Code example

```python
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)


class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            print("Handler A is handling the request.")
        else:
            super().handle_request(request)


class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            print("Handler B is handling the request.")
        else:
            super().handle_request(request)


# Usage
handler_chain = ConcreteHandlerA(ConcreteHandlerB())

handler_chain.handle_request("A")  # Output: Handler A is handling the request.
handler_chain.handle_request("B")  # Output: Handler B is handling the request.
handler_chain.handle_request("C")  # No output, as no handler can process the request.

```

In this example, Handler is the base class for all handlers, and each concrete handler (ConcreteHandlerA and ConcreteHandlerB) can either handle the request or pass it to the next handler in the chain.
