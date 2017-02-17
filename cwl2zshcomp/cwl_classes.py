import sys
from yaml import load
from collections import OrderedDict


class InputBinding:
    def __init__(self, ib):
        self.position = ib.get('position', None)
        self.prefix = ib.get('prefix', None)


class OutputBinding:
    def __init__(self, ob):
        self.glob = ob.get('glob', None)


class Param:
    optional = False
    default = None
    type = None

    def get_type(self):
        return self.type


class InputParam(Param):
    def __init__(self, param):
        self.id = param['id']
        self.type = param.get('type', None)
        if type(self.type) is str and self.type[-2:] == '[]': # v.1.0 syntax simplification ('<type>[]' == array of <type> )
            self.type = "array"
        if (type(self.type) is list and self.type[0] == 'null'):
            self.optional = True
        elif type(self.type) is str and self.type[-1] == '?':  # v.1.0 ('<type>?' == ['null', '<type>'])
            self.optional = True
            self.type = self.type[:-1]
        else:
            self.optional = False
        self.description = param.get('doc', param.get('description', None))
        self.default = param.get('default', None)
        self.separate = param.get('separate', True)
        input_binding = param.get('inputBinding', None)
        if input_binding:
            self.input_binding = InputBinding(input_binding)

    def get_type(self):
        if type(self.type) is list and self.type[0] == 'null':
            arg_type = self.type[1]
            if type(arg_type) is dict:
                return arg_type['type']
            else:
                return arg_type
        elif type(self.type) is dict:
            return self.type['type']
        else:
            return self.type


class Tool:
    def __init__(self, filename):

        with open(filename) as f:
            tool = load(f)
        try:
            self.tool_class = tool['class']
        except KeyError:
            sys.exit('`class` attribute of the CWL document not found')
        if self.tool_class != 'CommandLineTool':
            raise ValueError('Wrong tool class')

        try:
            self.basecommand = tool['baseCommand']
        except KeyError:
            sys.exit('`baseCommand` attribute of the CWL document not found')
        if type(self.basecommand) == list:
            if len(self.basecommand) == 1:
                self.basecommand = self.basecommand[0]
            else:
                raise ValueError('Multi part commands not yet implemented')

        self.inputs = OrderedDict()
        if type(tool['inputs']) is list:  # ids not mapped
            for param_dict in tool['inputs']:
                param = InputParam(param_dict)
                self.inputs[param.id] = param
        elif type(tool['inputs']) is dict:  # ids mapped
            for id, param_dict in tool['inputs'].items():
                param_dict['id'] = id
                param = InputParam(param_dict)
                self.inputs[id] = param

        self.description = tool.get('doc', tool.get('description', None))
        self.cwl_version = tool.get('cwlVersion', '')
