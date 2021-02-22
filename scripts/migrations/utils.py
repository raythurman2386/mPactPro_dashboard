import csv
from datetime import date, datetime
# Helper fn to get length of files
def get_length(i):
    count = 0
    with open(i) as f:
        r = csv.reader(f)

        for row in r:
            count += 1

    return count


def validate_dates(d):
    return datetime.strptime(d, '%m/%d/%y').strftime('%m/%d/%y')



options = {
    'ClientCaseStatus': ['New Intake', 'Active', 'Completed', 'Withdrew', 'Inactive', 'Completed - Education Only'],
    'ClientProgramEnrollment': ['Home Purchase', 'Mortgage Modification', 'Homelessness Assistance', 'Rental Topics', 'Homeowner Services', 'Education Services'],
    'gender': ['Male', 'Female'],
    'race': {
        'a': 'a. American Indian/Alaskan Native',
        'b': 'b. Asian',
        'c': 'c. Black or African American',
        'd': 'd. Native Hawaiian or Other Pacific Islander',
        'e': 'e. White',
        'f': 'f. American Indian or Alaska Native and White',
        'g': 'g. Asian and White',
        'h': 'h. Black or African American and White',
        'i': 'i. American Indian or Alaska Native and Black or African American',
        'j': 'j. Other multiple race',
        'k': 'k. Chose not to respond'},
    'ethnicity': {
        'a': 'a. Hispanic',
        'b': 'b. Not Hispanic',
        'c': 'c. Chose not to respond'},
    'incomeBand': {
        'a': '1. Below 30% of AMI',
        'b': '2. 30% - 49% of AMI',
        'c': '3. 50% - 79% of AMI',
        'd': '4. 80% - 100% of AMI',
        'e': '5. 101% - 120% of AMI',
        'f': '6. Chose not to respond'
    },
    'ruralStatus': ['a. Household lives in a rural area', 'b. Household does not live in a rural area', 'c. Chose not to respond'],
    'englishProficiency': ['a. Household is Limited English Proficient', 'b . Household is not Limited English Proficient', 'c. Chose not to respond'],
    'maritalStatus': {
        'a': 'Single',
        'b': 'Married',
        'c': 'Divorced',
        'd': 'Seperated',
        'e': 'Widowed',
    },
    'householdType': {
        'a': '1. Female headed single parent household',
        'b': '2. Male headed single parent household',
        'c': '3. Single adult',
        'd': '4. Two or more unrelated adults',
        'e': '5. Married with children',
        'f': '6. Married without children',
        'g': '7. Other',
    },
    'referralSource': {
        'a': '1. Print Advertisement',
        'b': '2. Bank',
        'c': '3. Government',
        'd': '4. TV',
        'e': '5. Realtor',
        'f': '6. Staff/Board Member',
        'g': '7. Walk-in',
        'h': '8. Friend',
        'i': '9. Radio',
        'j': '10. Newspaper Article',
        'k': '11. Other',
    }
}
