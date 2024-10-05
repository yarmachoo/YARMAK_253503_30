import logging

from django.contrib.auth.decorators import login_required
#from django.contrib.sites import requests
from django.shortcuts import render
import requests
from django.utils import timezone
from news.models import Articles
from appointments.models import Service
from main.forms import ReviewForm
from django.views.generic import ListView, DetailView
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def index(request):
    partners = Partner.objects.all()
    articles = Articles.objects.all()
    services = Service.objects.all()

    lastest_article = latest_article = max(articles, key=lambda article: article.public_date)

    logging.info("вывести страницу main/index.html")
    return render(request, 'main/index.html',  {'lastest_article': lastest_article, 'partners': partners, 'services':services})

@login_required
def about(request):
    logging.info("вывести страницу main/about.html")
    return render(request, "main/about.html")


def get_cat_fact():
    logging.info("Обратиться к стороннему API")
    url = 'https://catfact.ninja/fact'
    try:
        logging.info("Попытка обращения к стороннему API")
        response = requests.get(url)
        # Код 200 означает, что запрос был успешен
        if response.status_code == 200:
            cat_fact_data = response.json()
            return cat_fact_data.get('fact')
        else:
            return None
    except requests.RequestException as e:
        logging.exception("Попытка обращения к стороннему API не удалась")
        print(f"An error occurred: {e}")
        return None


def cat_fact_view(request):
    fact = get_cat_fact()
    return render(request, 'main/cat_fact.html', {'cat_fact': fact})


def get_random_dog_image():
    url = 'https://dog.ceo/api/breeds/image/random'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dog_data = response.json()
            return dog_data.get('message')  # 'message' содержит URL изображения собаки
        else:
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def random_dog_view(request):
    image_url = get_random_dog_image()
    return render(request, 'main/random_dog.html', {'image_url': image_url})


# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuestionForm, AnswerForm
from .models import Questions, Vacancy, PromoCode, Review, Partner


def questions_list(request):
    questions = Questions.objects.all().order_by('-date_added') # Получаем только вопросы без ответов
    return render(request, 'main/questions_list.html', {'questions': questions})


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'main/vacancy_list.html'


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'main/vacancy_detail.html'

def promocode_list(request):
    promocodes = PromoCode.objects.all()  # Получаем все промокоды из базы данных
    return render(request, 'main/promocode_list.html', {'promocodes': promocodes})


def reviews_list(request):
    reviews = Review.objects.all()  # Получаем все отзывы из базы данных
    return render(request, 'main/reviews_list.html', {'reviews': reviews})


def policy(request):
    return render(request, "main/policy.html")


def partner_list(request):
    partners = Partner.objects.all()
    return render(request, "main/index.html", {'partners': partners})


class QuestionDetailView(DetailView):
    logging.info("Details_view")
    model = Questions
    template_name = 'main/question_detail.html'
    context_object_name = 'question'


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Получаем текущего пользователя
            review.date = timezone.now().date()  # Устанавливаем текущую дату
            review.save()
            return redirect('reviews-list')
    else:
        form = ReviewForm()

    return render(request, 'main/add_review.html', {'form': form})
