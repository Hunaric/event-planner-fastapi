Invoke-RestMethod -Uri 'http://127.0.0.1:8000/event/new' `
  -Method Post `
  -Headers @{Accept = 'application/json'; 'Content-Type' = 'application/json'} `
  -Body '{"title": "FastAPI Book Launch", "image": "https://linktomyimage.com/image.png", "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts", "tags": ["python", "fastapi", "book", "launch"], "location": "Google Meet"}'

Invoke-RestMethod -Uri 'http://127.0.0.1:8000/event/66e2ddfe91053c3fd3185108' `
  -Method Put `
  -Headers @{Accept = 'application/json'; 'Content-Type' = 'application/json'} `
  -Body '{"title": "FastAPI Book Launch", "image": "https://linktomyimage.com/image.png", "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts", "tags": ["python", "fastapi", "book", "launch"], "location": "Google Meet"}'

Invoke-RestMethod -Uri 'http://127.0.0.1:8000/event' `
  -Method Get `
  -Headers @{Accept = 'application/json'; 'Content-Type' = 'application/json'}

Invoke-RestMethod -Uri 'http://127.0.0.1:8000/user/signup' `
  -Method Post `
  -Headers @{Accept = 'application/json'; 'Content-Type' = 'application/json'} `
  -Body '{"email": "reader@mybook.com", "password": "examplary"}'

Invoke-RestMethod -Uri 'http://127.0.0.1:8000/user/signin' `
  -Method Post `
  -Headers @{Accept = 'application/json'; 'Content-Type' = 'application/x-www-form-urlencoded'} `
  -Body "username=reader@mybook.com&password=examplary"

