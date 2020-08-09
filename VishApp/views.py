from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from .models import Administator, Cust_info, Pant_de, Shirt_de, Employee, Emp_Record
import sys


# Create your views here.
@csrf_exempt
def homePage(request):
    return render(request,'index.html')

@csrf_exempt
def lo_in_form(request):
    return render(request,'loginform.html')

@csrf_exempt
def validate_admin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = Administator.objects.get(email=email)
        if password == data.password:
            request.session['mail']=email
            request.session['psword']=password
            return render(request,'administrator.html')
        else:
            return render(request,'loginform.html',{'messege':'Email or Password Wrong!'})
    else:
        return HttpResponseRedirect('log_in_form/')

@csrf_exempt
def cust_form(request):
    if request.session['mail']:
        return render(request,'newcostomer.html')
    else:
        return HttpResponseRedirect('/login',{'messege':'Session time out!'})

# .......................................retrive data info from database to display of a user ..................................
def retrive_info(abcd):
    cust = Cust_info.objects.get(invoice=abcd)
    shirt  = Shirt_de.objects.get(invoice_s=abcd)
    pant = Pant_de.objects.get(invoice_p=abcd)

    return(cust , shirt,pant)



def get_invoice():
    last_invoice = Cust_info.objects.all().order_by('invoice').last()
    if not last_invoice:
        return(240000,0)
    else:
        a = last_invoice.invoice
        return(a+1, last_invoice.name)

@csrf_exempt
def submit_detils(request):
    if request.method == 'POST':
        invoice , namef= get_invoice()
        if namef != request.POST['name'] :
            name = request.POST['name']
            shirt = request.POST['shirt']
            pant = request.POST['pant']
            total_amount = request.POST['toal']
            date = request.POST['rdate']
            paid_amo = request.POST['paid']
            remai_amo = int(total_amount) - int(paid_amo)
            t_date = datetime.date.today()
            

            # shirt
            l1 = request.POST['L1']
            m1 = request.POST['M1']
            s1 = request.POST['S1']
            b1 = request.POST['B1']
            m2 = request.POST['M2']
            stype = request.POST['types']

            # pant
            l2 = request.POST['L2']
            k2 = request.POST['K2']
            h1 = request.POST['H1']
            g1 = request.POST['G1']
            h3 = request.POST['H3']
            ptype = request.POST['typep']

            asd = Cust_info(invoice=invoice, name=name, shirt = shirt, pant = pant, Total_amount = total_amount, rem_amount=remai_amo, recived_amount=paid_amo, delevery_date=date, oder_date=t_date, status=0)
            qsd = Shirt_de(invoice_s = invoice, name_s = name, sl=l1, sm1 = m1, ss = s1, sb = b1,  sm2 = m2, s_type=stype)
            wsd= Pant_de(invoice_p = invoice, name_p = name, pl = l2, p_k = k2, pg =g1, ph1 = h1, ph2 = h3, p_type = ptype )

            asd.save()
            qsd.save()
            wsd.save()
            cust,shirt,pant=retrive_info(invoice)
            return render(request,'recipt123.html',{'cust':cust, 'shirt':shirt, 'pant':pant})
        else:
            cust,shirt,pant=retrive_info(invoice-1)
            return render(request,'recipt123.html',{'cust':cust, 'shirt':shirt, 'pant':pant})
    else:
        HttpResponseRedirect('cust_form/')

#---------- Editing customer Information----------------

@csrf_exempt
def edit_info(request):
    cust_id=int(request.GET['id'])
    cust,shirt,pant=retrive_info(cust_id)
    a=cust.delevery_date
    return render(request,'Edit_cust_detail.html',{'cust':cust, 'shirt':shirt, 'pant':pant, 'a':a})
    

#-------------Updating Value of customer--------------------
@csrf_exempt
def cust_update(request):
    if request.method == 'POST':
        invoice = int(request.GET['id'])
        name = request.POST['name']
        shirt = request.POST['shirt']
        pant = request.POST['pant']
        total_amount = request.POST['toal']
        date = request.POST['rdate']
        paid_amo = request.POST['paid']
        remai_amo = int(total_amount) - int(paid_amo)
        t_date = datetime.date.today()
            

            # shirt
        l1 = request.POST['L1']
        m1 = request.POST['M1']
        s1 = request.POST['S1']
        b1 = request.POST['B1']
        m2 = request.POST['M2']
        stype = request.POST['types']

            # pant
        l2 = request.POST['L2']
        k2 = request.POST['K2']
        h1 = request.POST['H1']
        g1 = request.POST['G1']
        h3 = request.POST['H3']
        ptype = request.POST['typep']

        asd = Cust_info.objects.filter(invoice=invoice).update(name=name, shirt = shirt, pant = pant, Total_amount = total_amount, rem_amount=remai_amo, recived_amount=paid_amo, delevery_date=date, oder_date=t_date)
        qsd = Shirt_de.objects.filter(invoice_s=invoice).update(name_s = name, sl=l1, sm1 = m1, ss = s1, sb = b1,  sm2 = m2, s_type=stype)
        wsd= Pant_de.objects.filter(invoice_p=invoice).update(name_p = name, pl = l2, p_k = k2, pg =g1, ph1 = h1, ph2 = h3, p_type = ptype )

        cust,shirt,pant=retrive_info(invoice)
        return render(request,'recipt123.html',{'cust':cust, 'shirt':shirt, 'pant':pant})

#____________ check Status By User __________________ 
@csrf_exempt
def get_status(request):
    if request.method == 'POST' or request.method =='GET':
        try:
            abcd = request.POST['name']
        except:
            abcd = int(request.GET['id'])
        try:
            cust = Cust_info.objects.get(invoice=abcd)
            if cust.status == 1:
                message = "Your Order is ready :)"
            else:
                message = 'Your order in processing.......'
        except:
            return render('message.html',{'message':"Please Enter Correct Bill No....."})
        return render(request,'shoe_status.html',{'cust':cust,'message':message})

    else:
        return HttpResponseRedirect('/')


# ....................................searching and list of customer................................


@csrf_exempt
def Customer_list(request):
    info= Cust_info.objects.all()
    return  render(request,'Costomer_all.html',{'li':info})

# ----------------------------------------------update Status-------------------------------------------

@csrf_exempt
def show_update_list(request):
    info= Cust_info.objects.filter(status=0)
    return  render(request,'update_list_show.html',{'li':info})


# ----------------------------------------------update ready-------------------------------------------
@csrf_exempt
def status_ready(request):
    try:
        abcd = int(request.GET['id'])
        a = Cust_info.objects.filter(invoice=abcd).update(status=1)
        return HttpResponseRedirect('/show_update_list/')
    except:
        pass

# -------------------------------------employee_Board------------------------------



#--------------------------------------new_emp_regist_form--------------------------

@csrf_exempt
def emp_form(request):
    return render(request,'emp_form.html')



# ------------------------------------save_data_of_employee---------------------------

@csrf_exempt
def emp_acc(request):
    if  request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        adress = request.POST['adress']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['zip']
        ph_no = request.POST['number']
        mail = request.POST['email']
        adhar = request.POST['adhar']

        zas = Employee(name = name, second_name=lastname, adress=adress, city=city, state=state, pin=pin, phone=ph_no, email=mail, adhar=adhar)
        zas.save()

    emp = Employee.objects.all()

    return render(request,'emp_board.html',{'emp':emp})

#----------------------------------------emp_record_show---------------------------------------------


@csrf_exempt
def emp_record(request):
    if request.method=='GET':
        emp_id = int(request.GET['id'])
        qwe = Emp_Record.objects.filter(emp_id=emp_id)
        return render(request, 'Employee.html',{'asd':qwe})
    elif request.method=='POST':
        emp_id = int(request.GET['id'])
        date = datetime.date.today()
        pant = request.POST['pant']
        shirt = request.POST['shirt']
        money = request.POST['money']
        asd = Emp_Record(emp_id = emp_id, date = date, pant = pant, shirt = shirt, stepend = money)
        asd.save()
        return render(request, 'Employee.html',{'message':"today's data recorded"})
    else:
        return render(request, 'Employee.html')