from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Q
from django_htmx.http import trigger_client_event
from ..models import Registration, Site
from ..models import Case, AuditProgress, HospitalTrust


@login_required
def register(request, case_id):

    case = Case.objects.get(pk=case_id)

    active_template = "register"

    if not Registration.objects.filter(case=case).exists():
        audit_progress = AuditProgress.objects.create(
            registration_complete=False,
            initial_assessment_complete=False,
            assessment_complete=False,
            epilepsy_context_complete=False,
            multiaxial_description_complete=False,
            management_complete=False,
            investigations_complete=False,
            registration_total_expected_fields=4,
            registration_total_completed_fields=0,
            initial_assessment_total_expected_fields=0,
            initial_assessment_total_completed_fields=0,
            assessment_total_expected_fields=0,
            assessment_total_completed_fields=0,
            epilepsy_context_total_expected_fields=0,
            epilepsy_context_total_completed_fields=0,
            multiaxial_description_total_expected_fields=0,
            multiaxial_description_total_completed_fields=0,
            investigations_total_expected_fields=0,
            investigations_total_completed_fields=0,
            management_total_expected_fields=0,
            management_total_completed_fields=0
        )
        Registration.objects.create(
            case=case,
            audit_progress=audit_progress
        )
        active_template = "none"

    registration = Registration.objects.filter(case=case).get()

    hospital_list = HospitalTrust.objects.filter(
        Sector="NHS Sector").order_by('OrganisationName')

    previously_registered = 0

    lead_site = None

    registered_sites = Site.objects.filter(registration=registration)
    for registered_site in registered_sites:
        if registered_site.site_is_primary_centre_of_epilepsy_care and registered_site.site_is_actively_involved_in_epilepsy_care:
            lead_site = registered_site
        elif not registered_site.site_is_actively_involved_in_epilepsy_care:
            previously_registered += 1

    previously_registered_sites = None
    if previously_registered > 0:
        previously_registered_sites = Site.objects.filter(
            registration=registration, site_is_actively_involved_in_epilepsy_care=False, site_is_primary_centre_of_epilepsy_care=True).all()

    test_fields_update_audit_progress(registration)

    context = {
        "registration": registration,
        "case_id": case_id,
        "hospital_list": hospital_list,
        "site": lead_site,
        "previously_registered_sites": previously_registered_sites,
        "audit_progress": registration.audit_progress,
        "active_template": active_template
    }

    response = render(
        request=request,
        template_name='epilepsy12/register.html',
        context=context
    )

    trigger_client_event(
        response=response,
        name="registration_active",
        params={})  # reloads the form to show the active steps

    return response


# HTMX endpoints

"""
Lead site allocation, deletion, updating and transfer
"""


def allocate_lead_site(request, registration_id):
    """
    Allocate site when none have been assigned
    """
    registration = Registration.objects.get(pk=registration_id)
    new_trust_id = request.POST.get('allocate_lead_site')
    selected_hospital_trust = HospitalTrust.objects.get(pk=new_trust_id)

    # test if site exists
    if Site.objects.filter(
        registration=registration,
        hospital_trust=selected_hospital_trust,
        site_is_actively_involved_in_epilepsy_care=True
    ).exists():
        # this site already plays an active role in the care of this child
        # update the status therefore to include the lead role

        Site.objects.filter(
            registration=registration,
            hospital_trust=selected_hospital_trust,
            site_is_actively_involved_in_epilepsy_care=True
        ).update(
            site_is_primary_centre_of_epilepsy_care=True
        )
    else:
        # this site may still be associated with this registration but not actively
        # it is therefore safe to create a new record
        Site.objects.create(
            registration=registration,
            hospital_trust=selected_hospital_trust,
            site_is_actively_involved_in_epilepsy_care=True,
            site_is_primary_centre_of_epilepsy_care=True,
            site_is_childrens_epilepsy_surgery_centre=False,
            site_is_paediatric_neurology_centre=False,
            site_is_general_paediatric_centre=True
        )

    # retrieve the current active site
    site = Site.objects.filter(
        registration=registration,
        hospital_trust=selected_hospital_trust,
        site_is_primary_centre_of_epilepsy_care=True,
        site_is_actively_involved_in_epilepsy_care=True,
    ).get()

    test_fields_update_audit_progress(registration)

    # get the new

    hospital_list = HospitalTrust.objects.filter(
        Sector="NHS Sector").order_by('OrganisationName')

    context = {
        "hospital_list": hospital_list,
        "registration": registration,
        "site": site,
        "edit": False,
        "transfer": False
    }

    response = render(
        request=request, template_name="epilepsy12/partials/registration/lead_site.html", context=context)

    # activate registration button if eligibility and lead centre set
    trigger_client_event(
        response=response,
        name="registration_status",
        params={})  # updates the registration status bar with date in the client
    return response


def edit_lead_site(request, registration_id, site_id):
    """
    Edit lead centre button call back from lead_site partial
    Does not edit the centre - returns only the template with the edit set to true
    """
    registration = Registration.objects.get(pk=registration_id)
    site = Site.objects.get(pk=site_id)
    hospital_list = HospitalTrust.objects.filter(
        Sector="NHS Sector").order_by('OrganisationName')

    test_fields_update_audit_progress(registration)

    context = {
        "hospital_list": hospital_list,
        "registration": registration,
        "site": site,
        "edit": True,
        "transfer": False
    }

    response = render(
        request=request, template_name="epilepsy12/partials/registration/lead_site.html", context=context)

    # activate registration button if eligibility and lead centre set
    trigger_client_event(
        response=response,
        name="registration_status",
        params={})  # updates the registration status bar with date in the client
    return response


def transfer_lead_site(request, registration_id, site_id):
    registration = Registration.objects.get(pk=registration_id)
    site = Site.objects.get(pk=site_id)

    hospital_list = HospitalTrust.objects.filter(
        Sector="NHS Sector").order_by('OrganisationName').all()

    test_fields_update_audit_progress(registration)

    context = {
        "hospital_list": hospital_list,
        "registration": registration,
        "site": site,
        "edit": False,
        "transfer": True
    }

    response = render(
        request=request, template_name="epilepsy12/partials/registration/lead_site.html", context=context)

    # activate registration button if eligibility and lead centre set
    trigger_client_event(
        response=response,
        name="registration_status",
        params={})  # updates the registration status bar with date in the client
    return response


def cancel_lead_site(request, registration_id, site_id):
    registration = Registration.objects.get(pk=registration_id)
    site = Site.objects.get(pk=site_id)
    hospital_list = HospitalTrust.objects.filter(
        Sector="NHS Sector").order_by('OrganisationName')

    test_fields_update_audit_progress(registration)

    context = {
        "registration": registration,
        "site": site,
        "edit": False,
        "transfer": False,
        'hospital_site': hospital_list
    }

    response = render(
        request=request, template_name="epilepsy12/partials/registration/lead_site.html", context=context)

    # activate registration button if eligibility and lead centre set
    trigger_client_event(
        response=response,
        name="registration_status",
        params={})  # updates the registration status bar with date in the client
    return response


def update_lead_site(request, registration_id, site_id, update):
    """
    HTMX POST request on button click from the lead_site partial
    It either edits the existing lead centre or creates a new one and 
    set site_is_actively_involved_in_epilepsy_care and site_is_actively_involved_in_epilepsy_care
    to False in the current record.
    Returns a lead_site partial but also updates the previous_sites partial also
    """

    registration = Registration.objects.get(pk=registration_id)

    if update == "edit":
        new_trust_id = request.POST.get('edit_lead_site')
        new_hospital_trust = HospitalTrust.objects.get(pk=new_trust_id)
        Site.objects.filter(pk=site_id).update(
            hospital_trust=new_hospital_trust,
            site_is_primary_centre_of_epilepsy_care=True,
            site_is_actively_involved_in_epilepsy_care=True)
    elif update == "transfer":
        new_trust_id = request.POST.get('transfer_lead_site')
        new_hospital_trust = HospitalTrust.objects.get(pk=new_trust_id)
        Site.objects.filter(pk=site_id).update(
            site_is_primary_centre_of_epilepsy_care=True,
            site_is_actively_involved_in_epilepsy_care=False)
        Site.objects.create(
            hospital_trust=new_hospital_trust,
            site_is_primary_centre_of_epilepsy_care=True,
            site_is_actively_involved_in_epilepsy_care=True,
            registration=registration)

    site = Site.objects.filter(
        registration=registration,
        site_is_primary_centre_of_epilepsy_care=True,
        site_is_actively_involved_in_epilepsy_care=True).first()

    hospital_list = HospitalTrust.objects.filter(
        Sector="NHS Sector").order_by('OrganisationName')

    test_fields_update_audit_progress(registration)

    context = {
        "registration": registration,
        "site": site,
        "edit": False,
        "transfer": False,
        'hospital_list': hospital_list
    }

    response = render(
        request=request, template_name="epilepsy12/partials/registration/lead_site.html", context=context)

    if registration.eligibility_criteria_met:
        trigger_client_event(
            response=response, name="add_previously_registered_site", params={})

    return response


def delete_lead_site(request, registration_id, site_id):
    """
    HTMX POST request on button click from the lead_site partial
    It deletes the site.
    Returns a lead_site partial but also updates the previous_sites partial also
    """
    registration = Registration.objects.get(pk=registration_id)

    # test first to see if this site is associated with other roles
    # either past or present
    if Site.objects.filter(
        Q(registration=registration) &
        Q(pk=site_id) &
        Q(
            Q(site_is_childrens_epilepsy_surgery_centre=True) |
            Q(site_is_paediatric_neurology_centre=True) |
            Q(site_is_general_paediatric_centre=True)
        )
    ).exists():
        # remove the lead role allocation
        Site.objects.filter(
            pk=site_id
        ).update(site_is_primary_centre_of_epilepsy_care=False)

    else:
        # there are no other roles (previous or current)
        # it is safe to delete this record
        Site.objects.filter(pk=site_id).delete()

    lead_site = Site.objects.filter(
        registration=registration,
        site_is_primary_centre_of_epilepsy_care=True,
        site_is_actively_involved_in_epilepsy_care=True).first()

    hospital_list = HospitalTrust.objects.filter(
        Sector="NHS Sector").order_by('OrganisationName')

    test_fields_update_audit_progress(registration)

    context = {
        "registration": registration,
        "site": lead_site,
        "edit": False,
        "transfer": False,
        'hospital_list': hospital_list
    }

    response = render(
        request=request, template_name="epilepsy12/partials/registration/lead_site.html", context=context)
    trigger_client_event(
        response=response, name="add_previously_registered_site", params={})
    return response


@login_required
def previous_sites(request, registration_id):

    registration = Registration.objects.get(pk=registration_id)
    previous_sites = Site.objects.filter(
        registration=registration, site_is_actively_involved_in_epilepsy_care=False, site_is_primary_centre_of_epilepsy_care=True)

    context = {
        'previously_registered_sites': previous_sites,
        'registration': registration
    }
    return render(request=request, template_name="epilepsy12/partials/registration/previous_sites.html", context=context)


"""
Validation process
"""


@login_required
def confirm_eligible(request, registration_id):
    """
    HTMX POST request on button press in registration_form confirming child
    meets eligibility criteria of the audit.
    This will set the eligibility_criteria_met flag in the Registration model
    to True and replace the button with the is_eligible partial, a label confirming
    eligibility. The button will not be shown again.
    """
    context = {
        'has_error': False,
        'message': 'Eligibility Criteria Confirmed.'
    }
    try:
        Registration.objects.update_or_create(pk=registration_id, defaults={
            'eligibility_criteria_met': True
        })
    except Exception as error:
        context = {
            'has_error': True,
            'message': error
        }

    response = render(
        request=request, template_name='epilepsy12/partials/registration/is_eligible_label.html', context=context)

    registration = Registration.objects.filter(pk=registration_id).get()

    if registration.eligibility_criteria_met and Site.objects.filter(registration=registration, site_is_primary_centre_of_epilepsy_care=True).exists():
        # activate registration button if eligibility and lead centre set
        trigger_client_event(
            response=response,
            name="registration_status",
            params={})  # updates the registration status bar with date in the client

    # if all registration components present, update AuditProcess
    if registration.eligibility_criteria_met and registration.registration_date is not None:
        # registration now complete
        AuditProgress.objects.filter(pk=registration.audit_progress.pk).update(
            registration_complete=True
        )
        # TODO need to update this function and the registration_date function to include lead clinician
        # trigger a GET request from the steps template
        trigger_client_event(
            response=response,
            name="registration_active",
            params={})  # reloads the form to show the active steps

    return response


def registration_status(request, registration_id):

    registration = Registration.objects.get(pk=registration_id)
    case = registration.case

    context = {
        'case_id': case.pk,
        'registration': registration
    }

    return render(request=request, template_name='epilepsy12/partials/registration/registration_dates.html', context=context)


@login_required
def registration_date(request, case_id):
    """
    This defines registration in the audit. 
    Call back from POST request on button press of register button
    in registration_dates partial.
    This sets the registration date, and in turn, the cohort number
    It also triggers htmx 'registration_active' to enable the steps
    """
    registration_date = date.today()
    case = Case.objects.get(pk=case_id)

    # update the AuditProgress
    registration = Registration.objects.get(case=case_id)
    registration.registration_date = registration_date
    registration.audit_progress.registration_complete = True

    # update the Registration with the date and the audit_progress record
    registration.save()
    # if all registration components present, update AuditProcess
    registration = Registration.objects.filter(case=case_id).get()

    test_fields_update_audit_progress(registration)

    context = {
        'case_id': case_id,
        'registration': registration
    }

    response = render(
        request=request, template_name='epilepsy12/partials/registration/registration_dates.html', context=context)

    trigger_client_event(
        response=response,
        name="registration_active",
        params={})  # reloads the form to show the active steps

    return response


def total_fields_completed(model_instance):
    """
    Loops through all the fields in the model instance (except pk and related fields)
    and uses these to return a total number of fields that have already been completed.
    """
    counter = 0
    if model_instance.registration_date is not None:
        counter += 1
    if model_instance.referring_clinician is not None or model_instance.referring_clinician != '':
        counter += 1
    if model_instance.eligibility_criteria_met:
        counter += 1
    if Site.objects.filter(
        registration=model_instance,
        site_is_actively_involved_in_epilepsy_care=True,
        site_is_primary_centre_of_epilepsy_care=True
    ).exists():
        counter += 1

    return counter


def total_fields_expected(model_instance):
    """
    Returns the total number of fields that need to be scored to all the form to be complete
    In the Registration/Validation form this is:
    registration_date
    referring_clinician
    eligibility_criteria_met
    lead centre
    """
    return 4


def total_fields_completed(model_instance):
    # counts the number of completed fields
    fields = model_instance._meta.get_fields()

    counter = 0
    for field in fields:
        if (
            field.name is not None and
            field.name != 'id' and
            field.name != 'site' and
            field.name != 'initial_assessment'
            and field.name != 'initialassessment'
            and field.name != 'management'
            and field.name != 'investigations'
            and field.name != 'assessment'
            and field.name != 'epilepsy_context'
            and field.name != 'epilepsycontext'
            and field.name != 'registration'
        ):
            if getattr(model_instance, field.name) is not None:
                counter += 1
    return counter


def test_fields_update_audit_progress(model_instance):
    all_completed_fields = total_fields_completed(model_instance)
    all_fields = total_fields_expected(model_instance)
    AuditProgress.objects.filter(registration=model_instance).update(
        registration_total_expected_fields=all_fields,
        registration_total_completed_fields=all_completed_fields,
        registration_complete=all_completed_fields == all_fields
    )
