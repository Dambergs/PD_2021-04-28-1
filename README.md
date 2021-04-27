# Django Visits

## Uzdevumi 27.04.2021.

### 1. uzdevums
<details>
<summary>Uzdevuma saturs</summary>

- Pārveidot ``views.py`` izmantojot class based views
- Visit saraksts ('/') tiek atvasināts no ``ListView``
- Pārējie view tiek atvasināti no ``View``

</details>

### 2. uzdevums

<details>
<summary>Uzdevuma saturs</summary>

- Modelim ``Visit`` nomainīt date atribūta
tipu uz ``DateField``
  (izveidot migrācijas, migrēt)
  (pirms tam labāk izdzēst datubāzi, lai 
  nebūtu nepatīkumu kļūdu)
- Izveidot failu ``forms.py``, kur izveidot klasi
``VisitForm``, kas atvasināta no ``ModelForm``
- Formai ir lauki: ``name``, ``date``, ``reason``, ``room``
- Jauna forma tiek renderēta vecās formas vietā
('/add_visit')
- Pārveidot ``AddVisitView`` tā, lai strādātu ar jaunu
formu

</details>

### 3. uzdevums

<details>
<summary>Uzdevuma saturs</summary>

- Izdeidot VisitDetailView, kas parāda
'visit_detail.html'
- VisitDetailView vai piekļūt ar
'/visit/<primary key>'
- Izdarīt tā, lai '/' varētu uzspiest uz konkrēta 
  ``Visit`` un atvērtos ``VisitDetail``
  https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#url

</details>