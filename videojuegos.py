videojuegos = [
  {
    "name": "The Legend of Zelda: Breath of the Wild",
    "year": 2017,
    "rating": 5,
  },
  {
    "name": "Red Dead Redemption 2",
    "year": 2018,
    "rating": 4,
  },
  {
    "name": "God of War",
    "year": 2018,
    "rating": 5,
  },
  {
    "name": "Horizon Zero Dawn",
    "year": 2017,
    "rating": 4,
  },
  {
    "name": "Uncharted 4: A Thief's End",
    "year": 2016,
    "rating": 4,
  },
]

for juego in videojuegos:
  print(f"\nNombre: {juego['name']}")
  print(f"Año de publicación: {juego['year']}")
  print(f"Calificación: {juego['rating']}")
