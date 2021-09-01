class Excel:
    def open_excel(self, pc_name, flashver, vcsid, firmware):
        """Changes vcs id and firmware on attributes.csv"""
        import pandas as pd
        df = pd.read_csv(fr'C:\Users\{pc_name}\Desktop\fw-{firmware}\attributes.csv')
        last_index = df.index[-1]

        for i in range(0, last_index + 1):
            df.loc[i, 'DLE FW Version'] = flashver
            print(fr'{df.loc[i, "DLE FW Version"]} has been updated to {flashver}' + "\n")
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(fr'{df.loc[i, "DLE FW Version"]} has been updated to {flashver}' + "\n")
            df.loc[i, 'Customer Firmware Version'] = flashver
            print(fr"{df.loc[i, 'Customer Firmware Version']} has been updated to {flashver}" + "\n")
            f.write(fr"{df.loc[i, 'Customer Firmware Version']} has been updated to {flashver}" + "\n")
            df.loc[i, 'Customer FW Version Internal'] = flashver
            print(fr"{df.loc[i, 'Customer FW Version Internal']} has been updated to {flashver}" + "\n")
            f.write(fr"{df.loc[i, 'Customer FW Version Internal']} has been updated to {flashver}" + "\n")
            df.loc[i, 'VCS ID'] = vcsid
            print(fr"{df.loc[i, 'VCS ID']} has been updated to {vcsid}" + "\n")
            f.write(fr"{df.loc[i, 'VCS ID']} has been updated to {vcsid}" + "\n")
            f.close()
            df.to_csv(fr'C:\Users\{pc_name}\Desktop\fw-{firmware}\attributes.csv', index=False)

    def open_excel_calx2(self, pc_name, flashver, vcsid, firmware):
        """Changes vcs id and firmware on attributes.csv"""
        import pandas as pd
        df = pd.read_csv(fr'C:\Users\{pc_name}\Desktop\fw-{firmware}\attributes.csv')
        last_index = df.index[-1]

        for i in range(0, last_index + 1):
            df.loc[i, 'Inter Version'] = flashver
            print(fr'{df.loc[i, "Inter Version"]} has been updated to {flashver}' + "\n")
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(fr'{df.loc[i, "Inter Version"]} has been updated to {flashver}' + "\n")
            df.loc[i, 'Customer Firmware Version'] = flashver
            print(fr"{df.loc[i, 'Customer Firmware Version']} has been updated to {flashver}" + "\n")
            f.write(fr"{df.loc[i, 'Customer Firmware Version']} has been updated to {flashver}" + "\n")
            # df.loc[i, 'Customer FW Version Internal'] = flashver
            df.loc[i, 'VCS ID'] = vcsid
            print(fr"{df.loc[i, 'VCS ID']} has been updated to {vcsid}" + "\n")
            f.write(fr"{df.loc[i, 'VCS ID']} has been updated to {vcsid}" + "\n")
            f.close()
            df.to_csv(fr'C:\Users\{pc_name}\Desktop\fw-{firmware}\attributes.csv', index=False)
