from django.shortcuts import render, get_object_or_404
from django.contrib.auth import decorators
from django.urls import reverse_lazy, reverse

# Create your views here.
@decorators.login_required
def index(request):
    return render(request, 'dashboard/index.html')


from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from siteinfo.models import SiteSettings

class SiteSettingsUpdateView(LoginRequiredMixin, UpdateView):

    model = SiteSettings
    fields = '__all__'
    template_name = 'dashboard/sitesettings_update_form.html'



from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

class UserListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'dashboard/all_user_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extraProfile'] = UserProfile.objects.all()

        return context
    


class UserAccountCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_superuser'
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'user_permissions', 'is_superuser']
    template_name = 'auth/user_form.html'
    success_url = reverse_lazy('dashboard:profile_create')

    

class UserAccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    template_name = 'dashboard/user_form.html'

    

from dashboard.models import UserProfile
class UserProfileCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_superser'
    model = UserProfile
    fields = '__all__'
    success_url = reverse_lazy('dashboard:all-users')
    

    
class UserProfileUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'is_superuser'
    model = UserProfile
    #fields = '__all__'
    fields = ['nrc', 'phone', 'address', 'salary']
    #fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('dashboard:all-users')



    

class UserDeleteView(PermissionRequiredMixin, DeleteView):
    model = User



from products.models import Product, Stock, ProductImages, Price
class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/all_product_list.html'

    def get_queryset(self):
        return Product.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prices'] = Price.objects.all()
        context['stocks'] = Stock.objects.all()
        context['Pimages'] = ProductImages.objects.all()
        
        return context


    

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

  
    
class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_superuser'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('dashboard:product_stock_create')



    
class PriceCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_superuser'
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('dashboard:product_images_create')


    

class StockCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_superuser'
    model = Stock
    fields = '__all__'
    success_url = reverse_lazy('dashboard:product_price_create')


    

class ProductImagesCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_superuser'
    model = ProductImages
    fields = '__all__'
    success_url = reverse_lazy('dashboard:all-products')
