# standard imports
import requests

# third party imports
from django.conf import settings

# RCPCH imports
from ..constants import BENZODIAZEPINE_TYPES, ANTIEPILEPSY_MEDICINE_TYPES


def fetch_snomed(sctid, syntax):
    """
    Makes an API call to the RCPCH hosted instance of Hermes - a SNOMED terminology server developed by @mwardle
    This function accepts a SNOMED CT ID, together with the relevant ECL syntax.

    ECL syntax options include: memberOf, descendentOf, descendentSelfOf, childOf, childSelfOf, ancestorOf, ancestorSelfOf, parentOf, parentSelfOf

    Brief syntax	Long syntax	        Description
        <!	        childOf	            Children
        <<!	        childOrSelfOf	    Concept itself and children
        <	        descendantOf	    Descendants
        <<	        descendantOrSelfOf	Concept itself and descendants
        >!	        parentOf	        Parents
        >>!	        parentOrSelfOf	    Concept itself and parents
        >	        ancestorOf	        Ascendants
        >>	        ancestorOrSelfOf	Concept itself and ascendants
        ^	        memberOf	        Members of a reference set
    """

    VALID_SYNTAX = {'conceptOnly': '', 'memberOf': '^', 'descendentOf': '<', 'descendentSelfOf': '<<', 'childOf': '<!',
                    'childSelfOf': '<<!', 'ancestorOf': '>', 'ancestorSelfOf': '>>', 'parentOf': '>!', 'parentSelfOf': '>>!'}

    if syntax not in VALID_SYNTAX:
        raise KeyError(f'This SNOMED syntax: {syntax} is wrong.')

    # epilepsy = <<84757009

    ecl_url = f'{settings.RCPCH_HERMES_SERVER_URL}/expand?ecl={VALID_SYNTAX[syntax]}{sctid}'

    response = requests.get(ecl_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def snomed_search(search_term):
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/search?s={search_term}&constraint=<64572001'

    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def fetch_all_epilepsy():
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/search?constraint=<<84757009&offset=0&limit=1000'

    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def fetch_all_hereditary_epilepsy():
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/search?constraint=(<< 84757009 AND << 363235000 )&offset=0&limit=1000'

    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def fetch_ecl(ecl):
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/search?constraint={ecl}'
    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def search_ecl(search, ecl):
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/search?s={search}&constraint={ecl}&offset=0&limit=1000'

    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def search_all_epilepsy(search):
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/search?s={search}&constraint=<<84757009&offset=0&limit=1000'

    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def search_all_hereditary_epilepsy(search):
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/search?s={search}&constraint=(<< 84757009 AND << 363235000 )&offset=0&limit=1000'

    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def snomed_search_congenital_neurology(search_term):
    # developmental hereditary disorder | 363070008
    # 57148006 |Congenital anomaly of brain (disorder)| +
    # 35919005 |Pervasive developmental disorder (disorder)| +
    # 363235000 |Hereditary disorder of nervous system (disorder)| +

    # 39367000 |Inflammatory disease of the central nervous system (disorder)|
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/search?s={search_term}&constraint=<84757009'

    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def snomed_medicine_search(search_term):
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/search?s={search_term}&constraint=<373873005'

    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def fetch_concept(concept_id):
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/concepts/{concept_id}/extended'

    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    serialised = response.json()

    return serialised


def fetch_paediatric_neurodisability_outpatient_diagnosis_simple_reference_set():
    search_url = f'{settings.RCPCH_HERMES_SERVER_URL}/expand?ecl=^999001751000000105'
    response = requests.get(search_url)

    if response.status_code == 404:
        print("Could not get SNOMED data from server...")
        return None

    # filters out Autism-related entries
    response_no_asd = [
        item for item in response.json() if item['conceptId'] != 35919005]

    return response_no_asd


def compare_snomed_with_constant_drugs():
    drugs = fetch_ecl('<<255632006')
    index = 0
    for drug in drugs:
        print(f"{drug['preferredTerm']}")
        for benzo in BENZODIAZEPINE_TYPES:
            if drug['preferredTerm'] == benzo[1]:
                print(f"{drug['preferredTerm']} is a match with {benzo[1]}")
        for aem in ANTIEPILEPSY_MEDICINE_TYPES:
            if drug['preferredTerm'] == aem[1]:
                print(f"{drug['preferredTerm']} is a match with {aem[1]}")
        index += 1
    print(f"{index} drugs checked for matches")
