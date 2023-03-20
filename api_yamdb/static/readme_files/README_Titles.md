# *TITLES*
## Категории произведений
***
# <span style="color:green">GET</span>
### Получение списка всех жанров

**Права доступа:** Доступно без токена

#### url:
```
/api/v1/titles/
```
#### структура JSON в отклике:
```JSON
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
```
#### пример фильтрации по имени, году, жанру (slug) и категории (slug):
```
/api/titles/?name__icontains=game&year__gte=2010&genre__slug__iexact=action&category__slug__icontains=sci-fi
```
*Примечание: В этом примере мы запрашиваем список всех фильмов (или других объектов модели Title), которые содержат подстроку "game" в поле "name", имеют год выпуска не менее 2010, относятся к жанру "action" (у которого slug точно совпадает с "action"), и относятся к категории, которая содержит подстроку "sci-fi" в slug (т.е. в slug есть "sci-fi" в любом месте)*
***
# <span style="color:blue">POST</span>
### Добавление произведения
**Права доступа:** Администратор (`admin`).

*Примечание: поле slug каждого жанра должно быть уникальным.*

#### url:
```
/api/v1/titles/
```
#### структура JSON в запросе на добавление:
```JSON
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
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
`401 Необходим JWT-токен`
`403 Нет прав доступа`
***
# <span style="color:green">GET</span>
### Получение информации о произведении

**Права доступа:** Доступно без токена

#### url:
```
/api/v1/titles/{titles_id}/
```
#### структура JSON в отклике:
```JSON
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
Возможные коды ошибок:
`404 Обьект не найден`

***
# <span style="color:orange">PATCH</span>
### Частичное обновление информации о произведении

**Права доступа:** Администратор (`admin`).

#### url:
```
/api/v1/titles/{titles_id}/
```
#### структура JSON в запросе на обновление:
```JSON
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
#### структура JSON в отклике:
```JSON
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
Возможные коды ошибок:
`404 Обьект не найден`
`401 Необходим JWT-токен`
`403 Нет прав доступа`
***
# <span style="color:red">DELETE</span>
### Удаление произведения

**Права доступа:** Администратор.

#### url:
```
/api/v1/titles/{titles_id}/
```
*Примечание: Обязательное поле - `slug`.*

Возможные коды ошибок:
`401 Необходим JWT-токен`
`403 Нет прав доступа`
`404 Категория не найдена`

[Назад](../../../README.md/#Описание)