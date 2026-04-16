# -*- coding: utf-8 -*-

from dotenv import dotenv_values, find_dotenv
 
def get(verbose:bool = False)->dict:
    """
    Get project config values.
    verbose -- display information.
    return -- dictionary with keys and their respective values.
    """
    # find env file path
    dotenv_path = find_dotenv(usecwd=True)  # busca subiendo desde cwd
    # collect env values
    config = dotenv_values(dotenv_path)
    # display
    if verbose:
        print(f'[info] ".env" path: "{dotenv_path}"')
        print("[info] config variables:")
        for k, v in config.items():
            print('"{}": {}'.format(k, v))
    # return
    return config    
 
if __name__ == "__main__":
    print("get config dictionary:")
    config = get(True)
    print("display result:")
    print(config)
