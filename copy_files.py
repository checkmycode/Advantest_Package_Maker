import os
import shutil
import names
from names import BIN_FILES

class Copy_Files:

    def __init__(self):
        pass

    def copy_bins(self, PC_NAME, PATH_TO_BOT):
        '''Takes bin files from BOT file, and pastes it into firmware desktop folder'''
        import os.path
        from os import path
        parent_dir = fr'C:\Users\{PC_NAME}\Desktop' + '\CUSTFW' + '\SkuConfig'
        for name in names.BIN_FILES:
            pathway_to_firmware = f'{PATH_TO_BOT}'
            og_directory = os.getcwd()
            os.chdir(pathway_to_firmware)
            if path.exists(name):
                original = f'{PATH_TO_BOT}' + f'\\{name}'
                target = fr'C:\Users\{PC_NAME}\Desktop\CUSTFW\SkuConfig\{name}'
                shutil.copyfile(original, target)
                print(f'{name} has been transferred to {parent_dir}\n')
                f = open(r"C:\Users\Public\log.txt", "a+")
                f.write(f'{name} has been transferred to {parent_dir}\n')
                f.close()
            else:
                print('FAILED TO TRANSFER')
                f = open(r"C:\Users\Public\log.txt", "a+")
                f.write(f'{name} has been failed to transfer\n')
                f.close()
                os.chdir(og_directory)

    def copy_bot_files(self, PC_NAME, PATH_TO_BOT, FIRMWARE):
        '''Takes specific files from BOT folder, and pastes them into firmware desktop folder'''
        import os.path
        from os import path
        import names
        parent_dir = fr'C:\Users\{PC_NAME}\Desktop' + '\CUSTFW' + '\SkuConfig'
        for name in names.BOT_FILES:
            pathway_to_firmware = f'{PATH_TO_BOT}'
            og_directory = os.getcwd()
            os.chdir(pathway_to_firmware)
            original = f'{PATH_TO_BOT}' + f'\\CFG_{FIRMWARE}.bot'
            target = fr'C:\Users\{PC_NAME}\Desktop\CUSTFW\CFG_{FIRMWARE}.bot'
            shutil.copyfile(original, target)
            print(f'{name} has been transferred to {parent_dir}' + "\n")
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f'{name} has been transferred to {parent_dir}' + "\n")
            f.close()
            if path.exists(name):
                original = f'{PATH_TO_BOT}' + f'\\{name}'
                target = fr'C:\Users\{PC_NAME}\Desktop\CUSTFW\{name}'
                shutil.copyfile(original, target)
                print(f'{name} has been transferred to {parent_dir}' + "\n")
                f = open(r"C:\Users\Public\log.txt", "a+")
                f.write(f'{name} has been transferred to {parent_dir}' + "\n")
                f.close()
            else:
                print(f'{name} has failed to transfer')
                f = open(r"C:\Users\Public\log.txt", "a+")
                f.write(f'{name} has been failed to transfer' + "\n")
                f.close()
                os.chdir(og_directory)


    def copy_XML(self, PC_NAME, PATH_TO_FOLDER):
        '''Takes XML_Export_RAM.raw and FADI_SnapToolSchema.sdb and pastes them to firmware desktop folder'''
        import os.path
        from os import path
        parent_dir = fr'C:\Users\{PC_NAME}\Desktop' + '\CUSTFW'
        pathway_to_firmware = f'{PATH_TO_FOLDER}'
        og_directory = os.getcwd()
        os.chdir(pathway_to_firmware + '\\XML\\XML')
        if path.exists('XML_Export_RAM.raw'):
            original = f'{PATH_TO_FOLDER}' + '\\XML\\XML\\' + r'XML_Export_RAM.raw'
            target = fr'C:\Users\{PC_NAME}\Desktop\CUSTFW\XML_Export_RAM.raw'
            shutil.copyfile(original, target)
            print(f'XML_Export_RAM.raw has been transferred to {parent_dir}.' + "\n")
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f'XML_Export_RAM.raw has been transferred to {parent_dir}.' + "\n")
            f.close()
        else:
            print('XML_EXPORT_RAM FAILED TO TRANSFER')
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"XML_Export_RAM not found.")
            f.close()
            os.chdir(og_directory)

        pathway_to_firmware = f'{PATH_TO_FOLDER}'
        og_directory = os.getcwd()
        os.chdir(pathway_to_firmware + '\\XML\\ErrorLog')
        if path.exists(f'FADI_SnapToolSchema.sdb'):
            original = f'{PATH_TO_FOLDER}' + '\\XML\\ErrorLog\\' + r'FADI_SnapToolSchema.sdb'
            target = fr'C:\Users\{PC_NAME}\Desktop\CUSTFW\FADI_SnapToolSchema.sdb'
            shutil.copyfile(original, target)
            print(f'FADI_SnapToolSchema.sdb has been transferred to {parent_dir}.' + "\n")
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f'FADI_SnapToolSchema.sdb has been transferred to {parent_dir}.' + "\n")
            f.close()
        else:
            print(f"FADI_SnapToolSchema.sdb not found.")
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"FADI_SnapToolSchema.sdb not found." + "\n")
            f.close()
            os.chdir(og_directory)

