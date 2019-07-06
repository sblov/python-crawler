import MySQLdb
import Config

config = {
    'host': Config.MYSQL_IP,
    'port': Config.MYSQL_PORT,
    'user': Config.MYSQL_LOGIN,
    'passwd': Config.MYSQL_PASS,
    'db': Config.MYSQL_SCHEME,
    'charset': 'utf8'
}


def connectDB():
    db = MySQLdb.connect(**config)
    return db

def insertFaceJav(db, fj):
    DB_NAME = 't_facejav'
    print(fj['title'])

    cursor = db.cursor()

    sql = 'select count(1) from t_facejav where title = "%s"'%(fj['title'])

    cursor.execute(sql)
    result = cursor.fetchone()
    if result[0] != 0:
        return

    cursor = db.cursor()
    sql = 'insert into '+DB_NAME+' (title,IMGURL,PAGEURL,description,updateTime) values ("%s","%s","%s","%s",now())'%(fj['title'], fj['img'], fj['page'], fj['des'])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    
def initSave(fj_List):
    db = connectDB()
    for fj in fj_List:
        insertFaceJav(db, fj)

