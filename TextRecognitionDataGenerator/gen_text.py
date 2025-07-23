import os
from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont
import random

from trdg.generators.from_strings import GeneratorFromStrings
from trdg.data_generator import FakeTextDataGenerator
from trdg.string_generator import create_strings_from_wikipedia
from trdg.utils import load_dict, load_fonts
from trdg.generators import GeneratorFromDict

#Từ điển
dict_path = r"D:\text_generation\dict\Viet39K_normal.txt"
dict_path_upper=r"D:\text_generation\dict\Viet39K_uppercase.txt"
dict_path_upper1=r"D:\text_generation\dict\Viet39K_original_upper1.txt"
dict_path_gachchan=r"D:\text_generation\dict\Viet39K______.docx"
dict_path_mix=r"D:\text_generation\dict\Viet39K_mix.txt"
dict_path_test=r"D:\text_generation\dict\vn_dictionary.txt"
dict_path_boxung=r"D:\text_generation\dict\data_boxung"
dict_path_2st=r"D:\text_generation\dict\viet39k_2word_sentences (2).txt"
#font chữ
font_arial = r"D:\text_generation\fonts\ARIAL.TTF"
font_bold_path = r"D:\text_generation\fonts\ARIALBD.TTF"  
font_italic_path = r"D:\text_generation\fonts\ARIALI.TTF" 
font_bold_path_2= r"D:\text_generation\fonts\ARIALBD.TTF"
font_time=r"D:\text_generation\fonts\times.ttf"
font_bold_time_path=r"D:\text_generation\fonts\SVN-Times New Roman Bold.ttf"

#output_dir = r"D:\text_generation\train_2"
output_dir = r"D:\text_generation\data\aug_images"
background_dir=r"D:\text_generation\trdg\backgrounds"


#os.makedirs("output_test", exist_ok=True)

# Khởi tạo generator
generator = GeneratorFromDict(
    fonts=[font_bold_path,font_bold_path_2,font_bold_time_path],     # Danh sách font
    count=9000,              # Số lượng hình ảnh cần tạo
    path=dict_path_2st,       # Sử dụng tệp từ điển tùy chỉnh thay vì language
    length=1,            # Độ dài tối đa của mỗi chuỗi văn bản (số từ)
    allow_variable=True,  # Cho phép độ dài biến đổi
    size=64,              # Kích thước chữ
    skewing_angle=2,      # Góc nghiêng của văn bản
    random_skew=True,     # Ngẫu nhiên hóa góc nghiêng
    blur=2,               # Độ mờ
    random_blur=True,     # Ngẫu nhiên hóa độ mờ
    background_type=1,    # Loại nền: nhiễu Gaussian
    text_color="#282828", # Màu văn bản
    stroke_width=0,       # Độ dày viền chữ
    stroke_fill="#282828",# Màu viền chữ
    image_dir=background_dir,  # Thư mục chứa hình ảnh nền
    fit=True,             # Cắt sát văn bản
    output_mask=False,    # Không xuất mask
    word_split=True,      # Tách theo từ
    #distorsion_type=2,
    #distorsion_orientation=3,
    

)
# Mở tệp để append nhãn
label_file = open(r"D:\text_generation\train_full.txt", "a", encoding="utf-8")

counter = 1
existing_files = [f for f in os.listdir(output_dir) if f.startswith("img") and f.endswith(".jpg")]
if existing_files:
    try:
        # Trích xuất số 8 chữ số từ tên file (từ vị trí 3 đến 11)
        max_num = max(int(f[3:11]) for f in existing_files if len(f[3:11]) == 8 and f[3:11].isdigit())
        counter = max_num + 1
    except ValueError:
        print("No valid 8-digit number found in existing files, starting from 1.")
else:
    print("No existing files found, starting from 1.")
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