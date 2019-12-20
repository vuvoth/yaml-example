#!/usr/bin/env python3

import yaml
import sys


with open(sys.argv[1]) as f:
    datas = yaml.load_all(f, Loader=yaml.FullLoader)
    for data in datas:
        print(data)
