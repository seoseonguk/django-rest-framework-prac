curl -X POST -d "username=jmitchel3&password=123" http://127.0.0.1:8000/api/auth/token/

{"active":true,
"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsImV4cCI6MTQ2OTg2MjQyMiwiZW1haWwiOiJjb2Rpbmdmb3JlbnRyZXByZW5ldXJzQGdtYWlsLmNvbSIsInVzZXJfaWQiOjF9.hzeAALHcWkREOIXBpyiIGpoYOw35Cqy1-QHUifnx9a0",
"user":"jmitchel3"}


curl -X POST -d "text='some text'" http://127.0.0.1:8000/api/comment/.json
{"detail":"Authentication credentials were not provided."}%


curl -X POST -d "text='some text'" http://127.0.0.1:8000/api/comment/ -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImNvZGluZ2ZvcmVudHJlcHJlbmV1cnNAZ21haWwuY29tIiwidXNlcl9pZCI6MSwiZXhwIjoxNDY5ODYyODcwLCJ1c2VybmFtZSI6ImptaXRjaGVsMyJ9.QhS944hgupWalBHDw65qJzWfincm9_NaIlMI7T5rsiU"

{"user":["This field is required."]}%


curl -X POST -d "text='some text'&user=1" http://127.0.0.1:8000/api/comment/ -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImNvZGluZ2ZvcmVudHJlcHJlbmV1cnNAZ21haWwuY29tIiwidXNlcl9pZCI6MSwiZXhwIjoxNDY5ODYyODcwLCJ1c2VybmFtZSI6ImptaXRjaGVsMyJ9.QhS944hgupWalBHDw65qJzWfincm9_NaIlMI7T5rsiU"

{"url":"http://127.0.0.1:8000/api/comment/119/","id":119,"children":[],"user":1,"text":"'some text'"}%

curl -X DELETE http://127.0.0.1:8000/api/comment/119/ -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImNvZGluZ2ZvcmVudHJlcHJlbmV1cnNAZ21haWwuY29tIiwidXNlcl9pZCI6MSwiZXhwIjoxNDY5ODYyODcwLCJ1c2VybmFtZSI6ImptaXRjaGVsMyJ9.QhS944hgupWalBHDw65qJzWfincm9_NaIlMI7T5rsiU"

# return nil

curl GET http://127.0.0.1:8000/api/comment/119/ -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImNvZGluZ2ZvcmVudHJlcHJlbmV1cnNAZ21haWwuY29tIiwidXNlcl9pZCI6MSwiZXhwIjoxNDY5ODYyODcwLCJ1c2VybmFtZSI6ImptaXRjaGVsMyJ9.QhS944hgupWalBHDw65qJzWfincm9_NaIlMI7T5rsiU"


curl -X POST -d "text='some text'&user=1&video=24" http://127.0.0.1:8000/api/comment/ -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImNvZGluZ2ZvcmVudHJlcHJlbmV1cnNAZ21haWwuY29tIiwidXNlcl9pZCI6MSwiZXhwIjoxNDY5ODYyODcwLCJ1c2VybmFtZSI6ImptaXRjaGVsMyJ9.QhS944hgupWalBHDw65qJzWfincm9_NaIlMI7T5rsiU"

{"video":["Invalid hyperlink - No URL match."]}%


curl -X POST -d "text='some text like this'&user=1&video=http://127.0.0.1:8000/api/videos/24/" http://127.0.0.1:8000/api/comment/ -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJ1c2VyX2lkIjoxLCJleHAiOjE0Njk4NjMyNjJ9.7mfBB-U9GnRDHq48j5D2U3W01FqVYqJQxNWIlDAsp8I"

{"url":"http://127.0.0.1:8000/api/comment/120/","id":120,"children":[],"video":"http://127.0.0.1:8000/api/videos/24/","user":1,"text":"'some text like this'"}

curl -X POST -d "text=some text like this&user=1&video=http://127.0.0.1:8000/api/videos/24/" http://127.0.0.1:8000/api/comment/ -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJ1c2VyX2lkIjoxLCJleHAiOjE0Njk4NjMyNjJ9.7mfBB-U9GnRDHq48j5D2U3W01FqVYqJQxNWIlDAsp8I"

{"url":"http://127.0.0.1:8000/api/comment/121/","id":121,"children":[],"video":"http://127.0.0.1:8000/api/videos/24/","user":1,"text":"some text like this"}%

curl -X POST -d "text=some text like this&user=1&video=http://127.0.0.1:8000/api/videos/24/&parent=135" http://127.0.0.1:8000/api/comment/ -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJ1c2VyX2lkIjoxLCJleHAiOjE0Njk4NjMyNjJ9.7mfBB-U9GnRDHq48j5D2U3W01FqVYqJQxNWIlDAsp8I"

{"url":"http://127.0.0.1:8000/api/comment/122/","id":122,"children":[],"video":"http://127.0.0.1:8000/api/videos/24/","user":1,"text":"some text like this"}%


#api 2




curl -X POST -d "text=some text like this&user=1&video=http://127.0.0.1:8000/api/videos/24/&parent=135" http://127.0.0.1:8000/api2/projects/djangogap/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0Njk4NjkzNjYsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoiam1pdGNoZWwzIiwiZW1haWwiOiJjb2Rpbmdmb3JlbnRyZXByZW5ldXJzQGdtYWlsLmNvbSJ9.WIdFr1JimGtSc8NIJWI5niqqCWOoHpxRJcadxAFMrsY"

{"detail":"Method \"POST\" not allowed."}%


curl -X DELETE -d "text=some text like this&user=1&video=http://127.0.0.1:8000/api/videos/24/&parent=135" http://127.0.0.1:8000/api2/projects/djangogap/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0Njk4NjkzNjYsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoiam1pdGNoZWwzIiwiZW1haWwiOiJjb2Rpbmdmb3JlbnRyZXByZW5ldXJzQGdtYWlsLmNvbSJ9.WIdFr1JimGtSc8NIJWI5niqqCWOoHpxRJcadxAFMrsY"

{"detail":"Method \"DELETE\" not allowed."}%

curl -X PUT -d "text=some text like this&user=1&video=http://127.0.0.1:8000/api/videos/24/&parent=135" http://127.0.0.1:8000/api2/projects/djangogap/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0Njk4NjkzNjYsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoiam1pdGNoZWwzIiwiZW1haWwiOiJjb2Rpbmdmb3JlbnRyZXByZW5ldXJzQGdtYWlsLmNvbSJ9.WIdFr1JimGtSc8NIJWI5niqqCWOoHpxRJcadxAFMrsY"

{"detail":"Method \"PUT\" not allowed."}%



curl GET http://127.0.0.1:8000/api2/projects/djangogap/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0Njk4NjkzNjYsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoiam1pdGNoZWwzIiwiZW1haWwiOiJjb2Rpbmdmb3JlbnRyZXByZW5ldXJzQGdtYWlsLmNvbSJ9.WIdFr1JimGtSc8NIJWI5niqqCWOoHpxRJcadxAFMrsY"

{"url":"http://127.0.0.1:8000/api2/projects/djangogap/","id":2,"slug":"djangogap","title":"DjangoGap","description":"","image":"http://127.0.0.1:8000/media/images/djangogap.png"}

curl GET http://127.0.0.1:8000/api2/projects/djangogap/

{"detail":"Authentication credentials were not provided."}
