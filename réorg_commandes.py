from itertools import chain, groupby
from operator import attrgetter
# from lire_feuille import lire_une_feuille
# from time import time

# 将所有订单物件放在一个大清单中，然后按日期及有效性排序并重组订单
def réorg_les_comms(liste_comms):
    liste_plate = list(chain.from_iterable(liste_comms))
    liste_plate.sort(key=attrgetter('date', 'valide'))
    # print(liste_plate)
    
    return [(cl, list(gr)) for cl, gr in groupby(liste_plate, key=attrgetter('date', 'valide'))]

# if __name__ == '__main__':
#     t0 = time()
#     CC = [lire_une_feuille(2), lire_une_feuille(3), lire_une_feuille(299)]
#     print(CC)
#     print(f"Durée: {time()-t0} s")

#     t0 = time()
#     ro = réorg_les_comms(CC)
#     print(ro)
#     print(len(ro))
#     print(f"Durée: {time()-t0} s")