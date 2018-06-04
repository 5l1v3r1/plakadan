from django.shortcuts import render

# Create your views here.

# msg.append({'Kullanıcı Bilgileri Kaydedildi': 'success'})
# msg = []


def index(request):
    return render(request, "index.html", locals())

def collect_messages(request, msg):
    messages = []
    req_msg = request.session.get('messages')
    if messages:
        messages += msg
    if req_msg:
        messages += req_msg

    return messages
