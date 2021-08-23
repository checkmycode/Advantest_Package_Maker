import os
from os import path
import shutil

class Create_Folder:

    def __init__(self):
        pass

    def create_firmware_folder(self,PC_NAME, FIRMWARE):
        """Creates firmware folder"""
        # Directory
        directory = f'fw-{FIRMWARE}'

        # Parent Directory path
        parent_dir = fr'C:\Users\{PC_NAME}\Desktop'

        # Path
        path = os.path.join(parent_dir, directory)

        # Create the directory
        os.mkdir(path)
        print("Directory '% s' created" % directory)
        f = open(r"C:\Users\Public\log.txt", "a+")
        f.write("Directory '% s' created\n" % directory)
        f.close()

    def create_custfw_folder(self, PC_NAME):
        """Creates CUSTFW folder"""
        # Directory
        directory = "CUSTFW"

        # Parent Directory path
        parent_dir = fr'C:\Users\{PC_NAME}\Desktop'

        # Path
        path = os.path.join(parent_dir, directory)

        # Create the directory
        os.mkdir(path)
        print("Directory '% s' created" % directory)
        f = open(r"C:\Users\Public\log.txt", "a+")
        f.write("Directory '% s' created\n" % directory)
        f.close()

    def create_bin_folder(self,PC_NAME):
        '''Creates SkuConfig folder for bin files'''
        # Directory
        directory = "SkuConfig"

        # Parent Directory path
        parent_dir = fr'C:\Users\{PC_NAME}\Desktop' + '\CUSTFW'

        # Path
        path = os.path.join(parent_dir, directory)

        # Create the directory
        os.mkdir(path)
        print("Directory '% s' created" % directory)
        f = open(r"C:\Users\Public\log.txt", "a+")
        f.write("Directory '% s' created\n" % directory)
        f.close()


    def zip_folder(self, pc_name):
        '''Zips SkuConfig'''
        parent_dir = fr'C:\Users\{pc_name}\Desktop' + '\CUSTFW'
        original_working_directory = os.getcwd()
        os.chdir(parent_dir)
        print('Zipping SkuConfig\n')


        if path.exists('SkuConfig'):
            shutil.make_archive(
                'SkuConfig',
                'zip',
                parent_dir)
        os.chdir(original_working_directory)

    def delete_folder(self, pc_name):
        '''Deletes unzipped SkuConfig'''
        parent_dir = fr'C:\Users\{pc_name}\Desktop' + '\CUSTFW' + '\SkuConfig'
        shutil.rmtree(parent_dir)
        print('Deleting SkuConfig\n')
        f = open(r"C:\Users\Public\log.txt", "a+")
        f.write('Deleting SkuConfig' + "\n")
        f.close()

    def move_attributes(self, pc_name, base_fw):
        import os.path
        from os import path
        parent_dir = fr'C:\Users\{pc_name}\Desktop\base_fw\{base_fw}'
        os.chdir(parent_dir)
        name = r'attributes.csv'
        if path.exists(name):
            original = parent_dir + fr'\{name}'
            target = fr'C:\Users\{pc_name}\Desktop\CUSTFW\{name}'
            shutil.copyfile(original, target)
            print(fr'{name} has been transferred to {parent_dir}' + r'\CUSTFW')
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(fr'{name} has been transferred to {parent_dir}' + r'\CUSTFW' + "\n")
            f.close()
        else:
            print('attributes don\'t exist? fix this')

    def move_custfw(self, pc_name, firmware):
        import shutil
        original = fr'C:\Users\{pc_name}\Desktop\CUSTFW'
        target = fr'C:\Users\{pc_name}\Desktop\fw-{firmware}'

        shutil.move(original, target)
        print(fr'custfw has been transferred to {target}')
        f = open(r"C:\Users\Public\log.txt", "a+")
        f.write(fr'custfw has been transferred to {target}' + "\n")
        f.close()

    def move_firmware_foundation(self, pc_name, base_fw, firmware):
        # importing os module
        import shutil
        # path
        path = fr'C:\Users\7329711\Desktop\base_fw\{base_fw}'

        # Source path
        src = path

        # Destination path
        dest = fr'C:\Users\{pc_name}\Desktop\fw-{firmware}'

        shutil.copytree(src, dest)
        print(f"Moving firmware foundation to {dest}\n")
        f = open(r"C:\Users\Public\log.txt", "a+")
        f.write(fr'Moving firmware foundation to  {dest}' + "\n")
        f.close()


    def move_cust_fw_production(self, pc_name, pathway_to_bot, firmware):
        # importing os module
        import os

        # importing shutil module
        import shutil

        # Source path
        src = fr'{pathway_to_bot}'

        # Destination path
        dest = fr'C:\Users\{pc_name}\Desktop\fw-{firmware}\CUSTFW'

        shutil.copytree(src, dest)
        print(f"Moving custfw (production) to {dest}\n")
        f = open(r"C:\Users\Public\log.txt", "a+")
        f.write(f"Moving custfw (production) to {dest}\n")
        f.close()


