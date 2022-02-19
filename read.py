data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        #if count % 1000 == 0: # 每1000筆
            #print(len(data)) # 觀察讀取進度   
#print(f"檔案讀取完畢，總共有{len(data)}筆資料")

word_count = {}
for d in data: # d = 每筆留言
    words = d.split() # 過濾空白鍵
    for word in words: # words = 每個單字
        if word in word_count:
            word_count[word] += 1 # 改變 key 的 value
        else:
            word_count[word] = 1 # 新增新的key進word_count字典中

# 查找出現次數超過100的單字有哪些
for word in word_count:
    if word_count[word] > 1000000:
        print(word, word_count[word])

print(len(word_count)) # 查共有幾種單字
print(word_count["Allen"]) # "Allen"出現過幾次

total = 0
for d in data:
    total += len(d)
arg = total / len(data)
print("留言平均長度為", arg)

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print(f"留言長度低於100的有{len(new)}則")

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print(f"留言內容裡出現'good'的有{len(good)}則")

# 查詢單字出現次數的功能
while True:
    word = input("請問你想查什麼字：")
    if word == "q":
        break
    if word in word_count:
        print(f"{word}出現過的次數為{word_count[word]}")
    else:
        print(f"{word}出現過的次數為0")
print("感謝使用本查詢功能")
