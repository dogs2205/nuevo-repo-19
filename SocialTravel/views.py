from django.shortcuts import render
from SocialTravel.models import Post
from django.urls import reverse_lazy
from SocialTravel.forms import Post, PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm 

def index(request):
  return render(request, "SocialTravel/index.html")

def mostrar_otro_template(request):
  posts = Post.objects.all()
  return render(request, "SocialTravel/otro_template.html", {"posts": posts})

def mostrar_post(request):
    contex={
        "form":PostForm(),
   }
    return render(request, "SocialTravel/admin_post.html", contex)

def agregar_post(request):
    post_form=PostForm(request.POST)
    post_form.save()
    context={
        "posts": Post.objects.all(),
        "form":PostForm()

    }
    return render(request, "SocialTravel/admin_post.html", context)

def buscar_post(request):
    criterio = request.GET.get("criterio")
    context = { "posts": Post.objects.filter(carousel_caption_title__icontains=criterio).all()}
    
    return render(request, "SocialTravel/admin_post.html", context)

class PostList(ListView):
    model= Post
    context_object_name= "posts"

class PostDetail(DetailView):
    model = Post
    context_object_name= "post"

class PostDelete(DeleteView):
    model = Post
    context_object_name= "post"
    success_url = reverse_lazy("post-list")

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostSearch(ListView):
    model = Post
    
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = (Post.objects
        .filter(carousel_caption_title=criterio)
        .order_by("creado_el")
        .all())
        return result
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Resultados"
        return context

class Login(LoginView):
    next_page = reverse_lazy("index")

class SignUp(FormView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("post-list")




# Create your views here.
