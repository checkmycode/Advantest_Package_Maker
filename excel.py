import os
import pandas as pd

class Excel:
    def __init__(self):
        pass

    def get_vcs_fw(self, PC_NAME):
        """Pulls vcs id and firmware from CFG.bot"""
        vcsid_fw = []
        lookup = 'FlashVer: '
        lookup2 = 'VcsId: '
        with open(fr'C:\Users\{PC_NAME}\Desktop\CUSTFW\CFG.bot', encoding='latin1') as myFile:
            for num, line in enumerate(myFile, 1):
                if lookup in line.strip('\\n'):
                    vcsid_fw.append(line[-9:])
                    vcsid_fw_stripped = [x.replace('\n', '') for x in vcsid_fw]
                if lookup2 in line.strip('\\n'):
                    vcsid_fw.append(line[-11:])
            return vcsid_fw_stripped

    def get_vcs_fw_prod(self,PC_NAME, firmware):
        """Pulls vcs id and firmware from CFG.bot"""
        vcsid_fw = []
        lookup = 'FlashVer: '
        lookup2 = 'VcsId: '
        with open(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\CUSTFW\CFG.bot', encoding='latin1') as myFile:
            for num, line in enumerate(myFile, 1):
                if lookup in line.strip('\\n'):
                    vcsid_fw.append(line[-9:])
                    vcsid_fw_stripped = [x.replace('\n', '') for x in vcsid_fw]
                if lookup2 in line.strip('\\n'):
                    vcsid_fw.append(line[-11:])
            return vcsid_fw_stripped

    def open_excel(self, PC_NAME, flashver, vcsid, firmware):
        """Changes vcs id and firmware on attributes.csv"""
        import pandas as pd
        df = pd.read_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv')
        for i in range(0,26):
            df.loc[i, 'DLE FW Version'] = flashver
            df.loc[i, 'Customer Firmware Version'] = flashver
            df.loc[i, 'Customer FW Version Internal'] = flashver
            df.loc[i, 'VCS ID'] = vcsid
            df.to_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv', index=False)


    def open_excel_prod(self, PC_NAME, flashver, vcsid, firmware):
        """Changes vcs id and firmware on attributes.csv"""
        import pandas as pd
        df = pd.read_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv')
        for i in range(0,32):
            df.loc[i, 'DLE FW Version'] = flashver
            df.loc[i, 'Customer Firmware Version'] = flashver
            df.loc[i, 'Customer FW Version Internal'] = flashver
            df.loc[i, 'VCS ID'] = vcsid
            df.to_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv', index=False)