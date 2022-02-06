data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # 每1000筆
            print(len(data)) # 觀察讀取進度   
print(f"檔案讀取完畢，總共有{len(data)}筆資料")

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

# 清單快寫法
good1 = [d for d in data if 'good' in d]
print(f"留言內容裡出現'good'的有{len(good1)}則")

bad = ['bad' in d for d in data]
bad1 = sum('bad' in d for d in data)
print(f"留言內容裡出現'bad'的有{len(bad1)}則")