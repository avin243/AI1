import numpy as np
concepts = np.array([
 ['sunny','warm','normal','strong','warm','same'],
 ['sunny','warm','high','strong','warm','same'],
 ['rainy','cold','high','strong','warm','change'],
 ['sunny','warm','high','strong','cool','change']
])
target = np.array(['yes','yes','no','yes'])
def candidate_elimination(concepts, target):
 S = concepts[0].copy()
 G = [["?" for _ in range(len(S))]]
 for i, h in enumerate(concepts):
 if target[i] == "yes":
 for x in range(len(S)):
 if h[x] != S[x]:
 S[x] = "?"
 G = [g for g in G if all(g[x] == "?" or g[x] == h[x] or 
S[x] == "?" for x in range(len(S)))]
 else:
 new_G = []
 for x in range(len(S)):
 if S[x] != "?" and h[x] != S[x]:
   g = ["?"] * len(S)
 g[x] = S[x]
 new_G.append(g)
 G.extend(new_G)
 return S, G
S_final, G_final = candidate_elimination(concepts, target)
print("Final Specific Hypothesis:", S_final)
print("Final General Hypotheses:", G_final)
