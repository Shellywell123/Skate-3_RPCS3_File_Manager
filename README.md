# RPCS3-Skate3_File_Manager

Program being build as an extended version of my other repoistory [RPCS3_Skate3_Custom_Parks_Swapper]{https://github.com/Shellywell123/RPCS3_Skate3_Custom_Parks_Swapper}. Still under development. Written in python to automate swapping players, replays and custom park files in the RPCS3 emulator for skate 3. You should set the paths in the python file to be relative to your own machine and use the Repo_Template as a Template for how structure your directories containing files outside of RPCS3. I have also added a file showing my own repo structure in 'tree.txt. I will eventually write '.md' files to explain the setup in more detail.\
\
My understading thus far is, that the dir paths in RPCS3 are for:

 - ...BLES00760-ALIAS_SKATER/ for your player account
 - ...BLES00760-REPLY_SKATER/ for replays
 - ...BLES00760-SPARK_SKATER/ for custom parks
 - ...BLES00760-CFOTO_SKATER/ for photos
 - ...BLES00760-PHOTO_SKATER/ for photos
\
and that replays can be used for charcter glitches, customparks can be used to get other parks by trading save files and player accounts store your players information and settings i.e your skaters prefs and story progress.\
\
The program is written for a linux based command line (I use WSL), it uses a mixture of python 3 and os terminal commands to move files between a locally saved repository of different save files and the directories within the RPCS3 emulator.