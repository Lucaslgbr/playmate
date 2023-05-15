import os
from django.conf import settings
from django.apps import apps
from django.core.management import BaseCommand
from playmate.team_management.models import DeployScript
import importlib

class Command(BaseCommand):
    scripts_path_name='deploy_scripts' 
    
    def handle(self, *args, **options):
        ran_functions = 0
        for app in apps.get_app_configs():
            full_path = os.path.join(settings.BASE_DIR,'playmate',app.label,self.scripts_path_name)
            if not os.path.exists(full_path):
                continue
            for filename in os.listdir(full_path):
                script_name = filename[:-3]
                if DeployScript.objects.filter(name=script_name,app=app.label).exists():
                    continue
                module = f"playmate.{app.label}.{self.scripts_path_name}.{script_name}"
                _module = importlib.import_module(module)
                callback = getattr(_module,'run')
                print(f'Running {script_name}...')
                callback()
                DeployScript.objects.get_or_create(name=script_name,app=app.label)
                ran_functions +=1
        
        if not ran_functions:
            print('No scripts to apply')
