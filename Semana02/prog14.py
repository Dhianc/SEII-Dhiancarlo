#import os

#os.chdir('caminho/para/o/diretorio')
#print(os.getcwd())

#for f in os.listdir():
#    f_name, f_ext = os.path.splittext(f)
#    f_title, f_course, f_num = file_name.split('-')
#    print(f_title) //or f_course or f_num
#    f_title = f_title.strip()
#    f_course = f_course.strip()
#    f_num = f_num.strip()[1:].zfill(2) //zfill(2) transforma os digitos para 2 casas
#    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
#    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
#    os.rename(f, new_name)