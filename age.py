
drivihg = input('請問你開過車嗎？')
if drivihg != '有' and drivihg != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit # 終止程式運作

age = input('請問你的年齡？')
age = int(age)
if drivihg == '有':
    if age >= 18:
        print('你通過測驗了！')
    else:
        print('小朋友～未成年怎麼可以開車！')
elif drivihg == '沒有':
    if age >= 18:
        print('你可以考駕照囉！')
    else:
        print('等等～再過幾年就可以考駕照囉！')