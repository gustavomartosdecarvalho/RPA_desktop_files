from src.handling_files_service import HandlingFilesService
from src.log_service import LogService

import os

class MainService:
    def __init__(self):
        # > Declare classes
        self.handling_files = HandlingFilesService()
        self.log_service = LogService()
        # > Path variables 
        #   for this example, relative path will be used.
        #   But you can use the full path (/home/.../[destination folder]) or (C:/.../[destination folder])
        self.destination_path = os.path.relpath('repository/Destination')
        self.name_file_a = 'ReportsTeam_A'
        self.name_file_b = 'Reports_B'

    # >
    # > Main Method
    # >
    def start_execution(self): 
        # > Message variables
        topic_print = ' - '
        success_analysis = 'Success in analyzing the report  '
        failed_analysis =  'Failed to analyze the report '
        success_copy = 'Success to copy '
        failed_copy =  'Failed to copy '

        # > Analysis of the TeamA report 
        if self.analysis_team_a_report():
            print(topic_print + success_analysis + self.name_file_a)
            self.log_service.send_api_log(True, success_analysis + self.name_file_a)
        else:
            print(topic_print + failed_analysis + self.name_file_a)
            self.log_service.send_api_log(False, failed_analysis + self.name_file_a)
            return False

        # > Analysis of the TeamB report 
        if self.analysis_team_b_report():
            print(topic_print + success_analysis + self.name_file_b)
            self.log_service.send_api_log(True, success_analysis + self.name_file_b)
        else:
            print(topic_print + failed_analysis + self.name_file_b)
            self.log_service.send_api_log(False, failed_analysis + self.name_file_b)
            return False

        # > If everthing is ok return true
        return True

    # >
    # > Rules Methods
    # >
    def analysis_team_a_report(self): 
        # > Path variables 
        team_a_path = os.path.relpath('repository/Team_A')
        extension = 'txt'
        destination = self.destination_path + '/' +  self.name_file_a + self.handling_files.complement_datetime_name_yyyymmdd_hhmm() + '.' + extension
        # > Make sure the file exists
        origin = team_a_path + '/' + self.name_file_a + '.' + extension
        
        # > Analyze the file

        # > Copy file 
        if self.handling_files.copy_file(origin, destination):
            return True
        else:
            return False

    def analysis_team_b_report(self): 
        # > Path variables 
        team_b_path = os.path.relpath('repository/Team_B')
        extension = 'txt'
        destination = self.destination_path + '/' +  self.name_file_b + self.handling_files.complement_datetime_name_yyyymmdd_hhmm() + '.' + extension
        # > Find the newest version of the name_file_b in the path team_b_path
        origin = self.handling_files.find_latest_version_in_folder(self.name_file_b, extension, team_b_path)
        if not origin:
            return False 
        
        # > Analyze the file

        # > Copy file 
        if self.handling_files.copy_file(origin, destination):
            return True
        else:
            return False

