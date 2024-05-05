import mysql.connector as sql
fit=sql.connect(host='localhost',user='root',passwd='admin@123',database='fit_project')
if fit.is_connected():
    print('connected')
    c1=fit.cursor()
    c1.execute('create table Gym_items(object_id int(225) primary key,object_name varchar(65),date_of_parchase varchar(65),repairing_datvarchar(65),total_people_using int(65))')
    fit.commit()
    print('table created')
