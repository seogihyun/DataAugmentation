path = 'your image path'
file_list = os.listdir(path)
img_list = []
for file in file_list:
    if file[-1] == 'g':
        img_list.append(file)

for i in img_list:
    img = cv2.imread(i, cv2.IMREAD_GRAYSCALE) # 흑백 이미지로 로드
    cv2.imwrite('./to_gray/'+ i, img) # 이미지 저장