import os
from colours import *

#paths for python
repo_path = "/mnt/c/Users/benja/Documents/Entertainment/Gaming/ROM's/Playstation 3/DLC's and Extras/Skate 3/Skate_3_Mod_Repo/"
repo_parks_path      = repo_path + 'Custom_Parks/'
repo_replay_path     = repo_path + 'Replays/'
repo_player_path     = repo_path + 'Player_Accounts/'

#paths for terminal
os_repo_path           = "/mnt/c/Users/benja/Documents/Entertainment/Gaming/ROM\\'s/Playstation\\ 3/DLC\\'s\\ and\\ Extras/Skate\\ 3/Skate_3_Mod_Repo/"
os_repo_parks_path     = os_repo_path + 'Custom_Parks/'
os_repo_replay_path    = os_repo_path + 'Replays/'
os_repo_player_path    = os_repo_path + 'Player_Accounts/'

os_rpcs3_savedata_path   = "/mnt/c/Users/benja/Documents/Entertainment/Gaming/Launchers/PS3/dev_hdd0/home/00000001/savedata/"
os_rpcs3_player_path     = os_rpcs3_savedata_path + 'BLES00760-ALIAS_SKATER/'
os_rpcs3_replay_path     = os_rpcs3_savedata_path + 'BLES00760-REPLY_SKATER/'
os_rpcs3_parks_path      = os_rpcs3_savedata_path + 'BLES00760-SPARK_SKATER/'

#########################################################################
# General Functions                                                     #
#########################################################################

def empty_directory(path_to_dir):
    """empties the RPCS3 folder before a differrent save park file is swapped in"""
    os.system('rm {}*'.format(path_to_dir))
    print('Emptied {}'.format(path_to_dir))

def print_files_in_dir(path_to_dir):
    """shows the user the contents of the RPCS3 folder"""
    for d in os.listdir(path_to_dir) :
        print(' - '+str(d))

def print_subdirs_dirs_in_dir(path_to_dir):
    """shows the user the possible options of save park files he can swap between"""
    repo_list = []
    for d in os.listdir(path_to_dir) :
        if '.' not in d:
            print(' - '+green+str(d)+white)
            repo_list.append(d)

    return repo_list

#########################################################################
# CUSTOM PARKS                                                          #
#########################################################################

def park_ascii():
    """ascii art for begining og program"""
    print(yellow+
"--------------------------------------------------------------\n"+red+
"  __|  |  /    \ __ __| __|"+white+" __ /"+red+"    _ \  \    _ \  |  /   __| \n"+
"\__ \  . <    _ \   |   _| "+white+"  _ \\"+red+"    __/ _ \     /  . <  \__ \ \n"+
"____/ _|\_\ _/  _\ _|  ___|"+white+" ___/"+red+"   _| _/  _\ _|_\ _|\_\ ____/ \n"+
yellow+"--------------------------------------------------------------"+white)

def set_current_save_parks(newname):
    """sets txt log to be the name of the current skate parks file in the RPCS3 folder"""
    file = repo_parks_path+'CPIRPCS3(DoNotDelete).txt'

    with open(file, 'w') as f:
        f.write(newname)
 
def get_current_save_parks():
    """ retrieve the name of the current skateparks file in the RPCS3 file from the log txt"""
    file = repo_parks_path+'CPIRPCS3(DoNotDelete).txt'

    with open(file, 'r') as f:
       cont = f.read()
    print('\nCurrent Custom Park file in RPCS3:')
    print(' - '+cont)
    return cont

def update_park_save_changes():
    """ performs a backup of any changes to a skate park file in the  RPCS3 folder before it is swapped out """
    current_park_save = get_current_save_parks()
    try:
        osstr = 'cp {}* {}'.format(os_rpcs3_parks_path,os_repo_parks_path+current_park_save+'/')
        os.system(osstr)
        print('Saved any changes made to {} to your repository'.format(current_park_save))
    except:
        print('Updated of {} in Repo FAILED'.format(current_park_save))
        exit(0)

def swap_park_saves():
    """swaps out custom skate park saves in RPCS3 folder via a user input"""
    update_park_save_changes()
    
    print('\nCustom Park files in your repository:')
    choice_list = print_subdirs_dirs_in_dir(repo_parks_path)

    choice = input('\nInput which Park_Saves you want to play (can copy and paste from list above):\n'+input_colour)
    print(white+'')

    if choice == 'exit':
        exit(0)

    if choice in choice_list:
        empty_directory(os_rpcs3_parks_path)
        ostr = "cp {}* {}".format(os_repo_parks_path+choice+'/',os_rpcs3_parks_path)
        os.system(ostr)
        print('{} files copied into RPCS3 folder'.format(choice))
        set_current_save_parks(choice)
        print('--------------------------------------------------------------')
    else:
        print('not a valid input')

#########################################################################
# PLAYER ACCOUNTS                                                       #
#########################################################################

def player_ascii():
    """ """
    print(
yellow+"------------------------------------------------------------------------\n"+red+
"  __|  |  /    \ __ __| __|"+white+" __ /"+red+"    _ \ |       \ \ \  / __|  _ \   __| \n"+
"\__ \  . <    _ \   |   _| "+white+"  _ \\"+red+"    __/ |      _ \ \  /  _|     / \__ \ \n"+
"____/ _|\_\ _/  _\ _|  ___|"+white+" ___/"+red+"   _|  ____| _/  _\ _|  ___| _|_\ ____/ \n"+
yellow+"------------------------------------------------------------------------"+white)

def set_current_save_player(newname):
    """sets txt log to be the name of the current skate parks file in the RPCS3 folder"""
    file = repo_player_path+'CPIRPCS3(DoNotDelete).txt'

    with open(file, 'w') as f:
        f.write(newname)

def get_current_save_player():
    """ retrieve the name of the current skateparks file in the RPCS3 file from the log txt"""
    file = repo_player_path+'CPIRPCS3(DoNotDelete).txt'

    with open(file, 'r') as f:
       cont = f.read()
    print('\nCurrent Player Account in RPCS3:')
    print(' - '+cont)
    return cont

def update_player_save_changes():
    """ performs a backup of any changes to a skate park file in the  RPCS3 folder before it is swapped out """
    current_player_save = get_current_save_player()
    try:
        osstr = 'cp {}* {}'.format(os_rpcs3_player_path,os_repo_player_path+current_player_save+'/')
        os.system(osstr)
        print('Saved any changes made to {} to your repository'.format(current_player_save))
    except:
        print('Updated of {} in Repo FAILED'.format(current_player_save))
        exit(0)

def swap_player_saves():
    """swaps out custom skate park saves in RPCS3 folder via a user input"""
    update_player_save_changes()
    
    print('\nPlayer Accounts in your repository:')
    choice_list = print_subdirs_dirs_in_dir(repo_player_path)

    choice = input('\nInput which Player Account you want to play (can copy and paste from list above):\n'+input_colour)
    print(white+'')

    if choice == 'exit':
        exit(0)

    if choice in choice_list:
        empty_directory(os_rpcs3_player_path)
        ostr = "cp {}* {}".format(os_repo_player_path+choice+'/',os_rpcs3_player_path)
        os.system(ostr)
        print('{} files copied into RPCS3 folder'.format(choice))
        set_current_save_player(choice)
        print('--------------------------------------------------------------')
    else:
        print('not a valid input')


#########################################################################
# REPLAYS                                                               #
#########################################################################

def replay_ascii():
    """ """
    print(
yellow+"------------------------------------------------------------------------\n"+red+
"  __|  |  /    \ __ __| __|"+white+" __ /"+red+"    _ \  __|  _ \ |       \ \ \  /  __| \n"+
"\__ \  . <    _ \   |   _| "+white+"  _ \\"+red+"      /  _|   __/ |      _ \ \  / \__ \ \n"+
"____/ _|\_\ _/  _\ _|  ___|"+white+" ___/"+red+"   _|_\ ___| _|  ____| _/  _\ _|  ____/ \n"+yellow+
"-----------------------------------------------------------------------"+white)

def set_current_save_replay(newname):
    """sets txt log to be the name of the current skate parks file in the RPCS3 folder"""
    file = repo_replay_path+'CPIRPCS3(DoNotDelete).txt'

    with open(file, 'w') as f:
        f.write(newname)

def get_current_save_replay():
    """ retrieve the name of the current skateparks file in the RPCS3 file from the log txt"""
    file = repo_replay_path +'CPIRPCS3(DoNotDelete).txt'

    with open(file, 'r') as f:
       cont = f.read()
    print('\nCurrent Replay files in RPCS3:')
    print(' - '+cont)
    return cont

def update_replay_save_changes():
    """ performs a backup of any changes to a skate park file in the  RPCS3 folder before it is swapped out """
    current_replay_save = get_current_save_replay()
    try:
        osstr = 'cp {}* {}'.format(os_rpcs3_replay_path,os_repo_replay_path+current_replay_save+'/')
        os.system(osstr)
        print('Saved any changes made to {} to your repository'.format(current_replay_save))
    except:
        print('Updated of {} in Repo FAILED'.format(current_replay_save))
        exit(0)

def swap_replay_saves():
    """swaps out custom skate park saves in RPCS3 folder via a user input"""
    update_replay_save_changes()
    
    print('\nReplay files in your repository:')
    choice_list = print_subdirs_dirs_in_dir(repo_replay_path)

    choice = input('\nInput which Replay files you want (can copy and paste from list above):\n'+input_colour)
    print(white+'')

    if choice == 'exit':
        exit(0)

    if choice in choice_list:
        empty_directory(os_rpcs3_replay_path)
        ostr = "cp {}* {}".format(os_repo_replay_path+choice+'/',os_rpcs3_replay_path)
        os.system(ostr)
        print('{} files copied into RPCS3 folder'.format(choice))
        set_current_save_replay(choice)
        print('--------------------------------------------------------------')
    else:
        print('not a valid input')

#########################################################################

def chose_switcher():
    print(
yellow+"--------------------------------------------------------------------\n"+red+
"  __|  |  /    \ __ __| __|"+white+" __ /"+red+"     \  |   _ \  _ \  _ \  __|  _ \ \n"+
"\__ \  . <    _ \   |   _| "+white+"  _ \\"+red+"    |\/ |  (   | |  | |  | _|     / \n"+
"____/ _|\_\ _/  _\ _|  ___|"+white+" ___/"+red+"   _|  _| \___/ ___/ ___/ ___| _|_\ \n"+
yellow+"--------------------------------------------------------------------"+white)

    print('\nDirectories in your repository:')
    print_subdirs_dirs_in_dir(repo_path)
    choice = input('\nInput the directory name you want to switch: (can copy and paste from list above):\n'+input_colour)
    print(''+white)

    if choice == 'exit':
        exit(0)

    if choice == 'Replays':
        replay_ascii()
        swap_replay_saves()
        
    if choice == 'Player_Accounts':
        player_ascii()
        swap_player_saves()
        
    if choice == 'Custom_Parks':
        park_ascii()
        swap_park_saves()

#########################################################################

# run this
chose_switcher()