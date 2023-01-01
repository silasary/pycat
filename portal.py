import glob
from os import path
import modular
import worlds

class Portal(modular.ModularClient):
    def __init__(self, mud, _) -> None:
        super().__init__(mud)
        modules = glob.glob(path.join(path.dirname(worlds.__file__), '*.py'))
        self.worlds = [path.basename(f)[:-3] for f in modules if path.isfile(f) and not f.endswith('__init__.py')]

    def getHostPort(self) -> None:
        self.list_worlds()
        return None

    def alias(self, line: str):
        if line.startswith('#connect'):
            super().trigger(line)
        else:
            self.list_worlds()
            return True

    def list_worlds(self):
        msg = 'Please select a world to load:'
        for w in self.worlds:
            msg += f'\n#connect {w}'
        self.log(msg)




def getClass():
    return Portal
