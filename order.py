def order_data(string):
    store = None

    # string = "맘스터치에서 싸이버거 한개 감자튀김 두개 콜라 세개 주문해줘"
    string = string.replace(" ", "")

    words = string.split("에서")

    if "에서" in string:
        store = words[0]
        menus = words[1].split("주문해줘")[0]
    else:
        menus = words[0].split("주문해줘")[0]

    orders = menus.split("개")
    while '' in orders:
        orders.remove('')

    menu_list = []
    number_list = []

    for i in orders:
        value = i[len(i)-1]

        def text_to_num(value):
            return {
                "한": 1,
                "두": 2,
                "세": 3,
                "네": 4,
            }[value]

        menu_list.append(i[:len(i)-1])
        number_list.append(text_to_num(value))

    # print(list(li[0])[0])

    data = {
        "store": store,
        "menus": menu_list,
        "num": number_list
    }

    return store, menu_list, number_list
