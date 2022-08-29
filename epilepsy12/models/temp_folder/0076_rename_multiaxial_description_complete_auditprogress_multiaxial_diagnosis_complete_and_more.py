# Generated by Django 4.0.4 on 2022-08-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0075_alter_antiepilepsymedicine_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auditprogress',
            old_name='multiaxial_description_complete',
            new_name='multiaxial_diagnosis_complete',
        ),
        migrations.RenameField(
            model_name='auditprogress',
            old_name='multiaxial_description_total_completed_fields',
            new_name='multiaxial_diagnosis_total_completed_fields',
        ),
        migrations.RenameField(
            model_name='auditprogress',
            old_name='multiaxial_description_total_expected_fields',
            new_name='multiaxial_diagnosis_total_expected_fields',
        ),
        migrations.AlterField(
            model_name='antiepilepsymedicine',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='antiepilepsymedicine',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='case',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='case',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='comorbidity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='comorbidity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='epilepsycontext',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='epilepsycontext',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='initialassessment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='initialassessment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='investigations',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='investigations',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='management',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='management',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='multiaxialdiagnosis',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='multiaxialdiagnosis',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='site',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='site',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='syndrome',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='record created on <function now at 0x103a4cf70>'),
        ),
        migrations.AlterField(
            model_name='syndrome',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='record updated on <function now at 0x103a4cf70>'),
        ),
    ]
