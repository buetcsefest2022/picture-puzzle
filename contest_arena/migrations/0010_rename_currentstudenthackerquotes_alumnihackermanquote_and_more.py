# Generated by Django 4.0.5 on 2022-06-23 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest_arena', '0009_alter_puzzle_ans'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CurrentStudentHackerQuotes',
            new_name='AlumniHackermanQuote',
        ),
        migrations.RenameModel(
            old_name='AlumniHackermanQuotes',
            new_name='CurrentStudentHackerQuote',
        ),
    ]