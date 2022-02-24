import mimetypes
from django.shortcuts import render, get_object_or_404
from .models import article
from .forms import comment_form
from django.core import mail
from django.core.serializers import serialize
from django.http import HttpResponse
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging

# Create your views here.
def to_json(request):
    data = serialize('json',article.objects.all())
    return HttpResponse(data)

def detail(request):
    all_blog = article.objects.all()
    context = {
        'all_blog': all_blog
    }
    return render(request, 'blog-grid.html', context)


def blog(request, num):
    Single_blog = get_object_or_404(article, pk=num)
    all_coments = Single_blog.coment.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        commentform = comment_form(data=request.POST)
        if commentform.is_valid():
            new_comment = commentform.save(commit=False)
            new_comment.post = Single_blog
            new_comment.save()
            mail.send_mail(
                'new comment',
                'you have new comment on website',
                'a8888ralireza@gmail.com',
                ['a8888ralireza@gmail.com'],
                fail_silently=False
            )
    else:
        commentform = comment_form()

    context = {
        'single_blog': Single_blog,
        'all_coments': all_coments,
        'new_comment': new_comment,
        'commentform': commentform,
    }
    return render(request, 'blog-single.html', context)

#def dow(request,filename):
#    with open(r'shop/')


def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 10000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989904627626'  # اختیاری

    factory = bankfactories.BankFactory()
    bank = factory.create() # or factory.create(bank_models.BankType.BMI) or set identifier
    bank.set_request(request)
    bank.set_amount(amount)
    # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
    bank.set_client_callback_url('/callback-gateway')
    bank.set_mobile_number(user_mobile_number)  # اختیاری
    bank_record = bank.ready()
 
    # هدایت کاربر به درگاه بانک
    return bank.redirect_gateway()





def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")