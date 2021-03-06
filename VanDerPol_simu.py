import numpy as np
import matplotlib.pyplot as plt
    
#EQUATION D'EVOLUTION -> avec x qui est un tableau à deux dimensions : x1 , x2 et u est l'entrée
def f(x,u): 
#    m=1.0
#    g=9.81
#    l=2.0
#    mu=0.1
    
    Xdot =   [x[1], -((x[0]) ** 2-1) * x[1] - x[0]]
    return np.array(Xdot)

#METHODE D'EULER
def methode_euler(t,X0, h):
    #CONDITION INITIALES
    u=0
    X=np.zeros((len(X0), len(t)),'float')
    X[:,0]=X0
    
    for i in range( 0, len(t)-1):
        X[:, i+1] = X[:, i] + h*f(X[:, i], u)
        
    return X


#METHODE RK2 - Runge Kutta
def methode_RK(t,X0, h):
    #CONDITION INITIALES
    u=0
    X=np.zeros((len(X0), len(t)),'float')
    X[:,0]=X0
    
    for i in range( 0, len(t)-1):
        X[:, i+1] = X[:, i] + h*f(X[:, i] + h/2*f( X[ :, i], u), u)
        
    return X

def creationgraphique(X, Y, graphiquenumero, titre, labelX, labelY, ):  
    plt.figure(graphiquenumero)
    plt.plot(X, Y)
    plt.title(titre)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.show()
    
#MAIN
if __name__ == "__main__":
    print("Test Modele")
    
    X0=np.array([ 1.0 , 0]) # Valeur initiale de X0
    
    #PARAMETRE DE SIMULATION
    h = 0.05
    duree = 50
    t=np.arange( 0.0, duree, h)
    print("taille: ", len(t),"duree: ", t[-1])

    #METHODE EULER
    X=methode_euler(t, X0, h)   
    creationgraphique(t, X[1], 1, "Vitesse", "Temps", "Vitesse")
    creationgraphique(t, X[0], 2, "Position", "Temps", "Position")
    creationgraphique(X[0], X[1], 3, "Phase", "Distance", "Vitesse")

    
    #METHODE RUNGE KUTTA
    X=methode_RK(t, X0, h)   
    creationgraphique(t, X[1], 1, "Vitesse", "Temps", "Vitesse")
    creationgraphique(t, X[0], 2, "Position", "Temps", "Position")
    creationgraphique(X[0], X[1], 3, "Phase", "Distance", "Vitesse")
    
    
    #RESULTATS
print(t,",",X0)# -*- coding: utf-8 -*-

#vp= np.linalg.eig(np.array([[0, 1], [-1, 1]]))
#
#print (vp)
