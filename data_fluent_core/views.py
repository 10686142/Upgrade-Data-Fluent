from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required
def dashboard(request):
    return render(request, 'data_fluent_core/dashboard.html')


def mainReactApp(request):
    print(f"Starting react app....")
    # Info to pass down to request which passes it to React
    context = {
        'component': 'reactComponent',
        'props': {
            'ref': 'reactVS',
            'returnUrl': request.build_absolute_uri(), # The url from which the reques
        },
    }

    return render(request, 'data_fluent_core/main_app.html', context)
