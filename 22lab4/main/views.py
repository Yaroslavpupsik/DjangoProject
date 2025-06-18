from django.shortcuts import render

def home(request):
    context = {
        'title': 'Головна сторінка',
        'pages': [
            {'name': 'Про студента', 'url': 'about'},
            {'name': 'Навчання', 'url': 'education'},
            {'name': 'Хобі', 'url': 'hobbies'},
            {'name': 'Контакти', 'url': 'contacts'}
        ]
    }
    return render(request, 'main/home.html', context)

def about(request):
    context = {
        'title': 'Про студента',
        'student_info': {
            'name': 'Дмітрій',
            'surname': 'Поляков',
            'age': 17,
            'course': 2
        }
    }
    return render(request, 'main/about.html', context)

def education(request):
    context = {
        'title': 'Навчання',
        'education_info': {
            'specialty': 'Інформаційні системи та технології',
            'group': '22-ІСТ',
            'average_grade': 4,
            'subjects': ['комп\'ютерна графіка', 'веб-технології', 'основи програмування']
        }
    }
    return render(request, 'main/education.html', context)

def hobbies(request):
    context = {
        'title': 'Хобі',
        'hobbies': [
            'Програмування',
            'Спорт',
            'Читання',
            'Музика'
        ]
    }
    return render(request, 'main/hobbies.html', context)

def contacts(request):
    context = {
        'title': 'Контакти',
        'contact_info': {
            'email': 'example@email.com',
            'phone': '+380123456789',
            'social': '@username'
        }
    }
    return render(request, 'main/contacts.html', context) 