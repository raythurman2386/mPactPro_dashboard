from openpyxl import load_workbook
from utils import correct_date

# This is the file that will be corrected
# masterFile = sys.argv[1]

# This is the file that will be getting corrected
# file = load_workbook(filename=masterFile, data_only=True)

# case_sheet = file.active

# This will be a new workbook that we save our corrected values to
workbook = load_workbook(filename='SJHP.xlsx', data_only=True)
new_wb = load_workbook(filename='SJHP_modified.xlsx')
sheet = workbook['Case']
new_sheet = new_wb.create_sheet('Case')

# Create a hashtable to keep track of cases
cases = {}
case_id = 1

template_header = ['CaseType', 'ClientID', 'AssignedCounselor', 'AssignedCoach', 'AssignedLoanOfficer',
                   'HomePurchaseClientType', 'HomePurchaseClientFacilitation', 'ClientCaseStatus',
                   'ClientDisclosureFormPresent', 'ClientFirstName', 'ClientMiddleName', 'ClientLastName',
                   'DateofBirth', 'CreditScoreBefore', 'CreditScoreAfter', 'IntakeDate', 'SubsidizedHousingAssistance',
                   'PrimaryEmployer', 'EmployerAddress', 'SecondaryEmployer', 'SecondaryEmployerAddress',
                   'HomeOwnerLastThreeYears', 'RealEstateAgent', 'LastContactDate', 'LongTermClientDate',
                   'ShortTermClientDate', 'NearMortgageReadyDate', 'MortgageReadyDate', 'InFinancingDate',
                   'ActiveReportDateHUD', 'CompletedDate', 'DeniedDate', 'InactiveDate', 'PrivacyOptOut',
                   'RentalResolution', 'LMPackageStatus', 'MMSubjectPropertyPresent', 'MMLienInfoPresent'
                                                                                      'LevelOneDate', 'LevelTwoDate',
                   'SeekingShelterResolution', 'YearsAtCurrentAddress'
                                               'SeniorAsHoH', 'HomeOwnerResolutions', 'HomePurchaseResolution']

# Append our proper header to the new worksheet
new_sheet.append(template_header)
new_sheet.title = 'Case'

# Fill our clients hash table with every client
for row in sheet.iter_rows(min_row=2, values_only=True, min_col=2):
    # TODO: IF THE HEADER COLUMNS ARE IN DIFFERENT LOCATIONS, UPDATE THE VALUES FOR THE CLIENT!!!!!
    case = {
        'case_type': row[0],
        'client_id': row[1],
        'assigned_counselor': row[2],
        'assigned_coach': row[3],
        'assigned_loan_officer': None,
        'home_purchase_client_type': None,
        'home_purchase_client_facilitation': None,
        'client_case_status': row[7],
        'client_disclosure_form_present': None,
        'client_first_name': row[9],
        'client_middle_name': None,
        'client_last_name': row[11],
        'date_of_birth': correct_date(row[12]),
        'credit_score_before': None,
        'credit_score_after': None,
        'intake_date': correct_date(row[15]),
        'subsidized_housing_assistance': None,
        'primary_employer': None,
        'employer_address': None,
        'secondary_employer': None,
        'secondary_employer_address': None,
        'home_owner_last_three_years': None,
        'real_estate_agent': None,
        'last_contact_date': None,
        'long_term_client_date': None,
        'short_term_client_date': None,
        'near_mortgage_ready_date': None,
        'mortgage_ready_date': None,
        'in_financing_date': None,
        'active_report_date_hud': None,
        'completed_date': None,
        'denied_date': None,
        'inactive_date': None,
        'privacy_opt_out': None,
        'rental_resolution': None,
        'lm_package_status': None,
        'mm_subject_property_present': None,
        'mm_lien_info_present': None,
        'level_one_date': None,
        'level_two_date': None,
        'seeking_shelter_resolution': None,
        'years_at_current_address': None,
        'senior_as_hoh': None,
        'home_owner_resolutions': None,
        'home_purchase_resolution': None
    }
    # Save the client by the ID for easy Access
    cases[case_id] = case
    case_id += 1

# Add each client to the new spreadsheet
for case in cases:
    case_list = [v for k, v in cases[case].items()]

    # # TODO: Fix client data to match our requirements
    # corrected_case = fix_case_data(case_list)

    # Add corrected client to the worksheet
    new_sheet.append(case_list)

# Save the worksheet when all is complete
new_wb.save(filename='SJHP_modified_cases.xlsx')
