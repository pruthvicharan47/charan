from colored import fg, bg, attr


class PackTwo:
    def __init__(self):
        self.name = 'PackTwo'

    def process(self):
        print('This is {}{}{}'.format(fg(226), self.name, attr('reset')))
        return 2
