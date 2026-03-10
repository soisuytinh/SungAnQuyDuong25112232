import math

radius = 5 
volume_of_shpere = (4/3) * math.pi * radius**3

price_of_a_book = 24.95
shipping_cost = 3
cost_after_discount = price_of_a_book * 0.6

import time

starting_time = 6 * 3600 + 52 * 60
first_phase = 1
first_phase_pace = 8 * 60 + 15 
second_phase = 3
second_phase_pace = 7 * 60 + 12 
last_phase = 1
last_phase_pace = 8 * 60 + 15 

print("Thể tích của quả cầu có bán kính", radius, "là:", f"{volume_of_shpere:.3f}")
print("Nhà sách thu về số tiền là: ", f"{cost_after_discount * 60 + shipping_cost + (59 * 0.75):.2f}", "đồng")
print("Thời gian hoàn thành cuộc chạy là: ", 
    f"{(starting_time + first_phase * first_phase_pace + second_phase * second_phase_pace + last_phase * last_phase_pace) // 3600} giờ "
    f"{(starting_time + first_phase * first_phase_pace + second_phase * second_phase_pace + last_phase * last_phase_pace) % 3600 // 60} phút "
    f"{(starting_time + first_phase * first_phase_pace + second_phase * second_phase_pace + last_phase * last_phase_pace) % 60} giây "
)