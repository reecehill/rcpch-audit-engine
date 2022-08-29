# Generated by Django 4.0.4 on 2022-08-29 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0072_episode_nonepileptic_seizure_behavioural_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiaxialDiagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>')),
                ('syndrome_present', models.BooleanField(blank=True, default=None, null=True, verbose_name='Is there an identifiable epilepsy syndrome?')),
                ('seizure_cause_main', models.CharField(blank=True, choices=[('Str', 'Structural'), ('Gen', 'Genetic'), ('Inf', 'Infectious'), ('Met', 'Metabolic'), ('Imm', 'Immune'), ('NK', 'Not known')], default=None, max_length=3, null=True, verbose_name='main identified cause of seizure(s)')),
                ('seizure_cause_structural', models.CharField(blank=True, choices=[('FCD', 'Focal cortical dysplasia'), ('HyH', 'Hypothalamic Hamartoma'), ('LGT', 'Low grade tumour'), ('MCD', 'Malformations of Cortical Development'), ('NR', 'Not required'), ('StW', 'Sturge Weber'), ('TBI', 'Traumatic brain injury'), ('TbS', 'Tuberous Sclerosis'), ('TuO', 'Tumour (other)'), ('Vas', 'Vascular (eg arterial ischaemic stroke venous ischaemia cerebral haemorrhage)')], default=None, max_length=3, null=True, verbose_name='main identified structural cause of seizure(s)')),
                ('seizure_cause_genetic', models.CharField(blank=True, choices=[('AnS', 'Angelman Syndrome'), ('ChA', 'Chromosomal abnormality'), ('DrS', 'Dravet syndrome'), ('GTD', 'Glucose Transporter Defect'), ('GeA', 'Gene abnormality'), ('ReS', 'Rett Syndrome')], default=None, max_length=3, null=True, verbose_name='main identified genetic cause of seizure(s)')),
                ('seizure_cause_gene_abnormality', models.CharField(blank=True, choices=[('UBE', 'UBE3A'), ('GLU', 'GLUT1'), ('SLC', 'SLC2A1'), ('MEC', 'MECP2'), ('SCN', 'SCN1A'), ('STX', 'STXBP1'), ('CDK', 'CDKL5'), ('KCN', 'KCNQ2'), ('SCN', 'SCN2A'), ('KCN', 'KCNT1'), ('ARX', 'ARX'), ('FOX', 'FOXG1'), ('PCD', 'PCDH19'), ('GRI', 'GRIN2A'), ('Oth', 'Other')], default=None, max_length=3, null=True, verbose_name='main identified gene abnormality cause of seizure(s)')),
                ('seizure_cause_genetic_other', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='other identified genetic cause of seizure(s) not previously specified.')),
                ('seizure_cause_chromosomal_abnormality', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='main identified chromosomal cause of seizure(s)')),
                ('seizure_cause_infectious', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='main identified infectious cause of seizure(s)')),
                ('seizure_cause_metabolic', models.CharField(blank=True, choices=[('Mit', 'Mitochondrial disorder'), ('Neu', 'Neuronal Ceroid Lipofuscinosis (Batten Disease)'), ('PPM', 'Disorder of pyridoxine/pyridoxal phosphate metabolism'), ('BiM', 'Disorder of biotin metabolism'), ('CrM', 'Disorder of creatine metabolism'), ('AmA', 'Disorder of amino acid'), ('UrA', 'Disorder of urea cycle'), ('PyP', 'Disorder of pyrimidine and purine'), ('Cho', 'Disorder of cholesterol'), ('Oth', 'Other neurometabolic disorder')], default=None, max_length=3, null=True, verbose_name='main identified metabolic cause of seizure(s)')),
                ('seizure_cause_metabolic_other', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='other identified metabolic cause of seizure(s) not previously specified.')),
                ('seizure_cause_immune', models.CharField(blank=True, choices=[('RaE', 'Rasmussen Encephalitis'), ('AnM', 'Antibody mediated')], default=None, max_length=3, null=True, verbose_name='main identified immune cause of seizure(s).')),
                ('seizure_cause_immune_antibody', models.CharField(blank=True, choices=[('GAD', 'GAD'), ('MOG', 'MOG'), ('NMD', 'NMDAR'), ('Oth', 'Other'), ('TPO', 'TPO'), ('VGK', 'VGKC')], default=None, max_length=3, null=True, verbose_name='autoantibody identified as cause of seizure(s).')),
                ('seizure_cause_immune_antibody_other', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='other identified antibody not previously specified causing seizure(s).')),
                ('relevant_impairments_behavioural_educational', models.BooleanField(blank=True, default=None, max_length=50, null=True, verbose_name='Are there any relevant impairments: behavioural or educational, emotional problems?')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='record created by user in %(class)')),
            ],
            options={
                'verbose_name': 'DESSCRIBE assessment',
                'verbose_name_plural': 'DESSCRIBE assessments',
            },
        ),
        migrations.RemoveField(
            model_name='episode',
            name='registration',
        ),
        migrations.AlterField(
            model_name='antiepilepsymedicine',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='antiepilepsymedicine',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='case',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='case',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='comorbidity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='comorbidity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='desscribe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='desscribe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='epilepsycontext',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='epilepsycontext',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='initialassessment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='initialassessment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='investigations',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='investigations',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='management',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='management',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='site',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>'),
        ),
        migrations.AlterField(
            model_name='site',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>'),
        ),
        migrations.CreateModel(
            name='Syndrome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x1082b4f70>')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x1082b4f70>')),
                ('syndrome_diagnosis_date', models.DateField(blank=True, default=None, null=True, verbose_name='The date the syndrome diagnosis was made.')),
                ('syndrome_name', models.IntegerField(blank=True, choices=[(27, 'CDKL5-DEE'), (16, 'Childhood absence epilepsy'), (5, 'Childhood occipital visual epilepsy'), (34, 'DEE or EE with spike-and-wave activation in sleep'), (23, 'Dravet syndrome'), (20, 'Early infantile DEE'), (21, 'Epilepsy of infancy with migrating focal seizures'), (11, 'Epilepsy with auditory features'), (15, 'Epilepsy with eyelid myoclonia'), (19, 'Epilepsy with generalized tonic–clonic seizures alone'), (14, 'Epilepsy with myoclonic absences'), (32, 'Epilepsy with myoclonic–atonic seizures'), (39, 'Epilepsy with reading-induced seizures'), (24, 'Etiology-specific DEEs'), (10, 'Familial focal epilepsy with variable foci'), (8, 'Familial mesial temporal lobe epilepsy'), (35, 'Febrile infection-related epilepsy syndrome'), (29, 'GLUT1DS-DEE'), (31, 'Gelastic seizures with HH'), (12, 'Genetic epilepsy with febrile seizures plus'), (36, 'Hemiconvulsion–hemiplegia–epilepsy'), (22, 'Infantile epileptic spasms syndrome'), (17, 'Juvenile absence epilepsy'), (18, 'Juvenile myoclonic epilepsy'), (25, 'KCNQ2-DEE'), (33, 'Lennox–Gastaut syndrome'), (7, 'Mesial temporal lobe epilepsy with hippocampal sclerosis'), (13, 'Myoclonic epilepsy in infancy'), (28, 'PCDH19 clustering epilepsy'), (6, 'Photosensitive occipital lobe epilepsy'), (38, 'Progressive myoclonus epilepsies'), (26, 'Pyridoxine-dependent and pyridox(am)ine 5′ phosphate deficiency DEE'), (37, 'Rasmussen syndrome'), (1, 'Self-limited (familial) infantile epilepsy'), (0, 'Self-limited (familial) neonatal epilepsy'), (4, 'Self-limited epilepsy with autonomic seizures'), (3, 'Self-limited epilepsy with centrotemporal spikes'), (2, 'Self-limited familial neonatal-infantile epilepsy'), (9, 'Sleep-related hypermotor (hyperkinetic) epilepsy'), (30, 'Sturge–Weber syndrome')], default=None, null=True, verbose_name='Select an identifiable epilepsy syndrome?')),
                ('syndrome_diagnosis_active', models.BooleanField(default=None, null=True, verbose_name='Is the diagnosis of the syndrome still active?')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='record created by user in %(class)')),
                ('multiaxial_diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epilepsy12.multiaxialdiagnosis')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='record updated by user in %(class)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='multiaxialdiagnosis',
            name='registration',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='epilepsy12.registration'),
        ),
        migrations.AddField(
            model_name='multiaxialdiagnosis',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='record updated by user in %(class)'),
        ),
        migrations.AddField(
            model_name='episode',
            name='multiaxial_diagnosis',
            field=models.ForeignKey(default=53, on_delete=django.db.models.deletion.CASCADE, to='epilepsy12.multiaxialdiagnosis'),
        ),
    ]
