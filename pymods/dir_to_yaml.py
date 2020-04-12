import os

def create_mod_list(mod_root_path):
    '''
    This creates a list of available mods from a directory.
    '''
    mod_list = []

    # [f.name for f in os.scandir('..') if f.is_dir()]
    for file in os.scandir(mod_root_path):
        if file.is_dir():
            mod_list.append(file.name)

    return mods_list


#def create_actual_mod_tree(mod_root_path, mod_dir):
#    '''
#    Builds a tree of the actual mod directory.
#    '''

#    for mod_dir, dirs, files in os.walk(os.path.join(mod_root_path, mod_dir)):


def mod_directory_simplification(mod_root_path, mod_dir):
    '''
    Create replacement directory.
    '''

    new_mod_dir = rename_mod(mod_root_path, mod_dir)
    os.mkdir(os.path.join(mod_root_path, new_mod_dir))

    mod_key_dir_list = ['textures','meshes','skse','source']
    full_path_mod = os.path.join(mod_root_path, new_mod_dir)

    for key_dir in mod_key_dir_list:
        os.mkdir(os.path.join(full_path_mod, key_dir))

def rename_mod(mod_dir):
    '''
    Rewrite mod name into something pretty.
    '''

#    new_mod_dir = 
