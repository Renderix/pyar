import os

import pandas as pd

from pyar import Molecule
from pyar.interface import babel


def make_formula(at_ls):
    freq = {items: at_ls.count(items) for items in at_ls}
    return ''.join(f"{key}{value}" for key, value in freq.items()), files in os.walk(starting_point)

def collect_files(start, exclude_pattern, pattern):
    paths = []
    for root, dir, files in os.walk(start):
        for file in files:
            if pattern in file and os.path.splitext(file)[-1] == '.xyz' and exclude_pattern not in root:
                paths.append(os.path.join(root, file))
    return paths


def collect_data(xyz_files):
    ne = pd.DataFrame()
    for xyz_file in xyz_files:
        inchi_string = babel.make_inchi_string_from_xyz(xyz_file)
        smile_string = babel.make_smile_string_from_xyz(xyz_file)
        atoms_list, mol_coordinates, name, title, energy = Molecule.read_xyz(xyz_file)
        nat = len(atoms_list)
        formula = make_formula(atoms_list)
        ne.append([nat, formula, xyz_file, atoms_list, mol_coordinates, energy, smile_string, inchi_string])

    df = pd.DataFrame(ne, columns=['n_atoms', 'formula', 'Name', 'Atoms', 'coordinates', 'Energy', 'SMILE', 'InChi'])
    df.to_csv('data.csv')


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--starting-directory', default='./')
    parser.add_argument('--exclude', default='tmp')
    parser.add_argument('--pattern', default='result')
    args = parser.parse_args()
    xyz_files = collect_files(args.starting_directory, args.exclude, args.pattern)
    collect_data(xyz_files)

if __name__ == "__main__":
    main()
