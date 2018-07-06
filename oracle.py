import cx_Oracle
import os
from matplotlib import pyplot
from zhanming import zm
pyplot.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
pyplot.rcParams['axes.unicode_minus']=False #用来正常显示负号
conn = cx_Oracle.connect('bjtu', 'bjtu123', '222.249.239.122/orcl')
curs = conn.cursor()
sql1='''select jinzhan,FLOOR((OOOO-TRUNC(TO_DATE('2018/6/1','YYYY/MM/DD')))*24*60/30)*0.5 as shike ,COUNT(*) as renshu1
    FROM TEST74DELETE GROUP BY jinzhan,FLOOR((OOOO-TRUNC(TO_DATE('2018/6/1','YYYY/MM/DD')))*24*60/30)
    ORDER BY jinzhan, FLOOR((OOOO-TRUNC(TO_DATE('2018/6/1','YYYY/MM/DD')))*24*60/30)'''
sql2='''select chuzhan,FLOOR((dddd-TRUNC(TO_DATE('2018/6/1','YYYY/MM/DD')))*24*60/30)*0.5 as shike ,COUNT(*) as renshu1
    FROM TEST74DELETE GROUP BY chuzhan,FLOOR((dddd-TRUNC(TO_DATE('2018/6/1','YYYY/MM/DD')))*24*60/30)
    ORDER BY chuzhan, FLOOR((dddd-TRUNC(TO_DATE('2018/6/1','YYYY/MM/DD')))*24*60/30)'''
r1=curs.execute(sql1)
row1=curs.fetchall()
r2=curs.execute(sql2)
row2=curs.fetchall()
b=0
for a in zm:


    x=list(row1[i][1] for i in range(len(row1)) if row1[i][0]==a)
    y=list(row1[i][2] for i in range(len(row1)) if row1[i][0]==a)
    x1 = list(row2[i][1] for i in range(len(row2)) if row2[i][0] == a)
    y1 = list(-row2[i][2] for i in range(len(row2)) if row2[i][0] == a)
    pyplot.plot(x,y,'--',label='进站')
    pyplot.plot(x1,y1,'--',label='出站')
    pyplot.axhline(y=0)
    pyplot.xlabel('时间')
    pyplot.ylabel('人数')
    pyplot.title(a)
    pyplot.legend()
    pyplot.savefig('tupian/'+a+'.png')
    pyplot.close()
    #pyplot.show()

curs.close()
conn.close()

