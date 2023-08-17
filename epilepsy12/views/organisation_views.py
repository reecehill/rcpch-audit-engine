# Python/Django imports

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

# third party libraries
from django_htmx.http import HttpResponseClientRedirect
from django.db.models import Sum

# E12 imports
from django.apps import apps
from ..decorator import user_may_view_this_organisation
from epilepsy12.constants import (
    INDIVIDUAL_KPI_MEASURES,
    EnumAbstractionLevel,
)
from epilepsy12.models import (
    Organisation,
    Case,
    KPI,
    OrganisationKPIAggregation,
    TrustKPIAggregation,
    NHSRegionKPIAggregation,
    CountryKPIAggregation,
)
from ..common_view_functions import (
    sanction_user,
    trigger_client_event,
    cases_aggregated_by_sex,
    cases_aggregated_by_ethnicity,
    cases_aggregated_by_deprivation_score,
    all_registered_cases_for_cohort_and_abstraction_level,
    return_all_aggregated_kpis_for_cohort_and_abstraction_level_annotated_by_sublevel,
    return_tile_for_region,
    get_filtered_cases_queryset_for,
    calculate_kpi_value_counts_queryset,
    update_kpi_aggregation_model,
    get_abstraction_model_from_level,
    get_total_cases_registered_for_abstraction_level,
)
from ..general_functions import (
    get_current_cohort_data,
    value_from_key,
    calculate_kpi_average,
)
from ..constants import colors

from ..tasks import (
    aggregate_kpis_for_each_level_of_abstraction_by_organisation_asynchronously,
)


@login_required
@user_may_view_this_organisation()
def selected_organisation_summary(request, organisation_id):
    """
    This function presents the organisation view - comprising the organisation contact details,
    a demographic summary of the hospital trust and a table summary of the key performance indicators
    for that organisation, its parent trust, as well as comparisons at different levels of abstraction
    (eg nhs region, ICB, OPENUK region and so on)
    If a POST request from selected_organisation_summary.html on organisation select, it returns epilepsy12/partials/selected_organisation_summary.html
    Otherwise it returns the organisation.html template
    """

    nhsregion_tiles = return_tile_for_region("nhs_region")
    icb_tiles = return_tile_for_region("icb")
    country_tiles = return_tile_for_region("country")

    if request.POST.get("selected_organisation_summary") is not None:
        selected_organisation = Organisation.objects.get(
            pk=request.POST.get("selected_organisation_summary")
        )
        template_name = "epilepsy12/partials/selected_organisation_summary.html"
    else:
        # selected_organisation = return_selected_organisation(user=request.user)
        selected_organisation = Organisation.objects.get(pk=organisation_id)
        template_name = "epilepsy12/organisation.html"

    lhb_tiles = None

    if selected_organisation.ons_region.ons_country.Country_ONS_Name == "Wales":
        lhb_tiles = return_tile_for_region("lhb")

    cohort_data = get_current_cohort_data()

    # query to return all completed E12 cases in the current cohort in this organisation
    count_of_current_cohort_registered_completed_cases_in_this_organisation = (
        all_registered_cases_for_cohort_and_abstraction_level(
            organisation_instance=selected_organisation,
            cohort=cohort_data["cohort"],
            case_complete=True,
            abstraction_level="organisation",
        ).count()
    )

    # query to return all completed E12 cases in the current cohort in this organisation trust
    count_of_current_cohort_registered_completed_cases_in_this_trust = (
        all_registered_cases_for_cohort_and_abstraction_level(
            organisation_instance=selected_organisation,
            cohort=cohort_data["cohort"],
            case_complete=True,
            abstraction_level="trust",
        ).count()
    )
    # query to return all cases (including incomplete) registered in the current cohort at this organisation
    count_of_all_current_cohort_registered_cases_in_this_organisation = (
        all_registered_cases_for_cohort_and_abstraction_level(
            organisation_instance=selected_organisation,
            cohort=cohort_data["cohort"],
            case_complete=False,
            abstraction_level="organisation",
        ).count()
    )
    # query to return all cases (including incomplete) registered in the current cohort at this organisation trust
    count_of_all_current_cohort_registered_cases_in_this_trust = (
        all_registered_cases_for_cohort_and_abstraction_level(
            organisation_instance=selected_organisation,
            cohort=cohort_data["cohort"],
            case_complete=False,
            abstraction_level="trust",
        ).count()
    )

    if count_of_current_cohort_registered_completed_cases_in_this_organisation > 0:
        total_percent_organisation = int(
            (
                count_of_current_cohort_registered_completed_cases_in_this_organisation
                / (count_of_all_current_cohort_registered_cases_in_this_organisation)
            )
            * 100
        )

    else:
        total_percent_organisation = 0

    if count_of_current_cohort_registered_completed_cases_in_this_trust > 0:
        total_percent_trust = int(
            (
                count_of_current_cohort_registered_completed_cases_in_this_trust
                / (count_of_all_current_cohort_registered_cases_in_this_trust)
                * 100
            )
        )
    else:
        total_percent_trust = 0

    context = {
        "user": request.user,
        "selected_organisation": selected_organisation,
        "organisation_list": Organisation.objects.order_by("OrganisationName").all(),
        "cases_aggregated_by_ethnicity": cases_aggregated_by_ethnicity(
            selected_organisation=selected_organisation
        ),
        "cases_aggregated_by_sex": cases_aggregated_by_sex(
            selected_organisation=selected_organisation
        ),
        "cases_aggregated_by_deprivation": cases_aggregated_by_deprivation_score(
            selected_organisation=selected_organisation
        ),
        "percent_completed_organisation": total_percent_organisation,
        "percent_completed_trust": total_percent_trust,
        "count_of_all_current_cohort_registered_cases_in_this_organisation": count_of_all_current_cohort_registered_cases_in_this_organisation,
        "count_of_current_cohort_registered_completed_cases_in_this_organisation": count_of_current_cohort_registered_completed_cases_in_this_organisation,
        "count_of_all_current_cohort_registered_cases_in_this_trust": count_of_all_current_cohort_registered_cases_in_this_trust,
        "count_of_current_cohort_registered_completed_cases_in_this_trust": count_of_current_cohort_registered_completed_cases_in_this_trust,
        "cohort_data": cohort_data,
        "individual_kpi_choices": INDIVIDUAL_KPI_MEASURES,
        "nhsregion_tiles": nhsregion_tiles,
        "icb_tiles": icb_tiles,
        "country_tiles": country_tiles,
        "lhb_tiles": lhb_tiles,
    }

    return render(
        request=request,
        template_name=template_name,
        context=context,
    )


@login_required
@user_may_view_this_organisation()
def selected_trust_kpis(request, organisation_id):
    """
    HTMX get request returning trust_level_kpi.html partial

    This aggregates all KPI measures at different levels of abstraction related to the selected organisation
    Organisation level, Trust level, ICB level, NHS Region, OPEN UK level, country level and national level.
    """

    # Get all relevant Cases for this cohort
    cohort = get_current_cohort_data()["cohort"]
    organisation = Organisation.objects.get(pk=organisation_id)

    ALL_DATA = {}
    for enum_abstraction_level in EnumAbstractionLevel:
    
        filtered_cases = get_filtered_cases_queryset_for(
            abstraction_level=enum_abstraction_level,
            cohort=cohort,
        )

        # For these Cases, calculate KPI value counts, grouped by specified abstraction level
        kpi_value_counts = calculate_kpi_value_counts_queryset(
            filtered_cases=filtered_cases,
            abstraction_level=enum_abstraction_level,
            kpis="all",
        )

        # Update the relevant abstraction's KPIAggregation model(s)
        update_kpi_aggregation_model(
            abstraction_level=enum_abstraction_level,
            kpi_value_counts=kpi_value_counts,
            cohort=cohort,
        )

        # For the given abstraction, get the {ABSTRACTION}KPIAggregation model
        abstraction_kpi_agg_model_name = get_abstraction_model_from_level(
            enum_abstraction_level
        )["kpi_aggregation_model"]
        abstraction_kpi_agg_model = apps.get_model(
            "epilepsy12", abstraction_kpi_agg_model_name
        )

        # Get this organisation instance's abstraction relation entity. All the enum values are with respect to Organisation, thus the first element of .split('__') is the related field.
        abstraction_relation_field_name = enum_abstraction_level.value.split("__")[0]

        if enum_abstraction_level is EnumAbstractionLevel.ORGANISATION:
            abstraction_relation = organisation
        else:
            abstraction_relation = getattr(
                organisation, f"{abstraction_relation_field_name}"
            )
            if enum_abstraction_level is EnumAbstractionLevel.COUNTRY:
                abstraction_relation = getattr(abstraction_relation, "ons_country")

        # Get total cases
        total_cases_registered = get_total_cases_registered_for_abstraction_level(
            organisation=organisation,
            abstraction_level=enum_abstraction_level,
            cohort=cohort,
        )

        # Check if KPIAggregation model exists. If Organisation does not have any cases where that Organisation is primary care Site, then the KPIAgg will not exist.
        if abstraction_kpi_agg_model.objects.filter(
            abstraction_relation=abstraction_relation,
            cohort=cohort,
        ).exists():
            ALL_DATA[f"{enum_abstraction_level.name}_KPIS"] = {
                "aggregation_model": abstraction_kpi_agg_model.objects.get(
                    abstraction_relation=abstraction_relation,
                    cohort=cohort,
                ),
                "total_cases_registered": total_cases_registered,
            }
        else:
            ALL_DATA[f"{enum_abstraction_level.name}_KPIS"] = {
                "aggregation_model": None,
                "total_cases_registered": total_cases_registered,
            }
    [print(d) for d in ALL_DATA.items()]
    print(ALL_DATA['ORGANISATION_KPIS']['aggregation_model'].get_value_counts_for_kpis(['paediatrician_with_expertise_in_epilepsies']))
    
    # TODO: national kpi not yet implemented but placeholder
    ALL_DATA['NATIONAL_KPIS'] = {}
    
    context = {
        "organisation": organisation,
        "all_data": ALL_DATA,
        "kpis": KPI(),  # Instance of KPI to access field name help text attributes for KPI "Indicator" row values in table
        "open_access": False,
    }

    # TODO: 17/8/2023 -> check with @eatyourpeas re this trigger client code
    # response = render(request=request, template_name=template_name, context=context)

    # # trigger a GET request from the steps template
    # trigger_client_event(
    #     response=response, name="registration_active", params={}
    # )  # reloads the form to show the active steps

    return render(
        request=request,
        template_name="epilepsy12/partials/kpis/kpis.html",
        context=context,
    )


def selected_trust_kpis_open(request, organisation_id):
    """
    Open access endpoint for KPIs table
    """

    organisation = Organisation.objects.get(pk=organisation_id)

    # run the aggregations TODO This will need ultimately throttling to run only periodically

    # get aggregated KPIs for level of abstraction from KPIAggregation

    # create an empty instance of KPI model to access the labels - this is a bit of a hack but works and
    # and has very little overhead
    kpis = KPI.objects.create(
        organisation=organisation,
        parent_trust=organisation.ParentOrganisation_OrganisationName,
    )

    template_name = "epilepsy12/partials/kpis/kpis.html"
    context = {
        "organisation": organisation,
        # "organisation_kpis": organisation_kpis,
        # "trust_kpis": trust_kpis,
        # "icb_kpis": icb_kpis,
        # "nhs_kpis": nhs_kpis,
        # "open_uk_kpis": open_uk_kpis,
        # "country_kpis": country_kpis,
        # "national_kpis": national_kpis,
        "kpis": kpis,
        "organisation_list": Organisation.objects.all().order_by("OrganisationName"),
        "open_access": True,
    }

    # remove the temporary instance as otherwise would contribute to totals
    kpis.delete()

    response = render(request=request, template_name=template_name, context=context)

    return response


@login_required
@user_may_view_this_organisation()
def child_organisation_select(request, organisation_id, template_name):
    """
    POST call back from organisation_select to allow user to toggle between organisations in selected trust
    """

    selected_organisation_id = request.POST.get("child_organisation_select")

    # get currently selected organisation
    organisation = Organisation.objects.get(pk=selected_organisation_id)

    # trigger page reload with new organisation
    return HttpResponseClientRedirect(
        reverse(template_name, kwargs={"organisation_id": organisation.pk})
    )


@login_required
@user_may_view_this_organisation()
def view_preference(request, organisation_id, template_name):
    """
    POST request from Toggle in has rcpch_view_preference.html template
    Users can toggle between national, trust and organisation views.
    Only RCPCH staff can request a National level.
    """
    organisation = Organisation.objects.get(pk=organisation_id)

    request.user.view_preference = request.htmx.trigger_name
    request.user.save()

    return HttpResponseClientRedirect(
        reverse(template_name, kwargs={"organisation_id": organisation.pk})
    )


# @login_required
# @user_may_view_this_organisation()
def selected_trust_select_kpi(request, organisation_id):
    """
    POST request from dropdown in selected_organisation_summary.html

    It takes the kpi_name parameter in the HTMX request which contains the value of the selected KPI measure from
    the select field. This is then aggregated across the levels of abstraction
    """

    organisation = Organisation.objects.get(pk=organisation_id)
    kpi_name = request.POST.get("kpi_name")
    if kpi_name is None:
        # on page load there may be no kpi_name - default to paediatrician_with_experise_in_epilepsy
        kpi_name = INDIVIDUAL_KPI_MEASURES[0][0]
    kpi_value = value_from_key(key=kpi_name, choices=INDIVIDUAL_KPI_MEASURES)
    cohort_data = get_current_cohort_data()

    all_aggregated_kpis_by_open_uk_region_in_current_cohort = return_all_aggregated_kpis_for_cohort_and_abstraction_level_annotated_by_sublevel(
        cohort=cohort_data["cohort"], abstraction_level="open_uk", kpi_measure=kpi_name
    )
    open_uk_avg = calculate_kpi_average(
        decimal_places=1,
        kpi_data=all_aggregated_kpis_by_open_uk_region_in_current_cohort,
        kpi=kpi_name,
    )

    all_aggregated_kpis_by_nhs_region_in_current_cohort = return_all_aggregated_kpis_for_cohort_and_abstraction_level_annotated_by_sublevel(
        cohort=cohort_data["cohort"],
        abstraction_level="nhs_region",
        kpi_measure=kpi_name,
    )
    nhs_region_avg = calculate_kpi_average(
        decimal_places=1,
        kpi_data=all_aggregated_kpis_by_nhs_region_in_current_cohort,
        kpi=kpi_name,
    )

    all_aggregated_kpis_by_icb_in_current_cohort = return_all_aggregated_kpis_for_cohort_and_abstraction_level_annotated_by_sublevel(
        cohort=cohort_data["cohort"], abstraction_level="icb", kpi_measure=kpi_name
    )
    icb_avg = calculate_kpi_average(
        decimal_places=1,
        kpi_data=all_aggregated_kpis_by_icb_in_current_cohort,
        kpi=kpi_name,
    )

    all_aggregated_kpis_by_country_in_current_cohort = return_all_aggregated_kpis_for_cohort_and_abstraction_level_annotated_by_sublevel(
        cohort=cohort_data["cohort"], abstraction_level="country", kpi_measure=kpi_name
    )
    country_avg = calculate_kpi_average(
        decimal_places=1,
        kpi_data=all_aggregated_kpis_by_country_in_current_cohort,
        kpi=kpi_name,
    )

    context = {
        "kpi_name": kpi_name,
        "kpi_value": kpi_value,
        "selected_organisation": organisation,
        "open_uk": all_aggregated_kpis_by_open_uk_region_in_current_cohort,
        "open_uk_avg": open_uk_avg,
        "open_uk_title": f"{kpi_value} by OPEN UK Region",
        "open_uk_id": "open_uk_id",
        "icb": all_aggregated_kpis_by_icb_in_current_cohort,
        "icb_avg": icb_avg,
        "icb_title": f"{kpi_value} by Integrated Care Board",
        "icb_id": "icb_id",
        "nhs_region": all_aggregated_kpis_by_nhs_region_in_current_cohort,
        "nhs_region_avg": nhs_region_avg,
        "nhs_region_title": f"{kpi_value} by NHS Region",
        "nhs_region_id": "nhs_region_id",
        "country": all_aggregated_kpis_by_country_in_current_cohort,
        "country_avg": country_avg,
        "country_title": f"{kpi_value} by Country",
        "country_id": "country_id",
        # ADD COLOR PER ABSTRACTION
        "icb_color": colors.RCPCH_AQUA_GREEN,
        "open_uk_color": colors.RCPCH_LIGHT_BLUE,
        "nhs_region_color": colors.RCPCH_STRONG_BLUE,
        "country_color": colors.RCPCH_DARK_BLUE,
        "individual_kpi_choices": INDIVIDUAL_KPI_MEASURES,
    }

    template_name = "epilepsy12/partials/organisation/metric.html"

    return render(request=request, template_name=template_name, context=context)
