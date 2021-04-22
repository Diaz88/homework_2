import sqlite3
connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
cursor.execute("CREATE TABLE computers (monitor TEXT, cpu TEXT, ram TEXT, video_card TEXT, id INTEGER)");
cursor.execute("INSERT INTO computers VALUES ('samsung', 'intel_core', 'ddr', 'geforce', 1)");
cursor.execute("INSERT INTO computers VALUES ('acer', 'intel_core2', 'ddr2', 'geforce2', 2)");
cursor.execute("INSERT INTO computers VALUES ('hp', 'intel_core3', 'ddr3', 'geforce3', 3)");
cursor.execute("INSERT INTO computers VALUES ('lenovo', 'intel_core4', 'ddr4', 'geforce4', 4)");
cursor.execute("SELECT monitor, ram FROM computers");
cursor.execute("DELETE FROM computers where id = 2 and ram = ddr4");
cursor.execute("UPDATE computers SET cpu = intel_core7 where id = 3 ");


cursor.close()
connection.close()

