from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.
from .models import Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# photo list view
def photo_list(request):
    photos =Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

# Create -- CreateView
class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text'] # +author, created
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        # set login user id automatically
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/') # redirect to index.html
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'
    # redirects automatically to the detail template
