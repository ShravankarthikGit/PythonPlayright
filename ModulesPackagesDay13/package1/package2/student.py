class Student:
    def __init__(self, sid, sname, sgrad):
        self.sid = sid
        self.sname = sname
        self.sgrad = sgrad

    def displaystu(self):
        print("stuid:{} stuname:{} stusal:{}".format(self.sid, self.sname, self.sgrad))