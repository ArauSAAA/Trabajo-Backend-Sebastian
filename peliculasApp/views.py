from django.shortcuts import render
from datetime import datetime

# Create your views here.
def taquilla(request):
    fecha = datetime.now().year

    
    
    MOVIES = [
            { "id":1, "title":"Karate Kid", "year":2010, "genres":["Acción"], "rating":8.4, "gross":185_400_000, "tickets":18_900_000, "runtime":137, "synopsis":"En China, un modesto maestro de kung-fu enseña a Dre a defenderse de un matón", "studio":"Sony Pictures Home Entertainment", "portada": "karate_kid.jpg" },
            { "id":2, "title":"Los Simpson: La película", "year":2007, "genres":["Comedia"], "rating":7.2, "gross":54_900_000, "tickets":7_300_000, "runtime":102, "synopsis":"Cuando Homer contamina el lago de la ciudad con estiércol de cerdo que ha ido almacenando, lo despiden y ponen en cuarentena a los ciudadanos de Springfiel.", "studio":"Panorama", "portada":  "los_simpson_pelicula.jpg"  },
            { "id":3, "title":"Interestelar", "year":2014, "genres":["Terror","Drama"], "rating":7.8, "gross":96_200_000, "tickets":10_400_000, "runtime":114, "synopsis":"Con la humanidad al borde de la extinción, un grupo de astronautas viaja a través de un agujero de gusano en busca de otro planeta habitable.", "studio":"Lighthouse", "portada": "interstellar.jpg" },
            { "id":4, "title":"El conjuro", "year":2013, "genres":["Drama"], "rating":8.7, "gross":72_300_000, "tickets":6_100_000, "runtime":128, "synopsis":"Después de mudarse a una granja en Rhode Island, una familia experimenta fenómenos sobrenaturales y busca la ayuda de una famosa pareja de investigadores .", "studio":"Río Sur", "portada":  "el_conjuro.png"   },
            { "id":5, "title":"Son como niños", "year":2010, "genres":["Acción","Aventura"], "rating":7.9, "gross":132_000_000, "tickets":14_100_000, "runtime":121, "synopsis":"Después de la muerte de su entrenador de baloncesto de la escuela secundaria, cinco buenos amigos y ex compañeros de equipo se reúnen para un fin de semana.", "studio":"Atlas", "portada":  "son_ninos.jpg"   },
            { "id":6, "title":"Wonderland", "year":2024, "genres":["Animación","Aventura"], "rating":8.1, "gross":210_800_000, "tickets":25_500_000, "runtime":99, "synopsis":"Cuando la IA permite que quienes atraviesan un duelo se comuniquen con sus seres queridos, una azafata y una madre deben hallar el significado de la realidad.", "studio":"Peach Tree", "portada":  "wonderland.jpg" },
            { "id":7, "title":"Yo antes de ti", "year":2016, "genres":["Acción"], "rating":7.0, "gross":44_300_000, "tickets":5_200_000, "runtime":107, "synopsis":"Una joven forma un vínculo improbable con un hombre discapacitado del que está cuidando.", "studio":"Ironworks", "portada":  "antes_de_ti.jpg"   },
            { "id":8, "title":"Los Increíbles", "year":2004, "genres":["Ciencia Ficción","Drama"], "rating":8.9, "gross":256_700_000, "tickets":28_800_000, "runtime":141, "synopsis":"Una familia de superhéroes encubiertos tratando de vivir una tranquila vida suburbana se ven obligados a actuar para salvar al mundo.", "studio":"Zenith", "portada":  "los_increibles.jpg"   },
            { "id":9, "title":"Los increíbles 2", "year":2018, "genres":["Comedia","Terror"], "rating":7.6, "gross":61_700_000, "tickets":7_900_000, "runtime":106, "synopsis":"Reclutan a Elastigirl para una misión importante y Mr. Increíble se ve obligado a enfrentar el reto más grande de su vida: ser papá de tiempo completo.", "studio":"Nocturna", "portada":  "increibles_2.jpg"   },
            { "id":10, "title":"Jurassic World: el reino caído", "year":2018, "genres":["Aventura"], "rating":7.5, "gross":83_100_000, "tickets":9_600_000, "runtime":118, "synopsis":"Cuando una erupción volcánica amenaza Isla Nublar, Owen y Claire buscan un santuario para los dinosaurios del parque,", "studio":"Polar Films", "portada":  "jurasico_parque.jpg"   },
            { "id":11, "title":"Spider-Man: A través del Spider-Verso", "year":2023, "genres":["Fantasía","Aventura"], "rating":8.0, "gross":120_400_000, "tickets":13_000_000, "runtime":125, "synopsis":"Un bibliotecario descubre pasillos que llevan a mundos dentro de los libros.", "studio":"Starling", "portada":  "spiderman.jpg"   },
            { "id":12, "title":"Spider-Man: sin camino a casa", "year":2021, "genres":["Drama"], "rating":8.2, "gross":38_000_000, "tickets":4_900_000, "runtime":115, "synopsis":"Con sus seres queridos en riesgo, Peter Parker acude a Doctor Strange para recuperar su anonimato ", "studio":"Candela", "portada":  "no_way_home.jpg"   }
            ]
    

    contexto = {
        "fecha":fecha,
        "movies":MOVIES
    }
    
    return render(request, "peliculasApp/taquilla.html", contexto)





def login(request):
    return render(request, "peliculasApp/login.html")


def index(request):
    
    contexto = {"header":{
        "h1":"Proyecto Django",
        "p":"Documentación de cómo se creó el proyecto"
    },
    "container": {
        "h2":"1. Instalación de Django",
        "p1":"Primero se instala Django con el siguiente comando",
        "p2":"pip install django",
    },
    "creacion_proyecto":{
        "h2":"2. Creación del proyecto",
        "p1":"Se generó el proyecto principal con:",
        "p2":"django-admin startproject mi_proyecto",
    },
    "creacion_app":{
        "h2":"3. Creación de la aplicación",
        "p1":"Dentro del proyecto, se creó una aplicación llamada",
        "p2":"python manage.py startapp peliculasApp",
    },
    "configuracion":{
        "h2":"4. Configuración",
        "li1":"Se añadió la aplicación",
        "li2":"Se configuraron las plantillas en la carpeta",
        "li3":"Se agregaron los archivos estáticos en",
    },
    "modelsBdd":{
        "h2":"5. Modelos y Base de Datos",
        "p":"Se definieron los modelos en",
        "p2":"python manage.py makemigrations",
        "p3":"python manage.py migrate",
    },
    "vistas":{
        "h2":"6. Vistas y URLs",
        "p":"Se crearon vistas en", 
    },
    "servidor":{
        "h2":"7. Ejecución del servidor",
        "p":"Finalmente, se ejecutó el servidor de desarrollo:", 
        "p2":"python manage.py runserver",
        "h22":">Resultado",
        "p3":"Con esto, el proyecto Django quedó funcionando con páginas dinámicas y conexión a base de datos."
    },
    }
    
    return render(request, "peliculasApp/index.html", contexto)