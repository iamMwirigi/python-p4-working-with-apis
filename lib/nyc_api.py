import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.json()  # Use response.json() to directly parse the response content as JSON

    def program_school(self):
        programs_list = []
        programs = self.get_programs()

        for program in programs:
            print(program)  # Print the program to understand its structure
            programs_list.append(program["agency"])

        return programs_list

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)
