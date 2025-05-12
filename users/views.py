from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def profile(request):
    """View function for the user profile page."""
    return render(request, 'users/profile.html')

@login_required
def my_books(request):
    """View function for displaying the user's books."""
    # Add logic to fetch the user's books
    return render(request, 'users/my_books.html')
