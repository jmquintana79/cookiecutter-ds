# -*- coding: utf-8 -*-

from dotenv import dotenv_values
import os

## get project config values
def get(verbose:bool = False)->dict:
    """
    Get project config values.
    verbose -- display information.
    return -- dictionary with keys and their respective values.
    """
    # get project path
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
    # get .env path
    dotenv_path = os.path.join(project_dir, '.env')
    # display
    if verbose:
        print('[info] ".env" path: "{}"'.format(dotenv_path))
    # get values
    config = dotenv_values(dotenv_path)
    # display
    if verbose:
        print('[info] config variables:')
        for k,v in config.items():
            print('"{}": {}'.format(k, v))
    # return
    return config


if __name__ == '__main__':
    print('get config dictionary:')
    config = get(True)
    print('display result:')
    print(config)
