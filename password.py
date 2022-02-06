password = 'a123456'
num = 3 # 最多輸入次數
while num > 0:
    num -= 1
    input_password = input('請輸入密碼：')
    if input_password == password:
        print('登入成功')
        break
    else:
        if num > 0:
            print(f"密碼錯誤，還有{num}次機會")
        else:
            print('輸入次數已超過')
