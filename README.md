# Surveys

>Тестовое задание по созданию API, которое позволит создавать опросы, комбинируя разный формат вопросов.


Инструкции для администратора:
- активация виртуального окружения venv: source venv/bin/activate
- запуск сервера python manage.py runserver
- в адресной строке переход на адрес http://127.0.0.1:8000/admin
- для авторизации введите логин и пароль администратора: 
login=*survey_admin*, password=*1SuRVeySaReCooL1*
- во вкладке Surveys(Опросы) нажмите Add Survey, чтобы создать новый опрос
- введите Название, Дату начала, Дату завершения и Описание опроса (обратите внимание, 
что после создания опроса дату начала изменить будет невозможно!)
- после создания опроса, перейдите во вкладку Questions(Вопросы), нажмите Add Question, 
укажите название вопроса, опрос, к которому относится данный вопроc
- поле Варианты заполняйте только если планируете делать вопрос с вариантом ответа, 
в противном случае будет создан вопрос с текстовым вариантом ответа
- отметьте галочкой пункт Множественный выбор, если хотите создать вопрос с множественным выбором ответов
- после создания опроса он будет выведен на странице списка опросов
