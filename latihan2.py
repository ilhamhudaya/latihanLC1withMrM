# from Latihan import kalori_terbakar

# #looping
# def jumlah_Kalori_Terbakar(*latihan, durasi);
#     for i in latihan:
#         kalori_terbakar(durasi, i)
#     return durasi


# def main():
#     result = jumlah_Kalori_Terbakar('berlari', 'berenang', 'bersepeda', durasi=100)
#     print(result)

# if __name__=="__main__":
# main()
    
from Latihan import calories_burned

def total_session_burned_cal(*exercises, each_session_duration):
  total = 0
  for i in exercises:
    total = total + calories_burned(each_session_duration, i)
  return total

def main ():
  result = total_session_burned_cal('berenang', 'bersepeda', each_session_duration=10)
  print(result)

if __name__ == "__main__":
    main()
