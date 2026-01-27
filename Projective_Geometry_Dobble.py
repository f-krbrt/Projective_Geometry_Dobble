# p = 3 pour avoir Z3Z
p=3

class Z3Z:
    def __init__(self,a,b,c,d):
        self.x=a%p
        self.y=b%p
        self.z=c%p
        self.t=d%p
    def __add__(self,other):
        ma=(self.x+other.x)%p
        mb=(self.y+other.y)%p
        mc=(self.z+other.z)%p
        md=(self.t+other.t)%p
        return Z3Z(ma,mb,mc,md)
    def show(self):
        return (int(self.x),int(self.y),int(self.z),int(self.t))
    def vec_nul(self):
        return (self.x==0 and self.y==0 and self.z==0 and self.t==0 )
    def mult(sel,other):
        ma=(self.x*other.x)%p
        mb=(self.y*other.y)%p
        mc=(self.z*other.z)%p
        md=(self.t*other.t)%p
        return Z3Z(ma,mb,mc,md)
    def solution(self,other):
        return (self.x*other.x + self.y*other.y + self.z*other.z + self.t*other.t)%3==0


##Exemple :
#Ici on devrait avoir False
print(Z3Z.solution(Z3Z(1,2,1,0),Z3Z(0,0,1,2)))
#Ici on devrait avoir True
print(Z3Z.solution(Z3Z(1,2,0,0),Z3Z(1,1,0,2)))






def liste_points(p):
    """cette fonction crée une base de point (ou plan) dans ZPZ, dans notre cas on a p = 3"""
    L=[]
    for x in range(0,p):
        for y in range(0,p):
            for z in range(0,p):
                L.append(Z3Z(x,y,z,1))

            L.append(Z3Z(x,y,1,0))
        L.append(Z3Z(x,1,0,0))
    L.append(Z3Z(1,0,0,0))
    return L



def tri_pointaffine_pointsinfini(l):
    """
    cette fonction tri une liste de points (affine + infinie) et renvoie la liste de ces memes points en commencant
    par les points affines
    """
    laff=[]
    linf=[]
    for i in l:
        if Z3Z.show(i)[3]==1:
            laff.append(i)
        else:
            linf.append(i)
    return laff+linf




def affiche_liste_points(p):
    """
    Cette fonction affiche simplement tous les points créés par liste_points(p)
    """
    L=liste_points(p)
    for i in L:
        print(Z3Z.show(i))
        #print(type(Z3Z.show(i)))
    print(len(L))
    return

def affiche_liste_Z3Z(l):
    """
    Cette fonction affiche tous les point d'une liste l
    """
    for i in l:
        print(Z3Z.show(i))
    return None


#------Test--------
#affiche_liste_points(3)
#affiche_liste_Z3Z(liste_points(3))
affiche_liste_Z3Z(tri_pointaffine_pointsinfini(liste_points(3)))

###



def plans_sol(p,lplan):
    """argument : p = un point dans Z/3Z ;
                  lpan = liste de tous les plans existant dans Z/3Z

    renvoie la liste des plans auxquelle le point p appartient"""

    L=[]
    for m in lplan:
        if Z3Z.solution(p,m):
            L.append(m)
    return L





#print(len(plans_sol(liste_points(3)[0],liste_points(3))))


def affiche_plan_sol(p,lplan):
    """    
    Affiche les plans solution d'un point (plan auxquels il appartient)
    """
    lst_plan_sol = plans_sol(p,lplan)
    print("le point p :",Z3Z.show(p)," appartient a chacun de ces plan : \n\n")
    for i in lst_plan_sol:
        print(Z3Z.show(i))
        #print(type(Z3Z.show(i)))
    return None




affiche_plan_sol(liste_points(3)[1],liste_points(3))
print("\n")
affiche_plan_sol(liste_points(3)[15],liste_points(3))
print("\n")
affiche_plan_sol(liste_points(3)[38],liste_points(3))
print("\n")
affiche_plan_sol(liste_points(3)[17],liste_points(3))








symboles=["livre","barrière","épingle","lettre","lait","ballon","maison","piscine","chaise","horloge","église","nouille","oeuf","sac","vache","chaussettes","baleine","oignon","échelle","lunettes","tableau","appareil photo","chat","dragon","tomates","ninja","avion","soleil","telephone","écharpe","glace","lampadaire","fromage","fusil","poisson","arbre","fleurs","tobogan","fusée","bateau"]






###
def dico_final_image(symbole,l1,l2):
    """
    renvoie un dico dont les clés sont les points et dont la valeur est la liste des plan auxquelle appartient le point "clef".
    l1=liste des points en Z3Z ;
    l2= liste des plans en Z3Z ;
    """
    l1u=convert(l1)
    l2u=convert(l2)
    dico_image=attribut(symbole,l2u)
    dico_cartes=cartes(l1u)
    dico_final={}


    for i in range(0,len(l1)):
        Li_symboles=[]
        L_solution=convert(plans_sol(l1[i],l2))

        for j in range(0,len(L_solution)):
            Li_symboles.append(dico_image[L_solution[j]])
        dico_final[dico_cartes[l1u[i]]]=Li_symboles


    return dico_final





def attribut(symboles,lplan_uplet):
    """cette fonction associe à chacun des 40 plan une unique image/symbole"""
    dico={}
    for i in range(0,len(lplan_uplet)):
        dico[lplan_uplet[i]]=symboles[i]
    return dico



def cartes(lu):
    dico={}
    for i in range(0,len(lu)):
        dico[lu[i]]=i
    return dico



def convert(l):
    """
    cette fonction convertie un liste de uplet Z3Z en list de uplet d'entier"""
    lreturn=[]
    for i in range(0,len(l)):
        lreturn.append(Z3Z.show(l[i]))
    return lreturn



def meme3(l1,l2,l3):
    l=[]
    for i in l1:
        if (i in l2) and (i in l3):
            l.append(i)
    return l





def meme(l1,l2):
    l=[]
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if l1[i]==l2[j] and (l1[i] not in l):
                l.append(l1[i])
    return l










ddico=attribut(symboles,convert(liste_points(3)))


l1=liste_points(3) # liste des points
l2=liste_points(3) # liste des plan

ddddd=dico_final_image(symboles,l1,l2)


a=31
b=29
c=19

print(ddddd)
print("\n\n\n\n\n\n",ddddd[a],"\n","\n",ddddd[b],"\n","\n",ddddd[c])



print("\n\n\nvoici les elts commun a l1 et l2 \n",meme(ddddd[a],ddddd[b]))

print("\n\n\nvoici les elts commun a l1,l2 et l3 \n",meme3(ddddd[a],ddddd[b],ddddd[c]))


###

## probleme les plans peuvent en fait former des droites





def alignes(a,b,c):
    """
    cette fonction verifier si 3 points sont aligné ( renvoie True ou False )
    """

    #cas affine
    if a[3]==1 and b[3]==1 and c[3]==1:

        v1 = (b[0]-a[0],b[1]-a[1],b[2]-a[2])
        v2 = (c[0]-b[0],c[1]-b[1],c[2]-b[2])

        for k in range(0,p):
            if (v1[0]==k*v2[0]) and ((v1[1]==k*v2[1]) and (v1[2]==k*v2[2])):
                return True
            if (v1[0]==-k*v2[0]) and ((v1[1]==-k*v2[1]) and (v1[2]==-k*v2[2])):
                return True

        return False

    #cas pas affine





## on veut prendre des points tel que aucun triplet ne donne une droite (mais bien un plan)

"""

x . x
. . .
x . x

. . .
. x .
. . .

. x .
x . x
. x .

"""
# liste des points affine a laquelle on ajoute un point infini n'appartenant a aucune de droite deja existentes
l=[Z3Z(1,0,0,1),Z3Z(2,1,0,1),Z3Z(0,1,0,1),Z3Z(1,2,0,1),Z3Z(1,1,1,1),Z3Z(0,0,2,1),Z3Z(2,0,2,1),Z3Z(0,2,2,1),Z3Z(2,2,2,1)] 


