from django.shortcuts import render
from django.db.models import Q


from ice_cream.models import IceCream

# Играем с запросами, решаем задачку
# В проекте «Анфиса для друзей», развёрнутом на вашем компьютере, во view-функции index() напишите такой  запрос, 
# чтобы в контекст главной страницы были переданы сорта мороженого со значением True в поле is_published и у которых
# либо в поле is_on_main записано значение True;
# либо в названии есть слово «пломбир» (даже если в поле is_on_main у этого объекта стоит False).


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
    ).filter(Q(is_published=True) & (Q(is_on_main=True) | Q(title__contains='пломбир')))
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
