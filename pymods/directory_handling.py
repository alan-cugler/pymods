from pathlib import Path
from pathlib import PurePath
import patoolib


def extract_mods(mod_root_path, mod_comp_path):
    # Unpacks all compressed mods to the mod directory.

    for file in mod_comp_path.iterdir():
        if file.suffix in ('.7z','.rar','.zip'):
            mod_full_path = PurePath(mod_root_path).joinpath(PurePath(file.name))
            Path.mkdir(PurePath(mod_full_path))
            patoolib.extract_archive(file.name, outdir=mod_full_path)


def create_mod_list(mod_root_path):
    # This creates a list of available mods from a directory.
    mod_list = []

    for file in mod_root_path.iterdir():
        if file.is_dir():
            mod_list.append(file.name)

    return mod_list


#def rename_mod(mod_root_path, mod_dir):
    # parse mod name to readable mod for migration
    #['se','sse','SE','SSE']


def simplify_mod_dir(mod_root_path, mod_dir):
    # Create replacement directory.

    mod_key_dir_list = ['textures','meshes','skse','source']

    new_mod_dir = mod_dir + '_test'
    full_path_mod = PurePath(mod_root_path).joinpath(PurePath(new_mod_dir))

    full_path_mod.mkdir
    for key_dir in mod_key_dir_list:
        sub_mod_dir = PurePath(full_path_mod).joinpath(PurePath(key_dir))
        sub_mod_dir.mkdir
        if key_dir == 'skse':
            skse_path = PurePath(full_path_mod).joinpath(PurePath(key_dir))
            skse_plug_dir = PurePath(skse_path).joinpath(PurePath('plugins'))
            skse_plug_dir.mkdir

