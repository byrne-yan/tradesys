from . import Store
from holds import HeldStock
from stocks import Stock
import sqlite3


# def adapt_hold(hold):
#     return ("%f;%f" % (point.x, point.y)).encode('ascii')
#
#
# def convert_hold(s):
#     x, y = list(map(float, s.split(b";")))
#     return HoldedStock(x, y)


# Register the adapter
# sqlite3.register_adapter(HoldedStock, adapt_hold)

# Register the converter
# sqlite3.register_converter("stock", convert_hold)


class SQLite3Store(Store):
    ''

    def __init__(self, loc):
        # 链接数据库，若数据库不存在则创建
        self.con = sqlite3.connect(loc)

        # 在内存中创建数据库
        # con = sqlite3.connect(":memory:")

        # 创建游标对象
        self.cur = self.con.cursor()

        self.cur.execute("CREATE TABLE  IF NOT EXISTS holds(\
                 code TEXT PRIMARY KEY NOT NULL,\
                 price INT, \
                 volume INT,\
                 time DATE\
                 )")

    def get_holds(self):
        held_stocks = []
        for row in self.cur.execute("SELECT * FROM holds"):
            s = self.get_stock(row['code'])
            held_stocks.append(HeldStock(s, row['price'], row['volume'], row['time']))

        return held_stocks

    def get_stock(self):
        return Stock(self.cur.execute("SELECT * FROM stocks"))