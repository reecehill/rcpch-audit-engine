"""
## Update Tests

# Epilepsy12Users
    [x] Assert an Audit Centre Administrator CANNOT update users inside own Trust
    [x] Assert an Audit Centre Administrator CANNOT update users from outside own Trust 
    [x] Assert an audit centre clinician CANNOT update users inside own Trust
    [x] Assert an audit centre clinician CANNOT update users from outside own Trust 
    [x] Assert an Audit Centre Lead Clinician CANNOT update users outside own Trust

    [x] Assert an Audit Centre Lead Clinician can update users inside own Trust
    [x] Assert RCPCH Audit Team can update users in any trust
    [x] Assert Clinical Audit Team can update users in own trust
    [x] Assert Clinical Audit Team can update users in different trusts

# Cases
    [x] Assert an Audit Centre Administrator CANNOT update patient records outside own Trust
    [x] Assert an audit centre clinician CANNOT update patient records outside own Trust
    [x] Assert an Audit Centre Lead Clinician CANNOT update patient records outside own Trust

    [x] Assert an Audit Centre Administrator CAN update patient records inside own Trust
    [x] Assert an audit centre clinician can update patient records within own organisation
    [x] Assert an Audit Centre Lead Clinician can update patient records within own Trust
    [x] Assert RCPCH Audit Team can update patient records within an organisation
    [x] Assert Clinical Audit Team can update patient records within an organisation

# First Paediatric Assessment
    for field in fields: [
        'first_paediatric_assessment_in_acute_or_nonacute_setting',
        'has_number_of_episodes_since_the_first_been_documented',
        'general_examination_performed',
        'neurological_examination_performed',
        'developmental_learning_or_schooling_problems',
        'behavioural_or_emotional_problems'
    ]
    [x] Assert an Audit Centre Administrator cannot change 'field' inside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Administrator cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    
    [x] Assert an Audit Centre Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Lead Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can change 'field' - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can change 'field' - response.status_code == HTTPStatus.OK

# Epilepsy Context
    for field in fields: [
        'previous_febrile_seizure',                                 single_choice_multiple_toggle_button
        'previous_acute_symptomatic_seizure',                       single_choice_multiple_toggle_button
        'is_there_a_family_history_of_epilepsy',                    toggle_button
        'previous_neonatal_seizures',                               single_choice_multiple_toggle_button
        'were_any_of_the_epileptic_seizures_convulsive',            toggle_button
        'experienced_prolonged_generalized_convulsive_seizures',    single_choice_multiple_toggle_button
        'experienced_prolonged_focal_seizures',                     single_choice_multiple_toggle_button
        'diagnosis_of_epilepsy_withdrawn',                          toggle_button
    ]

    [x] Assert an Audit Centre Administrator cannot change 'field' inside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Administrator cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    
    [x] Assert an Audit Centre Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Lead Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can change 'field' - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can change 'field' - response.status_code == HTTPStatus.OK


# Multiaxial Diagnosis
    for field in fields: [
        'epilepsy_cause_known',                                         toggle_button
        'epilepsy_cause',                                               select
        'epilepsy_cause_categories',                                    multiple_choice_multiple_toggle_button
        'relevant_impairments_behavioural_educational',                 toggle_button
        'mental_health_screen',                                         toggle_button
        'mental_health_issue_identified',                               toggle_button
        'mental_health_issue',                                          single_choice_multiple_toggle_button
        'global_developmental_delay_or_learning_difficulties',          toggle_button
        'global_developmental_delay_or_learning_difficulties_severity', single_choice_multiple_toggle_button
        'autistic_spectrum_disorder',                                   toggle_button
    ]

    [x] Assert an Audit Centre Administrator cannot change 'field' inside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Administrator cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    
    [x] Assert an Audit Centre Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Lead Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can change 'field' - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can change 'field' - response.status_code == HTTPStatus.OK

# Episode
    for field in fields: [
        seizure_onset_date',                                                date_field
        seizure_onset_date_confidence',                                     single_choice_multiple_toggle_button
        episode_definition',                                                select
        has_description_of_the_episode_or_episodes_been_gathered',          toggle_button
        edit_description',                                                  string - updated in view function
        delete_description_keyword',                                        Keyword id - updated in view function
        epilepsy_or_nonepilepsy_status',                                    single_choice_multiple_toggle_button
        epileptic_seizure_onset_type',                                      single_choice_multiple_toggle_button
        focal_onset_epilepsy_checked_changed',                              updated in view function
        epileptic_generalised_onset',                                       single_choice_multiple_toggle_button
        nonepilepsy_generalised_onset',                                     single_choice_multiple_toggle_button
        nonepileptic_seizure_type',                                         select
        nonepileptic_seizure_subtype',                                      select
    ]
    [x] Assert an Audit Centre Administrator cannot change 'field' inside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Administrator cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
    
    [x] Assert an Audit Centre Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Lead Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can change 'field' - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can change 'field' - response.status_code == HTTPStatus.OK

# Comorbidity
    for field in fields: [
        'comorbidity_diagnosis_date',                                       date_field
        'comorbidity_diagnosis',                                            select
    ]
[ ] Assert an Audit Centre Administrator can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Administrator cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Lead Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Lead Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert RCPCH Audit Team can change 'field' - response.status_code == HTTPStatus.OK

# Assessment
for field in fields: [
    'consultant_paediatrician_referral_made',
    'consultant_paediatrician_referral_date',
    'consultant_paediatrician_input_date',
    'general_paediatric_centre',
    'edit_general_paediatric_centre',
    'update_general_paediatric_centre_pressed',
    'paediatric_neurologist_referral_made',
    'paediatric_neurologist_referral_date',
    'paediatric_neurologist_input_date',
    'paediatric_neurology_centre',
    'edit_paediatric_neurology_centre',
    'update_paediatric_neurology_centre_pressed',
    'childrens_epilepsy_surgical_service_referral_criteria_met',
    'childrens_epilepsy_surgical_service_referral_made',
    'childrens_epilepsy_surgical_service_referral_date',
    'childrens_epilepsy_surgical_service_input_date',
    'epilepsy_surgery_centre',
    'edit_epilepsy_surgery_centre',
    'update_epilepsy_surgery_centre_pressed',
    'delete_epilepsy_surgery_centre',
    'epilepsy_specialist_nurse_referral_made',
    'epilepsy_specialist_nurse_referral_date',
    'epilepsy_specialist_nurse_input_date',
]
[ ] Assert an Audit Centre Administrator can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Administrator cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Lead Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Lead Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert RCPCH Audit Team can change 'field' - response.status_code == HTTPStatus.OK

# Investigations
for field in fields: [
    'eeg_indicated',
    'eeg_request_date',
    'eeg_performed_date',
    'eeg_declined',
    'twelve_lead_ecg_status',
    'ct_head_scan_status',
    'mri_indicated',
    'mri_brain_requested_date',
    'mri_brain_reported_date',
    'mri_brain_declined',
]
[ ] Assert an Audit Centre Administrator can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Administrator cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Lead Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Lead Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert RCPCH Audit Team can change 'field' - response.status_code == HTTPStatus.OK

# Management
for field in fields: [
    'individualised_care_plan_in_place',
    'individualised_care_plan_date',
    'individualised_care_plan_has_parent_carer_child_agreement',
    'individualised_care_plan_includes_service_contact_details',
    'individualised_care_plan_include_first_aid',
    'individualised_care_plan_parental_prolonged_seizure_care',
    'individualised_care_plan_includes_general_participation_risk',
    'individualised_care_plan_addresses_water_safety',
    'individualised_care_plan_addresses_sudep',
    'individualised_care_plan_includes_ehcp',
    'has_individualised_care_plan_been_updated_in_the_last_year',
    'has_been_referred_for_mental_health_support',
    'has_support_for_mental_health_support',
]
[ ] Assert an Audit Centre Administrator can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Administrator cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Lead Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Lead Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert RCPCH Audit Team can change 'field' - response.status_code == HTTPStatus.OK

# Antiepilepsy Medicine
for field in fields: [
    'has_an_aed_been_given',
    'edit_antiepilepsy_medicine',
    'medicine_id',
    'antiepilepsy_medicine_start_date',
    'antiepilepsy_medicine_add_stop_date',
    'antiepilepsy_medicine_remove_stop_date',
    'antiepilepsy_medicine_stop_date',
    'antiepilepsy_medicine_risk_discussed',
    'is_a_pregnancy_prevention_programme_in_place',
    'has_a_valproate_annual_risk_acknowledgement_form_been_completed',
    'has_rescue_medication_been_prescribed',
]
[ ] Assert an Audit Centre Administrator can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Administrator cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert an Audit Centre Lead Clinician can change 'field' inside own Trust - response.status_code == HTTPStatus.OK
[ ] Assert an Audit Centre Lead Clinician cannot change 'field' inside a different Trust - response.status_code == HTTPStatus.FORBIDDEN
[ ] Assert RCPCH Audit Team can change 'field' - response.status_code == HTTPStatus.OK


"""
# python imports
import pytest
import json
from http import HTTPStatus
from datetime import date

# django imports
from django.urls import reverse
from django.contrib.auth.models import Group

# E12 imports
from epilepsy12.models import (
    Epilepsy12User,
    Organisation,
    Case,
    Episode,
    Keyword,
    EpilepsyCauseEntity,
    MultiaxialDiagnosis,
    ComorbidityEntity,
    Comorbidity,
)
from epilepsy12.tests.UserDataClasses import (
    test_user_audit_centre_administrator_data,
    test_user_audit_centre_clinician_data,
    test_user_audit_centre_lead_clinician_data,
    test_user_clinicial_audit_team_data,
    test_user_rcpch_audit_team_data,
)
from epilepsy12.tests.factories import E12UserFactory


@pytest.mark.django_db
def test_users_update_users_forbidden(
    client,
    seed_groups_fixture,
    seed_users_fixture,
    seed_cases_fixture,
):
    """
    Simulating different E12 Users attempting to update users in Epilepsy12

    Assert these users cannot change Epilepsy12Users
    """

    # set up constants

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )

    # ADDENBROOKE'S
    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ODSCode="RGT01",
        ParentOrganisation_ODSCode="RGT",
    )

    USER_FROM_DIFFERENT_ORG = E12UserFactory(
        email=f"{DIFF_TRUST_DIFF_ORGANISATION}_ADMINISTRATOR@email.com",
        first_name=f"{DIFF_TRUST_DIFF_ORGANISATION}_ADMINISTRATOR",
        role=test_user_audit_centre_administrator_data.role,
        # Assign flags based on user role
        is_active=test_user_audit_centre_administrator_data.is_active,
        is_staff=test_user_audit_centre_administrator_data.is_staff,
        is_rcpch_audit_team_member=test_user_audit_centre_administrator_data.is_rcpch_audit_team_member,
        is_rcpch_staff=test_user_audit_centre_administrator_data.is_rcpch_staff,
        organisation_employer=TEST_USER_ORGANISATION,
        groups=[
            Group.objects.get(name=test_user_audit_centre_administrator_data.group_name)
        ],
    )

    users = Epilepsy12User.objects.all().exclude(
        first_name__in=[
            "RCPCH_AUDIT_TEAM",
            "CLINICAL_AUDIT_TEAM",
            f"{DIFF_TRUST_DIFF_ORGANISATION}_ADMINISTRATOR",
        ]
    )

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        response = client.get(
            reverse(
                "edit_epilepsy12_user",
                kwargs={
                    "organisation_id": DIFF_TRUST_DIFF_ORGANISATION.id,
                    "epilepsy12_user_id": USER_FROM_DIFFERENT_ORG.id,
                },
            )
        )

        assert (
            response.status_code == HTTPStatus.FORBIDDEN
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update user {USER_FROM_DIFFERENT_ORG} in {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 403 response status code, received {response.status_code}"

        if test_user.first_name in [
            "AUDIT_CENTRE_ADMINISTRATOR",
            "AUDIT_CENTRE_CLINICIAN",
        ]:
            response = client.get(
                reverse(
                    "edit_epilepsy12_user",
                    kwargs={
                        "organisation_id": TEST_USER_ORGANISATION.id,
                        "epilepsy12_user_id": test_user.id,
                    },
                )
            )

            assert (
                response.status_code == HTTPStatus.FORBIDDEN
            ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update user {test_user} in {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 403 response status code, received {response.status_code}"


@pytest.mark.django_db
def test_users_update_users_success(
    client,
):
    """
    Simulating different E12 Users attempting to update users in Epilepsy12

    Assert these users are allowed to change Epilepsy12Users
    """

    # set up constants

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )

    # ADDENBROOKE'S
    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ODSCode="RGT01",
        ParentOrganisation_ODSCode="RGT",
    )

    USER_FROM_DIFFERENT_ORG = E12UserFactory(
        email=f"{DIFF_TRUST_DIFF_ORGANISATION}_ADMINISTRATOR@email.com",
        first_name=f"{DIFF_TRUST_DIFF_ORGANISATION}_ADMINISTRATOR",
        role=test_user_audit_centre_administrator_data.role,
        # Assign flags based on user role
        is_active=test_user_audit_centre_administrator_data.is_active,
        is_staff=test_user_audit_centre_administrator_data.is_staff,
        is_rcpch_audit_team_member=test_user_audit_centre_administrator_data.is_rcpch_audit_team_member,
        is_rcpch_staff=test_user_audit_centre_administrator_data.is_rcpch_staff,
        organisation_employer=DIFF_TRUST_DIFF_ORGANISATION,
        groups=[
            Group.objects.get(name=test_user_audit_centre_administrator_data.group_name)
        ],
    )

    users = Epilepsy12User.objects.all().exclude(
        first_name__in=[
            "AUDIT_CENTRE_ADMINISTRATOR",
            "AUDIT_CENTRE_CLINICIAN",
            USER_FROM_DIFFERENT_ORG.first_name,
        ]
    )

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        response = client.get(
            reverse(
                "edit_epilepsy12_user",
                kwargs={
                    "organisation_id": TEST_USER_ORGANISATION.id,
                    "epilepsy12_user_id": test_user.id,
                },
            )
        )

        assert (
            response.status_code == HTTPStatus.OK
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update user {test_user} in {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 200 response status code, received {response.status_code}"

        if test_user.first_name in ["RCPCH_AUDIT_TEAM", "CLINICAL_AUDIT_TEAM"]:
            response = client.get(
                reverse(
                    "edit_epilepsy12_user",
                    kwargs={
                        "organisation_id": DIFF_TRUST_DIFF_ORGANISATION.id,
                        "epilepsy12_user_id": USER_FROM_DIFFERENT_ORG.id,
                    },
                )
            )

            assert (
                response.status_code == HTTPStatus.OK
            ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update user {USER_FROM_DIFFERENT_ORG} in {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 403 response status code, received {response.status_code}"


@pytest.mark.django_db
def test_users_update_cases_forbidden(
    client,
):
    """
    Simulating different E12 Users attempting to update cases in Epilepsy12

    Assert these users cannot change cases
    """

    # set up constants

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )

    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ODSCode="RGT01",
        ParentOrganisation_ODSCode="RGT",
    )

    CASE_FROM_DIFFERENT_ORG = Case.objects.get(
        first_name=f"child_{DIFF_TRUST_DIFF_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.all().exclude(
        first_name__in=[
            "RCPCH_AUDIT_TEAM",
            "CLINICAL_AUDIT_TEAM",
            f"{TEST_USER_ORGANISATION}_ADMINISTRATOR",
        ]
    )

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        response = client.get(
            reverse(
                "update_case",
                kwargs={
                    "organisation_id": TEST_USER_ORGANISATION.id,
                    "case_id": CASE_FROM_DIFFERENT_ORG.id,
                },
            )
        )

        assert (
            response.status_code == HTTPStatus.FORBIDDEN
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update case {CASE_FROM_DIFFERENT_ORG} in {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 403 response status code, received {response.status_code}"


@pytest.mark.django_db
def test_users_update_cases_success(
    client,
):
    """
    Simulating different E12 Users attempting to update cases in Epilepsy12

    Assert these users can change cases
    """

    # set up constants

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )
    CASE_FROM_SAME_ORG = Case.objects.get(
        first_name=f"child_{TEST_USER_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.all().exclude(
        first_name__in=[
            f"{TEST_USER_ORGANISATION}_ADMINISTRATOR",
        ]
    )

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        response = client.get(
            reverse(
                "update_case",
                kwargs={
                    "organisation_id": TEST_USER_ORGANISATION.id,
                    "case_id": CASE_FROM_SAME_ORG.id,
                },
            )
        )

        assert (
            response.status_code == HTTPStatus.OK
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update case {CASE_FROM_SAME_ORG} in {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 200 response status code, received {response.status_code}"


@pytest.mark.parametrize(
    "URL",
    [
        ("first_paediatric_assessment_in_acute_or_nonacute_setting"),
        ("has_number_of_episodes_since_the_first_been_documented"),
        ("general_examination_performed"),
        ("neurological_examination_performed"),
        ("developmental_learning_or_schooling_problems"),
        ("behavioural_or_emotional_problems"),
    ],
)
@pytest.mark.django_db
def test_users_update_first_paediatric_assessment_forbidden(client, URL):
    """
    Simulating different E12 Users attempting to update first paediatric assessment in Epilepsy12

    Assert these users cannot change first paediatric assessment
    """

    # set up constants
    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )

    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ODSCode="RGT01",
        ParentOrganisation_ODSCode="RGT",
    )

    CASE_FROM_DIFFERENT_ORG = Case.objects.get(
        first_name=f"child_{DIFF_TRUST_DIFF_ORGANISATION.OrganisationName}"
    )

    user_first_names_for_test = [
        test_user_audit_centre_administrator_data.role_str,
        test_user_audit_centre_clinician_data.role_str,
        test_user_audit_centre_lead_clinician_data.role_str,
    ]
    users = Epilepsy12User.objects.filter(first_name__in=user_first_names_for_test)

    assert len(users) == len(
        user_first_names_for_test
    ), f"Incorrect queryset of test users. Requested {len(user_first_names_for_test)} users, queryset includes {len(users)}"

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        response = client.get(
            reverse(
                URL,
                kwargs={
                    "first_paediatric_assessment_id": CASE_FROM_DIFFERENT_ORG.registration.firstpaediatricassessment.id,
                },
            )
        )

        assert (
            response.status_code == HTTPStatus.FORBIDDEN
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update case {CASE_FROM_DIFFERENT_ORG} in {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 403 response status code, received {response.status_code}"


@pytest.mark.parametrize(
    "URL",
    [
        ("first_paediatric_assessment_in_acute_or_nonacute_setting"),
        ("has_number_of_episodes_since_the_first_been_documented"),
        ("general_examination_performed"),
        ("neurological_examination_performed"),
        ("developmental_learning_or_schooling_problems"),
        ("behavioural_or_emotional_problems"),
    ],
)
@pytest.mark.django_db
def test_users_update_first_paediatric_assessment_success(client, URL):
    """
    Simulating different E12 Users attempting to update first paediatric assessment in Epilepsy12

    Assert these users can change first paediatric assessment
    """

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )
    CASE_FROM_SAME_ORG = Case.objects.get(
        first_name=f"child_{TEST_USER_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.filter(
        first_name__in=[
            # f"{test_user_audit_centre_administrator_data.role_str}",
            f"{test_user_audit_centre_clinician_data.role_str}",
            f"{test_user_audit_centre_lead_clinician_data.role_str}",
            f"{test_user_clinicial_audit_team_data.role_str}",
            f"{test_user_rcpch_audit_team_data.role_str}",
        ]
    )

    if not users:
        assert False, f"No seeded users in test db. Has the test db been seeded?"

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        if URL == "first_paediatric_assessment_in_acute_or_nonacute_setting":
            # this is single_choice_multiple_toggle_button - select option 1
            response = client.get(
                reverse(
                    URL,
                    kwargs={
                        "first_paediatric_assessment_id": CASE_FROM_SAME_ORG.registration.firstpaediatricassessment.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "1", "Hx-Request": "true"},
            )
        else:
            # all other options are toggle buttons: select True
            response = client.get(
                reverse(
                    URL,
                    kwargs={
                        "first_paediatric_assessment_id": CASE_FROM_SAME_ORG.registration.firstpaediatricassessment.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "button-false", "Hx-Request": "true"},
            )

        assert (
            response.status_code == HTTPStatus.OK
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested to update first paediatric assessment for {CASE_FROM_SAME_ORG} in {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 200 response status code, received {response.status_code}"


# Epilepsy Context
@pytest.mark.parametrize(
    "URL",
    [
        ("previous_febrile_seizure"),
        ("previous_acute_symptomatic_seizure"),
        ("is_there_a_family_history_of_epilepsy"),
        ("previous_neonatal_seizures"),
        ("were_any_of_the_epileptic_seizures_convulsive"),
        ("experienced_prolonged_generalized_convulsive_seizures"),
        ("experienced_prolonged_focal_seizures"),
        ("diagnosis_of_epilepsy_withdrawn"),
    ],
)
@pytest.mark.django_db
def test_users_update_first_epilepsy_context_forbidden(client, URL):
    """
    Simulating different E12 Users attempting to update epilepsy context in Epilepsy12

    Assert these users cannot change epilepsy context
    """

    # set up constants
    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )

    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ODSCode="RGT01",
        ParentOrganisation_ODSCode="RGT",
    )

    CASE_FROM_DIFFERENT_ORG = Case.objects.get(
        first_name=f"child_{DIFF_TRUST_DIFF_ORGANISATION.OrganisationName}"
    )

    user_first_names_for_test = [
        test_user_audit_centre_administrator_data.role_str,
        test_user_audit_centre_clinician_data.role_str,
        test_user_audit_centre_lead_clinician_data.role_str,
    ]
    users = Epilepsy12User.objects.filter(first_name__in=user_first_names_for_test)

    assert len(users) == len(
        user_first_names_for_test
    ), f"Incorrect queryset of test users. Requested {len(user_first_names_for_test)} users, queryset includes {len(users)}"

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        response = client.get(
            reverse(
                URL,
                kwargs={
                    "epilepsy_context_id": CASE_FROM_DIFFERENT_ORG.registration.epilepsycontext.id,
                },
            )
        )

        assert (
            response.status_code == response.status_code == HTTPStatus.FORBIDDEN
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update epilepsy context {CASE_FROM_DIFFERENT_ORG} in {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 403 response status code, received {response.status_code}"


@pytest.mark.parametrize(
    "URL",
    [
        ("previous_febrile_seizure"),
        ("previous_acute_symptomatic_seizure"),
        ("is_there_a_family_history_of_epilepsy"),
        ("previous_neonatal_seizures"),
        ("were_any_of_the_epileptic_seizures_convulsive"),
        ("experienced_prolonged_generalized_convulsive_seizures"),
        ("experienced_prolonged_focal_seizures"),
        ("diagnosis_of_epilepsy_withdrawn"),
    ],
)
@pytest.mark.django_db
def test_users_update_epilepsy_context_success(client, URL):
    """
    Simulating different E12 Users attempting to update epilepsy context in Epilepsy12

    Assert these users can change epilepsy context
    """

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )
    CASE_FROM_SAME_ORG = Case.objects.get(
        first_name=f"child_{TEST_USER_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.filter(
        first_name__in=[
            # f"{test_user_audit_centre_administrator_data.role_str}",
            f"{test_user_audit_centre_clinician_data.role_str}",
            f"{test_user_audit_centre_lead_clinician_data.role_str}",
            f"{test_user_clinicial_audit_team_data.role_str}",
            f"{test_user_rcpch_audit_team_data.role_str}",
        ]
    )

    if not users:
        assert False, f"No seeded users in test db. Has the test db been seeded?"

    single_choice_multiple_toggle_fields = [
        "previous_febrile_seizure",
        "previous_acute_symptomatic_seizure",
        "is_there_a_family_history_of_epilepsy",
        "previous_neonatal_seizures",
        "experienced_prolonged_generalized_convulsive_seizures",
        "experienced_prolonged_focal_seizures",
    ]

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        if URL in single_choice_multiple_toggle_fields:
            # this is single_choice_multiple_toggle_button - select option 1
            response = client.get(
                reverse(
                    URL,
                    kwargs={
                        "epilepsy_context_id": CASE_FROM_SAME_ORG.registration.epilepsycontext.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "1", "Hx-Request": "true"},
            )
        else:
            # all other options are toggle buttons: select True
            response = client.get(
                reverse(
                    URL,
                    kwargs={
                        "epilepsy_context_id": CASE_FROM_SAME_ORG.registration.epilepsycontext.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "button-false", "Hx-Request": "true"},
            )

        assert (
            response.status_code == response.status_code == HTTPStatus.OK
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested to update epilepsy context for {CASE_FROM_SAME_ORG} in {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 200 response status code, received {response.status_code}"


# Multiaxial Diagnosis


@pytest.mark.parametrize(
    "URL",
    [
        ("epilepsy_cause_known"),
        ("epilepsy_cause"),
        ("epilepsy_cause_categories"),
        ("relevant_impairments_behavioural_educational"),
        ("mental_health_screen"),
        ("mental_health_issue_identified"),
        ("mental_health_issue"),
        ("global_developmental_delay_or_learning_difficulties"),
        ("global_developmental_delay_or_learning_difficulties_severity"),
        ("autistic_spectrum_disorder"),
    ],
)
@pytest.mark.django_db
def test_users_update_first_multiaxial_diagnosis_forbidden(client, URL):
    """
    Simulating different E12 Users attempting to update multiaxial diagnosis in Epilepsy12

    Assert these users cannot change multiaxial diagnosis
    """

    # set up constants
    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )

    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ODSCode="RGT01",
        ParentOrganisation_ODSCode="RGT",
    )

    CASE_FROM_DIFFERENT_ORG = Case.objects.get(
        first_name=f"child_{DIFF_TRUST_DIFF_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.all().exclude(
        first_name__in=[
            "RCPCH_AUDIT_TEAM",
            "CLINICAL_AUDIT_TEAM",
            f"{TEST_USER_ORGANISATION}_ADMINISTRATOR",
        ]
    )

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        response = client.get(
            reverse(
                URL,
                kwargs={
                    "multiaxial_diagnosis_id": CASE_FROM_DIFFERENT_ORG.registration.multiaxialdiagnosis.id,
                },
            )
        )

        assert (
            response.status_code == response.status_code == HTTPStatus.FORBIDDEN
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update multiaxial diagnosis {CASE_FROM_DIFFERENT_ORG} in {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 403 response status code, received {response.status_code}"


@pytest.mark.parametrize(
    "URL",
    [
        ("epilepsy_cause_known"),
        ("epilepsy_cause"),
        ("epilepsy_cause_categories"),
        ("relevant_impairments_behavioural_educational"),
        ("mental_health_screen"),
        ("mental_health_issue_identified"),
        ("mental_health_issue"),
        ("global_developmental_delay_or_learning_difficulties"),
        ("global_developmental_delay_or_learning_difficulties_severity"),
        ("autistic_spectrum_disorder"),
    ],
)
@pytest.mark.django_db
def test_users_update_multiaxial_diagnosis_success(client, URL):
    """
    Simulating different E12 Users attempting to update multiaxial diagnosis in Epilepsy12

    Assert these users can change multiaxial diagnosis
    """

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )
    CASE_FROM_SAME_ORG = Case.objects.get(
        first_name=f"child_{TEST_USER_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.all().exclude(
        first_name__in=[
            f"{TEST_USER_ORGANISATION}_ADMINISTRATOR",
            "AUDIT_CENTRE_ADMINISTRATOR",
        ]
    )

    toggle_fields = [
        "epilepsy_cause_known",
        "relevant_impairments_behavioural_educational",
        "mental_health_screen",
        "mental_health_issue_identified",
        "global_developmental_delay_or_learning_difficulties",
        "autistic_spectrum_disorder",
    ]

    single_choice_multiple_toggle_button_fields = [
        "mental_health_issue",
        "global_developmental_delay_or_learning_difficulties_severity",
    ]

    # select_fields = ["epilepsy_cause"] tested in separate function

    multiple_choice_multiple_toggle_button_fields = ["epilepsy_cause_categories"]

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        if URL in toggle_fields:
            # all other options are toggle buttons: select True
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "multiaxial_diagnosis_id": CASE_FROM_SAME_ORG.registration.multiaxialdiagnosis.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "button-true", "Hx-Request": "true"},
            )
        elif (
            URL in single_choice_multiple_toggle_button_fields
            or URL in multiple_choice_multiple_toggle_button_fields
        ):
            # this is single_choice_multiple_toggle_button - select option 1
            response = client.get(
                reverse(
                    URL,
                    kwargs={
                        "multiaxial_diagnosis_id": CASE_FROM_SAME_ORG.registration.epilepsycontext.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "1", "Hx-Request": "true"},
            )
        else:
            # all other options are selects: select True
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "multiaxial_diagnosis_id": CASE_FROM_SAME_ORG.registration.multiaxialdiagnosis.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "epilepsy_cause", "Hx-Request": "true"},
                data={"epilepsy_cause": "179"},
            )

        assert (
            response.status_code == response.status_code == HTTPStatus.OK
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested to update epilepsy context for {CASE_FROM_SAME_ORG} in {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 200 response status code, received {response.status_code}"


@pytest.mark.django_db
def test_update_multiaxial_diagnosis_cause_success(client):
    """
    Assert different E12 Users can update Cause section of multiaxial diagnosis.

    Endpoint url names:

        'epilepsy_cause_known',
        'epilepsy_cause_categories',
        'epilepsy_cause'
    """

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )
    CASE_FROM_SAME_ORG = Case.objects.get(
        first_name=f"child_{TEST_USER_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.filter(
        first_name__in=[
            # f"{test_user_audit_centre_administrator_data.role_str}",
            f"{test_user_audit_centre_clinician_data.role_str}",
            f"{test_user_audit_centre_lead_clinician_data.role_str}",
            f"{test_user_clinicial_audit_team_data.role_str}",
            f"{test_user_rcpch_audit_team_data.role_str}",
        ]
    )

    # Fryns macrocephaly
    EPILEPSY_CAUSE_ENTITY = EpilepsyCauseEntity.objects.get(id=179)

    if not users:
        assert False, f"Test db contains no users. Check db."

    for test_user in users:
        client.force_login(test_user)
        print(
            f"ECKnown before: {MultiaxialDiagnosis.objects.get(registration=CASE_FROM_SAME_ORG.registration).epilepsy_cause_known}"
        )
        response_epilepsy_cause_known = client.post(
            reverse(
                "epilepsy_cause_known",
                kwargs={
                    "multiaxial_diagnosis_id": CASE_FROM_SAME_ORG.registration.multiaxialdiagnosis.id,
                },
            ),
            headers={"Hx-Trigger-Name": "button-true", "Hx-Request": "true"},
        )
        print(
            f"ECKnown after: {MultiaxialDiagnosis.objects.get(registration=CASE_FROM_SAME_ORG.registration).epilepsy_cause_known}"
        )

        assert (
            MultiaxialDiagnosis.objects.get(
                registration=CASE_FROM_SAME_ORG.registration
            ).epilepsy_cause_known
            is True
        ), f"{test_user} from {test_user.organisation_employer} attempted POST True to epilepsy_cause_known but model did not update."

        print(
            f"epilepsy_cause_categories before: {MultiaxialDiagnosis.objects.get(registration=CASE_FROM_SAME_ORG.registration).epilepsy_cause_categories}"
        )
        response_epilepsy_cause_categories = client.post(
            reverse(
                "epilepsy_cause_categories",
                kwargs={
                    "multiaxial_diagnosis_id": CASE_FROM_SAME_ORG.registration.multiaxialdiagnosis.id,
                },
            ),
            headers={"Hx-Trigger-Name": "Gen", "Hx-Request": "true"},
        )

        print(
            f"epilepsy_cause_categories after: {MultiaxialDiagnosis.objects.get(registration=CASE_FROM_SAME_ORG.registration).epilepsy_cause_categories}"
        )

        assert MultiaxialDiagnosis.objects.get(
            registration=CASE_FROM_SAME_ORG.registration
        ).epilepsy_cause_categories == [
            "Gen"
        ], f"{test_user} from {test_user.organisation_employer} attempted POST `Gen` to epilepsy_cause_categories but model did not update."

        print(
            f"epilepsy_cause before: {MultiaxialDiagnosis.objects.get(registration=CASE_FROM_SAME_ORG.registration).epilepsy_cause}"
        )
        response_epilepsy_cause = client.post(
            reverse(
                "epilepsy_cause",
                kwargs={
                    "multiaxial_diagnosis_id": CASE_FROM_SAME_ORG.registration.multiaxialdiagnosis.id,
                },
            ),
            headers={"Hx-Trigger-Name": "epilepsy_cause", "Hx-Request": "true"},
            data={"epilepsy_cause": f"{EPILEPSY_CAUSE_ENTITY.id}"},
        )

        print(
            f"epilepsy_cause after: {MultiaxialDiagnosis.objects.get(registration=CASE_FROM_SAME_ORG.registration).epilepsy_cause}"
        )

        assert (
            MultiaxialDiagnosis.objects.get(
                registration=CASE_FROM_SAME_ORG.registration
            ).epilepsy_cause
            == EPILEPSY_CAUSE_ENTITY
        ), f"{test_user} from {test_user.organisation_employer} attempted POST `epilepsy_cause:{EPILEPSY_CAUSE_ENTITY.id}` but MultiaxialDiagnosis model field did not update."

        # Reset answers for next User
        print("Resetting answers for next user \n\n")
        MultiaxialDiagnosis.objects.filter(
            registration=CASE_FROM_SAME_ORG.registration
        ).update(
            epilepsy_cause_known=None,
            epilepsy_cause_categories=[],
            epilepsy_cause=None,
        )


@pytest.mark.parametrize(
    "URL",
    [
        ("seizure_onset_date"),
        ("seizure_onset_date_confidence"),
        ("episode_definition"),
        ("has_description_of_the_episode_or_episodes_been_gathered"),
        ("edit_description"),
        ("delete_description_keyword"),
        ("epilepsy_or_nonepilepsy_status"),
        ("epileptic_seizure_onset_type"),
        ("focal_onset_epilepsy_checked_changed"),
        ("epileptic_generalised_onset"),
        ("nonepilepsy_generalised_onset"),
        ("nonepileptic_seizure_type"),
        ("nonepileptic_seizure_subtype"),
    ],
)
@pytest.mark.django_db
def test_users_update_episode_forbidden(client, URL):
    """
    Simulating different E12 Users attempting to update episode in Epilepsy12

    Assert these users cannot change episode
    """

    # set up constants
    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )

    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ODSCode="RGT01",
        ParentOrganisation_ODSCode="RGT",
    )

    CASE_FROM_DIFFERENT_ORG = Case.objects.get(
        first_name=f"child_{DIFF_TRUST_DIFF_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.all().exclude(
        first_name__in=[
            "RCPCH_AUDIT_TEAM",
            "CLINICAL_AUDIT_TEAM",
            f"{TEST_USER_ORGANISATION}_ADMINISTRATOR",
        ]
    )

    # Create objs to search for
    episode = Episode.objects.create(
        episode_definition="a",
        multiaxial_diagnosis=CASE_FROM_DIFFERENT_ORG.registration.multiaxialdiagnosis,
    )

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        if URL == "delete_description_keyword":
            response = client.get(
                reverse(
                    URL,
                    kwargs={
                        "episode_id": episode.id,
                        "description_keyword_id": Keyword.objects.all().first().id,
                    },
                )
            )
        else:
            response = client.get(
                reverse(
                    URL,
                    kwargs={
                        "episode_id": episode.id,
                    },
                )
            )

        assert (
            response.status_code == response.status_code == HTTPStatus.FORBIDDEN
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update episode {CASE_FROM_DIFFERENT_ORG} in {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 403 response status code, received {response.status_code}"


@pytest.mark.parametrize(
    "URL",
    [
        ("seizure_onset_date"),
        ("seizure_onset_date_confidence"),
        ("episode_definition"),
        ("has_description_of_the_episode_or_episodes_been_gathered"),
        ("edit_description"),
        ("delete_description_keyword"),
        ("epilepsy_or_nonepilepsy_status"),
        ("epileptic_seizure_onset_type"),
        ("focal_onset_epilepsy_checked_changed"),
        ("epileptic_generalised_onset"),
        ("nonepilepsy_generalised_onset"),
        ("nonepileptic_seizure_type"),
        ("nonepileptic_seizure_subtype"),
    ],
)
@pytest.mark.django_db
def test_users_update_episode_success(client, URL):
    """
    Simulating different E12 Users attempting to update episode in Epilepsy12

    Assert these users can change episode
    """

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )
    CASE_FROM_SAME_ORG = Case.objects.get(
        first_name=f"child_{TEST_USER_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.all().exclude(
        first_name__in=[
            f"{TEST_USER_ORGANISATION}_ADMINISTRATOR",
            "AUDIT_CENTRE_ADMINISTRATOR",
        ]
    )

    date_fields = ["seizure_onset_date"]

    toggle_fields = ["has_description_of_the_episode_or_episodes_been_gathered"]

    single_choice_multiple_toggle_button_fields = [
        "seizure_onset_date_confidence",
        "epilepsy_or_nonepilepsy_status",
        "epileptic_seizure_onset_type",
        "epileptic_generalised_onset",
        "nonepilepsy_generalised_onset",
    ]

    select_fields = [
        "episode_definition",
        "nonepileptic_seizure_type",
        "nonepileptic_seizure_subtype",
    ]

    # Create objs to search for
    episode = Episode.objects.create(
        episode_definition="a",
        multiaxial_diagnosis=CASE_FROM_SAME_ORG.registration.multiaxialdiagnosis,
    )

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)

        if URL == "delete_description_keyword":
            keyword = Keyword.objects.all().first()
            description_keyword_list = [keyword.keyword]
            episode.description_keywords = description_keyword_list
            episode.save()

            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "episode_id": episode.id,
                        "description_keyword_id": 0,  # remove first item in list
                    },
                )
            )
        elif URL in single_choice_multiple_toggle_button_fields:
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "episode_id": episode.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "1", "Hx-Request": "true"},
            )
        elif URL in toggle_fields:
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "episode_id": episode.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "button-true", "Hx-Request": "true"},
            )
        elif URL in select_fields:
            post_body = None
            if URL == "episode_definition":
                post_body = "a"
            elif URL == "nonepileptic_seizure_type":
                post_body = "MAD"
            elif URL == "nonepileptic_seizure_subtype":
                post_body = "c"
            else:
                raise ValueError("No select chosen")
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "episode_id": episode.id,
                    },
                ),
                headers={"Hx-Trigger-Name": URL, "Hx-Request": "true"},
                data={URL: post_body},
            )
        elif URL in date_fields:
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "episode_id": episode.id,
                    },
                ),
                headers={"Hx-Trigger-Name": URL, "Hx-Request": "true"},
                data={URL: date.today()},
            )
        elif URL == "edit_description":
            # remaining values are strings
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "episode_id": episode.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "description", "Hx-Request": "true"},
                data={"description": "This is a description"},
            )
        else:
            # this is the choice for focal epilepsy
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "episode_id": episode.id,
                    },
                ),
                headers={"Hx-Trigger-Name": "LATERALITY", "Hx-Request": "true"},
                data={URL: "focal_onset_left"},
            )

        assert (
            response.status_code == response.status_code == HTTPStatus.OK
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update episode {CASE_FROM_SAME_ORG} in {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 200 response status code, received {response.status_code}"


#  Comorbidity


@pytest.mark.parametrize(
    "URL",
    [
        ("comorbidity_diagnosis_date"),
        ("comorbidity_diagnosis"),
    ],
)
@pytest.mark.django_db
def test_users_update_comorbidity_forbidden(client, URL):
    """
    Simulating different E12 Users attempting to update comorbidity in Epilepsy12

    Assert these users cannot change comorbidity
    """

    # set up constants
    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )

    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ODSCode="RGT01",
        ParentOrganisation_ODSCode="RGT",
    )

    CASE_FROM_DIFFERENT_ORG = Case.objects.get(
        first_name=f"child_{DIFF_TRUST_DIFF_ORGANISATION.OrganisationName}"
    )

    user_first_names_for_test = [
        test_user_audit_centre_administrator_data.role_str,
        test_user_audit_centre_clinician_data.role_str,
        test_user_audit_centre_lead_clinician_data.role_str,
    ]
    users = Epilepsy12User.objects.filter(first_name__in=user_first_names_for_test)

    assert len(users) == len(
        user_first_names_for_test
    ), f"Incorrect queryset of test users. Requested {len(user_first_names_for_test)} users, queryset includes {len(users)}"

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)
        comorbidity, created = Comorbidity.objects.update_or_create(
            multiaxial_diagnosis=CASE_FROM_DIFFERENT_ORG.registration.multiaxialdiagnosis,
            comorbidity_diagnosis_date=date.today(),
            comorbidityentity=ComorbidityEntity.objects.all().first(),
        )
        comorbidity.save()

        if URL == "comorbidity_diagnosis_date":
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "comorbidity_id": comorbidity.pk,
                    },
                ),
                headers={"Hx-Trigger-Name": URL, "Hx-Request": "true"},
                data={URL: date.today()},
            )
        elif URL == "comorbidity_diagnosis":
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "comorbidity_id": comorbidity.pk,
                    },
                ),
                headers={"Hx-Trigger-Name": URL, "Hx-Request": "true"},
                data={URL: ComorbidityEntity.objects.all().first().id},
            )

        if response.status_code == 200:
            print(
                f"{test_user.first_name} change permission: {test_user.has_perm('epilepsy12.change_comorbidity')} view permission: {test_user.has_perm('epilepsy12.view_comorbidity')}"
            )

        assert (
            response.status_code == HTTPStatus.FORBIDDEN
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested update comorbidity for {CASE_FROM_DIFFERENT_ORG} in {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 403 response status code, received {response.status_code}"


@pytest.mark.parametrize(
    "URL",
    [
        ("comorbidity_diagnosis_date"),
        ("comorbidity_diagnosis"),
    ],
)
@pytest.mark.django_db
def test_users_update_comorbidity_success(client, URL):
    """
    Simulating different E12 Users attempting to update comorbidity in Epilepsy12

    Assert these users can change comorbidity
    """

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ODSCode="RP401",
        ParentOrganisation_ODSCode="RP4",
    )
    CASE_FROM_SAME_ORG = Case.objects.get(
        first_name=f"child_{TEST_USER_ORGANISATION.OrganisationName}"
    )

    users = Epilepsy12User.objects.filter(
        first_name__in=[
            # f"{test_user_audit_centre_administrator_data.role_str}",
            f"{test_user_audit_centre_clinician_data.role_str}",
            f"{test_user_audit_centre_lead_clinician_data.role_str}",
            f"{test_user_clinicial_audit_team_data.role_str}",
            f"{test_user_rcpch_audit_team_data.role_str}",
        ]
    )

    if not users:
        assert False, f"No seeded users in test db. Has the test db been seeded?"

    for test_user in users:
        # Log in Test User
        client.force_login(test_user)
        comorbidity, created = Comorbidity.objects.update_or_create(
            multiaxial_diagnosis=CASE_FROM_SAME_ORG.registration.multiaxialdiagnosis,
            comorbidity_diagnosis_date=date.today(),
            comorbidityentity=ComorbidityEntity.objects.all().first(),
        )
        comorbidity.save()

        if URL == "comorbidity_diagnosis_date":
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "comorbidity_id": comorbidity.id,
                    },
                ),
                headers={"Hx-Trigger-Name": URL, "Hx-Request": "true"},
                data={URL: date.today()},
            )
        elif URL == "comorbidity_diagnosis":
            response = client.post(
                reverse(
                    URL,
                    kwargs={
                        "comorbidity_id": comorbidity.pk,
                    },
                ),
                headers={"Hx-Trigger-Name": URL, "Hx-Request": "true"},
                data={URL: ComorbidityEntity.objects.all().first().id},
            )

        assert (
            response.status_code == HTTPStatus.OK
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested to update comorbidities for {CASE_FROM_SAME_ORG} in {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()} Expected 200 response status code, received {response.status_code}"
