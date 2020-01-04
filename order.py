asd = "맘스터치에서 싸이버거 한개 감자튀김 두개 콜라 세개 주문해줘"
asd = asd.replace(" ", "")

words = asd.split("에서")

store = words[0]
menus = words[1].split("주문해줘")[0]

orders = menus.split("개")

while '' in orders:
    orders.remove('')

li = []
for i in orders:
  li.append({ i[:len(i)-1]: i[len(i)-1] })

print(store, li)