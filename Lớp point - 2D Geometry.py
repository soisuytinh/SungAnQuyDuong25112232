import math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def hien_thi(self):
        print(f"Điểm ({self.x}, {self.y})")

    def doi_xung_qua_O(self):
        return Point(-self.x, -self.y)

    def khoang_cach_den_O(self):
        return math.sqrt(self.x**2 + self.y**2)

    def khoang_cach_den(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


A = Point(3, 4)
print("Điểm A:"); A.hien_thi()
xb = int(input("Nhập x của B: "))
yb = int(input("Nhập y của B: "))
B = Point(xb, yb)
print("Điểm B:"); B.hien_thi()
C = B.doi_xung_qua_O()
print("Điểm C (đối xứng B qua O):"); C.hien_thi()
print(f"Khoảng cách B đến O: {B.khoang_cach_den_O():.2f}")
print(f"Khoảng cách A đến B: {A.khoang_cach_den(B):.2f}")
