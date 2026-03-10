seconds = 42*60 + 42
km_to_miles = 10*1.61
distance = 10
time = seconds
average_pace = time / distance
speed = distance / (time / 3600)

print("Có", seconds, "giây")
print("Có", km_to_miles, "dặm trong 10 km")
print("Thời gian trung bình mỗi dặm:", average_pace, "giây")
print("Tốc độ trung bình:", f"{speed:.3f}", "dặm/giờ")
