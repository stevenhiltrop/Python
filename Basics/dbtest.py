import sqlite3


def main():
    try:
        con = sqlite3.connect('test.db')

        cur = con.cursor()

        """
        # Using execute to insert 1 by 1
        
        
        cur.execute('CREATE TABLE pet(id INT, name TEXT, price INT)')
        cur.execute('INSERT INTO pet VALUES(1, "cat", 400)')
        cur.execute('INSERT INTO pet VALUES(2, "dog", 600)')
        cur.execute('INSERT INTO pet VALUES(3, "rabbit", 200)')
        cur.execute('INSERT INTO pet VALUES(4, "bird", 60)')
        """

        # Using executescript to insert it all in 1 go
        cur.executescript("""DROP TABLE IF EXISTS pet;
        CREATE TABLE pet(id INT, name TEXT, price INT);
            INSERT INTO pet VALUES(1, "cat", 400);
            INSERT INTO pet VALUES(2, "dog", 600);
        """)

        pet = ((3, "rabbit", 200),
               (4, "bird", 60),
               (5, "goat", 500))

        cur.executemany("INSERT INTO pet VALUES(?, ?, ?)", pet)

        con.commit()

        cur.execute('SELECT * FROM pet')
        data = cur.fetchall()

        for row in data:
            print(row)

    except sqlite3.Error:
        if con:
            print("Error! Rolling back")
            con.rollback()

    finally:
        if con:
            con.close()


if __name__ == '__main__':
    main()
