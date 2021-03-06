# Generated by Django 3.2 on 2021-04-19 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formations', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=3)),
                ('team_logo', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='formations.formation')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(blank=True, related_name='teams', to='players.Player')),
            ],
        ),
    ]
