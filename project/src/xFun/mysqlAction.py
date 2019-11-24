import pymysql as MySQLdb
import Config
import re

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
    DB_NAME = 't_img_resource'
    print(fj['img_src'])

    cursor = db.cursor()

    sql = 'select count(1) from t_img_resource where img_src = "%s"'%(fj['img_src'])

    cursor.execute(sql)
    result = cursor.fetchone()
    if result[0] != 0:
        return

    cursor = db.cursor()
    sql = 'insert into '+DB_NAME+' (img_src,img_alt,img_origin,created_time) values ("%s","%s","%s",now())'%(fj['img_src'], fj['img_alt'], 'http://img.netbian.com')
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    
def get_img_src(path):
    img_list = []

    with open(path,'r+',encoding='utf-8') as wallpapers:
        for line in wallpapers:
            wall_src = {}
            wall_src['img_src'] = re.search( r'img_src:(.*), *', line).group(1)
            wall_src['img_alt'] = re.search( r'img_alt:(.*)?"', line).group(1)
            img_list.append(wall_src)
            # print(wall_src)
    return img_list


def initSave(fj_List):
    img_src_list = get_img_src('./wallpaper.txt')
    db = connectDB()
    for fj in img_src_list:
        insertFaceJav(db, fj)


if __name__ == "__main__":
    initSave([])
