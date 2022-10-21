
# Soldier
import random

class Soldier:
    def __init__(self,health=0, strength=0):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health=self.health - damage
        return 
        

# Viking
class Viking(Soldier):
    
    def __init__(self,name="",health=0,strenght=0):
    
        Soldier.__init__(self)
        self.name=name
        self.health=health
        self.strenght=strenght 
    
    def receiveDamage(self,damage):
        
        self.health=self.health - damage
        if self.health >0:
            return(f'{self.name} has received {damage} points of damage')
        else:
            return(f'{self.name} has died in act of combat')
    
    def battleCry(self):
        return("Odin Owns You All!")
      
# Saxon
class Saxon(Soldier):
    def __init__(self,health=0,strenght=0):
        Soldier.__init(self)
        self.health=health
        self.strenght=strenght
    
    
    def receiveDamage(self,damage):
        self.health=self.health - damage
        if self.health > 0:
            return(f"A Saxon has received {the_damage} points of damage")
        else:
            return("A Saxon has died in combat")

# War
class War:
    def __init__(self):
        self.vikingArmy=vikingArmy=[]
        self.saxonArmy=saxonArmy=[]
        
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
                  
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
                  
    def vikingAttack(self):
        x=random.choice(self.vikingArmy)
        y=random.choice(self.saxonArmy)
        ret = y.receiveDamage(x.attack())
        if y.health <= 0:
            self.vikingArmy.pop(y)
        return ret
                  
    def saxonAtack(self):
        x=random.choice(self.vikingArmy)
        y=random.choice(self.saxonArmy)
        ret = x.receiveDamage(y.attack())
        if x.health <= 0:
            self.vikingArmy.pop(x)
        return ret
        
                 
    def showStatus(self):
        lvacia=[]
        if len(self.vikingArmy) == lvacia:
            return("Vikings have won the war of the century!")
        elif len(self.saxonArmy)== lvacia:
            return("Saxons have fought for their lives and survive another day...")
        else:
            return("Vikings and Saxons are still in the thick of battle.")
        
        
