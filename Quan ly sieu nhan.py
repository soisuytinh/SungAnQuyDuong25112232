class SieuNhan:
    def __init__(self, ten="", vu_khi="", mau_sac="", suc_manh=0):
        self.ten      = ten
        self.vu_khi   = vu_khi
        self.mau_sac  = mau_sac
        self.suc_manh = suc_manh

    def __str__(self):
        return (f"  ✦ {self.ten:10} | Vũ khí: {self.vu_khi:8} | "
                f"Màu: {self.mau_sac:8} | Sức mạnh: {self.suc_manh}")


# ---- Nhập danh sách bằng while ----
danh_sach = []
print("=== NHẬP DANH SÁCH SIÊU NHÂN ===")
print("(Nhấn Enter để kết thúc)\n")

while True:
    ten = input("Tên siêu nhân: ")
    if ten == "":
        break
    vu_khi  = input("Vũ khí: ")
    mau_sac = input("Màu sắc: ")
    suc_manh = int(input("Sức mạnh (1-100): "))
    danh_sach.append(SieuNhan(ten, vu_khi, mau_sac, suc_manh))
    print(f"  → Đã thêm {ten}!\n")

# ---- In danh sách bằng for ----
print(f"\n=== DANH SÁCH {len(danh_sach)} SIÊU NHÂN ===")
for i, sn in enumerate(danh_sach, 1):
    print(f"{i}.", sn)