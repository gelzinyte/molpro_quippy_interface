import os
from ase.io import read
from quippy.potential import Potential
from ase.io.extxyz import key_val_dict_to_str
import pdb
from ase.calculators.morse import MorsePotential
from molpro import Molpro


# example of how to call molpro calculator

# dftb = Potential(args_str='TB DFTB', param_filename=os.path.join(os.getcwd(), './tightbind.parms.DFTB.mio-0-1.xml'))


# template_path='/opt/project/template_e_f.inp'


template_path='/home/eg475/molpro_stuff/driver/template_e_f.inp'



calc_args = { \
              'template':'/home/eg475/molpro_stuff/driver/template_e_f.inp',
              # 'template' : '/opt/project/template_e_f.inp',
              'molpro' : '{/opt/molpro/bin/molprop}',
              'energy_from' : 'RKS',
              # 'append_lines' : None,
              'test_mode' : True,
              # 'working_dir' : {/scratch-ssd/eg475/tmp},
              'extract_forces' : True}

with open(template_path, 'r') as f:
    print('Molpro template:')
    for line in f.readlines():
        print(line.rstrip())


molpro=Molpro(calc_args=calc_args)

print('Molpro imported')
methane = read('methane.xyz')
methane.set_calculator(molpro)
print('calculator set')
energy = methane.get_potential_energy()
print(f'finally calculated energy: {energy}')
