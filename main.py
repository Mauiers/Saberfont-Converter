import os
import re
import shutil


def get_input():
    correct_input = [1, 2, 3, 4]
    while True:
        num = int(input(f'\nCFX folder found. Please select formats to convert to:\n'
                        f'\n'
                        f'1. Proffie\n'
                        f'2. Verso\n'
                        f'3. Xeno\n'
                        f'4. All of the above\n').strip())

        if num not in correct_input:
            print(f'\nChoice not recognized. Please try again.\n')
        else:
            return num


def can_convert_to_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# extract numbers from string
def extract_numbers(string):
    # Find one or more digits at the end of the string
    match = re.search(r'\d+', string)
    if match:
        numbers = match.group()
        return int(numbers)
    else:
        return 1


def reformat(choice):
    is_proffie, is_verso, is_xeno = False, False, False
    if choice == 1:
        is_proffie = True
    elif choice == 2:
        is_verso = True
    elif choice == 3:
        is_xeno = True
    elif choice == 4:
        is_proffie, is_verso, is_xeno = True, True, True

    if is_proffie:
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
                shutil.move(f'{proffie_path}{old_cfx_file}',
                            f'{proffie_path}/blst/blst{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
            elif 'clash' in old_cfx_file and old_cfx_file != 'clsh':
                shutil.move(f'{proffie_path}{old_cfx_file}',
                            f'{proffie_path}/clsh/clsh{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
            elif 'poweroff' in old_cfx_file and old_cfx_file != 'in':
                shutil.move(f'{proffie_path}{old_cfx_file}',
                            f'{proffie_path}/in/in{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
            elif 'poweron' in old_cfx_file and old_cfx_file != 'out':
                shutil.move(f'{proffie_path}{old_cfx_file}',
                            f'{proffie_path}/out/out{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
            elif 'stab' in old_cfx_file and old_cfx_file != 'stab':
                shutil.move(f'{proffie_path}{old_cfx_file}',
                            f'{proffie_path}/stab/stab{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
            elif 'hswing' in old_cfx_file and old_cfx_file != 'swingh':
                shutil.move(f'{proffie_path}{old_cfx_file}',
                            f'{proffie_path}/swingh/swingh{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
            elif 'lswing' in old_cfx_file and old_cfx_file != 'swingl':
                shutil.move(f'{proffie_path}{old_cfx_file}',
                            f'{proffie_path}/swingl/swingl{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')
            elif 'swing' in old_cfx_file and old_cfx_file != 'swng' and old_cfx_file != 'swingh' and old_cfx_file != 'swingl':
                shutil.move(f'{proffie_path}{old_cfx_file}',
                            f'{proffie_path}/swng/swng{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')

            # rename boots to match Proffie naming scheme
            elif 'boot' in old_cfx_file:
                os.rename(f'{proffie_path}{old_cfx_file}',
                          f'{proffie_path}boot{str(extract_numbers(old_cfx_file)).zfill(2)}.wav')

    if is_verso:
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

        for xeno_file in os.listdir(verso_path):
            if 'blaster' in xeno_file:
                os.rename(verso_path + xeno_file, verso_path + 'blast' + xeno_file[xeno_file.index('r') + 1:])
            elif 'hum' in xeno_file:
                os.rename(verso_path + xeno_file, verso_path + 'hum.wav')
            elif 'lockup' in xeno_file:
                os.rename(verso_path + xeno_file, verso_path + 'lockup' + str(lockup_iterator) + '.wav')
                lockup_iterator += 1
            elif 'hswing' in xeno_file:
                os.rename(verso_path + xeno_file, verso_path + 'swingh' + xeno_file[xeno_file.index('g') + 1:])
            elif 'lswing' in xeno_file:
                os.rename(verso_path + xeno_file, verso_path + 'swingl' + xeno_file[xeno_file.index('g') + 1:])
            elif 'stab' in xeno_file:
                os.remove(verso_path + xeno_file)
            elif 'poweron' in xeno_file or 'pwron' in xeno_file:
                os.rename(verso_path + xeno_file,
                          verso_path + 'on' + str(poweron_iterator) + xeno_file[xeno_file.index('.'):])
                poweron_iterator += 1
            elif 'poweroff' in xeno_file or 'pwroff' in xeno_file:
                os.rename(verso_path + xeno_file,
                          verso_path + 'off' + str(poweroff_iterator) + xeno_file[xeno_file.index('.'):])
                poweroff_iterator += 1
            elif 'swing' in xeno_file:
                os.rename(verso_path + xeno_file, verso_path + 'aswing' + xeno_file[xeno_file.index('g') + 1:])

    if is_xeno:
        # make xeno folder
        xeno_path = path + '/Xeno/'
        if not os.path.isdir(xeno_path):
            os.mkdir(xeno_path)

        # copy CFX files into Xeno folder
        for cfx_file in cfx_files:
            if cfx_file not in os.listdir(xeno_path):
                shutil.copy(cfx_path + cfx_file, xeno_path)

        max_power_on = 0
        max_pwr_off = 0

        for xeno_file in os.listdir(xeno_path):
            solo = '' if can_convert_to_int(xeno_file[xeno_file.index(".") - 1:xeno_file.index(".")]) else '1'

            if 'blaster' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}blaster ({solo}{xeno_file[xeno_file.index("r") + 1:xeno_file.index(".")]}).wav')
            elif 'humM' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}hum ({solo}{xeno_file[xeno_file.index("mM") + 2:xeno_file.index(".")]}).wav')
            elif 'lockup' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}lockup ({solo}{xeno_file[xeno_file.index("p") + 1:xeno_file.index(".")]}).wav')
            elif 'hswing' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}swingh ({solo}{xeno_file[xeno_file.index("g") + 1:xeno_file.index(".")]}).wav')
            elif 'lswing' in xeno_file:
                os.rename(xeno_path + xeno_file,
                          f'{xeno_path}swingl ({solo}{xeno_file[xeno_file.index("g") + 1:xeno_file.index(".")]}).wav')
            elif 'stab' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}stab ({solo}{xeno_file[xeno_file.index("b") + 1:xeno_file.index(".")]}).wav')
            elif 'clash' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}clash ({solo}{xeno_file[xeno_file.index("h") + 1:xeno_file.index(".")]}).wav')
            elif 'endlock' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}endlock ({solo}{xeno_file[xeno_file.index("k") + 1:xeno_file.index(".")]}).wav')
            elif 'lockup' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}lock ({solo}{xeno_file[xeno_file.index("p") + 1:xeno_file.index(".")]}).wav')
            elif 'poweron' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}out ({solo}{xeno_file[xeno_file.index("n") + 1:xeno_file.index(".")]}).wav')
            elif 'poweroff' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}in ({solo}{xeno_file[xeno_file.index("ff") + 2:xeno_file.index(".")]}).wav')
            elif 'preon' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}preon ({solo}{xeno_file[xeno_file.index("n") + 1:xeno_file.index(".")]}).wav')
            elif 'pstoff' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}postoff ({solo}{xeno_file[xeno_file.index("ff") + 2:xeno_file.index(".")]}).wav')
            elif 'swing' in xeno_file:
                os.rename(f'{xeno_path}{xeno_file}',
                          f'{xeno_path}swing ({solo}{xeno_file[xeno_file.index("g") + 1:xeno_file.index(".")]}).wav')

            # drop boots
            elif 'boot' in xeno_file:
                os.remove(f'{xeno_path}{xeno_file}')


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

        input_num = get_input()
        reformat(input_num)
