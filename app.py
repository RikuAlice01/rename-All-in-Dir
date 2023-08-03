import os
prefix_name = 'yamisung'
path = 'path'
files = os.listdir(path)
file_type = '.mp4'

for index, file in enumerate(files):
    file_path = path+file
    split_tup = os.path.splitext(file)
    ti_c = os.path.getctime(path+file)
    print(file,int(ti_c))
    if(split_tup[1]):
        file_type = split_tup[1]

    new_namefile = prefix_name+"-"+str(int(ti_c))

    if os.path.isfile(os.path.join(path, ''.join([str(new_namefile), file_type]))):
        j = 1
        while 1:
            if os.path.isfile(os.path.join(path, ''.join([str(new_namefile), '('+str(j)+')'+file_type]))):
                j = j + 1
                continue
            else:
                os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(new_namefile), '('+str(j)+')'+file_type])))
                break

    else:
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(new_namefile), file_type])))