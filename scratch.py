import numpy as np
import sys
import os
import fileinput as fi
#from BlueSky import main
# print(sys.argv)
#sys.argv.append("--headless")
#sys.arg,"--scenfile","\experimental\Trajectories.scn"])
#main()

# Scenario batch file
global scenario_manager, settings_config, dt
scenario_manager = "F:\Documents\Google Drive\Thesis 2018\BlueSky\scenario\experimental\\Trajectories-batch.scn"
settings_config = "F:\Documents\Google Drive\Thesis 2018\BlueSky\settings.cfg"
dt = '0.50' # format '#.##'
set_of_dt = ['0.05', '0.10', '0.20', '0.50', '1.00']
list_ensemble = list(range(1,5))

# Switches the ensemble in the scenario manager and adapts the name using the ensemble # and global dt
def replace_ensemble(ensemble):
    f = open(scenario_manager, 'r')
    filedata = list(f.read())
    f.close()
    ensemble = str(ensemble)

    if len(ensemble) < 2:
        filedata[63]    = str(0)
        filedata[64]    = ensemble[0]
        filedata[4135]  = str(0)
        filedata[4136]  = ensemble[0]
    else:
        filedata[63]    = ensemble[0]
        filedata[64]    = ensemble[1]
        filedata[4135]  = ensemble[0]
        filedata[4136]  = ensemble[1]

    filedata[4141]  = dt[0]
    filedata[4142]  = dt[1]
    filedata[4143]  = dt[2]
    filedata[4144]  = dt[3]

    filedata2 = str("".join(filedata))
    f = open(scenario_manager, 'w')
    f.write(filedata2)
    f.close()
    pass


# Changes the timestep in the settings config of BlueSky using the provided timestep
# Keep in mind that the savefile doesn't change its name, unless the timestep is set into the global variable dt
def set_dt(timestep):
    f = open(settings_config, 'r')
    filedata = list(f.read())
    f.close()

    filedata[1030] = timestep[0]
    filedata[1031] = timestep[1]
    filedata[1032] = timestep[2]
    filedata[1033] = timestep[3]

    filedata2 = str("".join(filedata))
    f = open(settings_config, 'w')
    f.write(filedata2)
    f.close()
    pass

# This functions replaces the dt in the settings.cfg with the globally defined dt
def replace_dt():
    f = open(settings_config, 'r')
    filedata = list(f.read())
    f.close()

    filedata[1030] = dt[0]
    filedata[1031] = dt[1]
    filedata[1032] = dt[2]
    filedata[1033] = dt[3]

    filedata2 = str("".join(filedata))
    f = open(settings_config, 'w')
    f.write(filedata2)
    f.close()
    pass

# Run a simulation of BlueSky using the desktop path
def run_bluesky_desktop():
    os.system("call C:\Programs\Tools\Anaconda\Program\Scripts\\activate.bat && \
                    cd C:\Documents\BlueSky && conda activate py36 && python BlueSky.py")

# Run a simulation of BlueSky using the laptop path
def run_bluesky_laptop():
    os.system("call I:\Programs\Anaconda\Program\Scripts\\activate.bat && \
                    cd I:\Documents\Google Drive\Thesis 2018\BlueSky Git2 && python BlueSky.py")

# assign the timestep and run the simulations X times
for i in set_of_dt:
    dt = i
    # replace_dt()
    for j in list_ensemble:
        # replace_ensemble(i)
        run_bluesky_laptop()

# os.system("call C:\Programs\Tools\Anaconda\Program\Scripts\\activate.bat && \
#             cd C:\Documents\BlueSky && conda activate py36 && python BlueSky.py")

#
# os.system("call C:\Programs\Tools\Anaconda\Program\Scripts\\activate.bat && \
#               cd C:\Documents\BlueSky && conda activate py36 && python BlueSky.py")

# os.system("call C:\Programs\Tools\Anaconda\Program\Scripts\\activate.bat && \
#            cd C:\Documents\BlueSky && conda activate py36 && \
#              python BlueSky.py --headless --scenfile \experimental\Trajectories.scn")
# #sys.argv.append('--headless')
#\BlueSky.py
#'--config-file'
#\experimental\Trajectories.scn

#"IC C:\Documents\BlueSky\scenario\experimental\Trajectories.scn"

