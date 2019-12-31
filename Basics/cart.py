# This file is an exercise on templates

from string import Template


class MyTemplate(Template):
    delimiter = '#'


def main():
    cart = [dict(item="Coke", price=8, qty=2), dict(item="Cake", price=12, qty=1), dict(item="Fish", price=32, qty=4)];
    t = MyTemplate("#qty x #item = #price")
    total = 0

    print("Cart: ")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]

    print("Total: " + str(total))


if __name__ == "__main__":
    main()
