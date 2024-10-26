from typing import Any
from django.db.models.query import QuerySet #type:ignore 
from django.shortcuts import render # type: ignore
from .models import Notes
from django.http import Http404 # type: ignore
from django.views.generic import CreateView,DetailView,ListView,UpdateView # type: ignore
from.forms import Notesform
from django.views.generic.edit import DeleteView #type:ignore
from django.contrib.auth.mixins import LoginRequiredMixin#type:ignore
from django.http.response import HttpResponseRedirect #type:ignore 
# Create your views here.

# class NotesCreateView(CreateView):
#     model=Notes
#     fields=['title','notes']
#     success_url='/smart/notes'

class NotesDeleteView(DeleteView):
    model=Notes
    success_url='/smart/notes'
    template_name='notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model=Notes
    form_class=Notesform
    success_url='/smart/notes'

class NotesCreateView(CreateView):
    model=Notes
    form_class=Notesform
    success_url='/smart/notes'

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin,ListView):
    model=Notes
    context_object_name='notes' 
    template_name='notes/notes_list.html'
    login_url='/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

# def list(request):
#     all_notes=Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})

class NotesDetailView(DetailView):     # class based view takes care of exception for us 
    model=Notes
    context_object_name="note"


# def detail(request,pk):
#     try:
#         note=Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Notes does not exist')
#     return render(request,'notes/notes_detail.html',{'note':note})
