class HangHoa:
    """Lớp cha — chứa thuộc tính chung của mọi loại hàng hóa.

    Tại sao dùng lớp cha?
    → Vì ma_hang, ten_hang, nha_sx là thuộc tính CHUNG cho tất cả
      các loại hàng. Thay vì viết lại 3 lần, ta viết 1 lần ở đây
      rồi cho các lớp con kế thừa.
    """

    def __init__(self, ma_hang, ten_hang, nha_sx):
        self.__ma_hang  = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx   = nha_sx

    # ── Getter ──
    def getMaHang(self):   return self.__ma_hang
    def getTenHang(self):  return self.__ten_hang
    def getNhaSX(self):    return self.__nha_sx

    def hien_thi(self):
        """Hiển thị thông tin chung — lớp con sẽ GHI ĐÈ (override)
        phương thức này để bổ sung thông tin riêng."""
        print(f"  Mã hàng  : {self.__ma_hang}")
        print(f"  Tên hàng : {self.__ten_hang}")
        print(f"  Nhà SX   : {self.__nha_sx}")

class HangDienMay(HangHoa):
    """Kế thừa HangHoa, thêm: giá, bảo hành, điện áp, công suất.

    Lưu ý cú pháp: class HangDienMay(HangHoa)
    → Dấu ngoặc tròn chứa tên lớp cha = kế thừa.
    """

    def __init__(self, ma_hang, ten_hang, nha_sx,
                 gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.__gia        = gia
        self.__tg_baohanh = tg_baohanh   
        self.__dien_ap    = dien_ap      
        self.__cong_suat  = cong_suat    

    def hien_thi(self):
        """Override hien_thi(): gọi lớp cha + in thêm thông tin riêng."""
        print("═══ HÀNG ĐIỆN MÁY ═══")
        super().hien_thi()          # Gọi hien_thi() của HangHoa
        print(f"  Giá      : {self.__gia:,.0f} VNĐ")
        print(f"  Bảo hành : {self.__tg_baohanh} tháng")
        print(f"  Điện áp  : {self.__dien_ap} V")
        print(f"  Công suất: {self.__cong_suat} W")


class HangSanhSu(HangHoa):
    """Kế thừa HangHoa, thêm: giá, loại nguyên liệu."""

    def __init__(self, ma_hang, ten_hang, nha_sx,
                 gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.__gia              = gia
        self.__loai_nguyen_lieu = loai_nguyen_lieu

    def hien_thi(self):
        print("═══ HÀNG SÀNH SỨ ═══")
        super().hien_thi()
        print(f"  Giá         : {self.__gia:,.0f} VNĐ")
        print(f"  Nguyên liệu : {self.__loai_nguyen_lieu}")


class HangThucPham(HangHoa):
    """Kế thừa HangHoa, thêm: giá, ngày SX, ngày hết hạn."""

    def __init__(self, ma_hang, ten_hang, nha_sx,
                 gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.__gia         = gia
        self.__ngay_sx     = ngay_sx
        self.__ngay_het_han = ngay_het_han

    def hien_thi(self):
        print("═══ HÀNG THỰC PHẨM ═══")
        super().hien_thi()
        print(f"  Giá        : {self.__gia:,.0f} VNĐ")
        print(f"  Ngày SX    : {self.__ngay_sx}")
        print(f"  Hết hạn    : {self.__ngay_het_han}")

dm = HangDienMay(
    "DM001", "Tủ lạnh Inverter 360L", "Samsung",
    12_500_000, 24, 220, 150
)

ss = HangSanhSu(
    "SS001", "Bộ chén sứ Minh Long", "Minh Long",
    850_000, "Sứ cao cấp"
)

tp = HangThucPham(
    "TP001", "Cà phê rang xay Aura Brew", "Aura Brew",
    185_000, "01/03/2026", "01/03/2027"
)

dm.hien_thi()
print()
ss.hien_thi()
print()
tp.hien_thi()
