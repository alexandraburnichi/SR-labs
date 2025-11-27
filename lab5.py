import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# 1. Definirea datelor manual (Demo)
users = ['Barr Faughny', 'Dennison Crosswaite', 'Gunar Cockshoot', "Wilone O'Kielt", 'Gigi Bohling']
items = ['A Tale of Two Cities', 'The Little Prince', "Harry Potter 1", 'And Then There Were None', 'Dream of Red Chamber']

# Matricea de rating-uri (0-5)
# Rows = Users, Columns = Items
data = [
    [5, 0, 4, 0, 0],  # Barr Faughny
    [0, 5, 0, 3, 0],  # Dennison Crosswaite
    [2, 0, 0, 5, 1],  # Gunar Cockshoot
    [0, 4, 5, 0, 0],  # Wilone O'Kielt
    [0, 0, 3, 4, 5]   # Gigi Bohling
]

user_item_matrix = np.array(data)

print("Matricea User-Item:")
print(pd.DataFrame(user_item_matrix, index=users, columns=items))

# 2. Calcul Similaritate (Item-Item)
# Transpunem matricea (.T) pentru ca liniile să fie itemi
item_similarity = cosine_similarity(user_item_matrix.T)

print("\nMatricea de Similaritate intre Carti:")
print(pd.DataFrame(item_similarity, index=items, columns=items).round(2))

# 3. Predictie pentru un User (ex: Barr Faughny - index 0)
user_id = 0
user_ratings = user_item_matrix[user_id]

# Scoruri = produs scalar intre ratingurile userului si similaritatea itemilor
scores = user_ratings.dot(item_similarity)

# Filtram cartile deja citite
scores[user_ratings > 0] = -1

print(f"\nRecomandari pentru {users[user_id]}:")
for idx in np.argsort(scores)[::-1]:
    if scores[idx] > -1:
        print(f"- {items[idx]} (Scor: {scores[idx]:.2f})")