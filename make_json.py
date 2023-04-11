import json
import os

# 画像の数
num_images = 300

# JSONに含まれるデータのリストを作成
data = []
for i in range(num_images):
    image_id = i + 1
    image_url = f"https://raw.githubusercontent.com/nk27/listview_images/main/output_images/image_{i}.png"
    image_data = {
        "id": image_id,
        "url": image_url
    }
    data.append(image_data)

# JSONを作成
json_data = json.dumps(data)

# JSONをファイルに書き込む
os.makedirs("json", exist_ok=True)
with open("json/data.json", "w") as file:
    file.write(json_data)

# 結果を表示
print("JSONデータをjsonフォルダ内に保存しました。")
