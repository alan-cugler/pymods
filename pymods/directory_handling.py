from pathlib import Path
from pathlib import PurePath
import patoolib


def extract_mods(mod_root_path, mod_comp_path):
    for file in mod_comp_path.iterdir():
        if file.suffix in ('.7z','.rar','.zip'):
            mod_full_path = mod_root_path / file.name
            mod_full_path.mkdir(exist_ok=True)
            patoolib.extract_archive(file.name, outdir=mod_full_path)


def create_mod_list(mod_root_path):
    mod_list = []

    for file in mod_root_path.iterdir():
        if file.is_dir():
            mod_list.append(file.name)

    return mod_list


def simplify_mod_dir(mod_root_path, mod_dir):
    new_mod_dir = mod_dir + '_simplified'
    #new_mod_dir = new_mod_name(mod_dir)

    full_path_mod = mod_root_path / new_mod_dir
    full_path_mod.mkdir(exist_ok=True)

    mod_key_dir_list = ['textures','meshes','skse','source']
    for key_dir in mod_key_dir_list:
        sub_mod_dir = full_path_mod / key_dir
        sub_mod_dir.mkdir(exist_ok=True)
        if key_dir == 'skse':
            skse_plug_dir = full_path_mod / key_dir / 'plugins'
            skse_plug_dir.mkdir(exist_ok=True)


def migrate_mod_files(mod_root_path, mod_dir):
    full_path_mod = mod_root_path / mod_dir

    mod_dir_and_files = full_mod_path.rglob('*.*')
    mod_files = [i for i in mod_dir_and_files if i.is_file()]
