import json,re
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dealer,Review,CarMake
from .serializers import DealerSerializer,ReviewSerializer,CarMakeSerializer
@api_view(["GET"])
def dealers(r):
    q=Dealer.objects.all()
    if r.GET.get("state"): q=q.filter(state__iexact=r.GET["state"])
    return Response(DealerSerializer(q,many=True).data)
@api_view(["GET","POST"])
def dealer_detail(r,id):
    try: d=Dealer.objects.get(pk=id)
    except Dealer.DoesNotExist: return Response({"error":"Not found"},status=404)
    if r.method=="POST":
        data=r.data.copy(); data["dealer"]=d.id; s=ReviewSerializer(data=data)
        if s.is_valid(): s.save(); return Response(s.data,status=201)
        return Response(s.errors,status=400)
    return Response(DealerSerializer(d).data)
@api_view(["GET"])
def reviews(r,id): return Response(ReviewSerializer(Review.objects.filter(dealer_id=id),many=True).data)
@api_view(["GET"])
def makes(r): return Response(CarMakeSerializer(CarMake.objects.all(),many=True).data)
@require_POST
def register(r):
    try: d=json.loads(r.body)
    except Exception: return JsonResponse({"error":"Invalid JSON"},status=400)
    if not d.get("username") or not d.get("password"): return JsonResponse({"error":"Username and password required"},status=400)
    if User.objects.filter(username=d["username"]).exists(): return JsonResponse({"error":"Username exists"},status=400)
    u=User.objects.create_user(username=d["username"],password=d["password"],first_name=d.get("first_name",""),last_name=d.get("last_name",""),email=d.get("email",""))
    return JsonResponse({"message":"Registered","username":u.username},status=201)
@require_POST
def login_view(r):
    try: d=json.loads(r.body)
    except Exception: return JsonResponse({"error":"Invalid JSON"},status=400)
    u=authenticate(r,username=d.get("username"),password=d.get("password"))
    if not u: return JsonResponse({"error":"Invalid credentials"},status=401)
    login(r,u); return JsonResponse({"message":"Logged in","username":u.username})
@require_POST
def logout_view(r): logout(r); return JsonResponse({"message":"Logged out"})
@api_view(["POST"])
def sentiment(r):
    t=r.data.get("text",""); words=re.findall(r"[a-z]+",t.lower())
    pos={"fantastic","great","excellent","good","amazing","wonderful"}; neg={"bad","poor","terrible","awful"}
    score=sum(w in pos for w in words); label="positive" if score else ("negative" if any(w in neg for w in words) else "neutral")
    return Response({"text":t,"sentiment":label,"score":score})
