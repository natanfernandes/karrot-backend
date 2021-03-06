# Generated by Django 2.0.7 on 2018-07-17 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversations', '0013_conversation_is_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationThreadParticipant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('muted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='conversationmessage',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread_messages', to='conversations.ConversationMessage'),
        ),
        migrations.AddField(
            model_name='conversationthreadparticipant',
            name='seen_up_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='conversations.ConversationMessage'),
        ),
        migrations.AddField(
            model_name='conversationthreadparticipant',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='conversations.ConversationMessage'),
        ),
        migrations.AddField(
            model_name='conversationthreadparticipant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='conversationthreadparticipant',
            unique_together={('user', 'thread')},
        ),
    ]
