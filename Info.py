import yaml

class Info():
    yaml_file = {}
    def __init__(self):
        # print("constructor")
        path = "./config.yaml"
        with open(path, 'r') as f:
            self.yaml_file = yaml.safe_load(f)

    def get(self, *args):
        if len(args) == 1:
            return self.yaml_file[args[0]]
        elif len(args) == 2:
            return self.yaml_file[args[0]][args[1]]
        else:
            exit(0)

    # def __del__(self):
    #     print("destructor")