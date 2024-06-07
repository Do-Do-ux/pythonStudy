import pymysql

class DaoEmp:
    def __init__(self):
        self.con = pymysql.connect(
        user="root",
        password="python",
        host="localhost",
        port=3305,
        database="python"
)
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
    def selectList(self):
        sql ="select * from emp"
        self.cur.execute(sql)
        
        list = self.cur.fetchall()
        return list
    
    def selectOne(self,e_id):
        sql = f"""
        select 
            e_id,
            e_name,
            gen,
            addr 
        from 
            emp 
        where 
            e_id='{e_id}'
        """
        self.cur.execute(sql)
        one = self.cur
        
        return one.fetchone()
    def insert(self,e_id,e_name,gen,addr):
        sql = f"""
        insert into emp(e_id,e_name,gen,addr)
        values('{e_id}','{e_name}','{gen}','{addr}')
        """
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
    
    def update(self,e_id,e_name,gen,addr):
        sql = f"""
        update emp
    
        set 
            e_id = {e_id},
            e_name = {e_name},
            gen = {gen},
            addr = {addr}
    
        where
            e_id = {e_id}
        """
        cnt = self.cur.execute(sql)
        self.con.commit();
        
        return cnt
    
    def delete(self,e_id):
        sql = f"""
       
        delete 
        
        from  emp
            
        where
            e_id = {e_id}
        """

        cnt = self.cur.execute(sql)
        self.con.commit();
        
        return cnt
            
            
    def __del__(self):
        self.cur.close()
        self.con.close()
    
        
if __name__ == '__main__':
    de = DaoEmp()
    list = de.selectList()
    # vo = de.insert('1','3','3','3')
    # cnt = de.update("3","6","6","6")
    cnt = de.delete("3")
    print(cnt)
    #print(list)
