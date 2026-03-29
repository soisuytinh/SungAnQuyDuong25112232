# ══════════════════════════════════════════════════════════════
#  Bài 3: Quản lý cán bộ đơn vị sản xuất — Menu tương tác
# ══════════════════════════════════════════════════════════════


class CanBo:
    """Lớp cha — thông tin cơ bản của mọi cán bộ."""

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self._ho_ten    = ho_ten
        self._tuoi      = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi   = dia_chi

    def loai_cb(self):
        """Trả về tên loại cán bộ — lớp con sẽ override."""
        return "Cán bộ"

    def hien_thi(self):
        print(f"  Họ tên    : {self._ho_ten}")
        print(f"  Tuổi      : {self._tuoi}")
        print(f"  Giới tính : {self._gioi_tinh}")
        print(f"  Địa chỉ   : {self._dia_chi}")

    def __str__(self):
        return f"{self.loai_cb():<10s} | {self._ho_ten}"


# ─────────────────────────────────────────────────────────────
class CongNhan(CanBo):
    """Công nhân — có thêm thuộc tính Bậc (1-10).

    Bậc quyết định trình độ tay nghề: bậc 1 là thấp nhất,
    bậc 10 là cao nhất. Ta validate giá trị khi khởi tạo.
    """

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise ValueError("Bậc phải từ 1 đến 10!")
        self.__bac = bac

    def loai_cb(self):
        return "Công nhân"

    def hien_thi(self):
        print(f"── CÔNG NHÂN ──")
        super().hien_thi()
        print(f"  Bậc       : {self.__bac}")


# ─────────────────────────────────────────────────────────────
class KySu(CanBo):
    """Kỹ sư — có thêm thuộc tính Ngành đào tạo."""

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dt):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh_dt = nganh_dt

    def loai_cb(self):
        return "Kỹ sư"

    def hien_thi(self):
        print(f"── KỸ SƯ ──")
        super().hien_thi()
        print(f"  Ngành ĐT  : {self.__nganh_dt}")


# ─────────────────────────────────────────────────────────────
class NhanVienSX(CanBo):
    """Nhân viên sản xuất — có thêm thuộc tính Công việc.

    Đặt tên NhanVienSX để tránh trùng với lớp NhanVien ở Bài 2.
    """

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec

    def loai_cb(self):
        return "Nhân viên"

    def hien_thi(self):
        print(f"── NHÂN VIÊN ──")
        super().hien_thi()
        print(f"  Công việc : {self.__cong_viec}")


# ═════════════════════════════════════════════════════════════
#  Lớp QLCB — Quản lý danh sách cán bộ với menu tương tác
# ═════════════════════════════════════════════════════════════
class QLCB:
    """Lớp quản lý cán bộ — cung cấp menu CRUD đơn giản.

    Chứa một list các đối tượng CanBo (hoặc lớp con).
    Nhờ đa hình, ta có thể gọi hien_thi() trên bất kỳ
    phần tử nào mà không cần biết nó là CongNhan, KySu
    hay NhanVienSX.
    """

    def __init__(self):
        self.__ds_can_bo = []

    def them_moi(self):
        """Nhập thông tin và thêm cán bộ mới vào danh sách."""
        print("\n── THÊM CÁN BỘ MỚI ──")
        print("  1. Công nhân")
        print("  2. Kỹ sư")
        print("  3. Nhân viên")
        loai = input("  Chọn loại (1/2/3): ").strip()

        # Nhập thông tin chung
        ho_ten    = input("  Họ tên    : ")
        tuoi      = int(input("  Tuổi      : "))
        gioi_tinh = input("  Giới tính : ")
        dia_chi   = input("  Địa chỉ   : ")

        if loai == "1":
            bac = int(input("  Bậc (1-10): "))
            cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
        elif loai == "2":
            nganh = input("  Ngành ĐT  : ")
            cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
        elif loai == "3":
            cv = input("  Công việc : ")
            cb = NhanVienSX(ho_ten, tuoi, gioi_tinh, dia_chi, cv)
        else:
            print("  ⚠ Loại không hợp lệ!")
            return

        self.__ds_can_bo.append(cb)
        print(f"  ✓ Đã thêm: {cb}")

    def tim_kiem(self):
        """Tìm cán bộ theo họ tên (tìm kiếm không phân biệt hoa/thường)."""
        tu_khoa = input("\n  Nhập họ tên cần tìm: ").strip().lower()
        ket_qua = [cb for cb in self.__ds_can_bo
                   if tu_khoa in cb._ho_ten.lower()]
        if not ket_qua:
            print("  Không tìm thấy!")
        else:
            print(f"  Tìm thấy {len(ket_qua)} kết quả:")
            for cb in ket_qua:
                print()
                cb.hien_thi()

    def hien_thi_ds(self):
        """Hiển thị toàn bộ danh sách cán bộ."""
        if not self.__ds_can_bo:
            print("\n  Danh sách trống!")
            return
        print(f"\n══ DANH SÁCH CÁN BỘ ({len(self.__ds_can_bo)} người) ══")
        for i, cb in enumerate(self.__ds_can_bo, 1):
            print(f"\n--- #{i} ---")
            cb.hien_thi()

    def chay(self):
        """Vòng lặp menu chính."""
        while True:
            print("\n╔══════════════════════════╗")
            print("║   QUẢN LÝ CÁN BỘ       ║")
            print("╠══════════════════════════╣")
            print("║  1. Thêm mới cán bộ     ║")
            print("║  2. Tìm kiếm theo tên   ║")
            print("║  3. Hiển thị danh sách   ║")
            print("║  4. Thoát                ║")
            print("╚══════════════════════════╝")

            chon = input("  Lựa chọn: ").strip()

            if   chon == "1": self.them_moi()
            elif chon == "2": self.tim_kiem()
            elif chon == "3": self.hien_thi_ds()
            elif chon == "4":
                print("  Tạm biệt! 👋")
                break
            else:
                print("  ⚠ Lựa chọn không hợp lệ!")


# ──── Chạy chương trình ────────────────────────────────────────
if __name__ == "__main__":
    ql = QLCB()
    ql.chay()