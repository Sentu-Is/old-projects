import json
import time
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests
response = requests.get("https://gameinfo.albiononline.com/api/gameinfo/events")
if response.status_code == 200:


    class killBoard:
        def __init__(self, i):
            old_kills = None
            self.i = 0
            var = None
            images_killer = []
            images_victim = []
            emptyPng = "../Resources/empty_png.png"
            data = response.json()
            while True:
                for names in data:

                    try:
                        self.killer_name = names["Killer"]["Name"]
                        self.killer_ip = names["Killer"]["AverageItemPower"]
                        if names["numberOfParticipants"] > 1:
                            for participants in names["Participants"]["Name"]:
                                self.participants_names = []
                                self.participants_names.append(participants)
                                print(participants)
                        else:
                            self.participants_names = ""
                        killer_main_hand = names["Killer"]["Equipment"]["MainHand"]

                        if killer_main_hand is None:
                                self.killer_main_hand_url = emptyPng
                        else:
                            killer_main_hand = names["Killer"]["Equipment"]["MainHand"]["Type"]
                            self.killer_main_hand_url = "https://render.albiononline.com/v1/item/" + str(killer_main_hand)

                        killer_off_hand = names["Killer"]["Equipment"]["OffHand"]
                        if killer_off_hand is None:
                                self.killer_off_hand_url = emptyPng
                        else:
                            killer_off_hand = names["Killer"]["Equipment"]["OffHand"]["Type"]
                            self.killer_off_hand_url = "https://render.albiononline.com/v1/item/"+ str(killer_off_hand)

                        killer_helmet = names["Killer"]["Equipment"]["Head"]
                        if killer_helmet is None:
                                self.killer_helmet_url = emptyPng
                        else:
                            killer_helmet = names["Killer"]["Equipment"]["Head"]["Type"]
                            self.killer_helmet_url = "https://render.albiononline.com/v1/item/"+ str(killer_helmet)


                        killer_armor = names["Killer"]["Equipment"]["Armor"]
                        if killer_armor is None:
                                self.killer_armor_url = emptyPng
                        else:
                            killer_armor = names["Killer"]["Equipment"]["Armor"]["Type"]
                            self.killer_armor_url = "https://render.albiononline.com/v1/item/"+ str(killer_armor)

                        killer_shoes = names["Killer"]["Equipment"]["Shoes"]
                        if killer_shoes is None:
                                self.killer_shoes_url = emptyPng
                        else:
                            killer_shoes = names["Killer"]["Equipment"]["Shoes"]["Type"]
                            self.killer_shoes_url = "https://render.albiononline.com/v1/item/"+ str(killer_shoes)


                        killer_potion = names["Killer"]["Equipment"]["Potion"]
                        if killer_potion is None:
                                self.killer_potion_url = emptyPng
                        else:
                            killer_potion = names["Killer"]["Equipment"]["Potion"]["Type"]
                            self.killer_potion_url = "https://render.albiononline.com/v1/item/"+ str(killer_potion)


                        killer_food = names["Killer"]["Equipment"]["Food"]
                        if killer_food is None:
                                self.killer_food_url = emptyPng
                        else:
                            killer_food = names["Killer"]["Equipment"]["Food"]["Type"]
                            self.killer_food_url = "https://render.albiononline.com/v1/item/"+ str(killer_food)


                        killer_bag = names["Killer"]["Equipment"]["Bag"]
                        if killer_bag is None:
                                self.killer_bag_url = emptyPng
                        else:
                            killer_bag = names["Killer"]["Equipment"]["Bag"]["Type"]
                            self.killer_bag_url = "https://render.albiononline.com/v1/item/"+ str(killer_bag)


                        killer_mount = names["Killer"]["Equipment"]["Mount"]
                        if killer_mount is None:
                                self.killer_mount_url = emptyPng
                        else:
                            killer_mount = names["Killer"]["Equipment"]["Mount"]["Type"]
                            self.killer_mount_url = "https://render.albiononline.com/v1/item/"+ str(killer_mount)


                        killer_cape = names["Killer"]["Equipment"]["Cape"]
                        if killer_cape is None:
                                self.killer_cape_url = emptyPng
                        else:
                            killer_cape = names["Killer"]["Equipment"]["Cape"]["Type"]
                            self.killer_cape_url = "https://render.albiononline.com/v1/item/"+ str(killer_cape)



                        self.victim_name = names["Victim"]["Name"]
                        victim_main_hand = names["Victim"]["Equipment"]["MainHand"]
                        if victim_main_hand is None:
                                self.victim_main_hand_url = emptyPng
                        else:
                            victim_main_hand = names["Victim"]["Equipment"]["MainHand"]["Type"]
                            self.victim_main_hand_url = "https://render.albiononline.com/v1/item/" + str(victim_main_hand)

                        victim_off_hand = names["Victim"]["Equipment"]["OffHand"]
                        if victim_off_hand is None:
                                self.victim_off_hand_url = emptyPng
                        else:
                            victim_off_hand = names["Victim"]["Equipment"]["OffHand"]["Type"]
                            self.victim_off_hand_url = "https://render.albiononline.com/v1/item/" + str(victim_off_hand)

                        victim_helmet = names["Victim"]["Equipment"]["Head"]
                        if victim_helmet is None:
                                self.victim_helmet_url = emptyPng
                        else:
                            victim_helmet = names["Victim"]["Equipment"]["Head"]["Type"]
                            self.victim_helmet_url = "https://render.albiononline.com/v1/item/" + str(victim_helmet)

                        victim_armor = names["Victim"]["Equipment"]["Armor"]
                        if victim_armor is None:
                                self.victim_armor_url = emptyPng
                        else:
                            victim_armor = names["Victim"]["Equipment"]["Armor"]["Type"]
                            self.victim_armor_url = "https://render.albiononline.com/v1/item/" + str(victim_armor)

                        victim_shoes = names["Victim"]["Equipment"]["Shoes"]
                        if victim_shoes is None:
                                self.victim_shoes_url = emptyPng
                        else:
                            victim_shoes = names["Victim"]["Equipment"]["Shoes"]["Type"]
                            self.victim_shoes_url = "https://render.albiononline.com/v1/item/" + str(victim_shoes)

                        victim_potion = names["Victim"]["Equipment"]["Potion"]
                        if victim_potion is None:
                                self.victim_potion_url = emptyPng
                        else:
                            victim_potion = names["Victim"]["Equipment"]["Potion"]["Type"]
                            self.victim_potion_url = "https://render.albiononline.com/v1/item/" + str(victim_potion)

                        victim_food = names["Victim"]["Equipment"]["Food"]
                        if victim_food is None:
                            self.victim_food_url = emptyPng
                        else:
                            victim_food = names["Victim"]["Equipment"]["Food"]["Type"]
                            self.victim_food_url = "https://render.albiononline.com/v1/item/" + str(victim_food)

                        victim_bag = names["Victim"]["Equipment"]["Bag"]
                        if victim_bag is None:
                                self.victim_bag_url = emptyPng
                        else:
                            victim_bag = names["Victim"]["Equipment"]["Bag"]["Type"]
                            self.victim_bag_url = "https://render.albiononline.com/v1/item/" + str(victim_bag)

                        victim_mount = names["Victim"]["Equipment"]["Mount"]
                        if victim_mount is None:
                                self.victim_mount_url = emptyPng
                        else:
                            victim_mount = names["Victim"]["Equipment"]["Mount"]["Type"]
                            self.victim_mount_url = "https://render.albiononline.com/v1/item/" + str(victim_mount)

                        victim_cape = names["Victim"]["Equipment"]["Cape"]
                        if victim_cape is None:
                                self.victim_cape_url = emptyPng
                        else:
                            victim_cape = names["Victim"]["Equipment"]["Cape"]["Type"]
                            self.victim_cape_url = "https://render.albiononline.com/v1/item/" + str(victim_cape)

                        self.victim_inventory = names["Victim"]["Inventory"]
                        if self.victim_inventory[0] is None:
                            print(self.victim_inventory)
                            self.victim_inventory_url = "../Resources/albion_png.jpg"
                        else:
                            self.victim_inventory = names["Victim"]["Inventory"]["Type"]
                            print(self.victim_inventory)
                            for items in self.victim_inventory:
                                self.victim_inventory_url = []
                                if items is None:
                                    continue
                                else:
                                    self.victim_inventory_url.append("https://render.albiononline.com/v1/item/" + str(items))
                                    print(self.victim_inventory_url)



                        print("Killer : ", self.i, self.killer_name)
                        print("Item : ", self.i, killer_main_hand)

                        old_kills = data

                        data = requests.get("https://gameinfo.albiononline.com/api/gameinfo/events")
                        data = data.json()
                        if old_kills is not None and data != old_kills:
                            print("la api se actualizo")
                            old_kills = data
                        else:
                            print("test")

                        self.i += 1
                        if self.i == i:
                            break



                    except TypeError:
                        pass
                if self.i == i:
                    break



        def kb_image(self):
            images_killer = [self.killer_main_hand_url,self.killer_off_hand_url,self.killer_helmet_url,self.killer_armor_url,self.killer_shoes_url, self.killer_potion_url, self.killer_food_url, self.killer_bag_url,self.killer_mount_url,self.killer_cape_url]
            self.final_image = Image.new("RGBA", (800, 600), (0,0,0, 1))
            for piece, killer_equipment in enumerate(images_killer):
                try:
                    equipment_download = requests.get(killer_equipment)
                    killer_equipment_image = Image.open(BytesIO(equipment_download.content))
                except:
                    killer_equipment_image = Image.open(killer_equipment)
                killer_equipment_image = killer_equipment_image.resize((100, 100))
                killer_equipment_image = killer_equipment_image.crop((10,10,100 - 10,100 - 10))
                if piece == 0:
                    self.final_image.paste(killer_equipment_image, (16,180))
                if piece == 1:
                    self.final_image.paste(killer_equipment_image, ( 185,  180))
                if piece == 2:
                    self.final_image.paste(killer_equipment_image, ( 100,  98))
                if piece == 3:
                    self.final_image.paste(killer_equipment_image, ( 100,  180))
                if piece == 4:
                    self.final_image.paste(killer_equipment_image, ( 100,  260))
                if piece == 5:
                    self.final_image.paste(killer_equipment_image, ( 16,  260))
                if piece == 6:
                    self.final_image.paste(killer_equipment_image, ( 185,  260))
                if piece == 7:
                    self.final_image.paste(killer_equipment_image, (16, 98))
                if piece == 8:
                    self.final_image.paste(killer_equipment_image, (100, 350))
                if piece == 9:
                    self.final_image.paste(killer_equipment_image, (185, 98))

                images_victim = [self.victim_main_hand_url, self.victim_off_hand_url, self.victim_helmet_url, self.victim_armor_url, self.victim_shoes_url, self.victim_potion_url,self.victim_food_url, self.victim_bag_url,self.victim_mount_url,self.victim_cape_url]
            for piece_v, victim_equipment in enumerate(images_victim):
                try:
                    equipment_download = requests.get(victim_equipment)
                    victim_equipment_image = Image.open(BytesIO(equipment_download.content))
                except:
                    victim_equipment_image = Image.open(victim_equipment)

                victim_equipment_image = victim_equipment_image.resize((100, 100))
                victim_equipment_image = victim_equipment_image.crop((10,10,100 - 10,100 - 10))
                if piece_v == 0:
                    self.final_image.paste(victim_equipment_image, ( 516, 180))
                if piece_v == 1:
                    self.final_image.paste(victim_equipment_image, ( 685,  180))
                if piece_v == 2:
                    self.final_image.paste(victim_equipment_image, ( 600,  98))
                if piece_v == 3:
                    self.final_image.paste(victim_equipment_image, ( 600,  180))
                if piece_v == 4:
                    self.final_image.paste(victim_equipment_image, ( 600,  260))
                if piece_v == 5:
                    self.final_image.paste(victim_equipment_image, ( 685,  260))
                if piece_v == 6:
                    self.final_image.paste(victim_equipment_image, ( 516,  260))
                if piece_v == 7:
                    self.final_image.paste(victim_equipment_image, (516, 98))
                if piece_v == 8:
                    self.final_image.paste(victim_equipment_image, (600, 350))
                if piece_v == 9:
                    self.final_image.paste(victim_equipment_image, (685, 98))

            vs_logo = Image.open("../Resources/vs_logo.png")

            self.final_image.paste(vs_logo, (325, 200))
            draw = ImageDraw.Draw(self.final_image)
            font = ImageFont.truetype(r"C:/Windows/Fonts/arial.ttf", 20)
            killer_color = (0,0,0)
            victim_color = (255, 255, 255)
            draw.text((20, 50),"Assassin: " + self.killer_name, font=font, fill=killer_color)
            draw.text((520, 50), "Victim: " + self.victim_name, font=font, fill=victim_color)

            return self.final_image
        def kb_inventory(self):
            height = 800
            weight = 600
            self.inventory = Image.new("RGBA", (height, weight), (0,0,0,1))
            for i, items in enumerate(self.victim_inventory_url):
                x = i * 100
                try:
                    inventory_download = requests.get(self.victim_inventory_url)
                    inventory_image = Image.open(BytesIO(inventory_download.content))
                except:
                    inventory_image = Image.open(self.victim_inventory_url)
                inventory_image = inventory_image.resize((100, 100))

                self.inventory.paste(inventory_image, (x, 20))
            return self.inventory












