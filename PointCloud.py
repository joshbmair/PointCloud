debug_point = False
debug_cloud = False

class Point:
    EPSILON = 1e-5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.EPSILON = 1e-5

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def toString(self):
        str = '({x}, {y})'.format(self.x, self.y)
        return str

    def __eq__(self, p):    # TODO Add feature for if p is not a point
        if abs(self.x - p.x) < Point.EPSILON and abs(self.y - p.y) < Point.EPSILON:
            return True
        else: return False

    def euclid_dist(self, p):
        dx = abs(self.x - p.x)
        dy = abs(self.y - p.y)

        return (dx**2 + dy**2) ** 0.5

class Cloud:
    def __init__(self):
        self.cloud = set()

####################
# TEST POINT CLASS #
####################

debug_point = True
if debug_point:
    print('Point class debug ON')
    print(format('EPSILON: {e}', e = Point.EPSILON))

    origin = Point(0.0, 0.0)
    p1 = Point(0.0, 4.0)
    p2 = Point(3.0000001, 3.9999999)
    p3 = Point(3.0, 4.0)
    p4 = Point(0.0,5.0)
    p5 = Point(12.0,0.0)

    print("origin: {p}", p = origin)
    print("p1: {p}", p = p1)
    print("p2: {p}", p = p2)
    print("p3: {p}", p = p3)
    print("p4: {p}", p = p4)
    print("p5: {p}", p = p5)

else: print('Point class debug OFF')

####################
# TEST CLOUD CLASS #
####################

# debug_cloud = False
# if debug_cloud:
#     print("Cloud class debug ON")