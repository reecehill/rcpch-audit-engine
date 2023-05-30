"""
Tests for Measure 3 `tertiary_input.

Each test depends on whether child has been referred / seen by a neurologist OR epilepsy surgery OR both, so first each test parametrizes each of these cases.

- [x] Measure 3 passed (registration.kpi.tertiary_input == 1) if age at first paediatric assessment is <= 3 and seen by neurologist / epilepsy surgery/both ( where age_at_first_paediatric_assessment = relativedelta(registration_instance.registration_date,registration_instance.case.date_of_birth).years)
- [x] Measure 3 passed (registration.kpi.tertiary_input == 1) if child is on 3 or more AEMS (see lines 115-120 for query) and seen by neurologist / epilepsy surgery/both
- [x] Measure 3 passed (registration.kpi.tertiary_input == 1) if child is under 4 and has myoclonic epilepsy (lines 128-133) and seen by neurologist / epilepsy surgery/both
- [x] Measure 3 passed (registration.kpi.tertiary_input == 1) if child is eligible for epilepsy surgery (registration_instance.assessment.childrens_epilepsy_surgical_service_referral_criteria_met) and seen by neurologist / epilepsy surgery/both
- [ ] Measure 3 failed (registration.kpi.tertiary_input == 0) if age at first paediatric assessment is <= 3 and not seen by neurologist / epilepsy surgery/both ( where age_at_first_paediatric_assessment = relativedelta(registration_instance.registration_date,registration_instance.case.date_of_birth).years)
- [ ] Measure 3 failed (registration.kpi.tertiary_input == 0) if child is on 3 or more AEMS (see lines 115-120 for query) and not seen by neurologist / epilepsy surgery/both
- [ ] Measure 3 failed (registration.kpi.tertiary_input == 0) if child is under 4 and has myoclonic epilepsy (lines 128-133) and not seen by neurologist / epilepsy surgery/both
- [ ] Measure 3 failed (registration.kpi.tertiary_input == 0) if child is eligible for epilepsy surgery (registration_instance.assessment.childrens_epilepsy_surgical_service_referral_criteria_met) and not seen by neurologist / epilepsy surgery/both
- [ ] Measure 3 ineligible (registration.kpi.tertiary_input == 2) if age at first paediatric assessment is > 3 and not not on 3 or more drugs and not eligible for epilepsy surgery and not >4y with myoclonic epilepsy
Measure 3b
- [ ] Measure 3b passed (registration.kp.epilepsy_surgery_referral ==1 ) if met criteria for surgery and evidence of referral or being seen (line 224)

Test Measure 3 - % of children and young people meeting defined criteria for paediatric neurology referral, with input of tertiary care and/or CESS referral within the first year of care

Numerator: "Number of children ([less than 3 years old at first assessment] AND [diagnosed with epilepsy] OR (number of children and young people diagnosed with epilepsy who had [3 or more maintenance AEDS] at first year) OR (Number of children less than 4 years old at first assessment with epilepsy AND myoclonic seizures)  OR (number of children and young people diagnosed with epilepsy  who met [CESS criteria] ) AND had [evidence of referral or involvement of a paediatric neurologist] OR [evidence of referral or involvement of CESS]"

^above in English:
    PASS IF ANY OF:
        1. (age < 3yo at first assessment) AND (seen by neurologist / epilepsy surgery/both)
        2. ((age < 4yo) AND (myoclonic epilepsy)) AND (seen by neurologist / epilepsy surgery/both)
        3. (on >= 3 AEMS) AND (seen by neurologist / epilepsy surgery/both)
        4. (eligible for epilepsy surgery) AND (seen by neurologist / epilepsy surgery/both)
    OR MORE SIMPLY:
        If *criteria met* AND *referred/seen by neurologist / epilepsy surgery/both*
"""

# Standard imports
import pytest
from datetime import date
from dateutil.relativedelta import relativedelta

# Third party imports

# RCPCH imports
from epilepsy12.common_view_functions import calculate_kpis
from epilepsy12.models import (
    Registration,
    KPI,
    AntiEpilepsyMedicine,
    MedicineEntity,
    Episode,
)
from epilepsy12.constants import (
    KPI_SCORE,
    GENERALISED_SEIZURE_TYPE,
)

# sets up paramtrization constant for running tests against seen neurologist/surgery/both/neither

CASE_PARAM_NAMES = "PAEDIATRIC_NEUROLOGIST_REFERRAL_DATE,PAEDIATRIC_NEUROLOGIST_INPUT_DATE, CHILDRENS_EPILEPSY_SURGICAL_SERVICE_REFERRAL_DATE,CHILDRENS_EPILEPSY_SURGICAL_SERVICE_INPUT_DATE, expected_kpi_score"

CASE_PARAM_VALUES = [
    (date(2023, 1, 10), date(2023, 1, 11), None, None, KPI_SCORE["PASS"]),
    (None, None, date(2023, 1, 10), date(2023, 1, 11), KPI_SCORE["PASS"]),
    (
        date(2023, 1, 10),
        date(2023, 1, 11),
        date(2023, 1, 10),
        date(2023, 1, 11),
        KPI_SCORE["PASS"],
    ),
    (
        None,
        None,
        None,
        None,
        KPI_SCORE["FAIL"],
    ),
]


@pytest.mark.parametrize(
    CASE_PARAM_NAMES,
    CASE_PARAM_VALUES,
)
@pytest.mark.django_db
def test_measure_3_age_3yo(
    e12_case_factory,
    PAEDIATRIC_NEUROLOGIST_REFERRAL_DATE,
    PAEDIATRIC_NEUROLOGIST_INPUT_DATE,
    CHILDRENS_EPILEPSY_SURGICAL_SERVICE_REFERRAL_DATE,
    CHILDRENS_EPILEPSY_SURGICAL_SERVICE_INPUT_DATE,
    expected_kpi_score,
):
    """
    *PASSED*
    1) age at First Paediatric Assessment (FPA) is <= 3 && seen by neurologist / epilepsy surgery/both
    """
    DATE_OF_BIRTH = date(2021, 1, 1)
    REGISTRATION_DATE = DATE_OF_BIRTH + relativedelta(
        years=3
    )  # a child who is exactly 3 at registration_date (=FPA)

    case = e12_case_factory(
        date_of_birth=DATE_OF_BIRTH,
        registration__registration_date=REGISTRATION_DATE,
        registration__assessment__paediatric_neurologist_referral_date=PAEDIATRIC_NEUROLOGIST_REFERRAL_DATE,
        registration__assessment__paediatric_neurologist_input_date=PAEDIATRIC_NEUROLOGIST_INPUT_DATE,
        registration__assessment__childrens_epilepsy_surgical_service_referral_date=CHILDRENS_EPILEPSY_SURGICAL_SERVICE_REFERRAL_DATE,
        registration__assessment__childrens_epilepsy_surgical_service_input_date=CHILDRENS_EPILEPSY_SURGICAL_SERVICE_INPUT_DATE,
    )

    # get registration for the saved case model
    registration = Registration.objects.get(case=case)

    calculate_kpis(registration_instance=registration)

    kpi_score = KPI.objects.get(pk=registration.kpi.pk).tertiary_input

    assert (
        kpi_score == expected_kpi_score
    ), f"Age at FPA is 3yo and seen by neurologist / surgery / both but did not pass measure" if expected_kpi_score==KPI_SCORE['PASS'] else f"Age at FPA is 3yo but not seen by neurologist / surgery and did not fail measure"


@pytest.mark.parametrize(
    CASE_PARAM_NAMES,
    CASE_PARAM_VALUES,
)
@pytest.mark.django_db
def test_measure_3_should_pass_3AEMs_seen(
    e12_case_factory,
    PAEDIATRIC_NEUROLOGIST_REFERRAL_DATE,
    PAEDIATRIC_NEUROLOGIST_INPUT_DATE,
    CHILDRENS_EPILEPSY_SURGICAL_SERVICE_REFERRAL_DATE,
    CHILDRENS_EPILEPSY_SURGICAL_SERVICE_INPUT_DATE,
    expected_kpi_score,
):
    """
    *PASSED*
    1) child is on 3 or more AEMS and seen by neurologist / epilepsy surgery/both
    """

    REGISTRATION_DATE = date(
        2023, 1, 1
    )  # explicit setting to ensure aems started before registration close date

    case = e12_case_factory(
        registration__registration_date=REGISTRATION_DATE,
        registration__assessment__paediatric_neurologist_referral_date=PAEDIATRIC_NEUROLOGIST_REFERRAL_DATE,
        registration__assessment__paediatric_neurologist_input_date=PAEDIATRIC_NEUROLOGIST_INPUT_DATE,
        registration__assessment__childrens_epilepsy_surgical_service_referral_date=CHILDRENS_EPILEPSY_SURGICAL_SERVICE_REFERRAL_DATE,
        registration__assessment__childrens_epilepsy_surgical_service_input_date=CHILDRENS_EPILEPSY_SURGICAL_SERVICE_INPUT_DATE,
    )

    # get registration for the saved case model
    registration = Registration.objects.get(case=case)

    # create total of 3 AEMs related to this registration instance
    aems = AntiEpilepsyMedicine.objects.filter(
        management=registration.management,
        is_rescue_medicine=False,
        antiepilepsy_medicine_start_date__lt=registration.registration_close_date,
    )
    aems_to_add = MedicineEntity.objects.filter(
        medicine_name__in=["Zonisamide", "Vigabatrin"]
    )
    for aem_to_add in aems_to_add:
        new_aem = AntiEpilepsyMedicine.objects.create(
            management=registration.management,
            medicine_entity=aem_to_add,
            is_rescue_medicine=False,
            antiepilepsy_medicine_start_date=REGISTRATION_DATE + relativedelta(days=5),
        )
        new_aem.save()
    aems_count = AntiEpilepsyMedicine.objects.filter(
        management=registration.management,
        is_rescue_medicine=False,
        antiepilepsy_medicine_start_date__lt=registration.registration_close_date,
    ).count()

    calculate_kpis(registration_instance=registration)

    kpi_score = KPI.objects.get(pk=registration.kpi.pk).tertiary_input

    assert (
        kpi_score == expected_kpi_score
    ), f"On >= 3 AEMS (n={aems_count}) and seen by neurologist / epilepsy surgery/both but did not pass measure" if expected_kpi_score==KPI_SCORE['PASS'] else f"On >= 3 AEMS (n={aems_count}) and not seen by neurologist / surgery and did not fail measure"


@pytest.mark.parametrize(
    CASE_PARAM_NAMES,
    CASE_PARAM_VALUES,
)
@pytest.mark.django_db
def test_measure_3_should_pass_lt_4yo_myoclonic_seen(
    e12_case_factory,
    e12_episode_factory,
    PAEDIATRIC_NEUROLOGIST_REFERRAL_DATE,
    PAEDIATRIC_NEUROLOGIST_INPUT_DATE,
    CHILDRENS_EPILEPSY_SURGICAL_SERVICE_REFERRAL_DATE,
    CHILDRENS_EPILEPSY_SURGICAL_SERVICE_INPUT_DATE,
    expected_kpi_score,
):
    """
    *PASSED*
    1) child is under 4 and has myoclonic epilepsy and seen by neurologist / epilepsy surgery/both
    """

    # SET UP CONSTANTS
    DATE_OF_BIRTH = date(2021, 1, 1)
    REGISTRATION_DATE = DATE_OF_BIRTH + relativedelta(
        years=3, months=11
    )  # a child who is 3y11m at registration_date (=FPA)
    MYOCLONIC = GENERALISED_SEIZURE_TYPE[5][0]

    case = e12_case_factory(
        date_of_birth=DATE_OF_BIRTH,
        registration__registration_date=REGISTRATION_DATE,
        registration__assessment__paediatric_neurologist_referral_date=PAEDIATRIC_NEUROLOGIST_REFERRAL_DATE,
        registration__assessment__paediatric_neurologist_input_date=PAEDIATRIC_NEUROLOGIST_INPUT_DATE,
        registration__assessment__childrens_epilepsy_surgical_service_referral_date=CHILDRENS_EPILEPSY_SURGICAL_SERVICE_REFERRAL_DATE,
        registration__assessment__childrens_epilepsy_surgical_service_input_date=CHILDRENS_EPILEPSY_SURGICAL_SERVICE_INPUT_DATE,
    )

    # get registration for the saved case model
    registration = Registration.objects.get(case=case)

    # Assign a myoclonic episode
    e12_episode_factory.create(
        multiaxial_diagnosis=registration.multiaxialdiagnosis,
        epileptic_seizure_onset_type_generalised=True,
        epileptic_generalised_onset=MYOCLONIC,
    )

    # count myoclonic episodes attached to confirm
    episodes = Episode.objects.filter(
        multiaxial_diagnosis=registration.multiaxialdiagnosis,
        epilepsy_or_nonepilepsy_status="E",
        epileptic_generalised_onset=MYOCLONIC,
    )

    calculate_kpis(registration_instance=registration)

    kpi_score = KPI.objects.get(pk=registration.kpi.pk).tertiary_input

    assert (
        kpi_score == expected_kpi_score
    ), f"Has myoclonic episode (n = {episodes.count()}) and seen by neurologist / epilepsy surgery/both but did not pass measure" if expected_kpi_score==KPI_SCORE['PASS'] else f"Has myoclonic episode (n = {episodes.count()}) and not seen by neurologist / surgery and did not fail measure"


@pytest.mark.parametrize(
    CASE_PARAM_NAMES,
    CASE_PARAM_VALUES,
)
@pytest.mark.django_db
def test_measure_3_should_pass_lt_meets_CESS_seen(
    e12_case_factory,
    PAEDIATRIC_NEUROLOGIST_REFERRAL_DATE,
    PAEDIATRIC_NEUROLOGIST_INPUT_DATE,
    CHILDRENS_EPILEPSY_SURGICAL_SERVICE_REFERRAL_DATE,
    CHILDRENS_EPILEPSY_SURGICAL_SERVICE_INPUT_DATE,
    expected_kpi_score,
):
    """
    *PASSED*
    1) child is eligible for epilepsy surgery (registration_instance.assessment.childrens_epilepsy_surgical_service_referral_criteria_met) and seen by neurologist / epilepsy surgery/both
    """

    case = e12_case_factory(
        registration__assessment__childrens_epilepsy_surgical_service_referral_criteria_met=True,
        registration__assessment__paediatric_neurologist_referral_date=PAEDIATRIC_NEUROLOGIST_REFERRAL_DATE,
        registration__assessment__paediatric_neurologist_input_date=PAEDIATRIC_NEUROLOGIST_INPUT_DATE,
        registration__assessment__childrens_epilepsy_surgical_service_referral_date=CHILDRENS_EPILEPSY_SURGICAL_SERVICE_REFERRAL_DATE,
        registration__assessment__childrens_epilepsy_surgical_service_input_date=CHILDRENS_EPILEPSY_SURGICAL_SERVICE_INPUT_DATE,
    )

    # get registration for the saved case model
    registration = Registration.objects.get(case=case)

    calculate_kpis(registration_instance=registration)

    kpi_score = KPI.objects.get(pk=registration.kpi.pk).tertiary_input

    assert (
        kpi_score == expected_kpi_score
    ), f"Met CESS criteria and seen by neurologist / epilepsy surgery/both but did not pass measure" if expected_kpi_score==KPI_SCORE['PASS'] else f"Met CESS criteria and not seen by neurologist / surgery and did not fail measure"
