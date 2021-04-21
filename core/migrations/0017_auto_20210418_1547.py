# Generated by Django 3.2 on 2021-04-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210418_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='icone',
            field=models.CharField(choices=[('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile'), ('lni-users', 'Usuarios'), ('lni-layers', 'Design'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete')], max_length=12, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='expectativa',
            name='area',
            field=models.CharField(choices=[('Front-end', 'Frontend'), ('Full-stack', 'Fullstack'), ('Back-end', 'Backend'), ('Mobile', 'Mobile')], max_length=50, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='expectativa',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Frontend'), ('lni-laptop-phone', 'Responsivo'), ('lni-mobile', 'Mobile'), ('lni-cog', 'Backend')], max_length=20, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='expectativa',
            name='modalidade',
            field=models.CharField(choices=[('CLT', 'Clt'), ('PJ', 'Pessoa_juridica'), ('Estagio', 'estagio')], max_length=50, verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='modalidade',
            field=models.CharField(choices=[('Analista de Redes', 'Analista_cop'), ('CLT', 'Clt'), ('PJ', 'Pessoa juridica'), ('Estagio', 'estagio')], max_length=20, verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='tecnologia',
            name='icone',
            field=models.CharField(choices=[('lni-laptop-phone', 'Responsivo'), ('lni-layers', 'Design'), ('lni-github', 'Github'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-leaf', 'Folha')], max_length=20, verbose_name='Icone'),
        ),
    ]
