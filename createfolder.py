import os
from os import path
import shutil


class CreateFolder:

    def create_firmware_folder(self, pc_name, firmware):
        """Creates firmware folder"""
        directory = f'fw-{firmware}'
        parent_dir = fr'C:\Users\{pc_name}\Desktop'
        pathway = os.path.join(parent_dir, directory)
        os.mkdir(pathway)
        print("Directory '% s' created" % directory)
        with open(r"C:\Users\Public\log.txt", "a+") as f:
            f.write("Directory '% s' created\n" % directory)

    def create_custfw_folder(self, pc_name):
        """Creates CUSTFW folder"""
        directory = "CUSTFW"
        parent_dir = fr'C:\Users\{pc_name}\Desktop'
        pathway = os.path.join(parent_dir, directory)
        os.mkdir(pathway)
        print("Directory '% s' created" % directory)
        with open(r"C:\Users\Public\log.txt", "a+") as f:
            f.write("Directory '% s' created\n" % directory)

    def create_bin_folder(self, pc_name):
        """Creates SkuConfig folder for bin files"""
        directory = "SkuConfig"
        parent_dir = fr'C:\Users\{pc_name}\Desktop' + r'\CUSTFW'
        pathway = os.path.join(parent_dir, directory)
        os.mkdir(pathway)
        print("Directory '% s' created" % directory)
        with open(r"C:\Users\Public\log.txt", "a+") as f:
            f.write("Directory '% s' created\n" % directory)

    def zip_folder(self, pc_name):
        """Zips SkuConfig"""
        parent_dir = fr'C:\Users\{pc_name}\Desktop' + r'\CUSTFW'
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
        """Deletes unzipped SkuConfig"""
        parent_dir = fr'C:\Users\{pc_name}\Desktop' + r'\CUSTFW' + r'\SkuConfig'
        shutil.rmtree(parent_dir)
        print('Deleting SkuConfig\n')
        with open(r"C:\Users\Public\log.txt", "a+") as f:
            f.write('Deleting SkuConfig' + "\n")

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
            with open(r"C:\Users\Public\log.txt", "a+") as f:
                f.write(fr'{name} has been transferred to {parent_dir}' + r'\CUSTFW' + "\n")
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
        import shutil
        src = fr'\\10.195.35.226\shared\mark.cuasay\base_fw\{base_fw}'
        dest = fr'C:\Users\{pc_name}\Desktop\fw-{firmware}'

        shutil.copytree(src, dest)
        print(f"Moving firmware foundation to {dest}\n")
        with open(r"C:\Users\Public\log.txt", "a+") as f:
            f.write(fr'Moving firmware foundation to  {dest}' + "\n")

    def move_cust_fw_production(self, pc_name, pathway_to_bot, firmware):
        import shutil
        src = fr'{pathway_to_bot}'
        dest = fr'C:\Users\{pc_name}\Desktop\fw-{firmware}\CUSTFW'
        shutil.copytree(src, dest)
        print(f"Moving custfw (production) to {dest}\n")
        with open(r"C:\Users\Public\log.txt", "a+") as f:
            f.write(f"Moving custfw (production) to {dest}\n")
