from news_portal.models import *


# Задание 1
User.objects.create_user('Denis')
User.objects.create_user('Alexandr')

# Задание 2
Author.objects.create(user = User.objects.get(username = 'Denis'))
Author.objects.create(user = User.objects.get(username = 'Alexandr'))

# Задание 3
cat_gam = Category.objects.create(name = 'Gaming')
cat_spt = Category.objects.create(name = 'Sport')
cat_ani = Category.objects.create(name = 'Anime')
cat_tec = Category.objects.create(name = 'Technology')

# Задание 4-5
post1 = Post.objects.create(title = "Почему жанр Souls-like стал новым стандартом индустрии?",
                            text = ("Еще десять лет назад игры от студии FromSoftware считались нишевым развлечением «для мазохистов»."
                            "Однако сегодня механики, заложенные в Demon’s Souls и Dark Souls, просочились практически в каждый крупный экшн."
                            "Сложные боссы, непрямое повествование через окружение и цена ошибки — вот столпы,"
                            "на которых держится современный геймдизайн. Секрет успеха кроется не в садизме разработчиков,"
                            "а в чувстве подлинного триумфа. Когда игрок побеждает босса после двадцатой попытки, он получает"
                            "дофаминовый всплеск, который не может дать ни одна казуальная игра. В мире, где маркеры на карте ведут"
                            "игрока за руку, Souls-like проекты предлагают самое ценное — чувство первооткрывателя и уважение к интеллекту геймера."),
                            content_type = 'AT',
                            posted_by = Author.objects.get(pk = 1))
post1.post_category.add(cat_gam, cat_tec)

post2 = Post.objects.create(title = "Феномен «Магической битвы»: как студия MAPPA изменила визуальный язык сёнэна",
                            text = ("Аниме-индустрия переживает золотой век анимации, и флагманом этого движения стала «Магическая битва» (Jujutsu Kaisen). "
                            "Если раньше классические сёнэны могли позволить себе статичные кадры во время диалогов, "
                            "то современные стандарты требуют динамики в каждой секунде хронометража. Режиссерские решения "
                            "и работа с камерой в последних эпизодах второго сезона больше напоминают высокобюджетное голливудское кино, "
                            "чем традиционную анимацию. Использование 3D-фонов в сочетании с невероятно детализированными 2D-спецэффектами "
                            "создает эффект погружения, который раньше казался невозможным. Однако за этой красотой скрывается острая проблема "
                            "переработок в индустрии, о которой всё чаще говорят ведущие аниматоры Японии."),
                            content_type = 'AT',
                            posted_by = Author.objects.get(pk = 1))
post2.post_category.add(cat_ani)

news1 = Post.objects.create(title = "Прорыв в квантовых вычислениях: представлен процессор с защитой от ошибок",
                            text = ("Компания Quantinuum объявила о важном достижении в области квантовых технологий. "
                                    "Инженерам удалось продемонстрировать работу логических кубитов, которые практически не "
                                    "подвержены системному шуму — главной проблеме современных квантовых компьютеров. "
                                    "В ходе эксперимента была достигнута точность вычислений в 99.9%, что открывает путь к "
                                    "созданию отказоустойчивых систем. Это означает, что эра «квантового превосходства», когда "
                                    "такие компьютеры смогут за секунды взламывать современные методы шифрования или моделировать новые "
                                    "лекарства, стала на шаг ближе. Ожидается, что первые коммерческие прототипы на базе этой архитектуры "
                                    "появятся на рынке уже к концу 2027 года."),
                            content_type = 'NW',
                            posted_by = Author.objects.get(pk = 2))
news1.post_category.add(cat_tec)


# Задание 6
com1 = Comment.objects.create(post = post1,
                              commentator = User.objects.get(pk = 2),
                              text = 'Согласен с автором, после Elden Ring обычные экшены с маркерами на каждом шагу кажутся какими-то пресными.'
                                     'Это чувство, когда ты полчаса учишь тайминги босса и наконец-то его'
                                     '"закрываешь" — лучший дофамин в геймдеве на сегодня.')
com2 = Comment.objects.create(post = post2,
                              commentator = User.objects.get(pk = 2),
                              text = 'Визуал во втором сезоне Магической битвы просто отвал всего, '
                                     'сцена с Тодзи в Окинаве до сих пор в голове стоит. Но честно, '
                                     'за ребят из MAPPA страшно — если они продолжат в таком темпе работать 24/7, '
                                     'студия просто сгорит.')
com3 = Comment.objects.create(post = news1,
                              commentator = User.objects.get(pk = 1),
                              text = '99.9% точности — это серьезный порог. Если они реально допилят защиту от шума, '
                                     'то современному шифрованию (тому же RSA) придет конец гораздо быстрее, чем мы думали. '
                                     'Пора закупать квантово-устойчивые токены.')
com4 = Comment.objects.create(post = news1,
                              commentator = User.objects.get(pk = 1),
                              text = 'Опять "через пару лет". Мы эти новости про квантовое превосходство слышим уже десятилетие, '
                                     'а на деле всё еще сидим на кремнии и радуемся лишним 5% производительности '
                                     'в новых процессорах. Поживем — увидим.')

# Задание 7
# Посты
for i in range(2536):
    post2.like()

for i in range(1714):
    post1.like()

for i in range(199):
    news1.like()

# Комментарии
for i in range(24):
    com3.like()

for i in range(439):
    com2.like()

for i in range(18):
    com4.dislike()

for i in range(393):
    com1.like()


# Задание 8
for author in Author.objects.all():
    author.update_rating()

# Задание 9
Author.objects.order_by('-rating').values('user__username').first()

# Задание 10
best_post = Post.objects.order_by('-rating').first()
if best_post:
    print(f"Дата: {best_post.creation_time}")
    print(f"Автор: {best_post.posted_by.user.username}")
    print(f"Рейтинг: {best_post.rating}")
    print(f"Заголовок: {best_post.title}")
    print(f"Превью: {best_post.preview()}")

# Задание 11
all_comms = Comment.objects.filter(post = best_post)
for comm in all_comms:
    print(f"Дата: {comm.creation_time}")
    print(f"Автор: {comm.commentator.username}")
    print(f"Рейтинг: {comm.rating}")
    print(f"Текст: {comm.text}")
    print()
