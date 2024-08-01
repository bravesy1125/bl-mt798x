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
    except Exception as e:
        print(f'发生错误: {e}')


def copy_file_with_directory_creation(source_path, destination_path):
    try:
        # 检查源文件是否存在
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"源文件未找到: {source_path}")

        # 获取目标文件的目录
        dest_dir = os.path.dirname(destination_path)
        
        # 如果目标目录不存在，则创建它
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        # 复制文件
        shutil.copy(source_path, destination_path)

    except FileNotFoundError as fnf_error:
        print(f'错误: {fnf_error}')
    except PermissionError as perm_error:
        print(f'权限错误: {perm_error}')
    except Exception as e:
        print(f'发生未知错误: {e}')

create_directory('我们需要的C文件都在这里面')
shutil.copy("listofall.o.files", './我们需要的C文件都在这里面/')
with open("listofall.o.files") as file:
    for line in file:
        str_c_file = line[:-2]+ 'c'
        try:
            copy_file_with_directory_creation(str_c_file, './我们需要的C文件都在这里面/' + str_c_file)
        except Exception as e:
            print(e)
