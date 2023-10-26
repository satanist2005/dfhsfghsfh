class Treyg:

    def __init__(self, x1, y1,x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def rasst(self):
        return ((self.x2 - self.x1)**2+(self.y2 - self.y1)**2)**0.5


rs = Treyg(2, 4, 6, 9)
rs2 = Treyg(6, 9, 6, 0)
rs3 = Treyg(6, 0, 2, 4)
rs4 = rs.rasst()+rs2.rasst()+rs3.rasst()
print(rs4)