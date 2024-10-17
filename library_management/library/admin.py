# Register your models here.
from django.contrib import admin
from library.models import Book, LibraryUser, Transaction

class BookAdmin(admin.ModelAdmin):
    pass

class LibraryUserAdmin(admin.ModelAdmin):
    pass

class TransactionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(LibraryUser, LibraryUserAdmin)
admin.site.register(Transaction, TransactionAdmin)