import sys

class pizza:
    def __init__(self):
        self.size = None
        self.toppings = None
        self.price = None

def main():

    pizza1 = pizza
    pizza2 = pizza

    pizza1.size = "Large"
    
    pizza2.size = "Small"


    print("Pizza 1 size:", pizza1.size)
    print("Pizza 2 size:", pizza2.size)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
