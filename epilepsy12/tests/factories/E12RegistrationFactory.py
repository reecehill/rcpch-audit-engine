"""Factory fn to create new E12 Registrations"""

# standard imports
import datetime

# third-party imports
import factory

# rcpch imports
from epilepsy12.models import (
    Site,
    Registration,
    KPI,
)
from .E12AuditProgressFactory import E12AuditProgressFactory
from .E12CaseFactory import E12CaseFactory
from .E12MultiaxialDiagnosisFactory import E12MultiaxialDiagnosisFactory

class E12RegistrationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Registration

    # Sets the minimal 'required' fields for a registration to be valid
    registration_date = datetime.date(2023, 1, 1)
    eligibility_criteria_met = True
    case = factory.SubFactory(E12CaseFactory)
    audit_progress = factory.SubFactory(E12AuditProgressFactory)
    
    # Getting the KPI organisation requires a more complex operation so we use the .lazy_attribute decorator. Once a Registration is .create()'d, filter Sites using the related Case to find the lead organisation - which is used to generate the kpi model. 
    @factory.lazy_attribute
    def kpi(self):
        lead_organisation = Site.objects.filter(
            case=self.case,
            site_is_primary_centre_of_epilepsy_care=True,
            site_is_actively_involved_in_epilepsy_care=True,
        ).get()
        return KPI.objects.create(
                organisation=lead_organisation.organisation,
                parent_trust=lead_organisation.organisation.ParentOrganisation_OrganisationName,
                paediatrician_with_expertise_in_epilepsies=0,
                epilepsy_specialist_nurse=0,
                tertiary_input=0,
                epilepsy_surgery_referral=0,
                ecg=0,
                mri=0,
                assessment_of_mental_health_issues=0,
                mental_health_support=0,
                sodium_valproate=0,
                comprehensive_care_planning_agreement=0,
                patient_held_individualised_epilepsy_document=0,
                patient_carer_parent_agreement_to_the_care_planning=0,
                care_planning_has_been_updated_when_necessary=0,
                comprehensive_care_planning_content=0,
                parental_prolonged_seizures_care_plan=0,
                water_safety=0,
                first_aid=0,
                general_participation_and_risk=0,
                service_contact_details=0,
                sudep=0,
                school_individual_healthcare_plan=0,
            )
    
    # Reverse dependencies
    multiaxial_diagnosis = factory.RelatedFactory(
        E12MultiaxialDiagnosisFactory,
        factory_related_name='registration'
    )