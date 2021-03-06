# Generated by Django 3.2 on 2021-04-18 17:57

import core.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210418_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('linkedin', models.CharField(default='#', max_length=100, verbose_name='Linkedin')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('github', models.CharField(default='#', max_length=100, verbose_name='Github')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.AlterField(
            model_name='curso',
            name='icone',
            field=models.CharField(choices=[('lni-users', 'Usuarios'), ('lni-stats-up', 'Gráfico'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete')], max_length=12, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='expectativa',
            name='area',
            field=models.CharField(choices=[('Mobile', 'Mobile'), ('Full-stack', 'Fullstack'), ('Back-end', 'Backend'), ('Front-end', 'Frontend')], max_length=50, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='expectativa',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Frontend'), ('lni-laptop-phone', 'Responsivo'), ('lni-cog', 'Backend'), ('lni-mobile', 'Mobile')], max_length=20, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='expectativa',
            name='modalidade',
            field=models.CharField(choices=[('Estagio', 'estagio'), ('PJ', 'Pessoa_juridica'), ('CLT', 'Clt')], max_length=50, verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='modalidade',
            field=models.CharField(choices=[('Estagio', 'estagio'), ('PJ', 'Pessoa juridica'), ('Analista de Redes', 'Analista_cop'), ('CLT', 'Clt')], max_length=20, verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='tecnologia',
            name='icone',
            field=models.CharField(choices=[('lni-github', 'Github'), ('lni-laptop-phone', 'Responsivo'), ('lni-cog', 'Engrenagem'), ('lni-layers', 'Design'), ('lni-leaf', 'Folha'), ('lni-rocket', 'Foguete')], max_length=20, verbose_name='Icone'),
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
    ]
