from Main.mysql_connection import select, commit

rows = select("SELECT * FROM railway.Habitacion;")
for r in rows:
    print(r)