# This won't work on your code.
# You need to get your own token and then
# do TOKEN = 'xxxxxxxxxxxxxxxxxx'
from myToken import TOKEN

# importing necessary libraries
import dropbox
import io

# Establish connection
def connect_to_dropbox():
    try:
        dbx = dropbox.Dropbox(TOKEN)
        print('Connected to Dropbox successfully\n')

    except Exception as e:
        print(str(e))

    return dbx


# explicit function to list files
# conn - the dropbox connection object.
# path - the path to the folder.
def list_files_in_folder(conn, path):
    try:
        # files_list_folder() is a built-in function of dropbox
        files = conn.files_list_folder(path).entries

        # print(type(files))  ->  <class 'list'>
        # print(type(files[0])) -> <class 'dropbox.files.FolderMetadata'>

        print("--- Listing Files in Folder {} --- ".format(path))

        for file in files:
            # listing
            print(file.name)
        print('\n')

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    # create an object which holds the connection
    dbx = connect_to_dropbox()

    #list_files_in_folder(dbx, '/')
    list_files_in_folder(dbx, '')

    dir_path = "/ex1"
    # list the files in the folders
    list_files_in_folder(dbx, dir_path)
    list_files_in_folder(dbx, dir_path + '/source')
    list_files_in_folder(dbx, dir_path + '/dest')

    src = dir_path + '/source'
    f_src = src + '/hello.txt'
    # No need to understand the method written below
    metadata, response = dbx.files_download(f_src)
    for data in response.iter_lines():
        print(type(data))
        print(data)

    dest = dir_path + '/dest'
    f_dest = dest + '/hello.txt'
    # # # built-in API copy function
    dbx.files_copy_v2(f_src, f_dest)
    print('\n###Post copy function###\n')
    list_files_in_folder(dbx, src)
    #
    # what happens if we try to copy again?
    # dbx.files_copy_v2(f_src, f_dest)
    #
    dbx.files_delete_v2(f_dest)
    print('\n###Post delete function###\n')
    list_files_in_folder(dbx, dest)

    # dbx.files_move_v2(src, dest)

    #src = '/ArielMedicalCenter/'

    #patients = dbx.files_download(src + 'patients.csv')
    #doctors = dbx.files_download(src + 'doctors.csv')
    #appointments = dbx.files_download(src + 'appointments.csv')

    # from main import read_data
    # print(read_data(patients))

    # dropbox_path = r"/Apps/cloud-with-python/ex1/source"
    # computer_path = r"C:/Users/amit/Downloads/hello.txt"
    # dbx.files_upload(open(computer_path, "rb").read(), dropbox_path)
    dbx.files_create_folder_v2(dir_path +'/test')