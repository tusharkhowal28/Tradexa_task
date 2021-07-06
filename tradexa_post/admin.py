
from django.contrib import admin
from .models import CustomUser,Post
from django.contrib.auth.admin import UserAdmin
from .forms import SignupForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    ordering = ('email',)

    model = CustomUser
    add_form = SignupForm

    fieldsets = (
        (None, {'fields': ('first_name','last_name','email', 'password', 'username', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('first_name','last_name','email', 'username', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)



    

admin.site.register(CustomUser ,CustomUserAdmin)
admin.site.register(Post)
