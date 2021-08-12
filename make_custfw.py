import os
import sys


class MakeCustfw:

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
        copy_files.copy_bins(pc_name, path_to_bot)
        create.zip_folder(pc_name)
        copy_files.copy_bot_files(pc_name, path_to_bot, firmware)
        copy_files.copy_XML(pc_name, path_to_folder)
        name_del = RenameDelete()
        create.delete_folder(pc_name)
        name_del.rename(firmware, pc_name)
        get_vcs_and_fw = Excel()
        get_vcs_and_fw.get_vcs_fw(pc_name)
        flashver = get_vcs_and_fw.get_vcs_fw(pc_name)[1]
        vcsid = get_vcs_and_fw.get_vcs_fw(pc_name)[0]
        excel = Excel()
        excel.open_excel(pc_name, flashver, vcsid, firmware)
        create.move_custfw(pc_name, firmware)
        self.move_logs(pc_name, firmware)
        self.delete_custfw(pc_name)
        self.good_bye()

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
        path_to_folder = os.getcwd()
        base_fw = bot_win.get_edit_lines_info()[0]
        create = Create_Folder()
        create.move_firmware_foundation(pc_name, base_fw, firmware)
        create.move_cust_fw_production(pc_name, path_to_bot, firmware)
        rename = RenameDelete()
        rename.del_dictionary(pc_name, firmware)
        rename.rename_production(firmware, pc_name)
        get_vcs_and_fw = Excel()
        get_vcs_and_fw.get_vcs_fw_prod(pc_name, firmware)
        flashver = get_vcs_and_fw.get_vcs_fw_prod(pc_name, firmware)[1]
        vcsid = get_vcs_and_fw.get_vcs_fw_prod(pc_name, firmware)[0]
        excel = Excel()
        excel.open_excel_prod(pc_name, flashver, vcsid, firmware)
        self.move_logs(pc_name, firmware)
        self.good_bye_prod()

    def delete_custfw(self, pc_name):
        import os.path
        dir = rf'C:\Users\{pc_name}\Desktop'
        os.chdir(dir)
        if os.path.isfile('./CUSTFW'):
            os.remove("CUSTFW")

    def move_logs(self, pc_name, firmware):
        import shutil
        shutil.move(r'C:\Users\Public\log.txt', fr'C:\Users\{pc_name}\Desktop\fw-{firmware}')

    def good_bye(self):
        import sys
        if self.make_custfw():
            print('final window should pop up')
            sys.exit()
        else:
            print('SOMETHING WENT WRONG')

    def good_bye_prod(self):
        import sys
        if self.make_custfw_prod():
            print('final window should pop up')
            sys.exit()
        else:
            print('SOMETHING WENT WRONG')



