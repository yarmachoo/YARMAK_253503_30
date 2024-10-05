import logging
from datetime import date

from django.db.models import Count, Sum
from django.db.models.functions import TruncDay
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, TemplateView
import pandas
from users.models import Client, Doctor

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")



def news_home(request):
    logging.info("News_home")
    news = Articles.objects.order_by('title')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    logging.info("Details_view")
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        logging.info("Create news")
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            logging.warning("Create news - форма заполнена неверно")
            error = "Форма заполнена неверно!"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    logging.info("Вывести страницу")
    return render(request, 'news/create.html', data)


def article_statistics_view(request):
    logging.info("article_statistics_view")
    data = Articles.objects.annotate(date=TruncDay('public_date')).values('date').annotate(count=Count('id')).order_by(
        'date')
    labels = [item['date'].strftime('%Y-%m-%d') for item in data]
    counts = [item['count'] for item in data]
    context = {
        'labels': labels,
        'data': counts,
    }
    logging.info("Вывести страницу")
    return render(request, 'news/articles_statistics.html', context)


class StatisticsView(TemplateView):
    template_name = 'news/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        users = Client.objects.all()

        today = date.today()
        ages = [today.year - user.date_birth.year - (
                (today.month, today.day) < (user.date_birth.month, user.date_birth.day)) for user in users]

        df_users = pandas.DataFrame(ages, columns=['age'])
        context['average_age'] = df_users['age'].mean()
        context['median_age'] = df_users['age'].median()

        #context['most_popular_type'] = PropertyType.objects.annotate(count=Count('property')).order_by('-count').first()
        #context['most_profitable_type'] = PropertyType.objects.annotate(total_income=Sum('property__price')).order_by(
        #   '-total_income').first()

        return context