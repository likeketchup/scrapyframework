data = {'Michael': "aa", 'Bob': "75", 'Tracy': "dss"}
cates = data.keys()
prefix = "".join(['INSERT INTO ', 'table_name'])
fields = ",".join([filed for filed in cates])
values = ",".join(["%s" % data[i] for i in cates])
sql = "".join([prefix, "(", fields, ") VALUES(\'", values, "\');"])
print(sql)