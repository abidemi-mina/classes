# 1. Import the os module
# 2. Change the directory to the folder u want to work with
# 3. List the content of the directory
# 4. split the file name in two part to give you the name and extention
# 5. on the name break it further again into three parts number, course intro, course
# 6. Take out spaces on number, course intro, course
# 6. take out the hash using the python slice
# 7. padd the number to two digit using the zfill() method
# 8. rearrange the file name
# 9. Lastly rename it

import os

folder_path = os.chdir('C:/Users/Dell/Desktop/python2021/day5/python_files1')
list_files = os.listdir(folder_path)
for f in list_files:
    file_name, extention = os.path.splitext(f)
    course, course_title, number = file_name.split('-')
    f_course_title = course_title.strip()
    f_number = number.strip()[1:].zfill(2)
    new_file = f'{f_number}-{f_course_title}{extention}'
    os.rename(f, new_file)
    print(f'{f_number}-{f_course_title}{extention}')

name = 'Benedict'
# print(name[-1:-1])
# print(name[:3])
# print(name[1:])

# surname, firstname = 'Uwazie Benedict'.split()
# print(surname)
# print(firstname)
