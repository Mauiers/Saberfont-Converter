import os
import re
import shutil


# extract numbers from string
def extract_numbers(string):
    # Find one or more digits at the end of the string
    match = re.search(r'\d+', string)
    if match:
        numbers = match.group()
        return int(numbers)
    else:
        return 1


def make_verso():
    # make verso folder
    verso_path = path + '/Verso/'
    if not os.path.isdir(verso_path):
        os.mkdir(verso_path)

    # copy CFX files into Verso folder
    for cfx_file in cfx_files:
        if cfx_file not in os.listdir(verso_path):
            shutil.copy(cfx_path + cfx_file, verso_path)

    # rename Verso files to proper format
    lockup_iterator = 1
    poweron_iterator = 1
    poweroff_iterator = 1

    for verso_file in os.listdir(verso_path):
        if 'blaster' in verso_file:
            os.rename(verso_path + verso_file, verso_path + 'blast' + verso_file[verso_file.index('r') + 1:])
        elif 'hum' in verso_file:
            os.rename(verso_path + verso_file, verso_path + 'hum.wav')
        elif 'lockup' in verso_file:
            os.rename(verso_path + verso_file, verso_path + 'lockup' + str(lockup_iterator) + '.wav')
            lockup_iterator += 1
        elif 'hswing' in verso_file:
            os.rename(verso_path + verso_file, verso_path + 'swingh' + verso_file[verso_file.index('g') + 1:])
        elif 'lswing' in verso_file:
            os.rename(verso_path + verso_file, verso_path + 'swingl' + verso_file[verso_file.index('g') + 1:])
        elif 'stab' in verso_file:
            os.remove(verso_path + verso_file)
        elif 'poweron' in verso_file or 'pwron' in verso_file:
            os.rename(verso_path + verso_file,
                      verso_path + 'on' + str(poweron_iterator) + verso_file[verso_file.index('.'):])
            poweron_iterator += 1
        elif 'poweroff' in verso_file or 'pwroff' in verso_file:
            os.rename(verso_path + verso_file,
                      verso_path + 'off' + str(poweroff_iterator) + verso_file[verso_file.index('.'):])
            poweroff_iterator += 1
        elif 'swing' in verso_file:
            os.rename(verso_path + verso_file, verso_path + 'aswing' + verso_file[verso_file.index('g') + 1:])


def make_proffie():
    # make proffie folder
    proffie_path = path + '/Proffie/'
    if not os.path.isdir(proffie_path):
        os.mkdir(proffie_path)

    # copy CFX files into proffie folder
    for cfx_file in cfx_files:
        if cfx_file not in os.listdir(proffie_path):
            shutil.copy(cfx_path + cfx_file, proffie_path)

    # create proffie subfolders
    prof_subfolders = ['blst', 'clsh', 'in', 'out', 'stab', 'swingh', 'swingl', 'swng']

    for subfolder in prof_subfolders:
        path_subfolder = proffie_path + '/' + subfolder
        if not os.path.isdir(path_subfolder):
            os.mkdir(path_subfolder)

    # move files to subfolders
    for old_cfx_file in os.listdir(proffie_path):
        if 'blaster' in old_cfx_file and old_cfx_file != 'blst':
            shutil.move(f'{proffie_path}{old_cfx_file}', f'{proffie_path}/blst/blst{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
        elif 'clash' in old_cfx_file and old_cfx_file != 'clsh':
            shutil.move(f'{proffie_path}{old_cfx_file}', f'{proffie_path}/clsh/clsh{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
        elif 'poweroff' in old_cfx_file and old_cfx_file != 'in':
            shutil.move(f'{proffie_path}{old_cfx_file}', f'{proffie_path}/in/in{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
        elif 'poweron' in old_cfx_file and old_cfx_file != 'out':
            shutil.move(f'{proffie_path}{old_cfx_file}', f'{proffie_path}/out/out{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
        elif 'stab' in old_cfx_file and old_cfx_file != 'stab':
            shutil.move(f'{proffie_path}{old_cfx_file}', f'{proffie_path}/stab/stab{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
        elif 'hswing' in old_cfx_file and old_cfx_file != 'swingh':
            shutil.move(f'{proffie_path}{old_cfx_file}', f'{proffie_path}/swingh/swingh{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
        elif 'lswing' in old_cfx_file and old_cfx_file != 'swingl':
            shutil.move(f'{proffie_path}{old_cfx_file}', f'{proffie_path}/swingl/swingl{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
        elif 'swing' in old_cfx_file and old_cfx_file != 'swng' and old_cfx_file != 'swingh' and old_cfx_file != 'swingl':
            shutil.move(f'{proffie_path}{old_cfx_file}', f'{proffie_path}/swng/swng{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
        # rename boots to match Proffie naming scheme
        elif 'boot' in old_cfx_file:
            os.rename(f'{proffie_path}{old_cfx_file}', f'{proffie_path}boot{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')


if __name__ == '__main__':
    paths = []
    # open paths.txt and set lines == every line in the file
    with open('paths.txt') as f:
        lines = f.readlines()

    # remove newlines and append to paths list for processing
    for line in lines:
        paths.append(line.replace('\n', ''))

    # for each path gathered from paths.txt
    for path in paths:
        # make sure CFX folder exists
        if 'CFX' not in os.listdir(path):
            print('CFX folder not found in ', path)
            continue

        # gather all files within CFX folder
        cfx_path = path + '/CFX/'
        cfx_files = os.listdir(cfx_path)

        make_verso()
        make_proffie()
