import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class MakeCustfw(QDialog):
    def __init__(self):
        super().__init__()

    update_progress = pyqtSignal(int)

    def make_custfw(self):
        from copy_files import Copy_Files
        from create_folder import Create_Folder
        from rename_delete import RenameDelete
        from excel import Excel
        from bot_window_eng import Ui_OtherWindow

        bot_win = Ui_OtherWindow()
        bot_win.make_logs()
        bot_win.get_edit_lines_info()
        path_to_bot = str(bot_win.get_edit_lines_info()[1][1:])
        bot_split = path_to_bot.split("\\")
        firmware = (bot_split[-3])
        uname = os.environ['HOMEPATH']
        pc_name = uname.replace("\\Users\\", "")
        os.chdir(path_to_bot)
        os.chdir('..')
        path_to_folder = os.getcwd()
        base_fw = bot_win.get_edit_lines_info()[0]
        create = Create_Folder()
        create.move_firmware_foundation(pc_name, base_fw, firmware)
        create.create_custfw_folder(pc_name)
        create.create_bin_folder(pc_name)
        copy_files = Copy_Files()
        worker_02 = WorkerThread_02()
        worker_02.copy_bins(pc_name, path_to_bot)
        create.zip_folder(pc_name)
        copy_files.copy_bot_files(pc_name, path_to_bot, firmware)
        copy_files.copy_XML(pc_name, path_to_folder)
        name_del = RenameDelete()
        create.delete_folder(pc_name)
        name_del.rename(firmware, pc_name)
        get_vcs_and_fw = WorkerThread()
        get_vcs_and_fw.get_vcs_fw(pc_name)
        flashver = get_vcs_and_fw.get_vcs_fw(pc_name)[1]
        vcsid = get_vcs_and_fw.get_vcs_fw(pc_name)[0]
        excel = Excel()
        excel.open_excel(pc_name, flashver, vcsid, firmware)
        create.move_custfw(pc_name, firmware)
        self.delete_custfw(pc_name)
        self.good_bye(pc_name, firmware)

    def make_custfw_prod(self):
        from create_folder import Create_Folder
        from rename_delete import RenameDelete
        from excel import Excel
        from bot_window_prod import Ui_OtherWindow

        bot_win = Ui_OtherWindow()
        bot_win.make_logs()
        bot_win.get_edit_lines_info()
        path_to_bot = str(bot_win.get_edit_lines_info()[1][1:])
        bot_split = path_to_bot.split("\\")
        firmware = (bot_split[-1])
        uname = os.environ['HOMEPATH']
        pc_name = uname.replace("\\Users\\", "")
        os.chdir(path_to_bot)
        os.chdir('..')
        base_fw = bot_win.get_edit_lines_info()[0]
        create = Create_Folder()
        create.move_firmware_foundation(pc_name, base_fw, firmware)
        create.move_cust_fw_production(pc_name, path_to_bot, firmware)
        rename = RenameDelete()
        rename.del_dictionary(pc_name, firmware)
        rename.rename_production(firmware, pc_name)
        get_vcs_and_fw = WorkerThread()
        get_vcs_and_fw.get_vcs_fw_prod(pc_name, firmware)
        flashver = get_vcs_and_fw.get_vcs_fw_prod(pc_name, firmware)[1]
        vcsid = get_vcs_and_fw.get_vcs_fw_prod(pc_name, firmware)[0]
        excel = Excel()
        excel.open_excel_prod(pc_name, flashver, vcsid, firmware)
        self.good_bye_prod(pc_name, firmware)

    def delete_custfw(self, pc_name):
        import os.path
        directory = rf'C:\Users\{pc_name}\Desktop'
        os.chdir(directory)
        if os.path.isfile('./CUSTFW'):
            os.remove("CUSTFW")

    def move_logs(self, pc_name, firmware):
        import shutil
        shutil.move(r'C:\Users\Public\log.txt', fr'C:\Users\{pc_name}\Desktop\fw-{firmware}')

    def good_bye(self, pc_name, firmware):
        self.move_logs(pc_name, firmware)
        QMessageBox.information(self, "Success!", f"Your package can now be found on your desktop named fw-{firmware}.")
        sys.exit()

    def msg_btn(self):
        sys.exit()

    def good_bye_prod(self, pc_name, firmware):
        self.move_logs(pc_name, firmware)
        QMessageBox.information(self, "Success!", f"Your package can now be found on your desktop named fw-{firmware}.")
        sys.exit()


class WorkerThread(QThread):
    update_progress = pyqtSignal(int)

    def copy_bins(self, pc_name, path_to_bot):
        import shutil
        import names
        import os.path
        from os import path
        parent_dir = fr'C:\Users\{pc_name}\Desktop' + 'CUSTFW' + 'SkuConfig'
        for name in names.BIN_FILES_01:
            pathway_to_firmware = f'{path_to_bot}'
            og_directory = os.getcwd()
            os.chdir(pathway_to_firmware)
            if path.exists(name):
                original = f'{path_to_bot}' + f'\\{name}'
                target = fr'C:\Users\{pc_name}\Desktop\CUSTFW\SkuConfig\{name}'
                shutil.copyfile(original, target)
                print(f'{name} has been transferred to {parent_dir}\n')
                f = open(r"C:\Users\Public\log.txt", "a+")
                f.write(f'{name} has been transferred to {parent_dir}\n')
                f.close()
                self.update_progress.emit(10)
            else:
                print('FAILED TO TRANSFER')
                f = open(r"C:\Users\Public\log.txt", "a+")
                f.write(f'{name} has been failed to transfer\n')
                f.close()
                os.chdir(og_directory)
                self.update_progress.emit(10)

    def get_vcs_fw(self, pc_name):
        """Pulls vcs id and firmware from CFG.bot"""
        vcsid_fw = []
        lookup = 'FlashVer: '
        lookup2 = 'VcsId: '
        with open(fr'C:\Users\{pc_name}\Desktop\CUSTFW\CFG.bot', encoding='latin1') as myFile:
            for num, line in enumerate(myFile, 1):
                if lookup in line.strip('\\n'):
                    vcsid_fw.append(line[-9:])
                    vcsid_fw_stripped = [x.replace('\n', '') for x in vcsid_fw]
                    self.update_progress.emit(10)
                if lookup2 in line.strip('\\n'):
                    vcsid_fw.append(line[-11:])
                    self.update_progress.emit(10)
            return vcsid_fw_stripped

    def get_vcs_fw_prod(self, pc_name, firmware):
        """Pulls vcs id and firmware from CFG.bot"""
        vcsid_fw = []
        lookup = 'FlashVer: '
        lookup2 = 'VcsId: '
        with open(fr'C:\Users\{pc_name}\Desktop\fw-{firmware}\CUSTFW\CFG.bot', encoding='latin1') as myFile:
            for num, line in enumerate(myFile, 1):
                if lookup in line.strip('\\n'):
                    vcsid_fw.append(line[-9:])
                    vcsid_fw_stripped = [x.replace('\n', '') for x in vcsid_fw]
                    self.update_progress.emit(10)
                if lookup2 in line.strip('\\n'):
                    vcsid_fw.append(line[-11:])
                    self.update_progress.emit(10)
            return vcsid_fw_stripped


class WorkerThread_02(QThread):
    """Takes bin files from BOT file, and pastes it into firmware desktop folder"""
    update_progress = pyqtSignal(int)
    def copy_bins(self, pc_name, path_to_bot):
        import shutil
        import names
        import os.path
        from os import path
        parent_dir = fr'C:\Users\{pc_name}\Desktop' + 'CUSTFW' + 'SkuConfig'
        for name in names.BIN_FILES_02:
            pathway_to_firmware = f'{path_to_bot}'
            og_directory = os.getcwd()
            os.chdir(pathway_to_firmware)
            if path.exists(name):
                original = f'{path_to_bot}' + f'\\{name}'
                target = fr'C:\Users\{pc_name}\Desktop\CUSTFW\SkuConfig\{name}'
                shutil.copyfile(original, target)
                print(f'{name} has been transferred to {parent_dir}\n')
                f = open(r"C:\Users\Public\log.txt", "a+")
                f.write(f'{name} has been transferred to {parent_dir}\n')
                f.close()
                self.update_progress.emit(10)
            else:
                print('FAILED TO TRANSFER')
                f = open(r"C:\Users\Public\log.txt", "a+")
                f.write(f'{name} has been failed to transfer\n')
                f.close()
                os.chdir(og_directory)
                self.update_progress.emit(10)


