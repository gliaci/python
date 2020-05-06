import pymysql
import pymysql.cursors as DictCursor


class BookingService:

    def __init__(self, dbConnectionData, dbUser, passwd):
        self.db_host = dbConnectionData['host']
        self.db_port = dbConnectionData['port']
        self.db_name = dbConnectionData['dbname']
        self.db_user = dbUser
        self.db_passwd = passwd
        self.db_cursor = None

        self.dbh = self.__makeConnection()

    def __makeConnection(self):
        db = pymysql.Connect(host=self.db_host, port=self.db_port,
                             user=self.db_user, password=self.db_passwd,
                             database=self.db_name)

        db.cursorclass = DictCursor.DictCursor

        if db is None:
            return None

        self.db_cursor = db.cursor()
        return db

    def getBookingFlights(self, booking):
        sql = "SELECT * FROM BOOKING_FLIGHTS WHERE ID_BOOKING = {};".format(booking)
        try:
            self.db_cursor.execute(sql)
            return self.db_cursor.fetchall()
        except pymysql.Error as e:
            print("MySql Error Code {}".format(e))
            self.dbh.close()
        return None
