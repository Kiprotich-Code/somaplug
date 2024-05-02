from django.shortcuts import render, redirect
from .forms import AddQuoteForm, ContactListForm

# Create your views here.
def base(request):
    if request.method == 'POST':
        add_quote_form = AddQuoteForm(request.POST)
        contact_list_form = ContactListForm(request.POST)
        if add_quote_form.is_valid():
            add_quote_form.save()
            return redirect('home')
        
        if contact_list_form.is_valid():
            contact_list_form.save()
            return redirect('home')
        
    else:
        add_quote_form = AddQuoteForm()
        contact_list_form = ContactListForm()

    context = {
        'add_quote_form': add_quote_form,
        'contact_list_form': contact_list_form,
    }

    return render(request, 'index.html', context)