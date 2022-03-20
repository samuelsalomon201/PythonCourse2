class MyMods(object):
    """This Is A List OF My Mods (More Villagers MrCrayFish's Furniture Mod Ripples Of The Past"""
    def __init__(self, stand, hamon, vamp, items):
        self.stand = stand
        self.hamon = hamon
        self.vamp = vamp
        self.items = items
    def print_ripplesofthepast(self,Content):
        print("Stands Are Star Platinum, The World, Magicians Red, Hierophant Green, Silver Chariot.", self.stand)
        print("Types Of Hamon Are LisaLisa, Joseph, Jonathan, Cesar.", self.hamon)
        print("Dio, Kars, (Forgot The Rest Of Em).", self.vamp)
        print("Zeppelin's Hat, Joseph Clangers, LisaLisa Scarf, Dio's Knives, Stand Arrow, Upgraded Stand Arrow.", self.items)

Mods1 = MyMods('Stands','Hamon','Vamp','Items')
print(Mods1)
print(Mods1.stand)
print(Mods1.hamon)
print(Mods1.vamp)
print(Mods1.items)


Mods1.print_ripplesofthepast("JOJOSTONEOCEANLALALALALA")

Mods2 = MyMods('Star Platinum','Cesar Hamon','Kars Vamp','Sledge Hammer')
print(Mods2)
print(Mods2.stand)
print(Mods2.hamon)
print(Mods2.vamp)
print(Mods2.items)

Mods2.print_ripplesofthepast("SevenPageMuda")
