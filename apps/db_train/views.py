from django.shortcuts import render
from django.views import View
from django.db.models import Q, Max, Min, Avg, Count
from .models import Author, AuthorProfile, Entry, Tag


class TrainView(View):
    def get(self, request):

        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        self.answer2 = Author.objects.annotate(
            entry_count=Count('entries')
        ).order_by('-entry_count').first()

        self.answer3 = Entry.objects.filter(
            Q(tags__name='Кино') | Q(tags__name='Музыка')
        ).distinct() # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?

        self.answer4 = Author.objects.filter(gender= 'ж').count()  # TODO Сколько авторов женского пола зарегистрировано в системе?

        total_authors = Author.objects.count()
        agreed_authors = Author.objects.filter(status_rule=True).count()
        self.answer5 = (agreed_authors / total_authors * 100) if total_authors > 0 else 0  # TODO Какой процент авторов согласился с правилами при регистрации?

        self.answer6 = Author.objects.filter(
            authorprofile__stage__gte=1,
            authorprofile__stage__lte=5
        ).distinct()  # TODO Какие авторы имеют стаж от 1 до 5 лет?

        self.answer7 = Author.objects.order_by('-age').first()  # TODO Какой автор имеет наибольший возраст?
        self.answer8 = Author.objects.exclude(phone_number__isnull=True).count()  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = Author.objects.filter(age__lt=25)  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer10 = Author.objects.annotate(
            entry_count=Count('entries', distinct=True)
        ).values('username', 'entry_count')  # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}
        return render(request, 'train_db/training_db.html', context=context)

