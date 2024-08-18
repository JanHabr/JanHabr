class File:
  import logging
  from shutil import Error
  from sre_constants import CATEGORY_LOC_WORD
  
  logger = logging.getLogger("File_processor")
  file_handler = logging.FileHandler("file_processor.log")
  logger.addHandler(file_handler)
  logger.setLevel(logging.DEBUG)
  
  
  class FileTools:
    """This class is used for basic file operations - good documentation on every func."""
  
    def __init__(self, raise_errors):
      self.raise_errors = raise_errors
      if isinstance(self.raise_errors, bool):
        if self.raise_errors == True:
          logger.debug("FileTools: raise_errors is True")
        else:
          logger.debug("FileTools: raise_errors is False")
        print("FileTools is available")
      else:
  
        logger.error(
            "raise_errors (atribute of the FileTools class) is a boolean")
        raise Exception(
            "FileTools is not available due to Type error. Please take a look at the error log."
        )
  
    def delete_file(self, file_path):
      """Deletes the inputted file of any type. Returns True if completed or False if a problem was found.
      An error could be raisen appending on the atribute given to FileTools class.\n
         Inputs:
         -- file: string: The file you want to delete. Example: 'my_file.png' \n"""
  
      import os
      try:
        if os.path.exists(f"{file_path}"):
          os.remove(f"{file_path}")
          return True
        else:
          logger.warning("The file does not exist.")
          if self.raise_errors == True:
            raise FileNotFoundError(f"The file {file_path} does not exist")
  
          else:
            print("The file does not exist.")
            return False
  
      except PermissionError:
        logger.warning("You do not have permission to delete this file.")
        if self.raise_errors == True:
          raise PermissionError(
              "You do not have permission to delete this file. Please try again."
          )
        else:
          print(
              "You do not have permission to delete this file. Please try again."
          )
          return False
    def file_exists(self, file_path):
      """Checks if the file exists. Returns True if it exists or False if not. \n
      Input:
      -- file_path: string: The file you want to check. Example: 'my_file.png' \n"""
      import os
      try:
        if os.path.exists(file_path):
          return True
        else:
          return False
      except PermissionError:
        logger.warning("You do not permission to acces that file.")
        if self.raise_errors:
          raise PermissionError("You do not permission to acces that file.")
        else:
          print("You do not have permission to acces that file.")
    def move_file(self, file_path, new_file_path):
      """Renames the inputted file of any type. Returns True if completed or False if a problem was found.
      An error could be raisen appending on the atribute given to FileTools class.\n
        Inputs:
        -- file_path: string: The path of the file you want to rename. Example: 'examples/my_file.png Warning no dots or file types! \n
        -- new_file: string: The new name of the file. Example: 'examples/my_new_file.png' Warning no dots or file types! \n"""
      import os
      try:
        if os.path.exists(f"{file_path}"):
          os.rename(f"{file_path}", f"{new_file_path}")
          return True
        else:
          logger.warning("The file does not exist.")
          if self.raise_errors == True:
            raise FileNotFoundError(f"The file {file_path} does not exist")
          else:
            print(f"The file {file_path} does not exist")
            return False
      except PermissionError:
        logger.warning("You do not have permission to rename this file.")
        if self.raise_errors == True:
          raise PermissionError(
              "You do not have permission to rename this file. Please try again."
          )
        else:
          print(
              "You do not have permission to rename this file. Please try again."
          )
          return False
    def create_folder(self, folder_path):
      """Creates a folder with the inputted name. Returns True if completed or False if not. \n
        Inputs:
        -- folder_path: string: The path of the folder you want to create. Example: examples/my_folder """
      try:
        import os
        if os.path.exists(f"{folder_path}"):
          logger.warning("The folder already exists.")
          if self.raise_errors == True:
            raise FileExistsError(f"The folder {folder_path} already exists")
          else:
            print(f"The folder {folder_path} already exists")
            return False
        else:
          os.mkdir(f"{folder_path}")
          print(f"Folder at {folder_path}")
          return True
      except PermissionError:
        logger.warning("You do not have permission to create this folder.")
        if self.raise_errors:
          raise PermissionError("You do not have permission to create this folder.")
        else:
          print("You do not have permission to create this folder.")
    def delete_folder(self, folder_name):
      """Deletes the inputted folder. Warning: The folder you want to delete must be empty! Returns True if completed or False if a problem was found.
      An error could be raisen appending on the atribute given to FileTools class.\n
      Inputs:
      -- folder_name: string: The name of the folder you want to delete. Example: 'my_folder'"""
      import os
      try:
        if os.path.exists(folder_name):
          with os.scandir(folder_name) as it:
            if any(it):
              if self.raise_errors == True:
                logger.warning(f"The folder {folder_name} is not empty.")
                raise OSError(
                    "The folder is not empty. Please delete the files in the folder first."
                )
              else:
                logger.warning(f"The folder {folder_name} is not empty.")
                print(
                    "The folder is not empty. Please delete the files in the folder first."
                )
                return False
            else:
              os.rmdir(folder_name)
              print("Succes")
              return True
  
        else:
          logger.warning(f"The folder {folder_name} does not exist.")
          if self.raise_errors:
            raise FileNotFoundError(f"The folder {folder_name} does not exist")
          else:
            print(f"The folder {folder_name} does not exist")
            return False
      except PermissionError:
        logger.warning("You do not have permission to delete this folder.")
        if self.raise_errors:
          raise PermissionError(
              "You do not have permission to delete this folder. Please try again."
          )
        else:
          print(
              "You do not have permission to delete this folder. Please try again."
          )
          return False
  
    def rename_folder(self, folder_name, new_folder_name):
      """Renames the inputted folder. Returns True if completed or False if a problem was found.
      An error could be raisen appending on the atribute given to FileTools class.\n
      Inputs:
      -- folder_name: string: The name of the folder you want to rename. Example: 'my_folder' \n"""
      import os
      try:
        if os.path.exists(folder_name):
          os.renames(folder_name, new_folder_name)
          return True
        else:
          logger.warning(f"The folder {folder_name} does not exist.")
          if self.raise_errors == True:
            raise FileNotFoundError(f"The folder {folder_name} does not exist")
          else:
            print(f"The folder {folder_name} does not exist")
            return False
      except PermissionError:
        logger.warning("You do not have permission to rename this folder.")
        if self.raise_errors == True:
          raise PermissionError(
              "You do not have permission to rename this folder. Please try again."
          )
        else:
          print(
              "You do not have permission to rename this folder. Please try again."
          )
          return False
  
    def read(self, file_path_):
      """Reads the inputted text file. Returns True if completed or False if a problem was found.
      An error could be raisen appending on the atribute given to FileTools class.\n
      Inputs: 
      -- file_path: string: The name of the file you want to read. Example: 'examples/my_file.txt"""
      import os
      try:
        if os.path.exists(f"{file_path_}"):
          file__ = file_path_
          text_ = open(file__).read()
          print(text_)
          return True
        else:
          logger.warning(f"The file {file_path_} does not exist.")
          if self.raise_errors == True:
            raise FileNotFoundError(f"The file {file_path_} does not exist")
          else:
            print(f"The file {file_path_} does not exist")
            return False
  
      except PermissionError:
        logger.warning("You do not have permission to read this text file.")
        if self.raise_errors == True:
          raise PermissionError(
              "You do not have permission to read this text file. Please try again."
          )
        else:
          print(
              "You do not have permission to read this text file. Please try again."
          )
          return False
  
    def read_split(self, file_path):
      """Reads the inputted text file and splits it into a list. Returns True if completed or False if a problem was found.
      An error could be raisen appending on the atribute given to FileTools class.\n
      Inputs:
      -- file_path: string: The path to the file you want to read. Example: 'examples/my_file.txt"""
      import os
      try:
        if os.path.exists(f"{file_path}"):
          list_ = open(f"{file_path}").read().split()
          print(list_)
          return True
        else:
          logger.warning(f"The file {file_path} does not exist.")
          if self.raise_errors == True:
            raise FileNotFoundError(f"The file {file_path} does not exist")
          else:
            print(f"The file {file_path} does not exist")
            return False
      except PermissionError:
        logger.warning("You do not have permission to read this text file.")
        if self.raise_errors == True:
          raise PermissionError(
              "You do not have permission to read this text file. Please try again."
          )
        else:
          print(
              "You do not have permission to read this text file. Please try again."
          )
          return False
  
    def assing_file_data(self, file_path):
      """Returns the files data. Returns file data if completed or False if a problem was found.
      An error could be raisen appending on the atribute given to FileTools class.\n
          Inputs:
          -- file_path: string: The path to the file you want to assign. Example: examples/my_file.png"""
      import os
      try:
        if os.path.exists(file_path):
          file_ = open(file_path)
          return file_
        else:
          logger.warning(f"The file {file_path} does not exist.")
          if self.raise_errors == True:
            raise FileNotFoundError(f"The file {file_path} does not exist")
          else:
            print(f"The file {file_path} does not exist.")
          return None
      except PermissionError:
        logger.warning("You do not have permission assign this file.")
        if self.raise_errors == True:
          raise PermissionError(
              "You do not have permission assign this file. Please try again.")
        else:
          print("You do not have permission assign this file. Please try again.")
        return None
  
    def close(self, file_path):
      """Closes the inputted file. Returns True if completed or False if a problem was found.
      An error could be raisen appending on the atribute given to FileTools class.\n
      Inputs:
      -- file_path: string: The path to the file you want to close. Example: examples/my_file.png"""
      import os
      try:
        if os.path.exists(file_path):
          file_ = open(file_path)
          file_.close()
          return True
        else:
          logger.warning(f"The file {file_path} does not exist.")
          if self.raise_errors == True:
            raise FileNotFoundError(f"The file {file_path} does not exist")
          else:
            print(f"The file {file_path} does not exist.")
            return False
      except PermissionError:
        logger.warning("You do not have permission to close this file.")
        if self.raise_errors == True:
          raise PermissionError(
              "You do not have permission to close this file. Please try again.")
        else:
          print(
              "You do not have permission to close this file. Please try again.")
          return False
  
    def copy_file(self, file_path, new_file_path):
      """This function duplicates the file under path. Returns True if completed or False if a problem was found.
      An error could be raisen appending on the atribute given to FileTools class. \n
      Inputs:
      -- file_path: string: The path to the file you want to copy. Example: examples/my_file.txt \n
      -- new_file_path: string: The path to the new file. Example: examples/my_new_file.txt"""
      import os
      import shutil
      try:
        if os.path.exists(file_path):
          file = open(file_path)
          shutil.copyfile(file_path, new_file_path)
          print("Succes")
          return True
        else:
          logger.warning("File path does not exist.")
          if self.raise_errors:
            raise FileNotFoundError("File path does not exist")
          else:
            print("File path does not exist")
            return False
      except PermissionError:
        if not self.raise_errors:
          print("You do not have permission to copy this file.")
          return False
        else:
          raise PermissionError(
              "You do not have permission to copy this file. Please try again.")
  
  logger_a = logging.getLogger("File_processor_a")
  file_handler = logging.FileHandler("Hashes.hsh")
  logger_a.addHandler(file_handler)
  logger_a.setLevel(logging.DEBUG)
  class FileToolsAdvanced:
  
    def __init__(self, raise_errors):
      self.raise_errors = raise_errors
      self.PERMISSION_E = "You do not have permission to do this."
      self.FILE_NOT_FOUND = "The file you are trying to access does not exist."
      self.ERROR = "An error has occured. Please try again."
      if isinstance(self.raise_errors, bool):
        if self.raise_errors:
          logger.debug("raise_errors is True")
        else:
          logger.debug("raise_errors is False")
        print("FileToolsAdvanced is available")
      else:
  
        logger.error(
            "raise_errors (atribute of the FileToolsAdvanced class) is a boolean"
        )
        raise Exception(
            "FileToolsAdvanced is not available due to Type error. Please take a look at the error log."
        )
  
    def install_needed_packages(self):
      
      """Installs the needed packages. Returns True if completed or False if a problem was found."""
      import os
      try:
        os.system("pip install cryptography")
        return True
      except OSError:
        logger.error(
            "The needed packages could not be installed. Please install them manually."
        )
        if self.raise_errors:
          raise OSError(
              "The needed packages could not be installed. Please install them manually."
          )
        else:
          print(
              "The needed packages could not be installed. Please install them manually."
          )
          return False
    def generate_en_key(self):
      
      """Generates a random encryption key. Returns the key if completed or False if a problem was found."""
  
      from cryptography.fernet import Fernet
      try:
        key = Fernet.generate_key()
        return key
      except Error:
        logger.error("The key could not be generated. Please try again.")
        if self.raise_errors:
          raise Error("The key could not be generated. Please try again.")
        else:
          print("The key could not be generated. Please try again.")
          return False
    def validate_file_type(self, files, validate_f_types):
      
      """IN - files: list of strings, validate_f_types: list of strings
         OUT - A list of the files that passed the validation. If no files passed the validation, returns False."""
      rtrn = []
      import os
      import mimetypes 
      if isinstance(files, list) and isinstance(validate_f_types, list):
        for file in files:
          try:
            if os.path.exists(file):
              type = ""
              add_to = False
              for wrd in file:
                if add_to:
                  type += wrd
                if wrd == ".":
                  add_to = True
              if type in validate_f_types:
                rtrn.append(file)
              else:
                pass
            else:
              logger.warning(f"The file {file} does not exist.")
              if self.raise_errors:
                raise FileNotFoundError(self.FILE_NOT_FOUND)
              else:
                print(self.FILE_NOT_FOUND)
          except PermissionError:
            logger.warning("You do not have permission to read this file.")
            if self.raise_errors:
              raise PermissionError(self.PERMISSION_E)
            else:
              print(self.PERMISSION_E)
        if any(rtrn):
          return rtrn
        else:
          return False
      else:
        logger.error("The files and validate_f_types parameters must be lists.")
        if self.raise_errors:
          raise TypeError("The files and validate_f_types parameters must be lists.")
        else:
          print("The files and validate_f_types parameters must be lists.")
    def validate_file_size(self, files, max_size):
      
      """IN - Files: list of files to validate.
         IN - max_size: maximum size of the file in bytes. (int) \n
         OUT - Returns a list of files that are under or = to the max size. If no files passed, returns an empty list."""
      rtrn = []
      import os
      if isinstance(files, list) and isinstance(max_size, int):
        
        for file in files:
          try:
            if os.path.exists(file):
              size = os.path.getsize(file)
              if size <= max_size:
                rtrn.append(file)
            else:
              logger.warning(f"The file {file} does not exist.")
              if self.raise_errors:
                raise FileNotFoundError(self.FILE_NOT_FOUND)
              else:
                print(self.FILE_NOT_FOUND)
          except PermissionError:
            logger.warning("You do not have permission to read this file.")
            if self.raise_errors:
              raise PermissionError(self.PERMISSION_E)
            else:
              print(self.PERMISSION_E)
        if any(rtrn):
          return rtrn
        else:
          return False
      else:
        logger.error("The files parameter must be a list and the max_size parameter must be an int.")
        if self.raise_errors:
          raise TypeError("The files parameter must be a list and the max_size parameter must be an int.")
        else:
          print("The files parameter must be a list and the max_size parameterr must be an int.")
    def create_file(self, file_path, file_data):
      
      """IN - file_path: string: The path to the file you want to create. Example: examples/my_file.png
         IN - file_data: string: The data you want to write in the file. Example: Hello, world! /n
        OUT - False if the file could not be created or True if it was created."""
      if not any(file_data):
        logger.error("The file_data parameter cannot be empty.")
        if self.raise_errors:
          raise ValueError("The file_data parameter cannot be empty.")
        else:
          print("The file_data parameter cannot be empty.")
          return False
      else:
        if isinstance(file_path, str) and isinstance(file_data, str): 
          try:
            with open(file_path, "w") as file:
              file.write(file_data)
              return True
          except PermissionError:
            logger.warning("You do not have permission to create this file.")
            if self.raise_errors:
              raise PermissionError(self.PERMISSION_E)
            else:
              print(self.PERMISSION_E)
              return False
        else:
          logger.error("All parameters must be strings.")
          if self.raise_errors:
            raise TypeError("All parameters must be strings.")
          else:
            print("All parameters must be strings.")
            
            return False
    def get_file_atribute(self, file_path, atribute):
      
      """IN - file_path: string: The path to the file you want to get the atribute of. Example: examples/my_file.png
         IN - atribute: string: The atribute you want to get hold of. Example: "size" /n
        OUT - The atribute of the file if it was found or False if not. """
      if isinstance(file_path, str) and isinstance(atribute, str):
        import os
        if os.path.exists(file_path):
          atribute.lower()
          try:
            err = "The atribute parameter must be either 'size', 'type', 'encoding', 'creation time' or 'lst modification time'."
            if atribute == "size":
              size = os.path.getsize(file_path)
              return size
            elif atribute == "type":
              type = ""
              add_to = False
              for wrd in file_path:
                if add_to:
                  type += wrd
                if wrd == ".":
                  add_to = True
                  type = ""
              return type
            elif atribute == "creation time":
              cr_t = os.path.getctime(file_path)
              return cr_t
            elif atribute == "lst modification time":
              rtrn = os.path.getmtime(file_path)
              return rtrn
            elif atribute == "exists":
              return True
            elif atribute == "get encoding":
              import locale
              rtrn = locale.getpreferredencoding(False)
              return rtrn
            else:
              logger.error(err)
              if self.raise_errors:
                raise ValueError(err)
              else:
                print(err)
                return False
          except PermissionError:
            logger.warning("You do not have permission to read this file.")
            if self.raise_errors:
              raise PermissionError(self.PERMISSION_E)
            else:
              print(self.PERMISSION_E)
              return False
  
      else:
        logger.error("All parameters must be strings.")
        if self.raise_errors:
          raise TypeError("All parameters must be strings.")
        else:
          print("All parameters must be strings.")
          return False
  
  
    def get_SHA256(self, file_path):
      
      import logging
      logger_a = logging.getLogger("File_processor_a")
      file_handler = logging.FileHandler("Hashes.hsh")
      logger_a.addHandler(file_handler)
      logger_a.setLevel(logging.DEBUG)
      if isinstance(file_path, str):
        try:
          import hashlib
          with open(file_path, "rb") as file: 
            file_data = file.read()
            sha256_hash = hashlib.sha256(file_data).hexdigest()
            logger_a.debug(f"The SHA256 hash of the {file_path} file is: " + sha256_hash)
            
            return sha256_hash
        except PermissionError:
          logger.warning("You do not have permission to know files SHA256.")
          if self.raise_errors:
            raise PermissionError(self.PERMISSION_E)
          else:
            print(self.PERMISSION_E)
            return False
        except FileNotFoundError:
          logger.warning(self.FILE_NOT_FOUND)
          if self.raise_errors:
            raise FileNotFoundError(self.FILE_NOT_FOUND)
          else:
            print(self.FILE_NOT_FOUND)
            return False
      else:
        logger.error("All parameters must be strings.")
        if self.raise_errors:
          raise TypeError("All parameters must be strings.")
        else:
          print("All parameters must be strings.")
          return False
    def compress_file(self, file_path):
      
      if isinstance(file_path, str):
        import os 
        import gzip
        if os.path.exists(file_path):
          try:
            with open(file_path, "rb") as file:
              file_data = file.read()
              with gzip.open(file_path + ".gz", "wb") as compressed_file:
                compressed_file.write(file_data)
                logger.info(f"The file {file_path} was compressed successfully.")
                return True
          except PermissionError:
            logger.warning("You do not have permission to compress this file.")
            if self.raise_errors:
              raise PermissionError(self.PERMISSION_E)
            else:
              print(self.PERMISSION_E)
              return False
        else:
          logger.warning("The file does not exist.")
          if self.raise_errors:
            raise FileNotFoundError(self.FILE_NOT_FOUND)
          else:
            print(self.FILE_NOT_FOUND)
            return False
      else:
        logger.error("All parameters must be strings.")
        if self.raise_errors:
          raise TypeError("All parameters must be strings.")
        else:
          print("All parameters must be strings.")
    def decompress_file(self, file_path):
      
      if isinstance(file_path, str):
        import os
        import gzip
        try:
          if os.path.exists(file_path):
            if file_path.endswith(".gz"):
              with open(file_path, "wb") as file:
                with gzip.open(file_path, "rb") as compressed_file:
                  file_data = compressed_file.read()
                  file.write(file_data)
                  logger.info(f"The file {file_path} was decompressed successfully.")
                  return True
          else:
            logger.warning("The file does not exist.")
            if self.raise_errors:
              raise FileNotFoundError(self.FILE_NOT_FOUND)
            else:
              print(self.FILE_NOT_FOUND)
              return False
        except PermissionError:
          logger.warning("You do not have permission to decompress this file.")
          if self.raise_errors:
            raise PermissionError(self.PERMISSION_E)
          else:
            print(self.PERMISSION_E)
            return False
      else:
        logger.error("All parameters must be strings.")
        if self.raise_errors:
          raise TypeError("All parameters must be strings.")
        else:
          print("All parameters must be strings.")
    def encrypter(self, file_path, key):
      
      import os
  
      from cryptography.fernet import Fernet
      try:
        if os.path.exists(file_path):
          with open(file_path, "rb") as file_:
            file_data = file_.read()
            encrypted_data = Fernet(key).encrypt(file_data)
            with open(file_path, "wb") as encrypted_file:
              encrypted_file.write(encrypted_data)
              
              import hashlib
              with open(file_path, "rb") as file: 
                file_data = file.read()
                sha256_hash = hashlib.sha256(file_data).hexdigest()
                logger_a.debug(f"The SHA256 hash of the encrypted {file_path} file is: " + sha256_hash)
              return True
              
  
        else:
          logger.warning(self.FILE_NOT_FOUND)
          if self.raise_errors:
            raise FileNotFoundError(self.FILE_NOT_FOUND)
          else:
            print(self.FILE_NOT_FOUND)
            return False
  
      except PermissionError:
        logger.warning("You do not have permission to encrypt this file.")
        if self.raise_errors:
          raise PermissionError(self.PERMISSION_E)
        else:
          print(self.PERMISSION_E)
          return False 
    def decrypter(self, file_path, key):
      
      import os
      from cryptography.fernet import Fernet
      try:
        if os.path.exists(file_path):
  
          with open(file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
            decrypted_data = Fernet(key).decrypt(encrypted_data)
            with open(file_path, "wb") as decrypted_file:
              decrypted_file.write(decrypted_data)
              import logging
              
              import hashlib
              with open(file_path, "rb") as file: 
                file_data = file.read()
                sha256_hash = hashlib.sha256(file_data).hexdigest()
                logger_a.debug(f"The SHA256 hash of the decrypted {file_path} file is: " + sha256_hash)
              return True
        else:
          logger.warning(self.FILE_NOT_FOUND)
          if self.raise_errors:
            raise FileNotFoundError(self.FILE_NOT_FOUND)
          else:
            print(self.FILE_NOT_FOUND)
            return False
      except PermissionError:
        logger.warning("You do not have permission to decrypt this file.")
        if self.raise_errors:
          raise PermissionError(self.PERMISSION_E)
        else:
          print(self.PERMISSION_E)
          return False
  # Jan Habr
    def compare_file_data(self, file_path_1, file_path_2):
      if isinstance(file_path_1, str) and isinstance(file_path_2, str):
        import os
        if os.path.exists(file_path_1) and os.path.exists(file_path_2):
          try:
            with open(file_path_1, "rb") as file_1:
              file_data_1 = file_1.read()
            with open(file_path_2, "rb") as file_2:
              file_data_2 = file_2.read()
            if file_data_1 == file_data_2:
              return True
            else:
              return False
          except PermissionError:
            logger.warning("You do not have permission to compare these files.")
            if self.raise_errors:
              raise PermissionError(self.PERMISSION_E)
            else:
              print(self.PERMISSION_E)
              return False
      else:
        logger.error("Both arguments must be strings.")
        if self.raise_errors:
          raise TypeError(self.FILE_NOT_FOUND)
        else:
          print(self.FILE_NOT_FOUND)
          return False
    def higlight_text_differences(self, file_path_1, file_path_2):
      import difflib
  
      with open(file_path_1, 'r') as file1:
          file1_content = file1.readlines()
  
      with open(file_path_2, 'r') as file2:
          file2_content = file2.readlines()
  
      diff = difflib.ndiff(file1_content, file2_content)
      rtrn = {}
      for line in diff:
          if line.startswith('+'):
             rtrn["Added"] = line[1:]
          elif line.startswith('-'):
            rtrn["Removed"] =  line[1:]
          elif line.startswith(' '):
            rtrn["Unchanged"] = line[1:]
      return rtrn
class Image:
  class ImageToolsQuick:
    """This Class is used to work with Image files from your project. \n 
    It's best for one time interactions with images. It's not recomended to use it for a lot actions around one Imgae. \n
    But it's quickly accesible and easy to use."""
  
    def __init__(self):
      self.hello = "hello"
  
    def convert_image_to(self, new_file_type, file_name, file_type):
      '''Converts inputted image into a different file type. \n
         Inputs: \n
         -- new_file_type: string: The file type you convert the image to. Example: "jpg" Warning do not write dots! \n
         --file_name: string: The name of the file you want to convert. Example: "my_image Warning do not write dots! \n
         --file_type: string: The file type of the Image you want to convert. Example: "webp" Warning do not write dots!'''
      from PIL import Image
      img = Image.open(f"{file_name}.{file_type}")
      img.save(f"{file_name}.{new_file_type}")
      print(
          f"Converting {file_name}.{file_type} to {new_file_type} was successfully completed. "
      )
  
    def image_resizer(self, file_name, file_type, new_file_name, resize_2_nums):
      '''This function can resize your Images. note: it's best to import them to the editor if you do not want to struggle \n
        Inputs: \n
        --file_name: string: only the name of the file. Example: "my_picture" Warning do not write dots! \n
        --file_type: string: the type of the image file. Example: "jpg" Warning do not write dots! \n
        --new_file_name: string: The name of the new file created. Example: "new_picture" Warning do not write dots! \n
        --resize_2_nums: (int, int): the two numbers what you resize your picture to. Example: (280, 280) Warning write it with braces!'''
      from PIL import Image
  
      img = Image.open(f'{file_name}.{file_type}')
  
      img_resize = img.resize((resize_2_nums))
      img_resize.save(f'{new_file_name}.{file_type}')
      print("Success")
  
    def image_preview(self, image_file, image_type):
      '''By triggering this function and entering the inputs it shows the image in a pygame window. \n
        Inputs: \n
        -- image_file: string: The name of the file. Example: "my_picture" Warning no dots or file types! \n
        -- image_type: string: The file type of the file. Example: "jpg" Warning do not write dots!'''
      import pygame
  
      pygame.init()
      window_width = 800
      window_height = 600
      game_display = pygame.display.set_mode((window_width, window_height))
      bg_image = pygame.image.load(f'{image_file}.{image_type}')
      running = True
  
      while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
  
        game_display.blit(bg_image, (0, 0))
        pygame.display.update()
      pygame.quit()
  
    def duplicate(self, file):
      '''Duplicates the inputted image file. \n
        Inputs: \n
        -- file: string: The complete name of the image file. Example: my_image.png'''
      from PIL import Image
      img = Image.open(f"{file}")
      img.save(f"duped_{file}")
      print("Success")
  
    def jpg(self, file_name, file_type):
      from PIL import Image
      '''Converts imputed image into jpg. New image saves under the same name but as a jpg. \n
        Inputs: \n
        -- file_name: string: The name of the file you want to convert. Example: "my_image" Warning no dots or file types! \n
        -- file_type: string: The file type of the image you want to convert. Example: "gif" Warning do not write dots!'''
      img = Image.open(f"{file_name}.{file_type}")
      img.save(f"{file_name}.jpg")
  
    def png(self, file_name, file_type):
      from PIL import Image
      '''Converts imputed image into png. New image saves under the same name but as a png. \n
        Inputs: \n
        -- file_name: string: The name of the file you want to convert. Example: "my_image" Warning no dots or file types! \n
        -- file_type: string: The file type of the image you want to convert. Example: "webp" Warning do not write dots!'''
      img = Image.open(f"{file_name}.{file_type}")
      img.save(f"{file_name}.png")
  
    def gif(self, file_name, file_type):
      from PIL import Image
      '''Converts imputed image into gif. New image saves under the same name but as a gif. \n
        Inputs: \n
        -- file_name: string: The name of the file you want to convert. Example: "my_image" Warning no dots or file types! \n
        -- file_type: string: The file type of the image you want to convert. Example: "png" Warning do not write dots!'''
      img = Image.open(f"{file_name}.{file_type}")
      img.save(f"{file_name}.gif")
  
    def webp(self, file_name, file_type):
      from PIL import Image
      '''Converts imputed image into webp. New image saves under the same name but as a webp. \n
        Inputs: \n
        -- file_name: string: The name of the file you want to convert. Example: my_image Warning no dots or file types! \n
        -- file_type: string: The file type of the image you want to convert. Example: "jpg" Warning do not write dots!'''
      img = Image.open(f"{file_name}.{file_type}")
      img.save(f"{file_name}.webp")
  
    def info(self):
      '''This function prints the information needed to use this package. For complete use of this package install the following on your device: \n
        -- pygame \n
        -- Pillow \n
        '''
      print("Please install the following on your device:")
      print("--pygame")
      print("--Pillow")
      print("using your devices console or Import using Shell.")
      print(" \n ")
      print(
          "Hello! You used the info() function. here is the list of available functions:"
      )
      print("--1 convert_image_to")
      print("--2 duplicate")
      print("--3 image_resizer")
      print("--4 image_preview")
      print("--5 jpg")
      print("--6 png")
      print("--7 webp")
      print("--8 gif")
      print(
          "For more info about functions take a look at the function comments.")
  
  
  class ImageTools:
    """This Class is used to work with Image files from your project. \n
    Needs two atributes: \n
    -- image_name: string: The name of the Image you want to work with. Example: "my_image" Warning do not write dots! \n
    -- file_type: string: The file type of the Image you want to work with. Example: "jpg" Warning do not write dots! """
  
    def __init__(self, image_name, file_type):
      self.image_name = image_name
      self.file_type = file_type
  
    def convert_image_to(self, new_file_type):
      '''Converts your image into a different file type. \n
         Inputs: \n
         -- new_file_type: string: The file type you convert the image to. Example: "jpg" Warning do not write dots! \n'''
      from PIL import Image
      img = Image.open(f"{self.image_name}.{self.file_type}")
      img.save(f"{self.image_name}.{new_file_type}")
      print(
          f"Converting {self.image_name}.{self.file_type} to {new_file_type} was successfully completed. "
      )
  
    def image_resizer(self, new_file_name, resize_2_nums):
      '''This function can resize your Images. note: it's best to import them to the editor if you do not want to struggle \n
        Inputs: \n
        --new_file_name: string: The name of the new file created. Example: "new_picture" Warning do not write dots! \n
        --resize_2_nums: (int, int): the two numbers what you resize your picture to. Example: (280, 280) Warning write it with braces!'''
      from PIL import Image
  
      img = Image.open(f'{self.image_name}.{self.file_type}')
  
      img_resize = img.resize((resize_2_nums))
      img_resize.save(f'{new_file_name}.{self.file_type}')
      print("Success")
  
    def image_preview(self):
      '''By triggering this function you can preview the image in a pygame window.'''
      import pygame
  
      pygame.init()
      window_width = 800
      window_height = 600
      game_display = pygame.display.set_mode((window_width, window_height))
      bg_image = pygame.image.load(f'{self.image_name}.{self.file_type}')
      running = True
  
      while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
  
        game_display.blit(bg_image, (0, 0))
        pygame.display.update()
      pygame.quit()
  
    def duplicate(self):
      '''Duplicates the image file. \n'''
      from PIL import Image
      img = Image.open(f"{self.image_name}.{self.file_type}")
      img.save(f"duped_{self.image_name}.{self.file_type}")
      print("Success")
  
    def jpg(self):
      from PIL import Image
      '''Converts image into jpg. New image saves under the same name but as a jpg. \n'''
      img = Image.open(f"{self.image_name}.{self.file_type}")
      img.save(f"{self.image_name}.jpg")
  
    def png(self):
      from PIL import Image
      '''Converts image into png. New image saves under the same name but as a png. \n'''
      img = Image.open(f"{self.image_name}.{self.file_type}")
      img.save(f"{self.image_name}.png")
  
    def gif(self):
      from PIL import Image
      '''Converts image into gif. New image saves under the same name but as a gif. \n'''
      img = Image.open(f"{self.image_name}.{self.file_type}")
      img.save(f"{self.image_name}.gif")
  
    def webp(self):
      from PIL import Image
      '''Converts image into webp. New image saves under the same name but as a webp. \n'''
      img = Image.open(f"{self.image_name}.{self.file_type}")
      img.save(f"{self.image_name}.webp")
  
    def info(self):
      '''This function prints the information needed to use this package. For complete use of this package install the following on your device: \n
        -- pygame \n
        -- Pillow \n
        '''
      print("Please install the following on your device:")
      print("--pygame")
      print("--Pillow")
      print("using your devices console or Import using Shell.")
      print(" \n ")
      print(
          "Hello! You used the info() function. here is the list of available functions:"
      )
      print("--1 convert_image_to")
      print("--2 duplicate")
      print("--3 image_resizer")
      print("--4 image_preview")
      print("--5 jpg")
      print("--6 png")
      print("--7 webp")
      print("--8 gif")
      print(
          "For more info about functions take a look at the function comments.")
  
