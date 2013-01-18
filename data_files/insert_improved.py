#!/usr/bin/python3

import sqlite3
import os

def main():
    PATH = '/home/a_teem/Documents/Projects/Python/PySide/new_stackedwidget/data_files'

    conn = sqlite3.connect('qtrainer.db')
    if not conn:
        raise Exception('Error: Connection failed')

    with conn:
        for root, dirs, files in os.walk(PATH):
            for name in files:
                with open(os.path.join(root, name), encoding='utf-8') as f:
                    conn.execute("insert into exercize values(null, ?)", (f.read(),))


if __name__ == '__main__':
    main()
