import sqlite3

db = sqlite3.connect('htmlpage.db')
cursor = db.cursor()

##cursor.execute("DROP TABLE bodytext")
##db.commit()

# to create the table if it doesn't already exist

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS \
            bodytext( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            Title TEXT, \
            Content TEXT \
            );")
    db.commit()

createTable()

# to add a record
def newPage(title, content):
    addvalues = "'{}', '{}'".format(title, content)
    addpage = "INSERT INTO bodytext (Title, Content) VALUES \
        ({});".format(addvalues)
    cursor.execute(addpage)
    db.commit()
    # return db.total_changes

# to delete a record
def deletePage(title):
    cursor.execute("DELETE FROM bodytext WHERE Title = '{}'".format(title))
    db.commit()
    # print(db.total_changes)

# to update a record
def updatePage(title, body):
    cursor.execute("UPDATE bodytext SET Content = '{}' WHERE Title = '{}'".format(body, title))
    db.commit()                   

# to return content
def displayItem(title):
    select = "SELECT Content FROM bodytext WHERE Title = '{}';".format(title)
    #select = "SELECT Content FROM bodytext WHERE Title = 'test';"
    #select = "SELECT Content FROM bodytext;"
    display = cursor.execute(select)
    rows = display.fetchall()
    return rows
    #print(rows)

# to return title
def findTitle(title):
    select = "SELECT Title FROM bodytext WHERE Title = '{}';".format(title)
    display = cursor.execute(select)
    rows = display.fetchall()
    #print(rows)
    return rows

# to return all data in bodytext table
def displayAll():
    select = "SELECT * FROM bodytext;"
    display = cursor.execute(select)
    rows = display.fetchall()
    return rows


##def testFindTitle():
##    if findTitle('blah'):
##        print('yes')
##    else:
##        print('no')
##testFindTitle()


##for item in displayAll():
##    print(item)
    
#displayItem(title)
