from random import randint

check = input("비밀번호를 입력하세요: ")

def lotto():
  a = randint(1, 45)
  b = randint(1, 45)
  c = randint(1, 45)
  d = randint(1, 45)
  e = randint(1, 45)
  f = randint(1, 45)
  list = [a, b, c, d, e, f]
  list.sort()
  return list

if check == "0104":
  number = lotto()
  print(number)
else:
  print("비밀번호 오류")
