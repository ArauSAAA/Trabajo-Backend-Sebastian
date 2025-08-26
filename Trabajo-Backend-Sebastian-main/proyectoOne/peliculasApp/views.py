from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    fecha = datetime.now().year
    
    def buscarGeneroPelicula(peliculas:list, coincidencia:str):
        categoriaPeliculas = []
        for movie in peliculas:
            if coincidencia in movie["genres"]:
                categoriaPeliculas.append(movie)
        
        return categoriaPeliculas
    
    
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
    
    return render(request, "peliculasApp/index.html", contexto)




MOVIES = [
            { "id":1, "title":"Karate Kid", "year":2025, "genres":["Acción"], "rating":8.4, "gross":185_400_000, "tickets":18_900_000, "runtime":137, "synopsis":"En China, un modesto maestro de kung-fu enseña a Dre a defenderse de un matón", "studio":"Nebula Pictures", "portada": "karate_kid.jpg" },
            { "id":2, "title":"Risas a Domicilio", "year":2024, "genres":["Comedia"], "rating":7.2, "gross":54_900_000, "tickets":7_300_000, "runtime":102, "synopsis":"Un repartidor convierte su ruta en un show improvisado que se vuelve viral.", "studio":"Panorama", "portada":  "amanecer_galactico.png"  },
            { "id":3, "title":"La Sombra del Lago", "year":2023, "genres":["Terror","Drama"], "rating":7.8, "gross":96_200_000, "tickets":10_400_000, "runtime":114, "synopsis":"Un pueblo enfrenta un misterio cuando aparecen reflejos que no les pertenecen.", "studio":"Lighthouse", "portada": "amanecer_galactico.png" },
            { "id":4, "title":"Caminos Paralelos", "year":2025, "genres":["Drama"], "rating":8.7, "gross":72_300_000, "tickets":6_100_000, "runtime":128, "synopsis":"Dos desconocidos toman decisiones opuestas el mismo día y sus destinos colisionan.", "studio":"Río Sur", "portada":  "amanecer_galactico.png"   },
            { "id":5, "title":"Operación Nébula", "year":2025, "genres":["Acción","Aventura"], "rating":7.9, "gross":132_000_000, "tickets":14_100_000, "runtime":121, "synopsis":"Una agente persigue un artefacto capaz de doblar el espacio-tiempo.", "studio":"Atlas", "portada":  "amanecer_galactico.png"   },
            { "id":6, "title":"Pixelandia", "year":2024, "genres":["Animación","Aventura"], "rating":8.1, "gross":210_800_000, "tickets":25_500_000, "runtime":99, "synopsis":"Una niña programadora entra en el videojuego que creó para salvar a su hermano.", "studio":"Peach Tree", "portada":  "amanecer_galactico.png" },
            { "id":7, "title":"El Último Asedio", "year":2023, "genres":["Acción"], "rating":7.0, "gross":44_300_000, "tickets":5_200_000, "runtime":107, "synopsis":"Un escuadrón intenta evitar la caída de una ciudad minera en el desierto.", "studio":"Ironworks", "portada":  "amanecer_galactico.png"   },
            { "id":8, "title":"Órbita Azul", "year":2025, "genres":["Ciencia Ficción","Drama"], "rating":8.9, "gross":256_700_000, "tickets":28_800_000, "runtime":141, "synopsis":"Una tripulación regresa a una Tierra alterada tras 20 años en hibernación.", "studio":"Zenith", "portada":  "amanecer_galactico.png"   },
            { "id":9, "title":"Café con Fantasmas", "year":2024, "genres":["Comedia","Terror"], "rating":7.6, "gross":61_700_000, "tickets":7_900_000, "runtime":106, "synopsis":"Una barista negocia con espíritus a cambio de historias para su podcast.", "studio":"Nocturna", "portada":  "amanecer_galactico.png"   },
            { "id":10, "title":"Ruta de Hielo", "year":2025, "genres":["Aventura"], "rating":7.5, "gross":83_100_000, "tickets":9_600_000, "runtime":118, "synopsis":"Un equipo atraviesa glaciares para entregar una vacuna en 72 horas.", "studio":"Polar Films", "portada":  "amanecer_galactico.png"   },
            { "id":11, "title":"La Biblioteca Infinita", "year":2023, "genres":["Fantasía","Aventura"], "rating":8.0, "gross":120_400_000, "tickets":13_000_000, "runtime":125, "synopsis":"Un bibliotecario descubre pasillos que llevan a mundos dentro de los libros.", "studio":"Starling", "portada":  "amanecer_galactico.png"   },
            { "id":12, "title":"Bajo la Lluvia", "year":2024, "genres":["Drama"], "rating":8.2, "gross":38_000_000, "tickets":4_900_000, "runtime":115, "synopsis":"Una violinista y un taxista se encuentran durante un apagón en la ciudad.", "studio":"Candela", "portada":  "amanecer_galactico.png"   }
            ]

for movie in MOVIES:
    print(movie["portada"])    
    


