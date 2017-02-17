cwlVersion: v1.0
class: CommandLineTool
baseCommand: andi

inputs:
  verbose_flag:
    doc: Print verbose output
    type: boolean
    default: false
    inputBinding:
      prefix: --verbose
  number_of_threads:
    doc: Prints additional information
    type: int?
    inputBinding:
      prefix: --threads
  threshold:
    doc: Significance of an anchor pair
    type: float?
    separate: False
    inputBinding:
      prefix: -p
  one_genome_per_file:
    doc: Treat all sequences from one file as a single genome
    type: boolean
    default: false
    inputBinding:
      prefix: --join
  version_information:
    doc: Print version string
    type: boolean
    default: false
    inputBinding:
      prefix: --version
  print_help:
    doc: Print help
    type: boolean
    default: false
    inputBinding:
      prefix: --help
  mutation_model:
    doc: Pick an evolutionary model
    type: [ 
      "null",
      {type: enum,
      symbols: [JC, Kimura, Raw]}
    ]
    inputBinding:
      prefix: --model
  files:
    doc: Input files in FASTA format
    type: File?
    streamable: true
    inputBinding:
      position: 5
  #*:file:_files

outputs:
  distmatrix:
    type: stdout
