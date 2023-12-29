from django.db.models.functions import Round
from django.shortcuts import render
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import add_items, categories, ordered_items, technician, wishlist, useraddress, review, contactdetails
from .models import cart
from django.db.models import Sum, Avg
from django.db.models import Q

# Create your views here.
a = add_items.objects.filter(category=1).count()
b = add_items.objects.filter(category=2).count()
c = add_items.objects.filter(category=3).count()
d = add_items.objects.filter(category=4).count()
e = add_items.objects.filter(category=5).count()
f = add_items.objects.filter(category=6).count()
g = add_items.objects.filter(category=7).count()
h = add_items.objects.filter(category=8).count()
i = add_items.objects.filter(category=9).count()
j = add_items.objects.filter(category=10).count()
k = add_items.objects.filter(category=11).count()
l = add_items.objects.filter(category=12).count()
m = add_items.objects.filter(category=13).count()
n = add_items.objects.filter(category=14).count()
o = add_items.objects.filter(category=15).count()
p = add_items.objects.filter(category=16).count()


def home(req):
    brm = add_items.objects.filter(category=1)
    cm = add_items.objects.filter(category=12)
    ck = add_items.objects.filter(category=9)
    mg = add_items.objects.filter(category=4)
    ch = add_items.objects.filter(category=8)
    cat = categories.objects.all()
    return render(req, 'index.html', {'data': brm, 'data1': cm, 'data2': ck, 'data3': mg, 'data4': ch, 'c': cat})


def index(req):
    brm = add_items.objects.filter(category=1)
    cm = add_items.objects.filter(category=12)
    ck = add_items.objects.filter(category=9)
    mg = add_items.objects.filter(category=4)
    ch = add_items.objects.filter(category=8)
    cat = categories.objects.all()
    return render(req, 'index.html', {'data': brm, 'data1': cm, 'data2': ck, 'data3': mg, 'data4': ch, 'c': cat})

def myaccount(req):
    if req.user.is_active:
        user = req.user
        order = ordered_items.objects.filter(user=user).exclude(payment_type="null")
        comp = technician.objects.filter(user=user)
        return render(req,'myaccount.html',{'o': order, 'c': comp})
    else:
        messages.info(req, "Please Login to visit the page")
        return render(req, 'login.html')

def about(req):
    return render(req, 'about.html')

def contact(req):
    return render(req, 'contact.html')

def category(req):
    products = add_items.objects.filter(Q(category=17) | Q(category=18))
    if req.user.is_active:
        user = req.user;
        cartitems = cart.objects.filter(user=user)
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        count = cartitems.count()
        wcount = wishlist.objects.filter(user=user).count()
        if cartitems.exists():
            cat = categories.objects.all()
            return render(req, 'category.html', {'data': products, 'items': cartitems, 'total': total, 'count': count, 'wcount': wcount, 'c': cat})
        else:
            cat = categories.objects.all()
            return render(req, 'category.html',{'data': products, 'items': cartitems, 'total': total, 'count': count, 'wcount': wcount, 'c': cat})
    else:
        messages.info(req, "Please login to visit the store")
        return render(req, 'login.html')


def store(req):
    products = add_items.objects.all()
    if req.user.is_active:
        user = req.user;
        cartitems = cart.objects.filter(user=user)
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        count = cartitems.count()
        wcount = wishlist.objects.filter(user=user).count()
        if cartitems.exists():
            cat = categories.objects.all()
            return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':count, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
        else:
            cat = categories.objects.all()
            return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':count, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
    else:
        messages.info(req, "Please login to visit the store")
        return render(req, 'login.html')


def checkout(req):
    cat = categories.objects.all()
    products = add_items.objects.all()
    user = req.user;
    cartitems = cart.objects.filter(user=user)
    total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=user).count()
    if cartitems.exists():
        return render(req, 'checkout.html', {'items': cartitems, 't': total, 'count': ccount, 'wcount': wcount, 'c': cat})
    else:
        messages.info(req, "Can't move to checkout.. No items in Cart..")
        return render(req, 'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})


def loadproduct(req):
    if req.user.is_active:
        cat = categories.objects.all()
        user = req.user;
        cartitems = cart.objects.filter(user=user)
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        ccount = cartitems.count()
        wcount = wishlist.objects.filter(user=user).count()
        if req.method == 'POST':
            pro = req.POST['some']
            print("The product details is", pro)
            pro_details = add_items.objects.get(item_name=pro)
            print("The product objects ", pro_details)
            revs = review.objects.filter(itemname=pro_details)
            rcount = revs.count()
            revc5 = review.objects.filter(itemname=pro_details, rating=5).count()
            revc4 = review.objects.filter(itemname=pro_details, rating=4).count()
            revc3 = review.objects.filter(itemname=pro_details, rating=3).count()
            revc2 = review.objects.filter(itemname=pro_details, rating=2).count()
            revc1 = review.objects.filter(itemname=pro_details, rating=1).count()
            ratav = review.objects.filter(itemname=pro_details).aggregate(Avg('rating'))
            if cartitems.exists():
                return render(req, 'product.html', {'d': pro_details, 'items': cartitems, 'total': total, 'count': ccount,
                                                'wcount': wcount, 'c': cat, 'r': revs, 'rc': rcount, 'rvc5': revc5,
                                                'rvc4': revc4, 'rvc3': revc3, 'rvc2': revc2, 'rvc1': revc1, 'avg': ratav})
            else:
                return render(req, 'product.html',{'d': pro_details, 'count': ccount, 'wcount': wcount, 'c': cat, 'r': revs, 'rc': rcount, 'rvc5': revc5,
                                                'rvc4': revc4, 'rvc3': revc3, 'rvc2': revc2, 'rvc1': revc1, 'avg': ratav})
        else:
            products = add_items.objects.all()
            return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
    else:
        messages.info(req, "Please login to visit the store")
        return render(req, 'login.html')

def signup(req):
    return render(req, 'signup.html')


def login(req):
    return render(req, 'login.html')


def sign(req):
    if req.method == 'POST':
        username = req.POST['uname']
        firstname = req.POST['fname']
        lastname = req.POST['lname']
        email = req.POST['email']
        password = req.POST['password']
        cpassword = req.POST['cpassword']
        if User.objects.filter(username=username).exists():
            messages.info(req, "User already exists.. Try a different Username..")
            return render(req, 'signup.html')
        else:
            if password == cpassword:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email, password=password)
                user.save()
                return render(req, 'login.html')
            else:
                messages.info(req, "Password does not match")
                return render(req, 'signup.html')
    else:
        return render(req, 'signup.html')


def log(req):
    global username
    if req.method == 'POST':
        username = req.POST['un']
        password = req.POST['ps']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            brm = add_items.objects.filter(category=1)
            cm = add_items.objects.filter(category=12)
            ck = add_items.objects.filter(category=9)
            mg = add_items.objects.filter(category=4)
            ch = add_items.objects.filter(category=8)
            cat = categories.objects.all()
            return render(req, 'index.html', {'data': brm, 'data1': cm, 'data2': ck, 'data3': mg, 'data4': ch, 'c': cat})
        else:
            messages.info(req, "Invalid Credentials")
            return render(req, 'login.html')
    else:
        return render(req, 'login.html')


def techpage(req):
    if req.user.is_active:
        return render(req, 'technician.html')
    else:
        messages.info(req,"Please Login to register Complaint")
        return render(req,'login.html')


def complaint(req):
    if req.user.is_active and req.method == 'POST':
        cuser = req.user
        name = req.POST['name']
        email = req.POST['email']
        address = req.POST['address']
        city = req.POST['city']
        pincode = req.POST['pincode']
        contact = req.POST['phno']
        cat = req.POST.get('category')
        complaint = req.POST['complaint']
        tech = technician(user=cuser,name=name, email=email, address=address, city=city, pincode=pincode, contact=contact,
                          category=cat, complaint=complaint)
        tech.save()
    brm = add_items.objects.filter(category=1)
    cm = add_items.objects.filter(category=12)
    ck = add_items.objects.filter(category=9)
    mg = add_items.objects.filter(category=4)
    ch = add_items.objects.filter(category=8)
    cat = categories.objects.all()
    return render(req, 'index.html', {'data': brm, 'data1': cm, 'data2': ck, 'data3': mg, 'data4': ch, 'c': cat})


def addtocart(req):
    # print("The current user is ",req.user)
    if req.user.is_authenticated and req.method == 'POST':
        current_user = req.user
        product = req.POST['productname']
        quantity = req.POST['qty']
        category = req.POST['cat']
        price = req.POST['price']
        price = float(price) * int(quantity)
        item = add_items.objects.get(item_name=product)
        x = cart(user=current_user, itemname=item, category=category, quantity=quantity, total_price=price)
        x.save()
        y = ordered_items(user=current_user, order_item=item, quantity=quantity)
        y.save()
        products = add_items.objects.all()
        user = req.user;
        cartitems = cart.objects.filter(user=user)
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        ccount = cartitems.count()
        wcount = wishlist.objects.filter(user=user).count()
        cat = categories.objects.all()
        return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
    else:
        messages.info(req, "An error occurred while adding item to cart")
        cartitems = cart.objects.filter(user=req.user)
        total = cart.objects.filter(user=req.user).aggregate(Sum('total_price'))
        products = add_items.objects.all()
        ccount = cart.objects.filter(user=req.user).count()
        wcount = wishlist.objects.filter(user=req.user).count()
        cat = categories.objects.all()
        return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})


def viewcart(req):
    user = req.user;
    if user.is_authenticated:
        cartitems = cart.objects.filter(user=user)
        # total = cart.get_total(cartitems.total_price,cartitems.quantity)
        # print(cart.get_total(cartitems))
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        print("the total sum is", total)
        ccount = cartitems.count()
        wcount = wishlist.objects.filter(user=req.user).count()
        cat = categories.objects.all()
        if cartitems.exists():
            return render(req, 'cart.html', {'items': cartitems, 'total': total, 'count': ccount, 'wcount': wcount, 'c': cat})
        else:
            messages.info(req, "No items in Cart")
            products = add_items.objects.all()
            return render(req,'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
    else:
        messages.info(req, "Please Login to view Cart")
        return render(req, 'login.html')

def wish(req):
    user = req.user;
    if user.is_authenticated:
        wishitems = wishlist.objects.filter(user=user)
        # total = wishlist.get_total(cartitems.total_price,cartitems.quantity)
        # print(wishlist.get_total(cartitems))
        wtotal = wishlist.objects.filter(user=user).aggregate(Sum('total_price'))
        cartitems = cart.objects.filter(user=user)
        ctotal = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        ccount = cartitems.count()
        wcount = wishlist.objects.filter(user=user).count()
        cat = categories.objects.all()
        if wishitems.exists():
            return render(req, 'wishlist.html', {'witems': wishitems, 'wtotal': wtotal, 'count': ccount, 'wcount': wcount,
                                             'items': cartitems, 'total': ctotal, 'c': cat})
        else:
            messages.info(req, "No items in Wishlist")
            products = add_items.objects.all()
            return render(req, 'store.html',{'data':products, 'items':cartitems, 'total':ctotal, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
    else:
        messages.info(req, "Please Login to view Wishlist")
        return render(req, 'login.html')


def deletecartitem(req):
    products = add_items.objects.all()
    if req.method == 'POST':
        item = req.POST['item']
        user = req.user;
        # y = add_items.objects.get(item_name=item)
        z = cart.objects.get(id=item)
        y = ordered_items.objects.filter(order_item=z.itemname, user=user).delete()
        x = cart.objects.filter(id=item, user=user).delete()
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        print("the total sum is ", total)
        items = cart.objects.filter(user=user)
        ccount = items.count()
        wcount = wishlist.objects.filter(user=user).count()
        cat = categories.objects.all()
        return render(req, 'cart.html', {'data': products, 'items': items, 'total': total, 'count': ccount,
                                         'wcount': wcount, 'c': cat})

def deletecartitem1(req):
    products = add_items.objects.all()
    if req.method == 'POST':
        item = req.POST['item']
        user = req.user;
        # y = add_items.objects.get(item_name=item)
        z = cart.objects.get(id=item)
        y = ordered_items.objects.filter(order_item=z.itemname, user=user).delete()
        x = cart.objects.filter(id=item, user=user).delete()
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        items = cart.objects.filter(user=user)
        ccount = items.count()
        wcount = wishlist.objects.filter(user=user).count()
        cat = categories.objects.all()
        return render(req, 'store.html', {'data':products, 'items':items, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def addtowish(req):
    # print("The current user is ",req.user)
    if req.user.is_authenticated:
        current_user = req.user
        product = req.POST['productname']
        quantity = req.POST['qty']
        category = req.POST['cat']
        price = req.POST['price']
        price = float(price) * int(quantity)
        item = add_items.objects.get(item_name=product)
        x = wishlist(user=current_user, itemname=item, category=category, quantity=quantity, total_price=price)
        x.save()
        products = add_items.objects.all()
        total = cart.objects.filter(user=current_user).aggregate(Sum('total_price'))
        items = cart.objects.filter(user=current_user)
        ccount = items.count()
        wcount = wishlist.objects.filter(user=current_user).count()
        cat = categories.objects.all()
        return render(req, 'store.html', {'data':products, 'items':items, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def deletewishitem(req):
    if req.method == 'POST':
        item = req.POST['item']
        user = req.user;
        # y = add_items.objects.get(item_name=item)
        x = wishlist.objects.filter(id=item, user=user).delete()
        wtotal = wishlist.objects.filter(user=user).aggregate(Sum('total_price'))
        witems = wishlist.objects.filter(user=user)
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        cartitems = cart.objects.filter(user=user)
        ccount = cartitems.count()
        wcount = wishlist.objects.filter(user=user).count()
        cat = categories.objects.all()
        if cartitems.exists():
            return render(req, 'wishlist.html', {'witems': witems, 'wtotal': wtotal, 'total': total, 'items': cartitems,
                                                 'count': ccount, 'wcount': wcount, 'c': cat})
        else:
            messages.info(req, "No items in wishlist")
            return render(req, 'wishlist.html', {'count': ccount, 'wcount': wcount, 'c': cat})

def wishtocart(req):
    # print("The current user is ",req.user)
    if req.user.is_authenticated and req.method == 'POST':
        current_user = req.user
        product = req.POST['productname']
        quantity = req.POST['qty']
        category = req.POST['cat']
        price = req.POST['price']
        price = float(price) * int(quantity)
        item = add_items.objects.get(item_name=product)
        x = cart(user=current_user, itemname=item, category=category, quantity=quantity, total_price=price)
        x.save()
        y = ordered_items(user=current_user, order_item=item, quantity=quantity)
        y.save()
        z = wishlist.objects.filter(itemname=item, user=current_user).delete()
        wishitems = wishlist.objects.filter(user=current_user)
        total = wishlist.objects.filter(user=current_user).aggregate(Sum('total_price'))
        cartitems = cart.objects.filter(user=current_user)
        carttotal = cart.objects.filter(user=current_user).aggregate(Sum('total_price'))
        ccount = cart.objects.filter(user=current_user).count()
        wcount = wishlist.objects.filter(user=current_user).count()
        cat = categories.objects.all()
        if wishitems.exists():
            return render(req, 'wishlist.html', {'witems': wishitems, 'wtotal': total, 'count': ccount,
                                                 'wcount': wcount, 'items': cartitems, 'total': carttotal, 'c': cat})
        else:
            messages.info(req,"No items in Wishlist")
            products = add_items.objects.all()
            return render(req,'store.html', {'data':products, 'items':cartitems, 'total':carttotal, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def confirm_order(req):
    cuser = req.user;
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    if req.method == 'POST':
        fname = req.POST['firstname']
        add = req.POST['address']
        city = req.POST['city']
        state = req.POST['state']
        zip = req.POST['zipcode']
        email = req.POST['email']
        num = req.POST['tel']
        cd = req.POST.get('payment')
        addres = fname+", "+add+", City : "+city+", State : "+state+", Zipcode : "+zip+", Email-id : "+email+", Phone : "+num
        if useraddress.objects.filter(user=cuser).exists():
            u = useraddress.objects.get(user=cuser)
            u.address=addres
            u.save()
        else:
            u = useraddress(user=cuser, address=addres, pno=num)
            u.save()
        y = ordered_items.objects.filter(user=cuser,payment_type="null")
        if cd == "cod":
            for i in y:
                i.payment_type = "Cash on Delivery"
                i.status = "Payment Pending"
                i.save()
                cart.objects.filter(user=cuser).delete()
        else:
             for i in y:
                i.payment_type = "Online Payment"
                i.status = "Payment Successful";
                i.save()
                cart.objects.filter(user=cuser).delete()
    return render(req, 'confirmation.html', {'items': cartitems, 't': total, 'count': ccount, 'wcount': wcount, 'c': cat})

def searchResult(req):
    user = req.user;
    if user.is_authenticated and req.method == 'POST':
        query = req.POST['query']
        c1 = req.POST.get('cat')
        print("the query value is ",query)
        cartitems = cart.objects.filter(user=user)
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        ccount = cartitems.count()
        wcount = wishlist.objects.filter(user=user).count()
        cat = categories.objects.all()
        if query == "":
            products = add_items.objects.filter(category=c1)
            return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
        products=add_items.objects.all().filter(Q(item_name__contains=query) | Q(description__contains=query)
                                                | Q(category=c1))
        return render(req,'store.html',{'query': query, 'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
    else:
        messages.info(req, "Please Login to visit the page")
        return render(req, 'login.html')

def logoutuser(req):
    logout(req)
    brm = add_items.objects.filter(category=1)
    cm = add_items.objects.filter(category=12)
    ck = add_items.objects.filter(category=9)
    mg = add_items.objects.filter(category=4)
    ch = add_items.objects.filter(category=8)
    cat = categories.objects.all()
    return render(req, 'index.html', {'data': brm, 'data1': cm, 'data2': ck, 'data3': mg, 'data4': ch, 'c': cat})

def ascsortby_name(req):
    products = add_items.objects.order_by('item_name')
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def dscsortby_name(req):
    products = add_items.objects.order_by('-item_name')
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def ascsortby_price(req):
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    products = add_items.objects.order_by('discount_price')
    return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def dscsortby_price(req):
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    products = add_items.objects.order_by('-discount_price')
    return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def pricesort(req):
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    if req.method=='POST':
        low=req.POST['pricemin']
        high=req.POST['pricemax']
        products=add_items.objects.filter(discount_price__range=(low,high))
        if products is not None:
            return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
        else:
            messages.info(req, "No products found in price range entered")
            return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})
    else:
        products = add_items.objects.all()
        return render(req, 'store.html', {'data': products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def trackorder(req):
    if req.method == 'POST':
        oid = req.POST['orderid']
        details = ordered_items.objects.filter(user=req.user,order_id=oid)
        user = req.user
        order = ordered_items.objects.filter(user=user).exclude(payment_type="null")
        comp = technician.objects.filter(user=user)
        return render(req, 'myaccount.html',{'tro':details,'o':order,'c':comp})

def trackcomplaint(req):
    if req.method == 'POST':
        cid = req.POST['compid']
        cdetails = technician.objects.filter(user=req.user,complaint_id=cid)
        user = req.user
        order = ordered_items.objects.filter(user=user).exclude(payment_type="null")
        comp = technician.objects.filter(user=user)
        return render(req, 'myaccount.html',{'trc':cdetails,'o':order,'c':comp})

def cat1(req):
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    products = add_items.objects.filter(category=1)
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat2(req):
    products = add_items.objects.filter(category=2)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat3(req):
    products = add_items.objects.filter(category=3)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat4(req):
    products = add_items.objects.filter(category=4)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat5(req):
    products = add_items.objects.filter(category=5)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat6(req):
    products = add_items.objects.filter(category=6)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat7(req):
    products = add_items.objects.filter(category=7)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat8(req):
    products = add_items.objects.filter(category=8)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat9(req):
    products = add_items.objects.filter(category=9)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat10(req):
    products = add_items.objects.filter(category=10)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat11(req):
    products = add_items.objects.filter(category=11)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat12(req):
    products = add_items.objects.filter(category=12)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat13(req):
    products = add_items.objects.filter(category=13)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat14(req):
    products = add_items.objects.filter(category=14)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat15(req):
    products = add_items.objects.filter(category=15)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat16(req):
    products = add_items.objects.filter(category=16)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat17(req):
    products = add_items.objects.filter(category=17)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def cat18(req):
    products = add_items.objects.filter(category=18)
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req,'store.html',{'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def special(req):
    products = add_items.objects.filter(Q(category=17) | Q(category=18))
    cuser = req.user
    cartitems = cart.objects.filter(user=cuser)
    total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
    ccount = cartitems.count()
    wcount = wishlist.objects.filter(user=cuser).count()
    cat = categories.objects.all()
    return render(req, 'store.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'bm':a, 'sm':b, 'fp':c, 'jmg':d, 'mo':e,
                                              'rm':f ,'gt':g, 'bc':h, 'ck':i, 'ckr':j, 'k':k, 'cm':l, 'afdf':m, 'wp':n, 'cmn':o, 'pm':p, 'c':cat})

def crock(req):
    if req.user.is_active:
        products = add_items.objects.filter(category=17)
        cuser = req.user
        cartitems = cart.objects.filter(user=cuser)
        total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
        ccount = cartitems.count()
        wcount = wishlist.objects.filter(user=cuser).count()
        cat = categories.objects.all()
        return render(req, 'category.html', {'data':products, 'items':cartitems, 'total':total, 'count':ccount, 'wcount':wcount, 'c':cat})
    else:
        messages.info(req, "Please Login to visit the page")
        return render(req, 'login.html')

def decor(req):
    if req.user.is_active:
        products = add_items.objects.filter(category=18)
        cuser = req.user
        cartitems = cart.objects.filter(user=cuser)
        total = cart.objects.filter(user=cuser).aggregate(Sum('total_price'))
        ccount = cartitems.count()
        wcount = wishlist.objects.filter(user=cuser).count()
        cat = categories.objects.all()
        return render(req, 'category.html',{'data': products, 'items': cartitems, 'total': total, 'count': ccount, 'wcount': wcount,'c': cat})
    else:
        messages.info(req, "Please Login to visit the page")
        return render(req, 'login.html')

def reviewrate(req):
    if req.method == 'POST':
        itemname = req.POST['item']
        name = req.POST['revname']
        email = req.POST['revemail']
        rev = req.POST['revdescription']
        rating = req.POST.get('rating')
        item = add_items.objects.get(item_name=itemname)
        r = review(itemname=item,name=name,mail=email,review=rev,rating=rating)
        r.save()
        cat = categories.objects.all()
        user = req.user;
        cartitems = cart.objects.filter(user=user)
        total = cart.objects.filter(user=user).aggregate(Sum('total_price'))
        ccount = cartitems.count()
        wcount = wishlist.objects.filter(user=user).count()
        pro_details = add_items.objects.get(item_name=itemname)
        revs = review.objects.filter(itemname=pro_details)
        rcount = revs.count()
        revc5 = review.objects.filter(itemname=pro_details, rating=5).count()
        revc4 = review.objects.filter(itemname=pro_details, rating=4).count()
        revc3 = review.objects.filter(itemname=pro_details, rating=3).count()
        revc2 = review.objects.filter(itemname=pro_details, rating=2).count()
        revc1 = review.objects.filter(itemname=pro_details, rating=1).count()
        ratav = review.objects.filter(itemname=pro_details).aggregate(Avg('rating'))
        if cartitems.exists():
            return render(req, 'product.html',{'d': pro_details, 'items': cartitems, 'total': total, 'count': ccount,
                               'wcount': wcount, 'c': cat, 'r': revs, 'rc' : rcount, 'rvc5': revc5, 'rvc4': revc4,
                                               'rvc3': revc3, 'rvc2': revc2, 'rvc1': revc1, 'avg': ratav})
        else:
            return render(req, 'product.html', {'d': pro_details, 'count': ccount, 'wcount': wcount, 'c': cat, 'r': revs, 'rc' : rcount})

def deletecomplaint(req):
    if req.method == 'POST':
        id = req.POST['comp']
        technician.objects.get(complaint_id=id).delete()
        user = req.user
        order = ordered_items.objects.filter(user=user).exclude(payment_type="null")
        comp = technician.objects.filter(user=user)
        return render(req, 'myaccount.html', {'o': order, 'c': comp})

def deleteorder(req):
    if req.method == 'POST':
        id = req.POST['order']
        ordered_items.objects.get(order_id=id).delete()
        user = req.user
        order = ordered_items.objects.filter(user=user).exclude(payment_type="null")
        comp = technician.objects.filter(user=user)
        return render(req, 'myaccount.html', {'o': order, 'c': comp})

def contactus(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        sub = req.POST['subject']
        mes = req.POST['message']
        con = contactdetails(name=name,email=email,subject=sub,message=mes)
        con.save()
    brm = add_items.objects.filter(category=1)
    cm = add_items.objects.filter(category=12)
    ck = add_items.objects.filter(category=9)
    mg = add_items.objects.filter(category=4)
    ch = add_items.objects.filter(category=8)
    cat = categories.objects.all()
    return render(req, 'index.html', {'data': brm, 'data1': cm, 'data2': ck, 'data3': mg, 'data4': ch, 'c': cat})