from django.contrib import admin
from .models import add_items
from .models import total
from .models import cart
from .models import useraddress
from .models import ordered_items
from .models import categories
from .models import technician
from .models import wishlist
from .models import review
from .models import contactdetails

class categoriesAdmin(admin.ModelAdmin):
    list_display = ('catid','category_name')
admin.site.register(categories,categoriesAdmin)

class add_itemAdmin(admin.ModelAdmin):
    list_display = ('item_id','item_name','category','sub_category','quantity','actual_price','image1','created_date','discount_price')
admin.site.register(add_items,add_itemAdmin)

class totalAdmin(admin.ModelAdmin):
    list_display = ('user','tpurchase')
admin.site.register(total,totalAdmin)

class cartAdmin(admin.ModelAdmin):
    list_display = ('user','itemname','category','quantity','total_price')
admin.site.register(cart,cartAdmin)

class useraddressAdmin(admin.ModelAdmin):
    list_display = ('user','address','pno')
admin.site.register(useraddress,useraddressAdmin)

class ordered_itemsAdmin(admin.ModelAdmin):
    list_display = ('order_id','user','date','payment_type','status','shipping_status','delivery_status')
admin.site.register(ordered_items,ordered_itemsAdmin)

class technicianAdmin(admin.ModelAdmin):
    list_display = ('complaint_id','user','name','contact','email','address','category')
admin.site.register(technician,technicianAdmin)

class wishAdmin(admin.ModelAdmin):
    list_display = ('user','itemname','category','quantity','total_price')
admin.site.register(wishlist,wishAdmin)

class reviewAdmin(admin.ModelAdmin):
    list_display = ('itemname','name','mail','review','rating')
admin.site.register(review,reviewAdmin)

admin.site.register(contactdetails)