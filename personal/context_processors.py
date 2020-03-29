from account.models import Profile

import datetime


def info(request):
    jatyam = Profile.objects.get(id=1)
    year = datetime.date.today().year
    cr = f"{year} Jatyam"
    return {'jatyam': jatyam, 'cr': cr}
