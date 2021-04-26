import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("CREATE TABLE computers(monitor TEXT, cpu TEXT, ram TEXT, video_card TEXT)")


class Pc:

    def __init__(self, monitor, cpu, ram, video_card):
        self.monitor = monitor
        self.cpu = cpu
        self.ram = ram
        self.video_card = video_card

    def save(self):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO computers values (?, ?, ?, ?)", self.monitor, self.cpu, self.ram, self.video_card)
        connection.commit()


computer = Pc('samsung', 'intel_core', 'ddr', 'geforce')
computer.save()
computer2 = Pc('acer', 'intel_core_2', 'ddr_2', 'geforce_2')
computer2.save()


