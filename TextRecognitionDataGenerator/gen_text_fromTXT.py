import os
import random
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from trdg.generators import GeneratorFromStrings

# Đường dẫn đến font chữ, từ điển, và thư mục hình nền
#Từ điển
dict_path = r"D:\text_generation\dict\Viet39K_normal.txt"
dict_path_upper=r"D:\text_generation\dict\Viet39K_uppercase.txt"
dict_path_upper1=r"D:\text_generation\dict\Viet39K_original_upper1.txt"
dict_path_gachchan=r"D:\text_generation\dict\Viet39K______.docx"
dict_path_mix=r"D:\text_generation\dict\Viet39K_mix.txt"
dict_path_test=r"D:\text_generation\dict\vn_dictionary.txt"
dict_39K_test=r"D:\text_generation\dict\Viet39K_test.txt"
dict_boxung=r"D:\text_generation\dict\data_boxung"
#font chữ
font_arial = r"D:\text_generation\fonts\ARIAL.TTF"
font_bold_path = r"D:\text_generation\fonts\ARIALBD.TTF"  
font_italic_path = r"D:\text_generation\fonts\ARIALI.TTF" 
font_bold_path_2= r"D:\text_generation\fonts\ARIALBD.TTF"
font_time=r"D:\text_generation\fonts\times.ttf"
font_bold_time_path=r"D:\text_generation\fonts\SVN-Times New Roman Bold.ttf"
#output_dir = r"D:\text_generation\train_2"
background_dir=r"D:\text_generation\trdg\backgrounds"


output_dir = r"D:\text_generation\data\aug_images"

data_in_used=r"D:\text_generation\dict\viet39k_5word_sentences_last.txt"

# Đọc toàn bộ dòng từ tệp Viet39K.txt
with open(data_in_used, "r", encoding="utf-8") as f:
    strings = [line.strip() for line in f if line.strip()]  # Loại bỏ dòng trống và khoảng trắng thừa
# Khởi tạo generator với toàn bộ dòng từ tệp
generator = GeneratorFromStrings(
    strings=strings,  
    count=len(strings),  
    fonts=[font_arial,font_time],
    size=64,
    skewing_angle=2,
    random_skew=True,
    blur=2,
    random_blur=True,
    background_type=1,
    text_color="#282828", # Màu văn bản
    stroke_width=0,
    stroke_fill="#282828",# Màu viền chữ
    image_dir=background_dir,
    fit=True,
    output_mask=False,
    distorsion_type=1,
    distorsion_orientation=1
)
# Mở tệp để append nhãn
label_file = open(r"D:\text_generation\train_full.txt", "a", encoding="utf-8")

# Khởi tạo bộ đếm
counter = 19625
#existing_files = [f for f in os.listdir(output_dir) if f.startswith("img") and f.endswith(".jpg")]
#if existing_files:
#    try:
#        # Trích xuất số 8 chữ số từ tên file (từ vị trí 3 đến 11)
#        max_num = max(int(f[3:11]) for f in existing_files if len(f[3:11]) == 8 and f[3:11].isdigit())
#        counter = max_num + 1
#    except ValueError:
#        print("No valid 8-digit number found in existing files, starting from 1.")
#else:
#    print("No existing files found, starting from 1.")
# Lặp qua generator để lấy hình ảnh và nhãn
for img, lbl in generator:
    img_name = f"img{counter:08d}.jpg"
    img_path = os.path.join(r"data/aug_images", img_name).replace("\\", "/")  # Thay \ bằng /
    
    # Lưu ảnh
    img.save(img_path)
    
    # Ghi nhãn, thêm debug
    label_file.write(f"{img_path}\t{lbl}\n")
    label_file.flush()  
    
    counter += 1  # Tăng bộ đếm

# Đóng tệp nhãn
label_file.close()