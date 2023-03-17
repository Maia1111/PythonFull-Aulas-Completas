from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='cargo',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cargo',
            field=models.ManyToManyField(to='autenticacao.cargos'),
        ),
    ]
