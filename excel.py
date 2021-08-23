class Excel:
    def open_excel(self, PC_NAME, flashver, vcsid, firmware):
        """Changes vcs id and firmware on attributes.csv"""
        import pandas as pd
        df = pd.read_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv')
        last_index = df.index[-1]

        for i in range(0, last_index + 1):
            df.loc[i, 'DLE FW Version'] = flashver
            df.loc[i, 'Customer Firmware Version'] = flashver
            df.loc[i, 'Customer FW Version Internal'] = flashver
            df.loc[i, 'VCS ID'] = vcsid
            df.to_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv', index=False)

    def open_excel_prod(self, PC_NAME, flashver, vcsid, firmware):
        """Changes vcs id and firmware on attributes.csv"""
        import pandas as pd
        df = pd.read_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv')
        last_index = df.index[-1]

        for i in range(0, last_index + 1):
            df.loc[i, 'DLE FW Version'] = flashver
            df.loc[i, 'Customer Firmware Version'] = flashver
            df.loc[i, 'Customer FW Version Internal'] = flashver
            df.loc[i, 'VCS ID'] = vcsid
            df.to_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv', index=False)

    def open_excel_calx2(self, PC_NAME, flashver, vcsid, firmware):
        """Changes vcs id and firmware on attributes.csv"""
        import pandas as pd
        df = pd.read_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv')
        last_index = df.index[-1]

        for i in range(0,last_index + 1):
            df.loc[i, 'Inter Version'] = flashver
            df.loc[i, 'Customer Firmware Version'] = flashver
            # df.loc[i, 'Customer FW Version Internal'] = flashver
            df.loc[i, 'VCS ID'] = vcsid
            df.to_csv(fr'C:\Users\{PC_NAME}\Desktop\fw-{firmware}\attributes.csv', index=False)