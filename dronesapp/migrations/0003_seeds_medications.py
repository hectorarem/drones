from django.db import migrations


def register_medications(apps, schema_editor):
    Medication = apps.get_model('dronesapp', 'Medication')
    # 1
    Medication.objects.get_or_create(
        name='MED_AaA_2025-02-05',
        weight_gr=10,
        code='MED_AAA',
        image='medication/aaa.jpeg',
    )
    # 2
    Medication.objects.get_or_create(
        name='MED_BbB_2025-02-05',
        weight_gr=100,
        code='MED_BBB',
        image='medication/bbb.jpeg',
    )
    # 3
    Medication.objects.get_or_create(
        name='MED_CcC_2025-02-05',
        weight_gr=90,
        code='MED_CCC',
        image='medication/ccc.jpeg',
    )
    # 4
    Medication.objects.get_or_create(
        name='MED_DdD_2025-02-05',
        weight_gr=200,
        code='MED_DDD',
        image='medication/ddd.jpeg',
    )
    # 5
    Medication.objects.get_or_create(
        name='MED_EeE_2025-02-05',
        weight_gr=105,
        code='MED_EEE',
        image='medication/eee.jpeg',
    )
    # 6
    Medication.objects.get_or_create(
        name='MED_FfF_2025-02-05',
        weight_gr=98,
        code='MED_FFF',
        image='medication/fff.jpeg',
    )
    # 7
    Medication.objects.get_or_create(
        name='MED_GgG_2025-02-05',
        weight_gr=300,
        code='MED_GGG',
        image='medication/ggg.jpeg',
    )
    # 8
    Medication.objects.get_or_create(
        name='MED_HhH_2025-02-05',
        weight_gr=10,
        code='MED_HHH',
        image='medication/hhh.jpeg',
    )
    # 9
    Medication.objects.get_or_create(
        name='MED_IiI_2025-02-05',
        weight_gr=135,
        code='MED_III',
        image='medication/iii.jpeg',
    )
    # 10
    Medication.objects.get_or_create(
        name='MED_JjJ_2025-02-05',
        weight_gr=300,
        code='MED_JJJ',
        image='medication/jjj.jpeg',
    )



def remove_medications(apps, schema_editor):
    Medication = apps.get_model('dronesapp', 'Medication')
    Medication.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('dronesapp', '0002_seeds_drones'),
    ]

    operations = [
        migrations.RunPython(register_medications, remove_medications),
    ]
