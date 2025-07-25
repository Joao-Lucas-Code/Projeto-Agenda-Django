from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from contact.models import Contact



def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(
            Q(show=True) &
            (Q(first_name__icontains=search_value) |
             Q(last_name__icontains=search_value) |
             Q(email__icontains=search_value))
        ) \
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'seach_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    contact_name = f'{single_contact.first_name} {single_contact.last_name}'

    context = {
        'contact': single_contact,
        'site_title': f'Contato - {contact_name} - '
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
