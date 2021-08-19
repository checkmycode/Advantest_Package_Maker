import os
import pandas as pd

class Excel:
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