# UnRecBin

```python
usage: UnRecBin.py [-h] -i INPUT [-o OUTPUT]

A tool to parse the $I metadata files from a Windows recycling bin to restore the file name to the $R files.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input Directory for metadata files and file contents,
                        default: current directory
  -o OUTPUT, --output OUTPUT
                        Output Directory for real file names, default: current
                        directory

Examples:
python3 UnRecBin.py -i $Recycle.Bin -o output

```
