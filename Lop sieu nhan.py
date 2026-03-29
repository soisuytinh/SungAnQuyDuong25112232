class SieuNhan:
    def __init__(self, ten: str, vu_khi: str, mau_sac: str):
        self.ten     = ten
        self.vu_khi  = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return (f"Siêu nhân {self.ten} | "
                f"Vũ khí: {self.vu_khi} | "
                f"Màu sắc: {self.mau_sac}")


# ---- Khởi tạo 2 đối tượng ----
sieu_nhan_A = SieuNhan("A", "kiếm", "đỏ")
sieu_nhan_B = SieuNhan("B", "khiên", "xanh")

# ---- In ra thể hiện ----
print(sieu_nhan_A)
print(sieu_nhan_B)