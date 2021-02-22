from utils import options

def fix_data(client):
  # Correct client case status index 1
  if client[1] == 'In-Process':
    client[1] = options['status'][1]
  elif client[1] == 'Fulfilled':
    client[1] = options['status'][2]
  elif client[1] == 'Suspended':
    client[1] = options['status'][4]

  # Correct Client Program Enrollment index 2
  if client[2] == 'Financial Capability Counseling':
    client[2] = options['ClientProgramEnrollment'][4]

  # Correct Gender if needed index 8
  if client[8] == 'M':
    client[8] = options['gender'][0]
  elif client[8] == 'Female':
    client[8] = options['gender'][1]

  # Correct Race index 9
  if client[9] == 'c. c. Black or African American or African American':
    client[9] = options['race']['c']

  elif client[9] == 'European' or client[9] == 'Cuban' or client[9] == 'Central America' or \
    client[9] == 'Colombian' or client[9] == 'Puerto Rican' or client[9] == 'South American':
    client[9] = options['race']['j']

  elif client[9] == None:
    client[9] = options['race']['k']

  # Correct Ethnicity index 10
  if client[10] == 'a.  Hispanic':
    client[10] = options['ethnicity']['a']
  elif client[10] == 'b.  Not Hispanic':
    client[10] = options['ethnicity']['b']
  else:
    client[10] = options['ethnicity']['c']


  # Correct Income Band index 17
  if client[17] == '<30%' or client[17] == '1':
    client[17] = options['incomeBand']['a']
  elif client[17] == '30-49%' or client[17] == '2':
    client[17] = options['incomeBand']['b']
  elif client[17] == '50-79%' or client[17] == '3':
    client[17] = options['incomeBand']['e']
  elif client[17] == '80-100%' or client[17] == '4':
    client[17] = options['incomeBand']['d']
  elif client[17] == '100%-120%' or client[17] == '>120%' or client[17] == '5':
    client[17] = options['incomeBand']['e']
  elif client[17] == '' or client[17] == '6':
    client[17] = options['incomeBand']['f']

  # Correct Rural Status index 27
  if client[27] == 'a. Household lives in a rural area':
    client[27] = options['ruralStatus'][0]
  elif client[27] == 'b. Household does not live in a rural area':
    client[27] = options['ruralStatus'][1]
  else:
    client[27] = options['ruralStatus'][2]

  # Correct English Proficiency index 28
  if client[28] == 'Is not English proficient':
    client[28] = options['englishProficiency'][0]
  elif client[28] == 'b . Household is not Limited English Proficient':
    client[28] = options['englishProficiency'][1]
  else:
    client[28] = options['englishProficiency'][2]

  # Correct Marital Status index 64
  if client[64] == 'Single':
    client[64] = options['maritalStatus']['a']
  elif client[64] == 'Married':
    client[64] = options['maritalStatus']['b']
  elif client[64] == 'Divorced':
    client[64] = options['maritalStatus']['c']
  elif client[64] == 'Widowed':
    client[64] = options['maritalStatus']['e']
  else:
    client[64] = None

  # Correct Household Type index 66

  # Correct Education index 67
  if client[67] == 'Some 4. Bachelors Degree' or client[67] == 'Junior 4. Bachelors Degree':
    client[67] = options['education']['d']
  elif client[67] == 'Junior High School':
    client[67] = options['education']['a']
  elif client[67] == 'Graduate School' or client[67] == 'Vocational' or client[67] == 'Primary':
    client[67] = options['education']['g']


  # Correct Referral Source index 68

  # Return the client with all corrections
  return client
