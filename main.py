import os
import shutil


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
        if subfolder not in os.path.listdir(proffie_path):
            os.mkdir(subfolder)

    lockup_iterator = 1
    poweron_iterator = 1
    poweroff_iterator = 1

    # move files to subfolders
    for old_cfx_file in proffie_path:
        if 'blaster' in old_cfx_file:
            os.move(proffie_path + old_cfx_file, proffie_path + '/blst/' + old_cfx_file[old_cfx_file.index('t') + 1:])
        # elif 'hum' in old_cfx_file:
        #     os.rename(proffie_path + old_cfx_file, proffie_path + 'hum.wav')
        # elif 'lockup' in old_cfx_file:
        #     os.rename(proffie_path + old_cfx_file, proffie_path + 'lockup' + str(lockup_iterator) + '.wav')
        #     lockup_iterator += 1
        # elif 'hswing' in old_cfx_file:
        #     os.rename(proffie_path + old_cfx_file, proffie_path + 'swingh' + proffie_file[proffie_file.index('g') + 1:])
        # elif 'lswing' in old_cfx_file:
        #     os.rename(proffie_path + old_cfx_file, proffie_path + 'swingl' + proffie_file[proffie_file.index('g') + 1:])
        # elif 'stab' in old_cfx_file:
        #     os.remove(proffie_path + old_cfx_file)
        # elif 'poweron' in old_cfx_file or 'pwron' in old_cfx_file:
        #     os.rename(proffie_path + old_cfx_file,
        #               proffie_path + 'on' + str(poweron_iterator) + proffie_file[proffie_file.index('.'):])
        #     poweron_iterator += 1
        # elif 'poweroff' in old_cfx_file or 'pwroff' in old_cfx_file:
        #     os.rename(proffie_path + old_cfx_file,
        #               proffie_path + 'off' + str(poweroff_iterator) + proffie_file[proffie_file.index('.'):])
        #     poweroff_iterator += 1
        # elif 'swing' in proffie_file:
        #     os.rename(proffie_path + proffie_file, proffie_path + 'aswing' + proffie_file[proffie_file.index('g') + 1:])

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

       # make_verso()

        make_proffie()