from django.apps import AppConfig


class WeeklyScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weekly_schedule'

def ready(self):
    import weekly_schedule.signals