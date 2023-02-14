import glob
import os

IMG_FORMAT="png"

def get_tar_list(tar_source):
    img_list=[]
    txt_list=[]

    for file_path in glob.glob(tar_source + "/*."+IMG_FORMAT,recursive=True):
        # 獲得不帶附檔名的檔名
        file_name = os.path.splitext(file_path)[0]  # remove ".txt"
        img_list.append(file_name)

    for file_path in glob.glob(tar_source + "/*.txt",recursive=True):
        file_name = os.path.splitext(file_path)[0]  # remove ".txt"
        txt_list.append(file_name)

    return img_list,txt_list

def com_lost_txt(img_list,txt_list):
    for x in img_list:
        if (x in txt_list) == False:
            os.remove(x + "." + IMG_FORMAT)
            print("remove:",x + "." + IMG_FORMAT)

def main():
    file_source ="test_file"
    img_list,txt_list = get_tar_list(file_source)
    com_lost_txt(img_list,txt_list)

if __name__ == "__main__":
    main()