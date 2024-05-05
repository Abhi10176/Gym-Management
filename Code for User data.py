import mysql.connector as sql
fit=sql.connect(host='localhost',user='root',passwd='admin@123',database='fit_project')
if fit.is_connected():
                print('connected')
                c1=fit.cursor()
                c1.execute('create table user_fitness_rahi(user_id varchar(10) primary key,password varchar(11),name varchar(10))')
                fit.commit()
                print('table created')
