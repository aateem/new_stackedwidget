#!/usr/bin/python3

import sqlite3

def main():

    conn = sqlite3.connect('qtrainer.db')
    if not conn:
        raise Exception('Error: Connection failed')

    stat_date = ((1, 1, 5, 288, '00:15:10', '2012-04-02 20:15:11.111', 2),
                 (1, 2, 3, 127, '00:08:05', '2012-04-02 20:45:15.121', 1),
                 (1, 3, 4, 301, '00:12:03', '2012-04-02 22:05:18.345', 2),
                 (1, 4, 5, 220, '00:10:16', '2012-04-02 22:05:18.345', 3)
                )

    with conn:
        cur = conn.cursor()

        cur.executemany("insert into statistic values(?, ?, ?, ?, ?, ?, ?)", stat_date)


if __name__ == '__main__':
    main()
