# cwl2zshcomp

cwl2zshcomp generates ZSH auto completions from CWL tool descriptions. The result is not perfect, but should replace a lot of manual labor.

If you read this, you might also like [biozsh](https://github.com/kloetzl/bioszsh), a curated directory of ZSH auto completions for bioinformatics tools.

## Installation

    $ git clone https://github.com/kloetzl/cwl2zshcomp
    $ cd cwl2zshcomp
    $ sudo pip install .
  
## Usage

    cwl2zshcomp [options] FILES...
    
Available options:
* `-d`, `--dest` - Destination directory to store resulting files
* `-h`, `--help` - Print help
* `-q`, `--quiet` - Do not print generated code to system output
* `-f` - Force overriding a output file, if it already exists


## License

Apache License 2.0

Original Code for [cwl2argparse](https://github.com/common-workflow-language/cwl2argparse) by Anton Khodak
