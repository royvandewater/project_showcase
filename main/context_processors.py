from models import Setting

def load_setting(request):
    setting_model = Setting.objects.get(active=True)
    setting = {'THEME':setting_model.theme}
    return setting
