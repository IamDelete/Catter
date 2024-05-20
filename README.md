# DOCUMENTATIE

## 1. Motivaţia alegerii temei, utilitatea aplicaţiei
Proiectul nostru este intitulat "Catter", acesta este o combinatie intre rater si cat, cuvintele din engleza de la cat = pisica si rater = evaluator.Acesta pune utilizatorul in situatia de a alege intre doua pisici pe baza calitatilor lor.
Acest website poate fi adaptat pentru mai multe lucruri urmand sa includem o multitudini de categori. Rolul acestui proiect este a oferi divertisment pasionatilor de animale.

## 2. Structura aplicaţiei: organizarea conţinutului informaţional, structuri de date utilizate
Websitul nostru este structurat in 5 pagini:
   - pagina principala
   - pagina de postare
   - paginile de autentificare
   - pagina de setari
   - pagina de clasament.

  ### Pagina principala
Aceasta pagina contine formularul de vot unde utilizator alege pisica pe care o considera mai adorabila.

  ### Pagina de postare
Are rol de a oferi utilizatorului posibilitatea de a participa la concursul Catter cu propria sa pisica prin intermediul formularului de inscriere.

  ### Paginile de autentificare(de scos daca nu implementam)
Cele doua pagini de autentificare indeplinesc rolurile de creeare si logare a utilizatorilor cu ajutorul formularelor.

  ### Pagina de settings(de scos daca nu implementam)
Pagina in care utilizatorul isi poate modifica diferite aspecte tehnice in legatura cu contul sau si preferintele sale.

  ### Pagina de clasamente
Aceasta pagina afiseaza clasamentul de pisici care sunt ordonate dupa criteriul de ranking (ELO , elo provine din sah unde jucatoarii erau pusi unul contra altuia si folosind diverse formule matematice determina castigul/ pierderea elo-ului in functie de elo-ul propriu si al adversarului). 
 
## 3. Detalii tehnice de implementare
Website-ul Catter este impartit pe doua arii de development:

  ### Frontend
Limbajele de programare folosite in aceasta arie sunt:
- HTML
- CSS
- JavaScript

  ### Backend
Limbajul de programare folosit in aceasta arie este Python, mai exact folosim framework-ul Django acesta fiind o varianta simpla dar eficienta pentru a da manage database-ului.

## 4. Resurse hard şi soft necesare
  ### client
Pe partea de client sau user aceta are nevoie noiar de un pc , web browser si conexiune la internet pentru a rula website-ul.
  ### sevrer-side
Pe partea de servere necesitam un service de hosting , un domain name si cand vom atinge un anumit prag de utilizator vom include un databse , o alegere buna pentru asta est aws acesta avand multe setari oferind o experienta buna pentru dezvoltatori ca si pentru utilizaotri
    
## 5. Modalităţi de utilizare
Website-l nostru este extrem de usor si intuativ de folosit acesta oferind o experinta neteda pentru utilizatorii noi.
  Pasii indicati de catre noi pentru utilizare sunt urmatorii:
  ### 1. Pornirea sitului 
  ### 2. Postarea unei poze cu felina proprie , acest pas nu este necesar pentru a juca
  ### 3. Bucurativa de jocul catter , alegand cea mai draguta pisica dintre cele doua de pe ecran

 **Daca ati decis sa participati , postand propria pisica, aveti posibiliatatea de a castiga 10% din veniturile noastre obtinute din reclame. Pentru a gasii locul in clasament al pisiici tale doar intra pe apgina de leaderboard si cauta numele pisicii.**
  
## 6. Posibilităţi de dezvoltare
- Desi pare un website relativ simplu cu putine imbunatatiri acesta este usor adaptabil pentru o multime de categorii. O categorie pe care dorim sa o implementam este posibilitatea de a alege dintre 2 desene , filme si cantece acestea fiind usor de evalua obiectiv.
- O alta posibilitate de dezvoltare este includerea optiuneai de a posta un videoclip amuzant , scurt si a fi evaluate pe baza amuzamentului oferit in video.
- includerea unei pagini de autentificare este un pas important si necesar pe care il vom face primul dupa ce primim posibilitatea de a dezvolta websitul .

## 7. Secvente relevante de cod

### HTML:
        <header>
            <div class="corner" id="leftTop"></div>
            <div class="corner" id="rightTop"></div>

            <h1 id="title">Catter</h1>

            <h2 id="subtitle">VIEW VOTE ENJOY</h2>

            <div class="corner" id="leftBottom"></div>
            <div class="corner" id="rightBottom"></div>

            <div id="descriptionContainer">
                <div id="textWrapper">
                    <p id="text">Welcome to the ultimate cat showdown! Our delightful feline contestants are ready to steal your heart. Cast your votes, compare their cuteness, and let the Elo-based system determine the winner.</p>
                </div>

                <!-- ARROW -->
                <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" id="arrow">
                    <g>
                        <path fill="rgba(255, 255, 255, 0.389)" d="M12,2A10,10,0,1,0,22,12,10.011,10.011,0,0,0,12,2Zm0,18a8,8,0,1,1,8-8A8.009,8.009,0,0,1,12,20Z"/>
                        <polygon fill="rgba(255, 255, 255, 0.389)" points="12 12.586 8.707 9.293 7.293 10.707 12 15.414 16.707 10.707 15.293 9.293 12 12.586"/>
                    </g>
                </svg>
            </div>

        </header>

### CSS:
    @media screen and (max-width: 756px) {
            main h1 {
                font-size: 10vw!important;
            }

            th {
                font-size: 5vw!important;
            }

            td {
                font-size: 3.5vw!important;
            }

            #textWrapper p {
                font-size: 4vw!important;
            }
        }

### JavaScript:

    const btn = document.getElementById('colorModeButton');
    const title = document.getElementById('title');
    const subTitle = document.getElementById('subTitle');
    const text = document.getElementById('text');
    const corners = document.querySelectorAll('.corner');

    let isDarkMode = false;

    function toggleMode() {
    if (isDarkMode) {
        // Switch to light mode
        title.style.color = 'var(--accentLight)';
        subTitle.style.color = 'var(--accentLight)';
            document.body.style.backgroundImage = 'var(--backgroundLight)';
            text.style.color = 'var(--mainDark)';
            corners.forEach(corner => {
                corner.style.borderColor = 'var(--mainDark)';
            });
    } else {
        // Switch to dark mode
        title.style.color = 'var(--accentDark)';
        subTitle.style.color = 'var(--accentDark)';
            document.body.style.backgroundImage = 'var(--backgroundDark)';
            text.style.color = 'var(--mid)';
            corners.forEach(corner => {
                corner.style.borderColor = 'var(--mainLight)';
            });
    }
    isDarkMode = !isDarkMode; // Toggle the mode
    }

    btn.addEventListener('click', toggleMode);

### Python:

    from django.contrib import admin
    from django.conf import settings
    from django.conf.urls.static import static
    from django.urls import path
    from django.contrib import admin
    from catter_index import views
    from django.urls import include


    urlpatterns = [
        path('', include('catter_index.urls')),
        path('admin/', admin.site.urls),
    ]

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#patter pentru media (poze mate)


  
  






