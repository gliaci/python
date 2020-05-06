import pymysql
import pymysql.cursors as DictCursor


class TourOperatorService:

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

    def getActivationIdsByBusinessProfiles(self, businessProfiles):
        sql = "SELECT ID FROM TOUR_OPERATOR_ACTIVATIONS WHERE ID_BUSINESS_PROFILE IN ('{}');".format("', '".join(businessProfiles))
        try:
            self.db_cursor.execute(sql)
            return self.db_cursor.fetchall()
        except pymysql.Error as e:
            print("MySql Error Code {}".format(e))
            self.dbh.close()
        return None

    def getActivationConfigurationsIdByActivationId(self, activationIds):
        sql = "SELECT ID_CONFIGURATIONS FROM TOUR_OPERATOR_ACTIVATIONS_CONFIGURATIONS where ID_ACTIVATIONS IN ({});".format(", ".join(activationIds))
        try:
            self.db_cursor.execute(sql)
            return self.db_cursor.fetchall()
        except pymysql.Error as e:
            print("MySql Error Code {}".format(e))
            self.dbh.close()
        return None

    def getConfigurationIdsByConfigurationIdsAndAirlineIds(self, configurationIds, airlineIds):
        sql = "SELECT ID FROM TOUR_OPERATOR_CONFIGURATIONS where ID in ({}) and ID_AIRLINE in ('{}');".format(", ".join(configurationIds), "', '".join(airlineIds))
        try:
            self.db_cursor.execute(sql)
            return self.db_cursor.fetchall()
        except pymysql.Error as e:
            print("MySql Error Code {}".format(e))
            self.dbh.close()
        return None
