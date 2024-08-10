


class Point:            # (100, 200)
    def __init__(self, p: tuple[int]) -> None:
        self.x, self.y = p
        self.list = [self.x, self.y]

    def __repr__(self):
        return f"({self.x}, {self.y})"
    

    @staticmethod
    def handlePoints(point1: tuple, point2: tuple) -> dict:
        x1, y1 = point1
        x2, y2 = point2

        # return variables:
        p1, p2, width, height = [None]*4 

        # condition (1) ( TopLeft-DownRight )
        if (x1 < x2) and (y1 < y2):
            p1 = Point((x1, y1))
            p2 = Point((x2, y2))
            width = x2 - x1
            height = y2 - y1

        # condition (2) ( TopRight-DownLeft )
        elif (x1 > x2) and (y1 < y2):
            p1 = Point((x2, y1))
            p2 = Point((x1, y2))
            width = (x1 - x2)
            height = (y2 - y1)

        # condition (3) ( DownRight-TopLeft )
        elif (x1 > x2) and (y1 > y2):
            p1 = Point((x2, y2))
            p2 = Point((x1, y1))
            width = (x1 - x2)
            height = (y1 - y2)

        # condition (4) ( DownLeft-TopRight )
        elif (x1 < x2) and (y1 > y2):
            p1 = Point((x1, y2))
            p2 = Point((x2, y1))
            width = x2 - x1
            height = y1 - y2

        return {
            "p1": p1,
            "p2": p2,
            "scale": (width, height)
        }



    @staticmethod
    def getPhotoScale(p1: tuple, p2: tuple):
        maxP = Point.getMaxScaleOfPoints(p1[0], p1[1], p2[0], p2[1])
        minP = Point.getMinScaleOfPoints(p1[0], p1[1], p2[0], p2[1])
        x, y = maxP.x - minP.x, maxP.y - minP.y
        return Point((x,y))

