from django.shortcuts import render,redirect
from .models import Contact
from .form import CreateContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def dashboard(request):
    return render(request,'contacts/dashboard.html')

def create_contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.success(request,'Contact created successfully...')
            return redirect('all-contacts')
        else:
            return render(request,'contacts/create-contact.html',{'form':form})
    else:
        form = CreateContactForm()
        return render(request,'contacts/create-contact.html',{'form':form})

def all_contacts(request):
    contacts = Contact.objects.filter(user = request.user,is_deleted = False)
    return render(request,'contacts/all-contacts.html',{'contacts':contacts})

def edit_contact(request,pk):
    contact = Contact.objects.get(pk =pk)
    if request.method == 'POST':
        form = CreateContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('all-contacts')
        else:
            messages.warning(request,'Oops, something went wrong.Please try again.')
            return render(request,'contacts/contact.html',{'form':form})
    else:
        form = CreateContactForm(instance=contact)
        return render(request,'contacts/contact.html',{'form':form,'contact':contact})
    
def move_to_trash(request,pk):
    contact = Contact.objects.get(pk=pk)
    contact.is_deleted = True
    contact.save()
    return redirect('all-contacts')

def contacts_trash(request):
    contacts = Contact.objects.filter(is_deleted = True,user = request.user)
    return render(request,'contacts/trash.html',{'contacts':contacts})

def restore_contact(request,pk):
    contact = Contact.objects.get(pk=pk)
    contact.is_deleted = False
    contact.save()
    return redirect('trash')

def delete_contact(request,pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('trash')



