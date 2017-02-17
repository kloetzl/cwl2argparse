import os

import argparse as ap
import sys

from cwl2zshcomp.cwl_argparse_translation import cwl2zshcomp


def main():
    help_text = """
        cwl2zshcomp generates ZSH completion scripts from CWL tool descriptions
        Example: $ cwl2zshcomp FILES [FILES ...] <options>
        """
    parser = ap.ArgumentParser(description=help_text, formatter_class=ap.RawDescriptionHelpFormatter)
    parser.add_argument('files', nargs='+', help='CWL tool descriptions or directories with tools')
    parser.add_argument('-d', '--dest', help='Directory to store resulting .py files')
    parser.add_argument('-q', '--quiet', action='store_true', help="Do not print generated code to system output")
    parser.add_argument('-f', action='store_true', help="Force override existing files without confirmation")
    args = parser.parse_args()

    files = args.files
    dest = args.dest or os.getcwd()
    for f in files:
        if os.path.isfile(f):
            cwl2zshcomp(f, dest, args.quiet, args.y, args.prefix)
        elif os.path.isdir(f):
            for file in os.listdir(f):
                cwl2zshcomp(os.path.join(f, file), dest, args.prefix)
        else:
            print("Couldn't process {0}: neither file nor directory".format(f))
    print('Generated to {0}'.format(os.path.abspath(dest)))
    sys.exit(0)


if __name__ == '__main__':
    main()
