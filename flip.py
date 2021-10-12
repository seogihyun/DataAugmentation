img_path_dir = "your image path"
file_list = os.listdir(img_path_dir)

# 파일명 
for file in files:  
   image = cv2.imread(file, cv2.IMREAD_UNCHANGED)
   for i in angle:
     filped = cv2.flip(image, 1)
     head_tail = os.path.split(file) 
     img_name = head_tail[1]
     print(img_name)
     print(i)
     cv2.imwrite("저장할 파일 경로"+ "filp_" + str(i)+_img_name)