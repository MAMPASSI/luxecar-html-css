#exercice sur les commmande et client (dernier exercice)
class client:
  def __init__(self,nom,adresse):
    self.Nom=nom
    self.adresse=adresse
  def afficher(self):
    print("le non du client",self.Nom)
    print("l'adresse du client",self.adresse)


class personne_morale(client):
  def __init__(self,nom,adresse,contact,limitecredit):
    client.__init__(self,nom,adresse)
    self.contact=contact
    self.limite=limitecredit
  
  def edieterfacture(self):
    print("la limite de la carte")
  
  def afficher(self):
    client.afficher(self)
    print("le contact de la personne morale :",self.contact)
    print("limite de carte de credit de la personne morale",self.limite)
    
  
  
class personne_physique(client):
  def __init__(self,nom,adresse,numero_carte):
    client.__init__(self,nom,adresse)
    self.carte=numero_carte
  def afficher(self):
    client.afficher(self)
    print("le numero de carte est le suivant:",self.carte)
  



class commande:
  def __init__(self,date,numero,client):
    self.date=date
    self.numero=numero
    self.prix=0
    self.client=client
    self.ligne_co=[]
  
  def aquitter(self):
    print("la commande a été payée")
    
  def ajout_ligne(self,ligne_commande):
    self.ligne_co.appennd(ligne_commande)
  
  def calculer_prix(self):
    for i in self.ligne_co:
      self.prix=self.prix+(self.pris*self.quantite)
  
  def detaille_commande(self):
    print("la commande est composé par les ligne suivant :")
    for i in self.ligne_co:
      i.afficher()
      
    
  
  def afficher(self):
    print("la date de la commande:",self.date)
    print("le numero dela comande",self.numero)
    print("le prix :",self.prix)
    self.client.afficher()
    

class ligne_commande:
  def __init__(self,quantite,a):
    self.quantite=quantite
    self.pris=a
  
  def afficher(self):
    print("la quantiter",self.quantite)
    print("le prix",self.pris)
    
    
#class article(ligne_commande):
  #def __init__(self,date,numero,prix,quantite,prix_Unitaire):
    #ligne_commande.__init__(self,date,numero,prix,quantite)
    #self.unitaire=prix_Unitaire
    
    
  #code principale
  p1=personne_morale("jean","paris",4578,300)
  p1.afficher()
  print("**************************************")
  p2=personne_physique("roli","brunoy",6789068)
  p2.afficher()
  
  print("**************************************************")
  
  c=commande("12/8/2023",23,p1)
  c.afficher()
  l1=ligne_commande(23,10)
  l2=ligne_commande(10,5)
  c.ajout_ligne(l1)
  c.ajout_ligne(l2)
  c.calculer_prix()
  print("************************************************************************************")
  print(c.prix)
  print("************************************************")
  c.detaille_commande()
  
  
  
    
    
  