

# สารบัญ

1. สร้างที่เก็บโค้ดใน Github Repository ของโปรเจคกัน 🐙

2. ติดตั้ง Django 🤠

   2.1 สร้าง Admin กัน ! 👩‍💼

3. เริ่มต้นสร้างแอพ 🎉

   3.1 เริ่มต้นสร้างแผนผังข้อมูล models.py 🛢

   3.2 สร้างปลายทางที่จะไป ด้วย urls.py 📫

   3.3 ศูนย์รวมการประมวลผลที่ views.py 🧠

   3.4 การ query ดึงข้อมูลมาดูกันหน่อย 🔍

   3.5 สร้างหน้ารายละเอียดของ Story กัน (Story Detail) 📖

   3.6 จัดระเบียบการแสดงผลด้วย Template กัน ✨

   3.7 มาทำให้หน้าเว็บเราเปลี่ยนแปลงข้อมูลโดยอัตโนมัติ (dynamic) 🦾

4. เพิ่มส่วนต่างๆให้กับเว็บเรา

   4.1 เพิ่มความสวยงามด้วย Bootstrap ✨

   4.2  เพิ่มประสิทธิภาพการแสดงผลด้วย {% block content %} 👆

   4.3 เพิ่ม story ด้วยการกรอกแบบฟอร์ม (Forms.py) 📄

   4.4 เพิ่มเอกลักษณ์ของเว็บโดยใส่ css ที่เราทำขึ้นเอง 💄

   4.5 ติดตั้ง Fonts กันเถอะ 🅰️

   4.6 แผนผังข้อมูลที่เปลี่ยนไป (models) 🛢



---

# 1. สร้างที่เก็บโค้ดใน Github Repository ของโปรเจคกัน 🐙



สร้าง new repository โดยเราจะเข้าไปที่ www.github.com และกดปุ่ม new เพื่อสร้าง repository

 หรือ เข้าตรงๆทาง https://github.com/new 

![Screen Shot 2563-07-30 at 16.20.28](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-30%20at%2016.20.28.png)







ขั้นตอนนี้จะกดสร้าง **README.md** และ **gitignore** เป็น Python ด้วย

![Screen Shot 2563-07-30 at 16.21.48](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-30%20at%2016.21.48.png)



![Screen Shot 2563-07-30 at 16.22.44](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-30%20at%2016.22.44.png)



คัดลอกลิ้งค์ เพื่อมา clone project ลงบนเครื่องของเรา

```
 git clone git@github.com:mesodiar/medium-test.git
```



เราจะพบว่ามี folder ชื่อ `medium-test` เกิดขึ้น และมีไฟล์ README.md ข้างใน

![Screen Shot 2563-07-30 at 16.25.11](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-30%20at%2016.25.11.png)





---



# 2. ติดตั้ง Django 🤠



เริ่มต้นรันคำสั่ง

```
pipenv install django

หรือ
python -m pipenv install django
```

![Screen Shot 2563-07-30 at 16.26.50](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-30%20at%2016.26.50.png)

จะได้ไฟล์ Pipfile กับ Pipfile.lock



```
pipenv shell

หรือ
python -m pipenv  shell
```




คราวนี้เราจะไป เริ่มสร้างโปรเจคกัน

```bash
django-admin startproject <project_name>
```



จะได้ structure ไฟล์ ตามนี้ (ใน Windows ลอง tree ได้)

```
.
├── Pipfile
├── Pipfile.lock
└── medium
    ├── manage.py
    └── medium
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
        
```


```
python manage.py migrate
python manage.py runserver
```





----



#### 2.1 สร้าง Admin กัน ! 👩‍💼

เราจะสร้าง Superuser หรือ admin ของไซต์ (นั่นคือเราเอง) เราจะใช้คำสั่งด้านล่าง และกรอกข้อมูลลงไป

```
python manage.py createsuperuser
```



-----



# 3. เริ่มต้นสร้างแอพ 🎉

เราจะสร้างแอพกันด้วยคำสั่ง

```
python manage.py startapp stories
```





---



## 3.1 สร้างปลายทางที่จะไป ด้วย urls.py 📫



ไฟล์ medium/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stories.urls'))
]

```

ไฟล์ stories/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```



## 3.2 ศูนย์รวมการประมวลผลที่ views.py 🧠





ไฟล์ stories/views.py

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is your story index")
```

คราวนี้ให้เราไปที่ localhost:8000/stories



![Screen Shot 2563-07-17 at 09.41.07](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2009.41.07.png)





## 3.3 เริ่มต้นสร้างแผนผังข้อมูล Models.py 🛢



ไฟล์ models.py

```python
from django.conf import settings
from django.db import models

class Story(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

```

* ถ้าไม่ใส่ (models.Model) จะ เกิด error ขึ้นว่า

  ```python
     for model in model_or_iterable:
  TypeError: 'type' object is not iterable
  แล้วจะ migrate ไม่ได้
  ```

   

* ไปแก้เพิ่ม 'story', ที่ installed_apps ไม่งั้นจะรันคำสั่งด้านล่างไม่ได้

```
python manage.py makemigrations
```



การ makemigrations จะเป็นการที่เราบอกว่าเรามี models ใหม่เกิดขึ้น หรือเราได้เปลี่ยนแปลง models 

โดยหลังจากที่เราสร้าง models จะมีไฟล์เกิดขึ้น



แล้วค่อยรันคำสั่ง

```
python manage.py migrate
```



---

แสดง Story ในหน้า admin



stories/admin.py

```python
from django.contrib import admin
from .models import Story

admin.site.register(Story)
```

---



## 3.4 การ query ดึงข้อมูลมาดูกันหน่อย 🔍

คราวนี้เราจะแสดงหน้ารายละเอียดในหน้า story กัน (story detail) กัน แต่เราต้องมีข้อมูลของ story ก่อน

ให้เราไปสร้างที่ localhost:8000/admin เพื่อทำการสร้างข้อมูล story เบื้องต้นก่อน

![Screen Shot 2563-07-17 at 10.56.48](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2010.56.48.png)





เราจะไปที่หน้าต่าง console (หรือ command prompt) กัน และรันคำสั่ง

```
python manage.py shell
```

และทำตามดังรูป



![Screen Shot 2563-07-17 at 11.11.29](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2011.11.29.png)

เราจะลอง `Story.objects.get(id=1)` และลอง `Story.objects.get(id=2)` ดู
จะเห็นว่าตอนนี้เรามีแค่ Story ที่ id 1 เท่านั้น

![Screen Shot 2563-07-17 at 11.13.17](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2011.13.17.png)





## 3.5 สร้างหน้ารายละเอียดของ Story กัน (Story Detail) 📖

คราวนี้เรากลับมา stories/urls.py อีกครั้ง เพื่อสร้าง path ไปยังหน้ารายละเอียดของ story (story detail)


```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stories/<int:story_id>/', views.detail, name='detail'), ## add this line
]
```

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is your story index")

## add this function
def detail(request, story_id):
    return HttpResponse(f'This is story detail of {story_id}') 
```



![Screen Shot 2563-07-17 at 11.07.40](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2011.07.40.png)



ไม่ว่าเราจะ http://localhost:8000/stories/2 หรือ 3 หรือ 4
เราก็จะเหมือนส่งผ่าน urls ไปยัง views

คราวนี้เราจะแสดงผลจากข้อมูลต่างๆใน Story ที่มีอยู่




ถ้าเราลองกลับไปแก้ที่ไฟล์ views.py อีกครั้ง

```
def detail(request, story_id):
    story = Story.objects.get(id=story_id)
    
    return HttpResponse(story)
```

เราจะเหมือนกับว่าเอา object ส่งไป render หน้าบ้าน



![Screen Shot 2563-07-17 at 11.15.10](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2011.15.10.png)



นั้นเพราะเรามี `__str__` ใน models.py มันจึงแสดงผลแค่ title แต่เราจะแสดงผล content ด้วย



ดังนั้นเราจะแสดงข้อมูลต่างๆใน Story ด้วยการอ้างอิงแบบนี้

```
def detail(request, story_id):
    story = Story.objects.get(id=story_id)
    
    return HttpResponse(f'{story.title} by {story.author}')
```








---



## 3.6 จัดระเบียบการแสดงผลด้วย Template กัน ✨



ตอนนี้หน้าบ้านเรามีแค่ `This is your story detail of {story_id}` แต่ในความเป็นจริงแล้ว เว็บไซต์เราไม่ได้มีการแสดงแค่นี้ มันจะแสดงสิ่งต่างๆเยอะมากและนั่นก็คือ HTML ที่ยาวมากๆนี่เอง เราจึงต้องใช้ Template ในการจัดการแต่ละหน้าในการแสดงข้อมูลต่างๆออกมา

ให้เราไป folder template โดยมี path ดังนี้

stories/templates/stories/detail.html

```html
<h1>This is from template</h1>
```



ในขณะเดียวกัน ที่ไฟล์ views.py ขั้นตอนนี้เราจะเปลี่ยน HttpResponse เป็น render()  

โดยเราจะใช้ render()  ในการบอกว่าเราจะใช้ template ที่ชื่อว่า detail.html



```python
from django.shortcuts import render
from django.http import HttpResponse

from stories.models import Story

def index(request):
    # stories = Story.objects.all()
    return HttpResponse('This is your home page')

def detail(request, story_id):
    story = Story.objects.get(id=story_id)
    # story.title + ' by ' + str(story.author) + '<br>' + story.content 
    return render(request, 'detail.html', story)

```



แต่เมื่อเรากลับมาที่เว็บของเรา จะพบว่าเกิด error ขึ้น

![Screen Shot 2563-07-17 at 11.50.58](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2011.50.58.png)



เราต้อง ส่ง story ในรูปแบบของ dictionary อันนี้เป็นสิ่งที่เราเรียกว่า **context**

```
from django.shortcuts import render
from django.http import HttpResponse

from stories.models import Story

def index(request):
    # stories = Story.objects.all()
    return HttpResponse('This is your home page')

def detail(request, story_id):
    story = Story.objects.get(id=story_id)
    # story.title + ' by ' + str(story.author) + '<br>' + story.content
    context = {'story': story}
    return render(request, 'detail.html', context)

```

คราวนี้เราก็จะได้หน้า story แรกมาอย่างสวยงามและไม่ติด error อีกต่อไป

![Screen Shot 2563-07-17 at 11.52.10](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2011.52.10.png)



ทั้งนี้เราจะกลับไปแก้ที่ template เพื่อแสดงข้อมูลต่างๆใน story เช่น ชื่อเรื่อง, ผู้แต่ง, และเนื้อหาบทความด้านใน


```
<h1>{{ story.title }} by {{ story.author }}</h1>
<p>{{ story.content }}</p>
```



คราวนี้เราก็จะได้ story มาอย่างสวยงามและครบครัน

![Screen Shot 2563-07-17 at 12.05.52](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2012.05.52.png)





## 3.7 มาทำให้หน้าเว็บเราเปลี่ยนแปลงข้อมูลโดยอัตโนมัติ (dynamic) 🦾


เราจะกลับมาที่ index.html คราวนี้เราอยากให้หน้านี้มีการแสดงลิ้งค์ของบทความทั้งหมด

```python
def index(request):
    stories = Story.objects.all()    
    context = {'stories': stories}
    return render(request, 'index.html', context)

```

```html
<h1>This is your story index</h1>
<ul>
{% for story in stories %}
    <li><a href="/stories/{{ story.id }}/">{{ story }}</a></li>
{% endfor %}
</ul>

<h1>This is your story index</h1>
<ul>
{% for story in stories %}
    <li><a href="{% url 'detail' story.id %}">{{ story }}</a></li>
{% endfor %}
</ul>
```

```
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


```



## ภาพรวม MVT ตอนนี้



![TA project-38](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/TA%20project-38.jpg)






---



# 4. เพิ่มส่วนต่างๆให้กับเว็บเรา



## 4.1 เพิ่มความสวยงามด้วย Bootstrap ✨



เราจะติดตั้ง Bootstrap ให้เว็บไซต์เราโดยเราจะใส่ code ด้านล่างในไฟล์ details.html

```
<link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
      integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"
      crossorigin="anonymous"
    />
    <script
      src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
      integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
      integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
      integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
      crossorigin="anonymous"
    ></script>
```



เราจะเห็นว่าหน้าเว็บไซต์เราสวยขึ้น

![Screen Shot 2563-07-17 at 15.00.10](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2015.00.10.png)





## 4.2 เพิ่มประสิทธิภาพการแสดงผลด้วย {% block content %} 👆

![TA project-39](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/TA%20project-39.jpg)

#### 

base.html

```
{% block content %}
{% endblock %}

```

detail.html

```
{% extends 'base.html' %}

```



ปรับหน้าตาให้สวยงามขึ้นด้วย Bootstrap

ไฟล์ base.html

```
##{% load static %}

<html>
  <header>
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
      integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"
      crossorigin="anonymous"
    />
    <script
      src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
      integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
      integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
      integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
      crossorigin="anonymous"
    ></script>
  </header>
  <body>
    <div class="container">
      <div class="row justify-content-md-center">
        <div class="col-lg-2"></div>
        <div class="col-md-auto">
          <div class="content">
            {% block content %} {% endblock %}
          </div>
        </div>
        <div class="col-lg-2"></div>
      </div>
    </div>
  </body>
</html>

```



ไฟล์ index.html

```python
{% extends 'base.html' %} 

{% block content %} 
{% for story in stories %}
<div class="card shadow p-3 mb-5 bg-white rounded">
  {% if story.image %}
  <img
    src="{{ MEDIA_URL }}{{ story.image.url }}"
    class="card-img-top"
    alt="..."
  />
  {% endif %}
  <div class="card-body">
    <a href="{% url 'detail' story.id %}"><h3>{{ story.title }}</h3></a>
    <h6 class="card-subtitle mb-2 text-muted">{{ story.author }}</h6>
    <p>{{ story.content }}</p>
  </div>
</div>
{% endfor %} 
{% endblock %}

```



ไฟล์ detail.html

```python
{% extends 'base.html' %}


{% block content %}
<div class="content">
  {% if story.image %}
  <img
    src="{{ MEDIA_URL }}{{story.image.url}}"
    class="card-img-top"
    alt="..."
  />
  {% endif %}

  <h3>{{ story.title }} by {{ story.author }}</h3>
  <p>{{ story.content }}</p>
</div>
{% endblock %}

```

## 4.3 เพิ่ม story ด้วยการกรอกแบบฟอร์ม (Forms.py) 📄



คราวนี้เราเป็น admin เราเลยมีสิทธิ์เพิ่ม story ได้ แต่จุดมุ่งหมายคือเราจะให้คนทั่วไปเขาสามารถสร้าง story ได้เอง เพราะหน้า admin จะให้แค่ คนที่เป็น admin เข้าได้เท่านั้น



ไฟล์ Urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stories/<int:story_id>/', views.detail, name='detail'),
    path('new-story/', views.new_story, name='new_story'),  ## Add this line
]


```



ไฟล์ views.py

```	python
from .forms import StoryForm

def new_story(request):
    form = StoryForm()
    return render(request, 'new_story.html', {'form': form})
```

เราจึงต้องทำ form.py

```python
from django import forms

from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('author', 'title', 'content')
```



ไฟล์ new_story.html

```python
{% extends 'base.html' %}

{% block content %}
    <h2>New Story</h2>
    <form method="POST" class="post-form">
    {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-dark">Save</button>
    </form>
{% endblock %}
```



แต่จะยังกด save ข้อมูลจาก form ไม่ได้

เราจะแก้ให้เป็น code ข้างล่างดังนี้

```python
from django.shortcuts import render, redirect

def new_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = StoryForm()
    return render(request, 'stories/new_story.html', {'form': form})
```



## 4.4 เพิ่มเอกลักษณ์ของเว็บโดยใส่ css ที่เราทำขึ้นเอง 💄



คราวนี้เราก็สร้าง ใช้ css ใน project ของเราเองบ้าง

โดยการสร้างไฟล์ css ที่  stories/static/css/story.css



story.css

```
h3 {
  color: #15c4b5;
  font-family: "PT Serif", serif;
}

.page-header,
.page-header a {
  background-color: #f8f6f6;
  padding: 20px 20px 20px 50px;
  margin-top: 0;
  font-size: 30px;
  font-family: "PT Serif", serif;
  color: #000;
}

.content {
  margin-top: 10px;
}

.card {
  width: 600px;
  margin-bottom: 30px;
}

```



แล้วเราก็ใส่ {% load static %}  และ import ไฟล์ story.css ด้วยโค้ดด้านล่างใน base.html 

```html
{% load static %}

<header>
....

<link rel="stylesheet" href="{% static 'css/story.css' %}" />  // เติมบรรทัดนี้

</header>
```

คราวนี้เราจะยังใช้ไม่ได้เพราะ django เรายังไม่รู้ว่าต้องไปหาไฟล์ css ที่ไหน
ถ้าเราลอง inspect ดูใน
http://localhost:8000/static/css/story.css 

จะพบว่าหาไฟล์นี้ไม่เจอ

ดังนั้น เราจะต้องประกาศ STATICFILES_DIRS ใน settings.py


```settings.py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

```

คราวนี้ถึงไม่ 404 แล้ว

![Screen Shot 2563-07-17 at 15.05.56](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2015.05.56.png)



![Screen Shot 2563-07-17 at 15.06.17](https://github.com/mesodiar/bootcamp-python-django/blob/master/attachments/Screen%20Shot%202563-07-17%20at%2015.06.17.png)





## 4.5 ติดตั้ง Fonts กันเถอะ 🅰️



เข้า [FontCDN: A search tool for Google web fonts](https://thomaspark.co/projects/fontcdn/) แล้วเลือกฟ้อนท์ชื่อ PT serif หรือเลือกฟอนท์ที่ต้องการ

และเราจะ import font นี้เข้ามาโดยใส่โค้ดด้านล่างภายใน <header> ของไฟล์ base.html

```html
<link href='https://fonts.googleapis.com/css?family=PT+Serif:700' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Abril+Fatface' rel='stylesheet' type='text/css'>
```

หากเราอยากใส่ฟอนท์นี้ที่ไหน ก็สามารถประกาศใน css ได้เลย

```
h1 {
  color: #15c4b5;
  font-family: "PT Serif", serif;  
}
```



คราวนี้เราก็ใช้ฟ้อนท์ได้แล้ว



## 4.6 แผนผังข้อมูลที่เปลี่ยนไป (models) 🛢

อยากเพิ่มรูปภาพเข้ามาประกอบใน story เราต้องแก้ที่แผนผังข้อมูลใน models.py

```
image = models.ImageField(null=True, blank=True)
```



เมื่อเรามีการเปลี่ยนแปลง models.py เราจะต้องบอก Django โดยการรันคำสั่ง

```
python manage.py makemigrations
```

เราจะพบว่าต้องลง Package ที่ชื่อว่า Pillow ด้วย 

```
pipenv install Pillow
```



หลังจากที่ลง Pillow แล้ว เราก็จะสามารถ makemigrations และ migrate ได้ปกติ

```
python manage.py makemigrations
python manage.py migrate
```



เมื่อเรามีการเก็บรูปภาพเข้ามา เราจะต้องเพิ่ม settings ด้านล่างใน settings.py ด้วย รวมถึงต้องเติม `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` ในไฟล์ medium_project/urls.py อีกด้วย

```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

```
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stories/', include('stories.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



คราวนี้อย่าลืมสร้าง folder ที่ชื่อว่า /media/ ด้วย (ที่เดียวกับที่มี manage.py)

พอจบขั้นตอนทั้งหมดเราก็สามารถอัพโหลดรูปเข้าไปในแต่ละบทความได้แล้ว เราอาจจะเข้า https://unsplash.com/ ไป download ภาพฟรี หรือจะเลือกรูปที่มีอยู่บนเครื่องแล้วก็ได้ สามารถ upload รูปเข้าทาง localhost:8000/admin ได้เลย



หรือถ้าอยากอัพโหลดผ่าน form ให้แก้ไฟล์ forms.py 

```python
from django import forms

from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('author', 'title', 'content', 'image')  ##เพิ่ม image เข้ามา
```













## 

