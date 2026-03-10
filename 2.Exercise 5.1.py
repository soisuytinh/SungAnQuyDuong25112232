import time
current_time = time.time()
days = int(current_time//86400)
seconds_today = int(current_time%86400)
hours = int(seconds_today//3600)
minutes = int((seconds_today%3600)//60)
seconds = int(seconds_today%60)

print("Số ngày kể từ epoch:", days)
print(f"Thời gian hiện tại là: {hours} giờ {minutes} phút {seconds} giây")
