from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render


@login_required
def profile_view(request):
    return render(request, 'accounts/account_detail.html')
