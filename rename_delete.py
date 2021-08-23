class RenameDelete:
    def __init__(self):
        pass

    def rename(self, firmware, pc_name):
        '''Renames CFG_Firmware.bot to CFG.bot'''
        import names
        import os
        rename_CFG = f'CFG_{firmware}.bot'
        print(f'Renaming {rename_CFG} to CFG.bot\n')
        os.rename(fr'C:\Users\{pc_name}\Desktop\CUSTFW\{rename_CFG}',
                  fr'C:\Users\{pc_name}\Desktop\CUSTFW\CFG.bot')
        f = open(r"C:\Users\Public\log.txt", "a+")
        f.write(f'Renaming {rename_CFG} to CFG.bot\n')
        f.close()

    def del_dictionary(self, pc_name, firmware):
        import os.path
        dir = rf'C:\Users\{pc_name}\Desktop\fw-{firmware}\CUSTFW'
        os.chdir(dir)
        if os.path.isfile('SetDictionary.dco'):
            os.remove('SetDictionary.dco')
            print("Deleting SetDictionary.dco\n")
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write("Deleting SetDictionary.dco\n")
            f.close()

        if os.path.isfile('FwtDictionary.fdo'):
            os.remove('FwtDictionary.fdo')
            print("Deleting FwtDictionary.fdo")
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write("Deleting FwtDictionary.fdo\n")
            f.close()

    def rename_production(self, firmware, pc_name):
        import os

        PRODUCTION_FILES = [

            fr'CFGenc_{firmware}.fluf',
            fr'CFGenc_S2079TAB_bricking.fluf',
            fr'CFG_{firmware}.bot',
            fr'FADI_SnapToolSchema_{firmware}.sdb',
            fr'FwtDictionary.fdo',
            fr'FwtDictionary_{firmware}.fdo',
            fr'manifest.json',
            fr'output.txt',
            fr'R2079_{firmware}.fluf',
            fr'SetDictionary.dco',
            fr'SetDictionary_{firmware}.dco',
            fr'SkuConfig_{firmware}.zip',
            fr'SkuConfig_{firmware}',
            fr'XML_Export_RAM_{firmware}',
            fr'XML_Export_RAM_{firmware}.raw',

        ]

        os.chdir(fr'C:\Users\{pc_name}\Desktop\fw-{firmware}\CUSTFW')
        for name in PRODUCTION_FILES:
            if os.path.isfile(name):
                new_name = name.replace(f'_{firmware}', '')
                os.rename(name, new_name)
                print(fr"Renaming {name} to {new_name}")
                f = open(r"C:\Users\Public\log.txt", "a+")
                f.write(fr"Renaming {name} to {new_name}")
                f.close()
