import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)
    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(Entry.objects.get(id__exact = 4))
    # print(Entry.objects.get(id = 4))
    # print(Blog.objects.get(name__iexact ="Путешествия по миру"))

    # print(Entry.objects.filter(headline__contains='мод'))

    # print(Entry.objects.filter(id__in=[1, 3, 4]))
    # print(Entry.objects.filter(number_of_comments__in='123'))

    # inner_qs = Blog.objects.filter(name__contains='Путешествия')
    # entries = Entry.objects.filter(blog__in=inner_qs)
    # print(entries)

    # print(Entry.objects.filter(number_of_comments__gt=10))

    import datetime
    # # print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
    #
    # # print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
    # # print(Entry.objects.filter(headline__lte="Зя"))
    #
    # # print(Entry.objects.filter(headline__startswith='Как'))
    # # print(Entry.objects.filter(headline__endswith='ния'))
    #
    # start_date=datetime.date(2023, 1, 1)
    # end_data = datetime.date(2023, 12, 31)
    # # print(Entry.objects.filter(pub_date__range=(start_date, end_data)))
    # print(Entry.objects.filter(pub_date__year=2023))

    # print(Entry.objects.filter(pub_date__year__lt=2022))
    # print(Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline'))
    # print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(pub_date__day__lte=15).values_list('author__name').distinct())
    # print(Entry.objects.filter(pub_date__week_day=2).values('blog__name', 'pub_date', 'headline'))

    # print(Entry.objects.filter(pub_date__date=datetime.date(2021, 6, 1)))
    # print(Entry.objects.filter(pub_date__date__gt=datetime.date(2024, 1, 1)))
    # print(Entry.objects.filter(pub_date__time=datetime.time(12,00)))
    # print(Entry.objects.filter(pub_date__time__range=(datetime.time(6), datetime.time(17))))

    # print(Entry.objects.filter(body_text__regex=r'\w*стран\w*'))
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)'))
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)').distinct())

    # all_obj = Blog.objects.all()
    # print("Вывод всех значений в таблице Blog\n", all_obj)
    # all_obj = Blog.objects.first()
    # print("Вывод первого значения в таблице Blog\n", all_obj)

    # all_obj = Blog.objects.all()
    # obj_first=all_obj.first()
    # print("Разные запросы на вывод в Blog\n", f"Первое значение таблицы = {obj_first}\n",
    #    f"Все значения = {all_obj}")

    # all_obj = Blog.objects.all()
    # for idx, value in enumerate(all_obj):
    #     print(f"idx = {idx}, value = {value}")
    # print(all_obj[0])
    # print(all_obj[2:4])

    # print(Blog.objects.get(id=1))
    # print(Blog.objects.get(id=1, name="Путешествия по миру"))

    # print(Blog.objects.filter(id__gte=2))

    # print(Blog.objects.exclude(id__gte=2))

    # try:
    #     Blog.objects.get(id=2, name="Путешествия по миру")
    # except Blog.DoesNotExist:
    #     print("Не существует")
    # print(Blog.objects.filter(id=2, name="Путешествия по миру").exists())

    # print(Blog.objects.count())
    # print(Blog.objects.filter(id__gte=2).count())

    # filtered_data = Blog.objects.filter(id__gte=2)
    # print(filtered_data.order_by("id"))
    # print(filtered_data.order_by("-id"))
    # print(filtered_data.order_by("-name", "id"))

    from django.db.models import Count, Avg, Q, Max, Min, StdDev, Variance, Sum
    # entry = Blog.objects.annotate(number_of_entries=Count('entries')).values('name', 'number_of_entries',)
    # print(entry)

    # blogs = Blog.objects.alias(number_of_entries=Count('entries')).filter(number_of_entries__gt=4)
    # print(blogs)

    # average_rating = Entry.objects.aggregate(
    #     average_rating=Avg('rating', distinct=True )
    # )
    # print(average_rating)

    # average_rating_with_default = Entry.objects.aggregate(
    #     average_rating2=Avg('rating', default=5.0)
    # )
    # print(average_rating_with_default)

    # average_rating = Entry.objects.aggregate(
    #     average_rating3=Avg('rating', filter=Q(pub_date__year__gt=2023))
    # )
    # print(average_rating)

    # count_author = Entry.objects.aggregate(
    #     count_authors=Count('author', distinct=True)
    # )
    # print(count_author)

    # entries_with_tags_count = Entry.objects.annotate(
    #     tag_count = Count('tags')).values('id', 'tag_count')
    # print(entries_with_tags_count)

    # calc_rating = Entry.objects.aggregate(
    #     max_rating = Max('rating'), min_rating=Min('rating')
    # )
    # print(calc_rating)

    # calc_rating = Entry.objects.aggregate(
    #     std_rating=StdDev('rating'), var_rating=Variance('rating')
    # )
    # print(calc_rating)

    # calc_rating = Entry.objects.aggregate(
    #     sum_comments=Sum('number_of_comments')
    # )
    # print(calc_rating)

    # filtered_data = Blog.objects.filter(id__gte=2)
    # print(filtered_data)
    # print(filtered_data.reverse())

    # print(Entry.objects.order_by('author', 'pub_date').distinct('author', 'pub_date'))

    # print(Blog.objects.filter(name__startswith='Фитнес'))
    # print(Blog.objects.filter(name__startswith = 'Фитнес').values())
    # print(Blog.objects.values('id', 'name'))

    # print(Blog.objects.values_list())
    # print(Blog.objects.values_list('id', 'name'))

    # blog_a_entries = Entry.objects.filter(blog__name='Путешествия по миру')
    # blog_b_entries = Entry.objects.filter(blog__name='Кулинарные искушения')
    # blog_c_entries = Entry.objects.filter(blog__name='Фитнес и здоровый образ жизни')
    # result_qs = blog_a_entries.union(blog_b_entries, blog_c_entries)
    # print(result_qs)

    # print(Entry.objects.filter(blog__name__in=['Путешествия по миру', 'Кулинарные искушения', 'Фитнес и здоровый образ жизни']))

    # blog_a_entries = Entry.objects.filter(blog__name='Путешествия по миру').values('author')
    # blog_b_entries = Entry.objects.filter(blog__name='Кулинарные искушения').values('author')
    # blog_c_entries = Entry.objects.filter(blog__name='Фитнес и здоровый образ жизни').values('author')
    # result_qs = Entry.objects.values('author').difference(blog_a_entries, blog_b_entries, blog_c_entries)
    # print(result_qs)

