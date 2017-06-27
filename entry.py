from __future__ import absolute_import
from __future__ import print_function

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flower.command import FlowerCommand
from flower.utils import bugreport



def main():
    try:
        flower = FlowerCommand()
        flower.execute_from_commandline()
    except:
        import sys
        print(bugreport(app=flower.app), file=sys.stderr)
        raise


if __name__ == "__main__":
    main()
