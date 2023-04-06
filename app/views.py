from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import json
from .models import Article ,User,Comment
import datetime 
from django.forms.models import model_to_dict
from urllib.parse import urlparse, parse_qs
import time
def home(request):
    try:
        dd = len(User.objects.filter(user_id = request.session["user_id"]))
        print(dd)
        if dd==1:
            print("home")   
            return render(request, "app/base.html")
        else:
            print(1)
            return redirect("/login")
    except:
        print(2)
        return redirect("/login")


def write(request):
    t = datetime.datetime.now().strftime('%Y/%m/%d')
    return render(request, "app/write_page.html", {"today":t})
def save_article_json(request):
    body = json.loads(request.body)
    title = body['title']
    content = body['content']
    date = datetime.datetime.now().strftime("%Y/%m/%d")
    Article(title=title,content  = content,date=date,user=User.objects.get(user_id = request.session["user_id"])).save()
    return JsonResponse({"ok":"ok"})
import re
def read_article_json(request):
    user_id = request.session["user_id"]
    user = User.objects.filter(user_id=user_id)[0]
    articles = Article.objects.filter(user = user.id)
    dic_ = {}
    date_list = []
    for i in articles:
        i = model_to_dict(i)
        i["strped_date"] = re.sub("/", "",i["date"])
        if i["date"] not in dic_.keys():
            date_list.append(i["date"])
            dic_[i["date"]] = [i]
        else:
            dic_[i["date"]].append(i)
    dic_["date_list"]=date_list
    return JsonResponse(dic_)
def read_article(request):
    id = request.GET.get('id')
    article = Article.objects.get(id= id)
    return render(request, "app/read_page.html",context = {"title":article.title, "content":article.content,"date":article.date})
def signup(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        phone  = request.POST.get("phone")
        if len(User.objects.filter(user_id=user_id))>0:
            error = "아이디 중복"
            return render(request, "app/signup.html", {"error":error})
            
        User(user_id = user_id,name =name, password =password, email =email, phone=phone).save()
        return redirect('/home')
    return render(request, "app/signup.html")
def login(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        print(user_id,password)
        if len(User.objects.filter(user_id=user_id, password=password))==1:
            request.session["user_id"]=user_id
            request.session['password'] = password
            return redirect("/home")
        else:
            return render(request, "app/login.html",context= {"ok":" 다시 입력해주세요 "})
    return render(request, "app/login.html")
def logout(request):
    request.session.flush()
    return redirect("/home/")
class Comment_request():
    def save(request):
        if request.method == "POST":
            comment = request.POST.get("comment")
            try:
                referer = request.META.get("HTTP_REFERER")
                parsed_url = urlparse(referer)
                query_params = parse_qs(parsed_url.query)
                article_id = query_params["id"][0]
                article = Article.objects.get(id = article_id)
                user = User.objects.get(user_id = request.session["user_id"])
                Comment(article = article, user = user, comment = comment).save()
                return redirect(referer)
            except:
                return HttpResponse("실패!")
    def delete(request):
        if request.method == "POST":
            article_id = request.POST.get("id")

        return HttpResponse("deletecomment!!")

    def thumbs_up(request):
        if request.method == "POST":
            article_id = request.POST.get("id")

        return HttpResponse("thumbs_up!")
    def show(request):
        referer = request.META.get("HTTP_REFERER")
        parsed_url = urlparse(referer)
        query_params = parse_qs(parsed_url.query)
        article_id = query_params["id"][0]
        comments = Comment.objects.filter(article = article_id)
        comment_list = []
        for comment in comments:
            info = model_to_dict(comment)
            user = User.objects.get(id = info["user"])
            info["user"]=user.user_id
            comment_list.append(info)
        return JsonResponse(comment_list, safe = False)
def about(request):
    return render(request,"app/about.html")