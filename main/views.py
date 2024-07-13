from .models import Aluno 
from django.http import HttpResponse
# Create your views here.
def alunoView(request):
     return HttpResponse('Hello World')