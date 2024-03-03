# Strategy Pattern

1. What is it?

   The Strategy Pattern is a design pattern in Python that helps organize your code by defining a family of algorithms, encapsulating each one, and making them interchangeable. It allows a client to choose an algorithm from a family of algorithms at runtime.

2. What is its purpose?

   The purpose of the Strategy Pattern is to define a set of algorithms, encapsulate each one, and make them interchangeable. This way, the client code can vary independently from the algorithms it uses. It promotes flexibility and easy maintenance of code.

3. When to use this?

   Use the Strategy Pattern when you want to have multiple ways (strategies) to perform a particular task, and you want to be able to switch between these strategies dynamically without altering the client code. It's handy when you have different variations of an algorithm and want to choose the one that fits a specific situation.

4. Small Code example

```python
# Define a strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Implement different payment strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

# Context class that uses the strategy
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)

# Example usage
credit_card_strategy = CreditCardPayment()
paypal_strategy = PayPalPayment()

cart1 = ShoppingCart(credit_card_strategy)
cart1.checkout(100)

cart2 = ShoppingCart(paypal_strategy)
cart2.checkout(50)

```

In this example, we have different payment strategies (Credit Card and PayPal). The ShoppingCart class can use any of these strategies for checkout without changing its code. This flexibility is the essence of the Strategy Pattern.
