from matplotlib import pyplot as plt
from collections import Counter
import math
import numpy as np

def distance(v,w) :
    squaredDiff = (v-w)**2;
    sumOfSquares = squaredDiff.sum()
    return math.sqrt(sumOfSquares)

def majority_vote(labels):
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
    for count in vote_counts.values()
        if count == winner_count])
    if(num_winners == 1):
            return winner # unique winner, so return it
    else:
            return majority_vote(labels[:-1]) # try again without the farthest

def knn_classify(k, labeled_points, new_point):
    """each labeled point should be a pair (point, label)"""
    # order the labeled points from nearest to farthest
    sorted_by_distance_from_new_point = sorted(labeled_points, key=lambda point, _ : distance(point, new_point))
    # find the labels for the k closest
    k_nearest_labels = [label for _, label in sorted_by_distance_from_new_point[:k]]
    # and let them vote
    return majority_vote(k_nearest_labels)


settings = { "Java" : {"marker" : "o", "color" : "r"}
            ,"Python" : {"marker" : "s", "color" : "g"}
            ,"R" : {"marker" : "^", "color" : "b"}
            }

def cityLangData() :
    lang = ["Python" , "R", "Java"]
    r =  [ [i[0] *180, i[1] *90 ] for i in np.random.rand(30,2) ]
    for i,v in enumerate(r) :
        alang = lang[i%3]
        r[i] = ( v , alang)
    return r # [ ( [long,lat ], lang), ... ]
cities = cityLangData()
print(cities)

newPoint = [120,70]
#newLabel = knn_classify(3,cities, newPoint);
#print(newLabel)

for(long, lat), lang in cities :
    langSetting = settings[lang]
    plt.scatter(long, lat, color= langSetting["color"], marker=langSetting["marker"])


plt.scatter(newPoint[0], newPoint[1], color="pink", marker="x")

plt.legend(loc=0) # let matplotlib choose the location
plt.show()


