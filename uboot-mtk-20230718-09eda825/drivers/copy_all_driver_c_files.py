import os
import shutil

result = os.system('rm listofall.o.files; find . -name "*.o" |grep -v "built-in.o" >> listofall.o.files')
# print(result)
result = os.system('rm -rf 我们需要的C文件都在这里面; mkdir 我们需要的C文件都在这里面')
# print(result)

def create_directory(directory_path):
    try:
        # 如果目录不存在，则创建它
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f'目录已创建: {directory_path}')
        else:
            print(f'目录已存在: {directory_path}')
    except Exception as e:
        print(f'发生错误: {e}')


create_directory('我们需要的C文件都在这里面')
shutil.copy("listofall.o.files", './我们需要的C文件都在这里面/')
with open("listofall.o.files") as file:
    for line in file:
        str_c_file = line[:-2]+ 'c'
        try:
            shutil.copy(str_c_file, './我们需要的C文件都在这里面/' + os.path.basename(str_c_file))
        except Exception as e:
            print(e)
