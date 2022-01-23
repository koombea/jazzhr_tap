






























record={
    "id": applicant['id'], 
    'first_name': applicant["first_name"],
    'last_name': applicant["last_name"],
    'email': applicant["email"],
    'address': applicant["address"],
    'location': applicant["location"],
    'linkedin_url': applicant["linkedin_url"],
    'eeo_gender': to_int(applicant["eeo_gender"]),
    'eeo_race': to_int(applicant["eeo_race"]),
    'eeo_disability': to_int(applicant["eeo_disability"]),
    'website': applicant["website"],
    'desired_salary': to_float(applicant["desired_salary"]),
    'desired_start_date': applicant["desired_start_date"],
    'languages': applicant["languages"],
    'wmyu': applicant["wmyu"],
    'has_driver_license': applicant["has_driver_license"],
    'willing_to_relocate': applicant["willing_to_relocate"],
    'citizenship_status': applicant["citizenship_status"],
    'education_level': applicant["education_level"],
    'has_cdl': applicant["has_cdl"],
    'over_18': applicant["over_18"],
    'can_work_weekends': applicant["can_work_weekends"],
    'can_work_evenings': applicant["can_work_evenings"],
    'can_work_overtime': applicant["can_work_overtime"],
    'has_felony': applicant["has_felony"],
    'felony_explanation': applicant["felony_explanation"],
    'twitter_username': applicant["twitter_username"],
    'college_gpa': applicant["college_gpa"],
    'college': applicant["college"],
    'references': applicant["references"],
    'notes': applicant["notes"],
    'comments_count': to_int(applicant["comments_count"]),
    'source': applicant["source"],
    'recruiter_id': applicant["recruiter_id"],
    'eeoc_veteran': to_int(applicant["eeoc_veteran"]),
    'eeoc_disability': to_int(applicant["eeoc_disability"]),
    'eeoc_disability_signature': applicant["eeoc_disability_signature"],
    'eeoc_disability_date': applicant["eeoc_disability_date"],
    'apply_date': applicant["apply_date"]