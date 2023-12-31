# *REVIEWS*
## Отзывы
***
# <span style="color:green">GET</span>
### Получение списка всех отзывов

**Права доступа:** Доступно без токена

#### url:

```
/api/v1/titles/{title_id}/reviews/
```
#### структура JSON в отклике:
```JSON
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results": [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "score": 1,
                "pub_date": "2019-08-24T14:15:22Z"
            }
        ]
    }
]
```

*Примечание: Обязательный PATH PARAMETER `titles_id`.*

Возможные коды ошибок:
`404 Произведение не найдено`
***
# <span style="color:blue">POST</span>
### Добавление нового отзыва
Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение.

**Права доступа:** `user`, `moderator`, `admin`

*Примечание: Обязательный PATH PARAMETER: `title_id`.*
*Обязательные поля: `text`, `score`.*
*Поле `score` (оценка) 1..10*


#### url:
```
/api/v1/titles/{title_id}/reviews/
```
#### структура JSON в запросе на добавление:
```JSON
{
  "text": "string",
  "score": 1
}
```
в ответе:

```JSON
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
`response status code 201`

Возможные коды ошибок:
`400 Отсутствует обязательное поле или оно некорректно`
#### структура JSON в отклике:
```JSON
{
"field_name": [
"string"
]
}
```
Другие возможные коды ошибок:
`401 Необходим JWT-токен`
`403 Нет прав доступа`
`404 Произведение не найдено`
***
# <span style="color:green">GET</span>
### Полуение отзыва по id
Получить отзыв по id для указанного произведения.

**Права доступа:** Доступно без токена
#### url:
```
/api/v1/titles/{title_id}/reviews/{review_id}/
```
*Примечание: Обязательные PATH PARAMETERS: `title_id`, `review_id`.*

#### структура JSON в отклике:
```JSON
{
    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"
}
```
Возможные коды ошибок:
`404 Произведение или отзыв не найден`
***
# <span style="color:orange">PATCH</span>
### Частичное обновление отзыва по id
Частично обновить отзыв по id.
**Права доступа:** `Автор отзыва`, `moderator` или `admin`.

#### url:
```
/api/v1/titles/{title_id}/reviews/{review_id}/
```
*Примечание: Обязательные PATH PARAMETERS: `title_id`, `review_id`.*
*Примечание: Обязательные поля `text`, `score`.*
#### структура JSON в запросе на изменение:
```JSON
{
    "text": "string",
    "score": 1
}
```
#### структура JSON в отклике:
```JSON
{
    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"
}
```

Возможные коды ошибок:
`400 Отсутствует обязательное поле или оно некорректно`
`401 Необходим JWT-токен`
`403 Нет прав доступа`
`404 Произведение не найдено`
***
# <span style="color:red">DELETE</span>
### Удаление отзыва по id
Удалить отзыв по id
**Права доступа:** `Автор отзыва`, `moderator` или `admin`.
#### url:
```
/api/v1/titles/{title_id}/reviews/{review_id}/
```
*Примечание: Обязательные PATH PARAMETERS - `titles_id`, `review_id`.*

Возможные коды ошибок:
`401 Необходим JWT-токен`
`403 Нет прав доступа`
`404 Произведение или отзыв не найдены`

[Назад](../../../README.md/#Описание)
