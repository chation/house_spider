from itemadapter import ItemAdapter
from house_need.settings import DATABASE_INFO
import pymysql

class HouseNeedPipeline:
    def __init__(self):
        self.db = pymysql.connect(DATABASE_INFO['host'], DATABASE_INFO['user'], DATABASE_INFO['pwd'], DATABASE_INFO['db'], charset=DATABASE_INFO['char'], port=DATABASE_INFO['port'])
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = "REPLACE INTO house_spider (subway, title, name, area, far, money, source) VALUES ('%s', '%s',  '%s',  '%s',  '%s', '%s', %d)" % ('杨家湾', item['title'], item['name'], item['area'], item['far'], item['money'], item['source'])
        print(sql)
        self.cursor.execute(sql)
        if self.cursor.rowcount == 1 :
            print('新数据 发送邮件通知')
        
        self.db.commit()
        print('REPLACR INTO SUCCESSFULL')

        return item
    
    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
