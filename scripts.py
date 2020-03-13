from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
import random

def get_schoolkid_and_error(name):
    error = None
    try:
        kid = Schoolkid.objects.get(full_name__contains=name)
    except ObjectDoesNotExist as e:
        kid, error = None, e
    except MultipleObjectsReturned as e:
        kid, error = None, e
    return kid, error

def fix_marks(name):
    kid, error = get_schoolkid_and_error(name)
    if not error:
        bad_marks = Mark.objects.filter(schoolkid=kid, points__lte=3)
        for mark in bad_marks:
            mark.points = 5
            mark.save()
        return None
    return error

def remove_chastisements(name):
    kid, error = get_schoolkid_and_error(name)
    if not error:
        chastisements = Chastisement.objects.filter(schoolkid=kid)
        chastisements.delete()
        return None
    return error

def create_commendation(name, subject):
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]
    kid, error = get_schoolkid_and_error(name)
    if not error:
        lessons = Lesson.objects.filter(year_of_study=kid.year_of_study, group_letter=kid.group_letter, subject__title=subject)
        lessons = lessons.order_by('-date')
        latest_lesson = lessons[0]
        commendation = Commendation.objects.create(text=random.choice(commendations), created=latest_lesson.date, schoolkid=kid,
            subject=latest_lesson.subject, teacher=latest_lesson.teacher)
        commendation.save()
        return None
    return error
