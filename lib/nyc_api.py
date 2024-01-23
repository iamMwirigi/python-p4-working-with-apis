import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.content

    def program_school(self):
        programs_list = []
        
        # Load the JSON response into a Python object
        programs = json.loads(self.get_programs())

        # Ensure that the response is a list of dictionaries
        if isinstance(programs, list):
            for program in programs:
                # Check if "agency" is present in the dictionary before accessing it
                if "agency" in program:
                    programs_list.append(program["agency"])

        return programs_list

# Create an instance of GetPrograms
programs = GetPrograms()

# Get the list of programs
programs_schools = programs.program_school()

# Print the unique school names
for school in set(programs_schools):
    print(school)
