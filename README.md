# Shalean API

## Request & Response

### API Resources

  - [GET /api/active_polls/](#get-active-polls)
  - [GET /api/answers_polls/](#get-answers-polls)
  - [POST /add_answer/](#post-add-answer)

### Stats

GET:

   curl -G "http://localhost:8000/api/stat/"
    
Response body:

    [
      {
          "id": 1,
          "poll_name": "SpaceX и BlueOrigin",
          "description": "Выбираем лучшую космическую корпорацию",
          "questions": [
              {
                  "id": 31,
                  "question_type": "own_asnwer",
                  "question_text": "В каком году был запущен SN10?",
                  "poll": 1
              },
              {
                  "id": 32,
                  "question_type": "own_asnwer",
                  "question_text": "Starlink это...",
                  "poll": 1
              }
          ],
          "data_begin": "2021-10-19",
          "data_end": "2021-10-29"
      },
      {
          "id": 2,
          "poll_name": "Что такое ИИ",
          "description": "Основные понятия и методы проектирования",
          "questions": [
              {
                  "id": 36,
                  "question_type": "own_asnwer",
                  "question_text": "Перцептрон это...",
                  "poll": 2
              },
              {
                  "id": 37,
                  "question_type": "own_asnwer",
                  "question_text": "Для чего служит тензор?",
                  "poll": 2
              }
          ],
          "data_begin": "2021-10-19",
          "data_end": "2021-10-29"
      }
    ]

* 200 - OK
* 201 - HTTP_201_CREATED
* 400 - Bad Request
