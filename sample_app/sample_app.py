from sample_app.package_one.pack_one import PackOne
from sample_app.package_two.pack_two import PackTwo
from configparser import ConfigParser
import sys
import os.path as path


def main():
    p1 = PackOne()
    p2 = PackTwo()
    p1.do()
    p2.process()
    # /etc/sample-app/conf/marvel.ini
    conffile = path.join('/', 'etc', 'sample-app', 'conf', sys.argv[1] + '.ini')
    config = ConfigParser()
    config.read(conffile)
    print(config['HEROES']['billionaire_bad_boy'])
    print(config['HEROES']['goody_two_shoes'])


if __name__ == '__main__':
    main()
