#!/usr/bin/env python3

import glob, argparse, sys, os, textwrap

def ret_os_path():
        if ((sys.platform == 'win32') and (os.environ.get('OS','') == 'Windows_NT')):
                return "\\"
        else:
                return "/"

def parse_metadata_files(input_folder, output_folder):
        for file in glob.glob(input_folder + ret_os_path() + "$I*"):
                f = open(file, "rb")
                g = f.read()
                filename = g.split(b"\\\x00")[-1].decode("utf-16le").replace("\x00", "")
                o = open(output_folder + ret_os_path() + filename, "wb")
                try:
                        t = open(input_folder + ret_os_path() + "$R" + file[2:], "rb")
                except:
                        f.close()
                        o.close()
                        continue
                o.write(t.read())
                t.close()
                o.close()
                f.close()

if __name__ == '__main__':
        parser = argparse.ArgumentParser(
                        formatter_class=argparse.RawDescriptionHelpFormatter,
                        description='A tool to parse the $I metadata files from a Windows recycling bin to restore the file name to the $R files.',
                        epilog=textwrap.dedent('''Examples:\npython3 UnRecBin.py -i $Recycle.Bin -o output''')
        )
        # https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
        parser.add_argument('-i','--input',  dest="input", default=".", required=True, help="Input Directory for metadata files and file contents, default: current directory")
        parser.add_argument('-o','--output', dest="output", default=".", required=False, help='Output Directory for real file names, default: current directory')

        args = parser.parse_args()

        if ((args.input == ".") and (args.output != ".")):
                parse_metadata_files(args.input, args.output)
        else:
                parser.print_help()