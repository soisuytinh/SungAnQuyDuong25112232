from abc import ABC, abstractmethod

class GiaKhongHopLeException(Exception):
    """Ngoại lệ khi giá không hợp lệ (< 0)."""
    pass


class MaHangTrungLapException(Exception):
    """Ngoại lệ khi mã hàng trùng lặp."""
    pass


class HangHoa(ABC):
    """Lớp cha — lớp trừu tượng chứa thuộc tính chung của mọi loại hàng hóa.

    Sử dụng ABC bắt buộc lớp con phải override các phương thức trừu tượng.
    """
    
    _danh_sach_ma_hang = set()

    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        if ma_hang in HangHoa._danh_sach_ma_hang:
            raise MaHangTrungLapException(f"Mã hàng '{ma_hang}' đã tồn tại!")
        HangHoa._danh_sach_ma_hang.add(ma_hang)
        
        self.__ma_hang  = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx   = nha_sx
        self.__gia      = gia

    @property
    def ma_hang(self):
        """Getter: mã hàng (read-only)."""
        return self.__ma_hang
    
    @property
    def ten_hang(self):
        """Getter: tên hàng (read-only)."""
        return self.__ten_hang
    
    @property
    def nha_sx(self):
        """Getter: nhà sản xuất (read-only)."""
        return self.__nha_sx
    
    @property
    def gia(self):
        """Getter: giá (read-only)."""
        return self.__gia
    
    @gia.setter
    def gia(self, gia_moi):
        """Setter: giá với validation (gia >= 0)."""
        if gia_moi < 0:
            raise GiaKhongHopLeException(f"Giá không được âm! Nhận được: {gia_moi}")
        self.__gia = gia_moi

    @abstractmethod
    def loai_hang(self):
        """Phương thức trừu tượng — lớp con phải override."""
        pass
    
    @abstractmethod
    def inTTin(self):
        """Phương thức trừu tượng — lớp con phải override với cùng tên."""
        pass
    
    def __str__(self):
        """Magic method: biểu diễn chuỗi của đối tượng."""
        return f"{self.loai_hang()} - {self.ma_hang}: {self.ten_hang} ({self.nha_sx}) - {self.gia:,.0f} VNĐ"
    
    def __eq__(self, other):
        """Magic method: so sánh bằng nhau (theo mã hàng)."""
        if not isinstance(other, HangHoa):
            return False
        return self.ma_hang == other.ma_hang
    
    def __lt__(self, other):
        """Magic method: so sánh nhỏ hơn (theo giá)."""
        if not isinstance(other, HangHoa):
            return NotImplemented
        return self.gia < other.gia
    
    def __hash__(self):
        """Magic method: hash để dùng trong set/dict."""
        return hash(self.ma_hang)


class HangDienMay(HangHoa):
    """Kế thừa HangHoa, thêm: bảo hành, điện áp, công suất."""

    def __init__(self, ma_hang, ten_hang, nha_sx, gia,
                 tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__tg_baohanh = tg_baohanh   
        self.__dien_ap    = dien_ap      
        self.__cong_suat  = cong_suat    

    @property
    def tg_baohanh(self):
        return self.__tg_baohanh
    
    @property
    def dien_ap(self):
        return self.__dien_ap
    
    @property
    def cong_suat(self):
        return self.__cong_suat

    def loai_hang(self):
        """Override: trả về loại hàng."""
        return "HÀNG ĐIỆN MÁY"
    
    def inTTin(self):
        """Override: in thông tin hàng điện máy."""
        print("═══ HÀNG ĐIỆN MÁY ═══")
        print(f"  Mã hàng  : {self.ma_hang}")
        print(f"  Tên hàng : {self.ten_hang}")
        print(f"  Nhà SX   : {self.nha_sx}")
        print(f"  Giá      : {self.gia:,.0f} VNĐ")
        print(f"  Bảo hành : {self.tg_baohanh} tháng")
        print(f"  Điện áp  : {self.dien_ap} V")
        print(f"  Công suất: {self.cong_suat} W")


class HangSanhSu(HangHoa):
    """Kế thừa HangHoa, thêm: loại nguyên liệu."""

    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyen_lieu = loai_nguyen_lieu

    @property
    def loai_nguyen_lieu(self):
        return self.__loai_nguyen_lieu

    def loai_hang(self):
        """Override: trả về loại hàng."""
        return "HÀNG SÀNH SỨ"
    
    def inTTin(self):
        """Override: in thông tin hàng sành sứ."""
        print("═══ HÀNG SÀNH SỨ ═══")
        print(f"  Mã hàng  : {self.ma_hang}")
        print(f"  Tên hàng : {self.ten_hang}")
        print(f"  Nhà SX   : {self.nha_sx}")
        print(f"  Giá      : {self.gia:,.0f} VNĐ")
        print(f"  Nguyên liệu : {self.loai_nguyen_lieu}")


class HangThucPham(HangHoa):
    """Kế thừa HangHoa, thêm: ngày SX, ngày hết hạn."""

    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx     = ngay_sx
        self.__ngay_het_han = ngay_het_han

    @property
    def ngay_sx(self):
        return self.__ngay_sx
    
    @property
    def ngay_het_han(self):
        return self.__ngay_het_han

    def loai_hang(self):
        """Override: trả về loại hàng."""
        return "HÀNG THỰC PHẨM"
    
    def inTTin(self):
        """Override: in thông tin hàng thực phẩm."""
        print("═══ HÀNG THỰC PHẨM ═══")
        print(f"  Mã hàng  : {self.ma_hang}")
        print(f"  Tên hàng : {self.ten_hang}")
        print(f"  Nhà SX   : {self.nha_sx}")
        print(f"  Giá      : {self.gia:,.0f} VNĐ")
        print(f"  Ngày SX    : {self.ngay_sx}")
        print(f"  Hết hạn    : {self.ngay_het_han}")


class QuanLyHangHoa:
    """Context Manager để quản lý file danh sách hàng hóa."""
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.danh_sach = []
    
    def __enter__(self):
        """Mở file và đọc dữ liệu."""
        print(f"→ Mở file: {self.file_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Đóng file và lưu dữ liệu."""
        print(f"→ Đóng file: {self.file_name}")
        if exc_type:
            print(f"⚠ Lỗi: {exc_val}")
        return False
    
    def them_hang(self, hang):
        """Thêm hàng hóa vào danh sách."""
        self.danh_sach.append(hang)
    
    def hien_thi_tat_ca(self):
        """Hiển thị tất cả hàng hóa."""
        for hang in self.danh_sach:
            hang.inTTin()
            print()
    
    def sap_xep_theo_gia(self):
        """Sắp xếp theo giá (sử dụng __lt__)."""
        return sorted(self.danh_sach)


if __name__ == "__main__":
    try:
        dm = HangDienMay(
            "PS5001", "PlayStation 5", "Sony",
            10_500_000, 24, 220, 100
        )

        ss = HangSanhSu(
            "SS001", "Bộ chén sứ Minh Long", "Minh Long",
            850_000, "Sứ cao cấp"
        )

        tp = HangThucPham(
            "TP001", "Cà phê rang xay Aura Brew", "Aura Brew",
            185_000, "01/03/2026", "01/03/2027"
        )

        with QuanLyHangHoa("danh_sach_hang_hoa.txt") as quan_ly:
            quan_ly.them_hang(dm)
            quan_ly.them_hang(ss)
            quan_ly.them_hang(tp)
            
            print("\n【 DANH SÁCH HÀNG HÓA 】\n")
            quan_ly.hien_thi_tat_ca()
            
            print("\n【 SAU KHI SẮP XẾP THEO GIÁ (TĂNG DẦN) 】\n")
            danh_sach_sap_xep = quan_ly.sap_xep_theo_gia()
            for hang in danh_sach_sap_xep:
                print(f"  • {hang}")
            
            print("\n【 KIỂM TRA MAGIC METHODS 】\n")
            print(f"✓ __eq__ (ss == dm): {ss == dm}")
            print(f"✓ __eq__ (ss == ss): {ss == ss}")
            print(f"✓ __lt__ (tp < dm): {tp < dm}")
            print(f"✓ __hash__ (dùng trong set): {len({dm, ss, tp})} loại hàng")
            
            print("\n【 KIỂM TRA VALIDATION 】\n")
            try:
                dm.gia = -100
            except GiaKhongHopLeException as e:
                print(f"⚠ Bắt được lỗi: {e}")
            
            try:
                dm_dup = HangDienMay("PS5001", "Test", "Test", 1000, 12, 220, 100)
            except MaHangTrungLapException as e:
                print(f"⚠ Bắt được lỗi: {e}")
    
    except Exception as e:
        print(f"❌ Lỗi chung: {e}")