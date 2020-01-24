def total(basket):
    price = 800
    discount = {
        2: 5,
        3: 10,
        4: 20,
        5: 25
    }

    # Make group of books
    groups = list()
    while basket:
        books = list()
        for book in set(basket):
            books.append(book)
            basket.pop(basket.index(book))
        groups.append(books)

    # Calculate price
    bill = 0
    for group in groups:  # [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2]]
        if len(group) in discount:
            percentage = discount[len(group)]
            bill += len(group) * (price - (price / 100 * percentage))  # 5 x (8 - 2.00) == 5 x 6.00 == $30.00
        else:
            bill += len(group) * price

    return bill
