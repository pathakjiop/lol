
dbms
prc 1 dbms evolution conclusion 

prc 2 ddl create alter (add modify drop rename) truncate drop rename

prc 3 dml select(* few) insert(single specific &) update(single few all) delete(where few all  ) merge

prc 4 slect * specific + - * / operator precedance parentheses as concatination mixed  concatination distincet  

prc 5 
cartesian product selecr * from table 1, table 2 
equi join select * from emp e dept d where edeptno = d.deptno
non equi join select * form table1, table 2 where table1.com > table2.col
joining select * form t1 , t2 where condition 
loj slect * from t1 t2 where t1.col = t2.com(+)
roj slect * from t1 t2 where t1.col(+) = t2.com
self join select a.col, b.col orm tableA tableB where a.col = b.col
cross join select* from t1 cross join t2
natural join select * from t1 natural jion t2 
using select * from t1 join t2 using (col_name)
on slect * from t1 join t2 on t1.col = t2.col
loj select * from table loj table on confition 
roj --
foj--

prc 6 sum avg min max count (colum * ) distince nvl group by 
illeagl usage  select emp_name, sum(salary) form employee;
order by asc desc 
having 

prc 7
subqueries  
in select * from empluee where salary in(select min (salary) fro empliyee group by did)
any slect * from employee where salaru < any( select salaty whrom eployee where jid = 10) 
all select  * from empoyee where sallary < all( select salry from empluee where jid = 10)

prc 8
not null unique primary key foreign key check
add drop disable enable cascade viewing 
