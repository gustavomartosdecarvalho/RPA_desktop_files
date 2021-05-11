from datetime import datetime
import shutil
import glob
import os


class HandlingFilesService:
    # > Open a file in read-only mode and return the read content
    def read_file(self, file_dir):
        try:
            with open(file_dir, 'r') as op_file:
                result =  op_file.read()
                return result
        except Exception as e:
            print(" - Error to read the file {}: {}".format(file_dir, e))
            return False

    # > Open a file or create and write new content
    def write_file(self, file_dir, content):
        try:
            with open(file_dir, 'w') as op_file:
                result =  op_file.write(content)
                return True
        except Exception as e:
            print(" - Error to write the file {}: {}".format(file_dir, e))
            return False

    # > Open a file and append the new content in the end
    def append_to_file(self, file_dir, content):
        try:
            with open(file_dir, 'a') as op_file:
                result =  op_file.write(content)
                return True
        except Exception as e:
            print(" - Error to append the file {}: {}".format(file_dir, e))
            return False

    # > In this method to copy a file the original must match the specification
    def copy_file(self, origin, destination):
        try:
            shutil.copy(origin, destination)
            return True
        except Exception as e:
            print(" - Error to copy file {}: {}".format(origin, e))
            return False
    
    # > Remove a specific file
    def remove_file(self, origin):
        try:
            os.remove(origin)
            return True
        except Exception as e:
            print(" - Error to remove file {}: {}".format(origin, e))
            return False
    
    # > This method remove a folder
    def remove_dir(self, dir_path):
        try:
            os.rmdir(dir_path)
            return True
        except Exception as e:
            print(" - Error to remove dir {}: {}".format(dir_path, e))
            return False

    # > This method search for a latest version
    def find_latest_version_in_folder(self, name, extension, origin):
        try:
            file_base = os.path.join(origin, '*.' + extension)
            files_search = sorted(glob.iglob(file_base), key=os.path.getctime, reverse=True)
            for file_s in files_search:
                if file_s.__contains__(name):
                    return file_s
            return False
        except Exception as e:
            print(" - Error to inspect file {}: {}".format(name, e))
            return False

    # > This method return a string with atual datetime to complement the name file
    def complement_datetime_name_yyyymmdd_hhmm(self):
        date_today = datetime.now()
        return '_' + date_today.strftime('%Y%m%d_%H%M')

