from flask import Flask
from storage import backbone

app = Flask(__name__)


class dbStructure(object):

    def __init__(self):
        nn = "NOT NULL"
        self.tableNames = ['Bill', 'dbNames', 'cows']
        self.id = {'id' : 'Integer PRIMARY KEY autoincrement'}
        self.name = {'name': ' varchar(75) ' + nn}
        self.creationDate = {'dateCreated' : 'DATE'}
        self.lastName = {'LastName','varchar(255) ' + nn}
        self.fistName = {'FirstName','varchar(255) ' + nn}
        self.address = {'Address', 'varchar(255) ' + nn}
        self.city = {'City', 'varchar(255) ' + nn}
        self.feed = backbone.get_db()

    def main(self):
        a = {}

        for table in self.tableNames:

            if self.verifyTableExistence(table):
                a.update({table:True})

            else:
                a.update({table:False})

        return a

    def dbSelect(self, table=None, listColumns=None):
        db = backbone.get_db()
        listSelection = ", ".join(listColumns)
        try:
            cur = db.execute('SELECT ' + listSelection + ' from ' + table)
            results = cur.fetchall()
        except:
            results = ["Incorrect Column"]
        # return render_template('home.html', labels=labels, results=results, list=list)
        return (results)

    def verifyTableExistence(self, table=None):

        try:
            self.feed.execute('SELECT 1 FROM ' + table + ' LIMIT 1;')
            return True

        except:

            self.tablecreation(t)
            return False

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
