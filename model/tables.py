from flask import Flask
from storage import backbone
from model import func as func_

app = Flask(__name__)

class dbStructure(object):

    def __init__(self):
        self.tableNames = {'Bill':'billing', 'cows':'test', 'queryTableNames':'d'}

        '''
        Key = sqlite3 sets
        Value = URL Query
        '''
        self.operatorList = {'SELECT':'view', 'CREATE':'insert','DROP':'delete','UPDATE':'update'}
#        nn = "NOT NULL"
#        self.id = {'id' : 'Integer PRIMARY KEY autoincrement'}
#        self.name = {'name': ' varchar(75) ' + nn}
#        self.creationDate = {'dateCreated' : 'DATE'}
#        self.lastName = {'LastName','varchar(255) ' + nn}
#        self.fistName = {'FirstName','varchar(255) ' + nn}
#        self.address = {'Address', 'varchar(255) ' + nn}
#        self.city = {'City', 'varchar(255) ' + nn}
        self.feed = backbone.get_db()

    def main(self, queryTableName, queryOperator=None, searchingFor=None ):
        a = {}
        default = {queryTableName:False}

        secureTableName = func_.dictValueExist(queryTableName, self.tableNames)

        if self.verifyTableExistence(secureTableName):

            if queryOperator != None:

                tableOperator = func_.dictValueExist(queryOperator, self.operatorList)

                return self.dbSelectForResults(secureTableName, tableOperator, searchingFor)

            else:
                a = {"Table Exist, no operator specified": False}

        else:
            a.update(default)

        return a

    def dbSelectForResults(self, table=None, operator=None, listColumns="*"):
        db = backbone.get_db()
        listSelection = ", ".join(listColumns)
        try:
            cur = db.execute(operator + ' ' + listSelection + ' FROM ' + table)
            results = cur.fetchall()
        except:
            results =  {"No Results found or error with operator": False}
        # return render_template('home.html', labels=labels, results=results, list=list)
        return (results)

    def verifyTableExistence(self, table=None):

        try:
            self.feed.execute('SELECT 1 FROM ' + table + ' LIMIT 1;')
            return True

        except:

            return {"Table doesn't exist", False}

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
