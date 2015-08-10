from flask import Flask
from storage import backbone
from model import func as func_

app = Flask(__name__)

class dbStructure(object):

    def __init__(self):
        ''' Takes the URL Query request, compares to our static dict, and looks through our database '''
        self.tableNames = {'Bill':'billing', 'cows':'test', 'queryTableNames':'d'}

        ''' Same thing here, URL Query to predetermined dict, compares and continues to database '''
        self.operatorList = {'SELECT':'view', 'CREATE':'insert','DROP':'delete','UPDATE':'update'}

        ''' Let's put our database connection on standby'''
        self.feed = backbone.get_db()

        self.default = {}

    def main(self, queryTableName, queryOperator=None, dbColumnSearch=None ):
        '''
        Example:
            [queryOperator=SELECT] [dbColumnSearch=id, name, date] FROM [queryTableName=Billing]
        '''

        a = {}
        secureTableName = func_.dictValueExist(queryTableName, self.tableNames)

        if self.verifyTableExistence(secureTableName):

            if queryOperator != None:

                tableOperator = func_.dictValueExist(queryOperator, self.operatorList)

                return self.dbSelectForResults(secureTableName, tableOperator, dbColumnSearch)

            else:
                a = {"Table Exist, no operator specified": False}

        else:
            msg = "The requested table doesn't exist '%s'"% secureTableName
            self.default = {msg: False}
            return self.default

        return a

    def dbSelectForResults(self, table=None, operator=None, searchColumns="*"):
        db = backbone.get_db()
        listSelection = ", ".join(searchColumns)

        try:
            cur = db.execute(operator + ' ' + listSelection + ' FROM ' + table)

            return cur.fetchall()

        except:

            self.default = {"No Results found or error with operator": False}

    def verifyTableExistence(self, table=None):

        try:
            self.feed.execute('SELECT 1 FROM ' + table + ' LIMIT 1;')
            return True

        except:
            self.default = {"Table doesn't exist", False}

    def tablecreation(self, naming):
        print ''
        self.feed.execute(
        "CREATE Table " + naming + " (id integer, chair varchar(52) NOT Null)")

    def nothing(self):
        print ''
        '''
        create table dbNames(
            id integer PRIMARY KEY autoincrement,
            name varchar(255) NOT NULL,
            description varchar(255) NOT NULL,
            datatype varchar(255),
            dateCreated DATE
        );
        '''
