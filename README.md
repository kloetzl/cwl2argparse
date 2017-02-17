# cwl2zshcomp

cwl2zshcomp generates ZSH auto completions from CWL tool descriptions. The result is not perfect, but should replace a lot of manual labor.

## Installation

    $ git clone https://github.com/kloetzl/cwl2zshcomp
    $ cd cwl2zshcomp
    $ sudo pip install .
  
## Usage

    cwl2zshcomp FILES [FILES ...] [options]
    
Options:
* `FILES` - a list of CWL tool descriptions or directories with tools
* `-d`, `--dest` - Destination directory to store resulting files
* `-q`, `--quiet` - Do not print generated code to system output
* `-f` - If a file with a name the same as the generated one already exists, force overriding


## License

Apache License 2.0

Original Code for [cwl2argparse](https://github.com/common-workflow-language/cwl2argparse) by Anton Khodak
