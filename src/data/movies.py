# Lista de Películas

import random
import string


peliculas = [
    "El Padrino",
    "Pulp Fiction",
    "Titanic",
    "Forrest Gump",
    "El Irlandés",
    "Roma",
    "El Club de la Pelea",
    "Origen",
    "El Silencio de los Inocentes",
    "El Resplandor",
    "Matrix",
    "Parásitos",
    "El Viaje de Chihiro",
    "Coraline",
    "El Laberinto del Fauno",
    "El Gran Hotel Budapest",
    "La La Land",
    "Bird Box",
    "Don't Look Up",
    "El Dilema",
    "El Hombre de Toronto",
    "A través de mi ventana",
    "A Star is Born",
    "El Protegido",
    "El Hombre del Norte",
    "El Power of the Dog",
    "El Ángel",
    "Okja",
    "El Hoyo",
    "La Purga",
    "Misión de Rescate",
    "Army of the Dead",
    "Extraction",
    "Enemy",
    "Relic",
    "La Isla Siniestra",
    "El Faro",
    "Midsommar",
    "Hereditary",
    "El Conjuro",
    "It",
    "Los Otros",
    "Fragmentado",
    "Madre!",
    "El Hombre Invisible",
    "Jurassic Park",
    "Tiburón",
    "E.T.",
    "Back to the Future",
    "Indiana Jones y los Cazadores del Arca Perdida",
    "Gladiador",
    "Braveheart",
    "El Señor de los Anillos: La Comunidad del Anillo",
    "Harry Potter y la Piedra Filosofal",
    "Dunkerque",
    "1917",
    "Salvar al Soldado Ryan",
    "Top Gun: Maverick",
    "Avatar",
    "Interstellar",
    "Gravity",
    "Marte (The Martian)",
    "Blade Runner 2049",
    "Drive",
    "Baby Driver",
    "John Wick",
    "Kill Bill: Volumen 1",
    "Django Desencadenado",
    "Bastardos sin Gloria",
    "Érase una vez en Hollywood",
    "El Caballero de la Noche",
    "Joker",
    "V de Vendetta",
    "Watchmen",
    "Scott Pilgrim",
    "Deadpool",
    "Logan",
    "El Renacido",
    "El Lobo de Wall Street",
    "El Gran Gatsby",
    "El Diablo viste a la Moda",
    "La Sociedad de los Poetas Muertos",
    "Cadena Perpetua",
    "Million Dollar Baby",
    "El Curioso Caso de Benjamin Button",
    "Seven",
    "Zodiac",
    "Los Infiltrados",
    "Shutter Island",
    "El Depredador",
    "Alien",
    "Prometheus",
    "Terminator 2",
    "RoboCop",
    "Starship Troopers",
    "Pacific Rim",
    "Ready Player One",
    "Warcraft",
    "Rápidos y Furiosos 7",
    "Godzilla vs. Kong"
]


print("Total de Películas:", len(peliculas))  # Verificación: 100 elementos

"""


peliculas = [
    "El Irlandés", "Roma", "Bird Box", "Extraction", "El Camino: A Breaking Bad Movie",
    "La Vieja Guardia", "Triple Frontera", "Misión Rescate", "La Balada de Buster Scruggs",
    "Enola Holmes", "La Justicia de Roma", "El Hoyo", "Okja", "Historia de un Matrimonio",
    "El Diablo a Todas Horas", "Mudbound", "Las Crónicas de Navidad", "Los Dos Papas",
    "El Juicio de los 7 de Chicago", "La Caza", "Annihilation", "Amor de Madre",
    "La Sociedad de la Nieve", "No Mires Arriba", "La Plataforma", "Klaus", "6 en la Sombra",
    "La Casa de Papel: El Fenómeno", "La Red Avispa", "La Tigra, Chica Siniestra",
    "La Calle de la Amargura", "Misión Imposible 8", "Alerta Roja", "La Gran Apuesta",
    "Love and Monsters", "Army of the Dead", "Raya y el Último Dragón", "El Practicante",
    "Spenser Confidential", "La Excavación", "La Luz de Mi Vida", "El Camino de Xico",
    "Extraction 2", "Un Lugar en Silencio", "Tiempo", "Bright", "Los Mitchell Contra las Máquinas",
    "El Padre", "El Misterio de las Siete Cartas", "El Hombre Invisible", "Rápido y Furioso 10",
    "El Puente de los Espías", "Creed", "El Juego de la Fortuna", "El Escándalo",
    "El Gran Gatsby", "La La Land", "Gladiador", "Forrest Gump", "Matrix",
    "Joker", "Parásitos", "El Origen", "El Renacido", "Mad Max: Furia en el Camino",
    "El Señor de los Anillos: La Comunidad del Anillo", "El Señor de los Anillos: Las Dos Torres",
    "El Señor de los Anillos: El Retorno del Rey", "Harry Potter y la Piedra Filosofal",
    "Harry Potter y la Cámara Secreta", "Harry Potter y el Prisionero de Azkaban",
    "Harry Potter y el Cáliz de Fuego", "Harry Potter y la Orden del Fénix", "Harry Potter y el Misterio del Príncipe",
    "Harry Potter y las Reliquias de la Muerte: Parte 1", "Harry Potter y las Reliquias de la Muerte: Parte 2",
    "Los Vengadores", "Avengers: Infinity War", "Avengers: Endgame", "Spider-Man: Lejos de Casa",
    "Capitán América: Civil War", "Guardianes de la Galaxia", "Thor: Ragnarok", "Black Panther",
    "Deadpool", "Logan", "Doctor Strange", "Ant-Man", "Wonder Woman",
    "Aquaman", "Shazam!", "Liga de la Justicia", "Batman v Superman", "Justice League",
    "Spider-Man: Homecoming", "Spider-Man: No Way Home", "Capitana Marvel", "Iron Man",
    "Iron Man 2", "Iron Man 3"
]

"""

# peliculas = [random.randint(1, 100) for _ in range(100)]

# peliculas = [random.choice(string.ascii_uppercase) for _ in range(100)]