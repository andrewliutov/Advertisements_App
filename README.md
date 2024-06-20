## Backend для приложения с объявлениями

Бэкенд для мобильного приложения с объявлениями. Объявления можно создавать и просматривать. Есть возможность фильтровать объявления по дате и статусу.

Создавать объявления могут только авторизованные пользователи. Для просмотра объявлений авторизация не нужна.

У объявления есть статусы: `OPEN`, `CLOSED`. У пользователя может быть не более 10 открытых объявлений.

Обновлять и удалять объявление может только его автор (помимо админов).

Чтобы боты и злоумышленники не нагружали систему, существуют лимиты на запросы:

- для неавторизованных пользователей: 10 запросов в минуту;
- для авторизованных пользователей: 20 запросов в минуту.

Реализована функциональность для админов: можно менять и удалять любые объявления.

Есть возможность добавлять объявления в избранное. Автор объявления не может добавить своё объявление в избранное. Добавлена возможность фильтрации по избранным объявлениям. Например, пользователь хочет посмотреть все объявления, которые он добавил в избранное.

Добавлена возможность поставить статус `DRAFT` — черновик. Пока объявление в черновике, оно показывается только автору объявления, другим пользователям оно недоступно.



#### Примеры запросов:

* Успешный запрос:
  
![Успех](./screenshots/success.png)

* Неправильный токен:
  
![Неправильный токен](./screenshots/bad_token.png)

* Пример фильтрации:
  
![Фильтрация по дате](./screenshots/date_filter.png)

* С примерами запросов к API можно ознакомиться в [файле requests-examples.http](./requests-examples.http).



#### Документация по проекту

Для запуска проекта необходимо

Установить зависимости:

```bash
pip install -r requirements.txt
```

Создать базу в postgres и прогнать миграции:

```base
manage.py migrate
```

Выполнить команду:

```bash
python manage.py runserver
```