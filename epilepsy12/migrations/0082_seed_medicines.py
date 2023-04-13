# Generated by Django 4.2 on 2023-04-12 13:53

from django.db import migrations
from ..constants import SNOMED_BENZODIAZEPINE_TYPES, SNOMED_ANTIEPILEPSY_MEDICINE_TYPES
from ..general_functions import fetch_ecl, fetch_concept


def seed_medicines(apps, schema_editor):
    """
    Loop through the medicines stored as constants - if exist in the database then skip
    If not, seed the database with name from constant, and if SNOMED record exists, store the conceptId
    """
    MedicineEntity = apps.get_model('epilepsy12', 'MedicineEntity')
    # drugs = fetch_ecl('<<255632006')
    # for drug in drugs:

    # if this drug is not in the table already
    for benzo in SNOMED_BENZODIAZEPINE_TYPES:
        if not MedicineEntity.objects.filter(
                medicine_name=benzo[1]).exists():
            # if the drug is not in the database already
            new_drug = MedicineEntity(
                medicine_name=benzo[1],
                is_rescue=True,
            )
            if benzo[0] not in [1001, 1002]:
                concept = fetch_ecl(benzo[0])
                new_drug.conceptId = concept[0]['conceptId'],
                new_drug.term = concept[0]['term'],
                new_drug.preferredTerm = concept[0]['preferredTerm']
            new_drug.save()
    for aem in SNOMED_ANTIEPILEPSY_MEDICINE_TYPES:
        if not MedicineEntity.objects.filter(
            medicine_name=aem[1],
            is_rescue=False
        ).exists():
            # if the drug is not in the database already
            aem_drug = MedicineEntity(
                medicine_name=aem[1],
            )
            if aem[0] not in [1001, 1002]:
                concept = fetch_ecl(int(aem[0]))
                aem_drug.conceptId = concept[0]['conceptId'],
                aem_drug.term = concept[0]['term'],
                aem_drug.preferredTerm = concept[0]['preferredTerm']
            aem_drug.save()


class Migration(migrations.Migration):
    dependencies = [
        ("epilepsy12", "0081_medicineentity_historicalmedicineentity"),
    ]

    operations = [
        migrations.RunPython(seed_medicines)
    ]
