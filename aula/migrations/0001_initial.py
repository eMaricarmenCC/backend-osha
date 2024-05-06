# Generated by Django 5.0.3 on 2024-05-06 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoRegistro',
            fields=[
                ('estregcod', models.AutoField(db_column='EstRegCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('estregnom', models.CharField(db_column='EstRegNom', max_length=40, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'EstadoRegistro',
                'verbose_name_plural': 'EstadosRegistro',
                'db_table': 'estado_registro',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('curcod', models.AutoField(db_column='CurCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('curnom', models.CharField(db_column='CurNom', max_length=80, verbose_name='Nombre')),
                ('curestregcod', models.ForeignKey(db_column='CurEstRegCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estadoregistro', verbose_name='Codigo EStReg')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'db_table': 'curso',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('estcod', models.AutoField(db_column='EstCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('estnom', models.CharField(db_column='EstNom', max_length=60, verbose_name='Nombre')),
                ('estape', models.CharField(db_column='EstApe', max_length=60, verbose_name='Apellidos')),
                ('estdocide', models.CharField(db_column='EstDocIde', max_length=50, verbose_name='Documento de identidad')),
                ('email', models.EmailField(db_column='EstEma', max_length=255, unique=True, verbose_name='Email')),
                ('estpai', models.CharField(blank=True, db_column='EstPai', max_length=50, verbose_name='Pais')),
                ('estciu', models.CharField(blank=True, db_column='EstCiu', max_length=50, verbose_name='Ciudad')),
                ('estdir', models.CharField(blank=True, db_column='EstDir', max_length=100, verbose_name='Direccion')),
                ('estestregcod', models.ForeignKey(db_column='EstEstReg', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estadoregistro')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'db_table': 'estudiante',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('exacod', models.AutoField(db_column='ExaCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('exacurcod', models.ForeignKey(db_column='ExaCurCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.curso', verbose_name='Codigo Curso')),
                ('exaestregcod', models.ForeignKey(db_column='ExaEstRegCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estadoregistro', verbose_name='Codigo EStReg')),
            ],
            options={
                'verbose_name': 'Examen',
                'verbose_name_plural': 'Examenes',
                'db_table': 'examen',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('modcod', models.AutoField(db_column='ModCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('modnom', models.CharField(db_column='ModNom', max_length=100, verbose_name='Nombre')),
                ('modcurcod', models.ForeignKey(db_column='ModCurCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.curso', verbose_name='Codigo Curso')),
                ('modestregcod', models.ForeignKey(db_column='ModEstRegCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estadoregistro', verbose_name='Codigo EStReg')),
            ],
            options={
                'verbose_name': 'Modulo',
                'verbose_name_plural': 'Modulos',
                'db_table': 'modulo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NotaCurso',
            fields=[
                ('notcurcod', models.AutoField(db_column='NotCurCod', primary_key=True, serialize=False, verbose_name='codigo')),
                ('notcurpun', models.DecimalField(db_column='NotCurPun', decimal_places=2, max_digits=5, verbose_name='Puntuacion')),
                ('notcurcurcod', models.ForeignKey(db_column='NotCurCurCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.curso', verbose_name='Codigo Curso')),
                ('notcurestcod', models.ForeignKey(db_column='NotCurEstCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estudiante', verbose_name='Codio Estudiante')),
            ],
            options={
                'verbose_name': 'NotaCurso',
                'verbose_name_plural': 'NotaCursos',
                'db_table': 'nota_curso',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('precod', models.AutoField(db_column='preCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('pretex', models.CharField(db_column='PreTex', max_length=300, verbose_name='Texto')),
                ('preestregcod', models.ForeignKey(db_column='PreEstRegCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estadoregistro', verbose_name='Codigo EStReg')),
                ('preexacod', models.ForeignKey(db_column='PreExaCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.examen', verbose_name='Codigo EXamen')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Pregunta',
                'db_table': 'Pregunta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('altcod', models.AutoField(db_column='AltCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('alttex', models.CharField(db_column='AltTex', max_length=500, verbose_name='Texto')),
                ('altCor', models.BooleanField(db_column='AltCor', verbose_name='Correcto')),
                ('altestregcod', models.ForeignKey(db_column='AltEstRegCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estadoregistro', verbose_name='Codigo EstReg')),
                ('altprecod', models.ForeignKey(db_column='AltPreCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.pregunta', verbose_name='Codigo Pregunta')),
            ],
            options={
                'verbose_name': 'Alternativa',
                'verbose_name_plural': 'Alternativas',
                'db_table': 'alternativa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('procod', models.AutoField(db_column='ProCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('pronom', models.CharField(db_column='ProNom', max_length=100, verbose_name='Nombre')),
                ('procodosh', models.CharField(db_column='ProCodOsh', max_length=30, verbose_name='Codigo osha')),
                ('proestregcod', models.ForeignKey(db_column='ProEstRegCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estadoregistro', verbose_name='Codigo EstReg')),
            ],
            options={
                'verbose_name': 'Programa',
                'verbose_name_plural': 'Programas',
                'db_table': 'programa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('matcod', models.AutoField(db_column='MatCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('matestcod', models.ForeignKey(db_column='MatEstCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estudiante', verbose_name='Codigo Estudiante')),
                ('matestregcod', models.ForeignKey(db_column='MatEstRegCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estadoregistro', verbose_name='Codigo EstReg')),
                ('matprocod', models.ForeignKey(db_column='MatProCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.programa', verbose_name='Codigo Programa')),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
                'db_table': 'matricula',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='curprocod',
            field=models.ForeignKey(db_column='CurProCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.programa', verbose_name='Codigo Programa'),
        ),
        migrations.CreateModel(
            name='NotaPrograma',
            fields=[
                ('notprocod', models.AutoField(db_column='NotProCod', primary_key=True, serialize=False, verbose_name='codigo')),
                ('notpropun', models.DecimalField(db_column='NotProPun', decimal_places=2, max_digits=5, verbose_name='Puntuacion')),
                ('notproestcod', models.ForeignKey(db_column='NotProEstCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estudiante', verbose_name='Codio Estudiante')),
                ('notproprocod', models.ForeignKey(db_column='NotProProCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.programa', verbose_name='Codigo Programa')),
            ],
            options={
                'verbose_name': 'NotaPrograma',
                'verbose_name_plural': 'NotaProgramas',
                'db_table': 'nota_programa',
                'managed': True,
                'unique_together': {('notproestcod', 'notproprocod')},
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('rescod', models.AutoField(db_column='ResCod', primary_key=True, serialize=False, verbose_name='Codigo')),
                ('respun', models.DecimalField(db_column='ResPun', decimal_places=2, max_digits=5, verbose_name='Puntuacion')),
                ('resaltcod', models.ForeignKey(db_column='ResAltCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.alternativa', verbose_name='Codigo Alternativa')),
                ('resestcod', models.ForeignKey(db_column='ResEstCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estudiante', verbose_name='Codigo Estudiante')),
                ('resestregcod', models.ForeignKey(db_column='AltEstRegCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.estadoregistro', verbose_name='Codigo EstReg')),
                ('resexacod', models.ForeignKey(db_column='ResExaCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.examen', verbose_name='Codigo Examen')),
                ('resprecod', models.ForeignKey(db_column='ResPreCod', on_delete=django.db.models.deletion.DO_NOTHING, to='aula.pregunta', verbose_name='Codigo Pregunta')),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
                'db_table': 'respuesta',
                'managed': True,
                'unique_together': {('resestcod', 'resexacod', 'resprecod')},
            },
        ),
    ]
