from src.main_service import MainService
from src.log_service import LogService

import os

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   
#    The following RPA is a didactic model based on real projects.
#    The robot is responsible for opening the files, analyzing,
#    renaming, saving to another destination and sending the results
#    to an API.
#    Can be used in Docker, scheduled or triggered by the user. 
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print("\n - - - - - - - - - - - - - - - - - - - -")
print(" - Starting extraction of weekly reports")
print("\n - User:", os.getlogin())

LogService().send_api_log(True, "Starting extraction. user: " + os.getlogin())

if MainService().start_execution():
    print(" - Extraction completed successfully")
    LogService().send_api_log(True, "Sucessfully completed")
else:
    print(" - Extraction terminated with failure")
    LogService().send_api_log(False, "Terminated with failure")


print("\n - Finish extraction of weekly reports")
print(" - - - - - - - - - - - - - - - - - - - -")