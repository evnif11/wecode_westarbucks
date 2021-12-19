## 📍 개요
---
스타벅스 홈페이지의 ERD를 그리고 그에 맞는 model을 설계한다.  
<br>
## 🚀 학습 목표
---
- conda를 이용해 가상환경 생성하고 프로젝트를 관리할 수 있다.
- Django의 MVT 패턴을 이해하고 URLconf, View, Model 역할을 설명할 수 있다.
- ER 다이어그램을 활용해 DB 스키마를 정의할 수 있다.
- Entity에 적절한 ManyToMany, OneToMany, OneToOne 관계를 설정할 수 있다. 
- gitignore 파일을 생성하고, Git 버전 관리에서 제외할 파일(민감한 정보 등)을 지정할 수 있다.

<br>


## 📝 배운 내용
---
1. 가상환경 설정하기 
    ```zsh
    conda create -n "westarbucks" python=3.8
    conda activate westarbucks

    pip install django
    pip install mysqlclient 
    pip install django-cors-headers
    ```
- cors-headers 필요한 이유? 예전의 웹은 백엔드와 프론트엔드가 나눠져있지 않았기 때문에 api 요청을 같은 서버 내에서 해서 문제가 없었다. 하지만 3세대 웹 부터는 프론트와 백이 나누어지고 다른 서버에서 클라이언트 요청을 보내기 때문에 Cross Domain 설정을 풀어줘야한다. 같은 로컬호스트 내에서도 Port 번호가 다르면 다른 서버로 인식하기때문에 Cross Domain 에러가 발생한다.

    ```zsh
    # westarbucks 프로젝트 구조
    ├── manage.py
    ├── my_settings.py
    ├── products 
    │   ├── models.py
    │   ├── urls.py
    │   └── views.py
    └── westarbucks 
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    ```
- 파이썬은 init 파일이 있으면 패키지로 인식한다.
- wsgi는 웹서버가 직접 파이썬 코드를 실행할 수 없기 때문에 대신 어플리케이션 실행할 수 있도록 도와주는 인터페이스 역할을 해준다. 웹 서버 위에 wsgi 서버가 

<br>

2. 장고 MVT 패턴에 대한 이해
<img width="928" alt="스크린샷 2021-12-19 오후 5 52 29" src="https://user-images.githubusercontent.com/50139787/146669129-16523409-1752-4ad2-b2c3-42a4d2cdfcea.png">

- ```url.py```는 http 요청을 분석하여 알맞는 엔드포인트를 호출한다.
- ```view.py```는 method에 맞는 로직을 수행한다. 
- ```model.py```는 데이터베이스를 설계하고 통신하는 역할을 한다. 

세가지 요소를 활용해 사용자 요청에 맞는 응답을 데이터베이스와 통신해서 돌려주는 백엔드 API를 구현한다.

> 주의 : MVC 패턴과 다르게 장고는 특이하게 Model-View-Template 즉 MVT 구조로 이루어져있다. 혼동하지 말아야할 부분은 MVC의 view는 장고의 view와 전혀 다른 맥락을 가진다는 것이다. MVC의 controller에 해당하는 부분이 장고의 view 에 해당한다. 

<br>

3. Westarbucks ERD

<img width="1429" alt="스크린샷 2021-12-19 오후 2 19 58" src="https://user-images.githubusercontent.com/50139787/146664903-c4fb014c-9569-4959-a62d-2966c8772478.png">
<img width="1147" alt="스크린샷 2021-12-19 오후 5 27 20" src="https://user-images.githubusercontent.com/50139787/146668570-7520e8e6-044e-4e21-b53f-f02e9120fea6.png">  

<br>
<br>

![westarbucks-Page-1 drawio](https://user-images.githubusercontent.com/50139787/146664815-308a568f-b858-4f13-9a1e-411fe1cacb29.png)

- 데이터베이스에서 Foreign Key를 사용해 관계형 테이블을 만드는 이유는 중복된 데이터를 획기적으로 줄이고 효과적으로 데이터를 관리하기 위함이다.

- 1:N 인 경우 반드시 N에 해당하는 곳에 FK를 만든다. 
- OOP의 개념으로 생각했을 땐 해당하는 카테고리의 모든 음료를 가져오는 것이 가능하지만 DB의 관점에서는 음료 테이블에서 카테고리를 조건으로 데이터를 가져오는게 더욱 효율적인 쿼리이다.

<br>

4. 관계테이블
    ```python
    class Product(models.Model):
        korean_name = models.CharField(max_length=100)
        english_name = models.CharField(max_length=100)
        description = models.TextField()
        category = models.ForeignKey('Category', on_delete=models.CASCADE)
        allergy = models.ManyToManyField('Allergy')
        sizes = models.ManyToManyField('Size', through="Nutrition")
    ```
- ManyToMany 필드에서 생성되는 관계테이블에 추가적인 정보를 더하고 싶을 땐 직접 class를 정의하고 through를 통해 연결해준다.

- 일반적으로는 FK로만 이루어진 관계테이블은 ManyToMany 필드로 선언해놓으면 장고에서 자동으로 생성해준다.(직접 클래스로 정의할 필요가 없다)

- 공식 문서에서는 OneToOne, ManyToMany는 필드를 어느 쪽에다 선언해도 상관없다고 말하지만 일반적으로 자주 사용되는 메인 클래스에 설정하는 것이 편리하다. 
 
 <br>

## 📚 느낀점
---
- 장고 웹 프레임워크를 핵심을 깊게 이해하고 이를 통해 웹 통신의 전반적인 과정을 살펴볼 수 있었다.

- 웹 프레임워크는 서비스를 빠르게 개발하는 것을 도와주지만 동시에 많은 권한을 가지기 때문에 어느 정도까지가 프레임워크의 역할인지 명확히 구분할 필요가 있다.
- DB 설계를 할 때 어느 데이터까지 저장해야할 것인지 기획에 대한 고민도 들었다. 당장의 서비스가 구현되기 위해 필요한 데이터 뿐만 아니라 추후 분석에 활용될 수 있는 데이터도 저장할 필요가 있기 때문이다.
- 현재에는 스타벅스 홈페이지에 보여지기 위한 데이터 테이블 설계만을 했기 때문에 주문 기능이 추가 되기 위해선 테이블이 수정될 필요가 있다. 
- 다양한 요구사항의 변화에 유연하게 동작하기 위해서 테이블 설계시 변화될 데이터와 변화되지 않는 데이터를 구분할 줄 알아야한다.
- 음료 사이즈처럼 정해진 개수의 데이터도 테이블로 설계하는게 효율적인지 Enum 타입으로 정의하는 게 나은지 고민했으나 음료 사이즈가 유일하고 변하지 않는 값이란 보장이 없고 Enum타입은 정규화 규칙을 위반하기 때문에 테이블로 정의하는 것이 최선이라는 결론을 내렸다.
