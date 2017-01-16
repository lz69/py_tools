base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

print("输入透明度，如:80")

t = input()

i = 255 * int(t) / 100

print(int(round(i)))

def dec2hex(string_num): 
  num = int(string_num) 
  mid = [] 
  while True: 
    if num == 0: break
    num,rem = divmod(num, 16) 
    mid.append(base[rem]) 
  
  return ''.join([str(x) for x in mid[::-1]])

print(dec2hex(int(round(i))))
