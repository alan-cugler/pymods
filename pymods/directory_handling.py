from pathlib import Path
from pathlib import PurePath
import patoolib


def extract_mods(mod_root_path, mod_comp_path):
    # Unpacks all compressed mods to the mod directory.

    for file in mod_comp_path.iterdir():
        if file.suffix in ('.7z','.rar','.zip'):
            patoolib.extract_archive(file.name, outdir=mod_root_path)


def create_mod_list(mod_root_path):
    # This creates a list of available mods from a directory.
    mod_list = []

    for file in mod_root_path.iterdir():
        if file.is_dir():
            mod_list.append(file.name)

    return mod_list


def rename_mod(mod_root_path, mod_dir):
    # parse mod name to readable mod for migration

    if mod_dir in



def simplify_mod_dir(mod_root_path, mod_dir):
    # Create replacement directory.

    new_mod_dir = rename_mod(mod_root_path, mod_dir)
    Path.mkdir(PurePath(mod_root_path).joinpath(PurePath(new_mod_dir)))

    mod_key_dir_list = ['textures','meshes','skse','source']
    full_path_mod = PurePath(mod_root_path).joinpath(PurePath(new_mod_dir))

    for key_dir in mod_key_dir_list:
        Path.mkdir(PurePath(full_path_mod).joinpath(PurePath(key_dir)))


