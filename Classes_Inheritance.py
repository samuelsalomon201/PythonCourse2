class MyMods(object):
    """This Is A List OF My Mods (More Villagers MrCrayFish's Furniture Mod Ripples Of The Past"""
    def __init__(self, stand, hamon, vamp, items):
        self.stand = stand
        self.hamon = hamon
        self.vamp = vamp
        self.items = items
    def print_ripplesofthepast(self, content):
        print("Stands Are Star Platinum, The World, Magicians Red, Hierophant Green, Silver Chariot.", self.stand)
        print("Types Of Hamon Are LisaLisa, Joseph, Jonathan, Cesar.", self.hamon)
        print("Dio, Kars, (Forgot The Rest Of Em).", self.vamp)
        print("Zeppelin's Hat, Joseph Clangers, LisaLisa Scarf, Dio's Knives, Stand Arrow, Upgraded Stand Arrow.", self.items)
        print("The Stand & Hamon Combined: "), self.stand + content