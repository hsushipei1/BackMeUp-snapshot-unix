#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-

"""
BackMeUp Project

o Version：
o Author: HsuShiPei(徐世裴) (hsushipei1@gmail.com)
o Features: 
o Program Flow Chart:
o Update Record:
"""

##### Import modules 
from os import system, path, getcwd
from clear_console import clear_console
# Part 0
from project_info import ProjInfo
from author_info import AuthrInfo

# Part 1
from backup_plan_viewer import existn_database_finder, \
								user_input_plan_name
from choose_mode import immediate_or_scheduled_backup,\
                        path_to_backup,\
					    backup_location,\
                        entire_or_extension_backup
from configure import configure_scheduled
from full_backup import locate_all_file_multi_dir
from selected_backup import extens_input,\
							find_multi_type_in_multi_dir 
from keep_tree import keep_tree_ornot
from backup_tag import backup_tagging,\
					   add_tag_2_backupLocation

from verify_inputs import verify_user_inputs
from start_copy_via_database import copying_keep_tree,\
									copying_dont_keep_tree

##### Part 0: Welcome message, project and author info
# Clear the terminal screen at startup
clear_console()
# Show the project and author info 
ProjInfo()
AuthrInfo()
# Brief intro to BackMeUp?

##### Part 1: Backup configuration
## Backup Plan Viewer
database_extension = ".BakDataBase"    # will use this var below

# Obtain the existing name of database
(preex_database_name_list, existn_DatabaseCheck) = \
	existn_database_finder(database_extension)

# Obtain new name for current backup plan
new_name_backup_plan = \
user_input_plan_name(preex_database_name_list, existn_DatabaseCheck)

# Immediate or Schduled backup(value returned)
immed_or_schedu = immediate_or_scheduled_backup()
if immed_or_schedu == "1": # immediate backup, continue
	pass
elif immed_or_schedu == "2": # schedule backup, jump to configure
	configure_scheduled()

# Path to directories that user wants to backup
# "path_input"=>  A LIST containing paths in UNICODE type.
path_input = path_to_backup()

# Choose backup entire dir or select extension(number is returned)
# The name of database is given here.
backup_style = entire_or_extension_backup()
if backup_style == "1": # 1 go to full backup
	database_name = new_name_backup_plan+database_extension
	locate_all_file_multi_dir(path_input, database_name)
	exten_input = 0  # "0" is to tell "verify_user_inputs" user chose full
elif backup_style == "2": # 2 go to selected backup
	database_name = new_name_backup_plan+database_extension
	exten_input = extens_input()
	find_multi_type_in_multi_dir(path_input,exten_input, database_name)

# keep dir tree(relative path)?(value returned)
keep_tree_value = keep_tree_ornot()

# Backup location
backup_loc = backup_location()

# Ask user if he/she needs a backup tag. 
backup_tag = backup_tagging()
new_backup_loc = add_tag_2_backupLocation(backup_tag, backup_loc)

##### Part 2: Verify user inputs
verify_user_inputs(new_name_backup_plan, immed_or_schedu,\
path_input, backup_loc,	backup_style,exten_input,\
keep_tree_value, backup_tag)

##### Part 3: Start backup(copying): keep tree or not
# Start copying. read data base and new backup path
# decide to preserve directory tree or not
if keep_tree_value == "1": # keep dir tree
	copying_keep_tree(database_name, new_backup_loc)
elif keep_tree_value == "2": # do not keep dir tree
    copying_dont_keep_tree(database_name, new_backup_loc)


exit("============= FINISH COPYING ================")




