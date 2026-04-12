from abc import ABC, abstractmethod
import pickle
import os

class TuoiKhongHopLe(Exception):
    """Exception cho tuổi không hợp lệ (18-65)."""
    pass

class BacKhongHopLe(Exception):
    """Exception cho bậc công nhân không hợp lệ (1-10)."""
    pass

class CanBo(ABC):
    """Lớp trừu tượng — thông tin cơ bản của mọi cán bộ."""

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self._ho_ten    = ho_ten
        self.tuoi       = tuoi  # Dùng property setter để validate
        self._gioi_tinh = gioi_tinh
        self._dia_chi   = dia_chi

    @property
    def tuoi(self):
        """Getter tuổi."""
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        """Setter tuổi với validation (18-65)."""
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(f"Tuổi phải từ 18 đến 65, nhận được: {value}")
        self._tuoi = value

    @abstractmethod
    def mo_ta(self):
        """Mô tả cán bộ — lớp con bắt buộc phải override."""
        pass

    def hien_thi(self):
        """Hiển thị thông tin cán bộ."""
        print(f"  Họ tên    : {self._ho_ten}")
        print(f"  Tuổi      : {self._tuoi}")
        print(f"  Giới tính : {self._gioi_tinh}")
        print(f"  Địa chỉ   : {self._dia_chi}")
        print(f"  Mô tả     : {self.mo_ta()}")

    def __str__(self):
        return f"{self.mo_ta():<15s} | {self._ho_ten} ({self._tuoi})"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._ho_ten}', {self._tuoi}, '{self._gioi_tinh}', '{self._dia_chi}')"

    def __eq__(self, other):
        """So sánh theo tên + tuổi."""
        if isinstance(other, CanBo):
            return self._ho_ten == other._ho_ten and self._tuoi == other._tuoi
        return False

    def __lt__(self, other):
        """So sánh để sắp xếp theo tên (ABC)."""
        if isinstance(other, CanBo):
            return self._ho_ten < other._ho_ten
        return NotImplemented


class CongNhan(CanBo):
    """Công nhân — có thêm thuộc tính Bậc (1-10).

    Bậc quyết định trình độ tay nghề: bậc 1 là thấp nhất,
    bậc 10 là cao nhất. Ta validate giá trị khi khởi tạo.
    """

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac 

    @property
    def bac(self):
        """Getter bậc."""
        return self._bac

    @bac.setter
    def bac(self, value):
        """Setter bậc với validation (1-10)."""
        if not (1 <= value <= 10):
            raise BacKhongHopLe(f"Bậc phải từ 1 đến 10, nhận được: {value}")
        self._bac = value

    def mo_ta(self):
        """Override mo_ta() — đa hình."""
        return f"Công nhân (bậc {self._bac})"

    def hien_thi(self):
        print(f"── CÔNG NHÂN ──")
        super().hien_thi()
        print(f"  Bậc       : {self._bac}")


class KySu(CanBo):
    """Kỹ sư — có thêm thuộc tính Ngành đào tạo."""

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dt):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._nganh_dt = nganh_dt

    def mo_ta(self):
        """Override mo_ta() — đa hình."""
        return f"Kỹ sư ({self._nganh_dt})"

    def hien_thi(self):
        print(f"── KỸ SƯ ──")
        super().hien_thi()
        print(f"  Ngành ĐT  : {self._nganh_dt}")


class NhanVienSX(CanBo):
    """Nhân viên sản xuất — có thêm thuộc tính Công việc.

    Đặt tên NhanVienSX để tránh trùng với lớp NhanVien ở Bài 2.
    """

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._cong_viec = cong_viec

    def mo_ta(self):
        """Override mo_ta() — đa hình."""
        return f"Nhân viên ({self._cong_viec})"

    def hien_thi(self):
        print(f"── NHÂN VIÊN ──")
        super().hien_thi()
        print(f"  Công việc : {self._cong_viec}")

class QLCB:
    """Lớp quản lý cán bộ — cung cấp menu CRUD đơn giản.

    Chứa một list các đối tượng CanBo (hoặc lớp con).
    Nhờ đa hình, ta có thể gọi mo_ta() và hien_thi() trên bất kỳ
    phần tử nào mà không cần biết nó là CongNhan, KySu hay NhanVienSX.
    
    Hỗ trợ lưu/đọc danh sách từ file dùng pickle.
    """

    FILE_SAVE = "danh_sach_can_bo.pkl"

    def __init__(self):
        self.__ds_can_bo = []
        self.__load_file()

    def __load_file(self):
        """Tự động đọc dữ liệu từ file khi khởi tạo."""
        if os.path.exists(self.FILE_SAVE):
            try:
                with open(self.FILE_SAVE, 'rb') as f:
                    self.__ds_can_bo = pickle.load(f)
                print(f"✓ Đã tải {len(self.__ds_can_bo)} cán bộ từ file.")
            except Exception as e:
                print(f"⚠ Lỗi đọc file: {e}")
                self.__ds_can_bo = []

    def __save_file(self):
        """Lưu danh sách vào file dùng pickle và with statement."""
        try:
            with open(self.FILE_SAVE, 'wb') as f:
                pickle.dump(self.__ds_can_bo, f)
            print(f"✓ Đã lưu {len(self.__ds_can_bo)} cán bộ vào file.")
        except Exception as e:
            print(f"⚠ Lỗi lưu file: {e}")

    def them_moi(self):
        """Nhập thông tin và thêm cán bộ mới vào danh sách."""
        print("\n── THÊM CÁN BỘ MỚI ──")
        print("  1. Công nhân")
        print("  2. Kỹ sư")
        print("  3. Nhân viên")
        loai = input("  Chọn loại (1/2/3): ").strip()

        try:
            ho_ten    = input("  Họ tên    : ").strip()
            tuoi      = int(input("  Tuổi      : ").strip())
            gioi_tinh = input("  Giới tính : ").strip()
            dia_chi   = input("  Địa chỉ   : ").strip()

            if loai == "1":
                bac = int(input("  Bậc (1-10): ").strip())
                cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
            elif loai == "2":
                nganh = input("  Ngành ĐT  : ").strip()
                cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
            elif loai == "3":
                cv = input("  Công việc : ").strip()
                cb = NhanVienSX(ho_ten, tuoi, gioi_tinh, dia_chi, cv)
            else:
                print("  ⚠ Loại không hợp lệ!")
                return

            self.__ds_can_bo.append(cb)
            print(f"  ✓ Đã thêm: {cb}")
            self.__save_file()

        except TuoiKhongHopLe as e:
            print(f"  ⚠ Lỗi tuổi: {e}")
        except BacKhongHopLe as e:
            print(f"  ⚠ Lỗi bậc: {e}")
        except ValueError as e:
            print(f"  ⚠ Lỗi nhập liệu: {e}")

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

    def sap_xep_ds(self):
        """Sắp xếp danh sách theo tên (ABC) nhờ __lt__."""
        if not self.__ds_can_bo:
            print("\n  Danh sách trống!")
            return
        self.__ds_can_bo.sort()
        print(f"\n  ✓ Đã sắp xếp danh sách theo tên.")
        self.hien_thi_ds()
        self.__save_file()

    def so_sanh_cb(self):
        """Demo __eq__ — so sánh hai cán bộ theo tên + tuổi."""
        if len(self.__ds_can_bo) < 2:
            print("\n  Cần ít nhất 2 cán bộ để so sánh!")
            return
        
        print(f"\n  Hiện có {len(self.__ds_can_bo)} cán bộ:")
        for i, cb in enumerate(self.__ds_can_bo, 1):
            print(f"  {i}. {cb}")
        
        try:
            idx1 = int(input("  Nhập vị trí cán bộ 1: ").strip()) - 1
            idx2 = int(input("  Nhập vị trí cán bộ 2: ").strip()) - 1
            
            if 0 <= idx1 < len(self.__ds_can_bo) and 0 <= idx2 < len(self.__ds_can_bo):
                cb1 = self.__ds_can_bo[idx1]
                cb2 = self.__ds_can_bo[idx2]
                if cb1 == cb2:
                    print(f"  ✓ Hai cán bộ này BẰNG NHAU (cùng tên + tuổi).")
                else:
                    print(f"  Hai cán bộ này KHÔNG bằng nhau.")
            else:
                print("  ⚠ Vị trí không hợp lệ!")
        except ValueError:
            print("  ⚠ Vui lòng nhập số!")

    def chay(self):
        """Vòng lặp menu chính."""
        while True:
            print("\n╔══════════════════════════════╗")
            print("║   QUẢN LÝ CÁN BỘ           ║")
            print("╠══════════════════════════════╣")
            print("║  1. Thêm mới cán bộ         ║")
            print("║  2. Tìm kiếm theo tên       ║")
            print("║  3. Hiển thị danh sách       ║")
            print("║  4. Sắp xếp danh sách (ABC) ║")
            print("║  5. So sánh hai cán bộ       ║")
            print("║  6. Thoát                    ║")
            print("╚══════════════════════════════╝")

            chon = input("  Lựa chọn: ").strip()

            if   chon == "1": self.them_moi()
            elif chon == "2": self.tim_kiem()
            elif chon == "3": self.hien_thi_ds()
            elif chon == "4": self.sap_xep_ds()
            elif chon == "5": self.so_sanh_cb()
            elif chon == "6":
                print("  Tạm biệt! 👋")
                break
            else:
                print("  ⚠ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    ql = QLCB()
    ql.chay()