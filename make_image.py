from PIL import Image, ImageDraw, ImageFont
import os

# 保存用ディレクトリを作成
output_dir = "output_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 画像サイズを指定
image_size = (512, 100)

# フォントのサイズを指定
font_size = 60

# 画像を生成する関数
def generate_image(num):
    img = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(img)

    # フォントを選択し、サイズを指定
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)

    # テキストを描画する
    text = str(num)
    text_width, text_height = draw.textsize(text, font)
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    draw.text(position, text, (0, 0, 0), font)

    # 画像を保存
    img.save(os.path.join(output_dir, f"image_{num}.png"))

# 300枚の画像を生成
for i in range(300):
    generate_image(i)
