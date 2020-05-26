import pandas as pd #dataframe
import numpy as np #matma
import matplotlib.pyplot as plt #rysowanie
import random #random generator
import copy #do kopiowania wartosci


#zdefiniuj minvalue, maxvalue, dots
minvalue = 0
maxvalue = 100
number_of_dots = 60



#zdefiniuj dots = [x, y]
dots = pd.DataFrame({
    'x': [random.randint(minvalue, maxvalue) for i in range(number_of_dots)],
    'y': [random.randint(minvalue, maxvalue) for i in range(number_of_dots)]
})

#DEBUG print(str(dots))

# zdefiniuj kolory
colmap = {1: 'r', 2: 'g', 3: 'b', 4: 'c', 5: 'm', 6: 'y'}

# zdefiniuj ilosc centroidow k (program przewiduje wartosci 1-6)
k = 5

# centroids[i] = [x, y]
centroids = {
    i+1: [random.randint(minvalue, maxvalue), random.randint(minvalue, maxvalue)]
    for i in range(k)
}

#DEBUG print(str(centroids))

#############################################################
#nanies punkty, zdefiniuj kolory, narysuj slajd iteracji

def first_slide():
    fig = plt.figure(figsize=(5, 5))
    plt.scatter(dots['x'], dots['y'], color='k')
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])
    plt.xlim(minvalue, maxvalue)
    plt.ylim(minvalue, maxvalue)
    return 0

def slide_after_assigment():
    fig = plt.figure(figsize=(5, 5))
    plt.scatter(dots['x'], dots['y'], color=dots['color'], alpha=0.5, edgecolor='k')
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])
    plt.xlim(minvalue, maxvalue)
    plt.ylim(minvalue, maxvalue)
    return 0

def slide_after_update():
    fig = plt.figure(figsize=(5, 5))
    ax = plt.axes()
    plt.scatter(dots['x'], dots['y'], color=dots['color'], alpha=0.5, edgecolor='k')
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])
    plt.xlim(minvalue, maxvalue)
    plt.ylim(minvalue, maxvalue)
    for i in old_centroids.keys():
        old_x = old_centroids[i][0]
        old_y = old_centroids[i][1]
        dx = (centroids[i][0] - old_centroids[i][0]) * 0.75
        dy = (centroids[i][1] - old_centroids[i][1]) * 0.75
        ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])
    return 0

def slide_final():
    fig = plt.figure(figsize=(5, 5))
    plt.scatter(dots['x'], dots['y'], color=dots['color'], alpha=0.5, edgecolor='k')
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])
    plt.xlim(minvalue, maxvalue)
    plt.ylim(minvalue, maxvalue)
    return 0

#############################################################
#assigment - funkcja przydzielajaca punkty dots do centroidów
def assignment(dots, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        dots['distance_from_{}'.format(i)] = (
            np.sqrt(
                (dots['x'] - centroids[i][0]) ** 2
                + (dots['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    dots['closest'] = dots.loc[:, centroid_distance_cols].idxmin(axis=1)
    dots['closest'] = dots['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    dots['color'] = dots['closest'].map(lambda x: colmap[x])
    return dots


#funkcja aktualizujaca pozycje centroidow na podstawie 'closest'
def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(dots[dots['closest'] == i]['x'])
        centroids[i][1] = np.mean(dots[dots['closest'] == i]['y'])
    return k



#DEBUG print(dots.head())


#############################################################
#tzw. firstrun, czyli pokaz pierwszy slajd, assigment, pokaz slajd, update, pokaz slajd
first_slide()
plt.show()

dots = assignment(dots, centroids)
slide_after_assigment()
plt.show()

old_centroids = copy.deepcopy(centroids)
centroids = update(centroids)
slide_after_update()
plt.show()


iteration_sum = 1


# petla iteracji
while True:
    iteration_sum += 1

    dots = assignment(dots, centroids)
    slide_after_assigment()
    plt.show()

    old_centroids = copy.deepcopy(centroids)
    closest_centroids = dots['closest'].copy(deep=True) #skopiuj wartosci 'closest' do closest_centroids
    centroids = update(centroids)
    slide_after_update()
    plt.show()

    if closest_centroids.equals(dots['closest']): #porownaj wartosci 'closest' z closest_centroids
        break


# rysuj wynik
slide_final()
plt.show()
print('Liczba iteracji:', str(iteration_sum))
