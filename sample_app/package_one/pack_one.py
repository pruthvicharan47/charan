import os
import os.path as path


class PackOne:
    def __init__(self):
        self.name = 'PackOne'
        self._res = path.join(path.dirname(__file__), 'res')

    def do(self):
        return 'My name is {}'.format(self.name)

    def process_img(self):
        imgfile = path.join(self._res, 'picture.jpg')
        return os.stat(imgfile)

    def process_csv(self):
        csvfiles = [path.join(self._res, 'data_1.csv'),
                    path.join(self._res, 'data_2.csv')]
        lines = []
        for csvfile in csvfiles:
            with open(csvfile) as f:
                lines.append(f.readlines())
        return lines
