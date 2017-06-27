from __future__ import absolute_import
from __future__ import print_function

from dcs_flower.command import FlowerCommand
from dcs_flower.utils import bugreport


def main():
    try:
        dcs_flower = FlowerCommand()
        dcs_flower.execute_from_commandline()
    except:
        import sys
        print(bugreport(app=dcs_flower.app), file=sys.stderr)
        raise


if __name__ == "__main__":
    main()
