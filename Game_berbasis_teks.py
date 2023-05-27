import time
import sys
import os
import textwrap


skip_time = 0.5
NAME = 'name'
DESCRIPTION = ' description'
DIRECTION = 'direction'
ITEM_GROUND = 'item_ground'
SCREEN_WIDTH = 'screen_width'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
DESCWORDS = 'descwords'
CRAFTED = 'crafted'
QUANTITY = 'quantity'
INGREDIENTS = 'ingredients'
FUNC = 'func'
STATUS = 'status'
COOK = 'cook'
CAN_USE = 'can_use'
USE = 'use'

pondok1 = 0
pondok2 = 0
hutan2_1 = 0
hutan2_2 = 0
pantai = 0
triger_statue = 3


class Player:
    def __init__(self, ):
        self.location = "GUA"
        self.inventory = []


pemain = Player()
SCREEN_WIDTH = 80


default_direction = (0, 0, 0, 0, 0, 0)
location_dict ={
    'GUA': {
        NAME : 'GUA',
        DESCRIPTION: "kau berada di gua",
        DIRECTION : default_direction, # direction = (utara, timur, selatan, barat)
                                    # 0 menunjukan arah yg tidak dapat dilalui
        ITEM_GROUND : ['Cairan gua', 'Cairan gua', 'Cairan gua']
    },
    'HUTAN1': {
        NAME : 'HUTAN1',
        DESCRIPTION: "kau berada di hutan1",
        DIRECTION : default_direction,
        ITEM_GROUND : ['Pohon', 'Buah anggur','Buah anggur','Buah anggur'],},
    
    'RUMAH POHON' : {
        NAME : 'RUMAH POHON',
        DESCRIPTION: "kau masuk ke rumah pohon",
        DIRECTION : default_direction,
        ITEM_GROUND : ['Tombak'],
    },
        
    'SUNGAI': {
        NAME : 'SUNGAI',
        DESCRIPTION: "kau berada di sungai",
        DIRECTION : default_direction,
        ITEM_GROUND : ['Ikan', 'Air']
    },
    'PONDOK': {
        NAME : 'PONDOK',
        DESCRIPTION: "kau berada di pondok",
        DIRECTION : default_direction,
        ITEM_GROUND : ['Tungku api']
    },
    'HUTAN2': {
        NAME : 'HUTAN2',
        DESCRIPTION: "kau berada di hutan2",
        DIRECTION : default_direction,
        ITEM_GROUND : ['Patung']
    },
    'PANTAI': {
        NAME : 'PANTAI',
        DESCRIPTION: "kau berada di pantai",
        DIRECTION : default_direction,
        ITEM_GROUND : ['Pasir', 'Kerang']
    },
    'LAUT': {
        NAME : 'LAUT',
        DESCRIPTION: "kau berada di laut",
        DIRECTION : default_direction,
        ITEM_GROUND : ['Ikan Laut', 'Rumput Laut']
    }, 
}

Item_dict = {

    'Cairan gua': {
        GROUNDDESC: 'Sebuah cairan dari kelelawar gua', 
        LONGDESC: 'Ini adalah sebuah cairan yang ditemukan pada gua ,kemungkinan ini dihasilkan dari kotoran kelelawar gua', 
        SHORTDESC: 'cairan gua',
        TAKEABLE : True,
        DESCWORDS : ['cairan', 'cairan gua']},
    
    'Etanol': {
        GROUNDDESC: 'Cairan yang didapat dari anggur yang di masak', 
        LONGDESC: 'Etanol didapat dari anggur yang dimasak , digunakan untuk membuat cairan pembangkit', 
        SHORTDESC: 'etanol',
        TAKEABLE : True,
        DESCWORDS : ['etanol']},

    'Pohon': {
        GROUNDDESC: 'Didekatmu ada sebuah pohon besar', 
        LONGDESC: "ada sebuah tulisan yang tergores dipohon : 'jika kau sudah bangun  aku ada di utara diseberang sungai'", 
        SHORTDESC: 'Pohon besar',
        TAKEABLE : False,
        DESCWORDS : ['pohon']},
        
    'Buah anggur': {
        GROUNDDESC: 'Sebuah buah anggur yang kelihatan lezat', 
        LONGDESC: 'Sebuah anggur, nampaknya ini masih anggur yang sama seperti 3000 tahun lalu mungkin ini bisa berguna', 
        SHORTDESC: 'buah anggur',
        TAKEABLE : True,
        DESCWORDS : ['anggur', 'buah anggur'],
        COOK : 'Etanol',},
    
    'Patung' :{
        GROUNDDESC: 'patung manusia yang berubah jadi patung batu ', 
        LONGDESC: 'manusia yang menjadi patung batu 3000 tahun lalu karena kejadian misterius', 
        SHORTDESC: 'Patung ',
        TAKEABLE : False,
        DESCWORDS : ['patung', 'patung batu', 'patung rani'],
        USE : 'Nital',
        CAN_USE : False},

    'Ikan': {
        GROUNDDESC: 'Ikan dari sungai', 
        LONGDESC: 'Ikan yang besar dan nampak enak untuk dimakan ', 
        SHORTDESC: 'Ikan sungai',
        TAKEABLE : True,
        DESCWORDS : ['ikan', 'lele', 'ikan sungai']},
    
    'Ikan Laut': {
        GROUNDDESC: 'ikan laut yang besar besar ', 
        LONGDESC: 'Ikan laut yang besar dan nampak enak untuk dimakan ', 
        SHORTDESC: 'Ikan laut',
        TAKEABLE : True,
        DESCWORDS : ['ikan', 'ikan laut']},
        
    'Air': {
        GROUNDDESC: 'sebuah air yang jernih dari sungai', 
        LONGDESC: 'Ini adalah sebuah cairan yang ditemukan pada gua ,kemungkinan ini dihasilkan dari kotoran kelelawar gua', 
        SHORTDESC: 'Air sungai',
        TAKEABLE : True,
        DESCWORDS : ['air', 'air sungai', 'air tawar']},

    'Pasir': {
        GROUNDDESC: 'Pasir putih di pantai yang indah', 
        LONGDESC: 'Pasir putih jernih di pantai, mungkin ini berguna.', 
        SHORTDESC: 'Pasir',
        TAKEABLE : True,
        DESCWORDS : ['pasir', 'pasir pantai']},

    'Kerang': {
        GROUNDDESC: 'kerang diantara batu dan pasir-pasir pantai ', 
        LONGDESC: 'Kerang laut yang terbawa arus laut biasanya mudah ditemukan diarea pantai', 
        SHORTDESC: 'Kerang',
        TAKEABLE : True,
        DESCWORDS : ['kerang']},
        

    'Rumput Laut' : {
        GROUNDDESC: 'rumput laut kelihatan segar  ', 
        LONGDESC: 'Rumput laut bahan yang sangat penting pada zaman batu ini', 
        SHORTDESC: 'Rumput laut',
        TAKEABLE : True,
        DESCWORDS : ['rumput laut']},
    

    'Tungku api':{
        GROUNDDESC: 'Tungku api dari tembikar tanah liat', 
        LONGDESC: 'Tungku api ini bisa digunakan untuk membakar bahan-bahan', 
        SHORTDESC: 'Tungku api',
        TAKEABLE : False,
        DESCWORDS : ['tungku', 'tungku api'],
        FUNC : ['Masak',]},

    
    'Tombak':{
        GROUNDDESC: 'Tombak batu lancip', 
        LONGDESC: 'Tombak batu yang dibuat dari batu yang diasah sampai tajam', 
        SHORTDESC: 'Tombak',
        TAKEABLE : True,
        DESCWORDS : ['tombak', 'tombak batu'],
        FUNC : ['Buru']},
    
    'Etanol': {
        GROUNDDESC: 'Cairan yang didapat dari anggur yang di masak', 
        LONGDESC: 'Etanol didapat dari anggur yang dimasak , digunakan untuk membuat cairan pembangkit', 
        SHORTDESC: 'etanol',
        TAKEABLE : True,
        DESCWORDS : ['etanol']},     
        
    'Nital':{
        INGREDIENTS : ['Etanol', 'Cairan gua'],
        GROUNDDESC: 'cairan pembangkit patung ', 
        LONGDESC: 'perpaduan etanol dari anggur dan asam nitrat dari cairan gua', 
        SHORTDESC: 'Cairan pembangkit',
        TAKEABLE : True,
        DESCWORDS : ['cairan pembangkit','nital'],
        FUNC :['To_object']},
}


#direction north, east, south, west, in, out
location_dict['GUA'][DIRECTION] =(0, 0 ,0 , location_dict['HUTAN1'][NAME], 0, 0)
location_dict['HUTAN1'][DIRECTION] = (location_dict['SUNGAI'][NAME], location_dict['GUA'][NAME], 0, 0, 0, 0)
location_dict['SUNGAI'][DIRECTION] = (location_dict['PONDOK'][NAME], 0, location_dict['HUTAN1'][NAME], 0, 0, 0)
location_dict['PONDOK'][DIRECTION] = (location_dict['PANTAI'][NAME], 0,location_dict['SUNGAI'][NAME], location_dict['HUTAN2'][NAME], location_dict['RUMAH POHON'][NAME], 0)
location_dict['HUTAN2'][DIRECTION] = (0, location_dict['PONDOK'][NAME],0, 0, 0, 0)
location_dict['PANTAI'][DIRECTION] = (location_dict['LAUT'][NAME], 0 ,location_dict['PONDOK'][NAME] , 0, 0, 0)
location_dict['LAUT'][DIRECTION] = (0, 0 ,location_dict['PANTAI'][NAME] , 0, 0, 0)
location_dict['RUMAH POHON'][DIRECTION] = (0,0,0,0,0,location_dict['PONDOK'][NAME])


def title_screen():
    os.system('cls')
    print("""
 _    _      _                            _____        
| |  | |    | |                          |_   _|       
| |  | | ___| | ___ ___  _ __ ___   ___    | | ___     
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \    
\  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) |   
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/    
                                                       
 _____ _                     _    _            _     _ 
/  ___| |                   | |  | |          | |   | |
\ `--.| |_ ___  _ __   ___  | |  | | ___  _ __| | __| |
 `--. \ __/ _ \| '_ \ / _ \ | |/\| |/ _ \| '__| |/ _` |
/\__/ / || (_) | | | |  __/ \  /\  / (_) | |  | | (_| |
\____/ \__\___/|_| |_|\___|  \/  \/ \___/|_|  |_|\__,_| 

            ##############################
            # Welcome to The Stone World #
            ############################## 
            #           -play-           #
            #           -help-           #
            #           -quit-           #
            ############################## 
        """)

    start_game_option()
        



def start_game_option():
    option = input("\n>>>").lower()
    if option == "play":
        story()
    elif option == "help":
        help()
    elif option == "quit":
        sys.exit()
    
    while option not in ["play", "help", "quit"] :
        print("masukan perintah yang benar")
        option = input("\n>>>").lower()
        if option == "play":
            story()
        elif option == "help":
            help()
        elif option == "quit":
            sys.exit()



def help():
    os.system('cls')
    print("""
    *************************
    * KETIKAN 'jalan ke (utara,timur,selatan,barat) untuk berjalan'       *
    * KETIKAN 'masuk dan keluar' untuk masuk dalam area yang bisa dimasuki*
    *************************
    * KETIKAN 'lihat' lalu ketik :                                        *
    * 1. area         untuk melihat area sekitar                          *
    * 2.'nama item'   untuk melihat item pada lokasi dan inventory        *
    *************************
    * KETIKAN 'ambil'     untuk mengambil item                            *
    * KETIKAN 'buang'     untuk membuang item                             *
    * KETIKAN 'inventory' untuk membuka inventory                         *
    *************************
    * KETIKAN 'gunakan' untuk menggunakan item                            *
    * KETIKAN 'buat'    untuk membuat item                                *
    *************************
    *                pilih pilihan untuk lanjut                           *
    *                          -play-                                     *
    *                          -help-                                     *
    *                          -quit-                                     *
    *************************
    """)
    start_game_option()


def help_in_game():
    print("""
    *************************
    * KETIKAN 'jalan ke (utara,timur,selatan,barat) untuk berjalan'       *
    * KETIKAN 'masuk dan keluar' untuk masuk dalam area yang bisa dimasuki*
    *************************
    * KETIKAN 'lihat' lalu ketik :                                        *
    * 1. area         untuk melihat area sekitar                          *
    * 2.'nama item'   untuk melihat item pada lokasi dan inventory        *
    *************************
    * KETIKAN 'ambil'     untuk mengambil item                            *
    * KETIKAN 'buang'     untuk membuang item                             *
    * KETIKAN 'inventory' untuk membuka inventory                         *
    *************************
    * KETIKAN 'gunakan' untuk menggunakan item                            *
    * KETIKAN 'buat'    untuk membuat item                                *
    *************************
    *                pilih pilihan untuk lanjut                           *
    *                          -play-                                     *
    *                          -help-                                     *
    *                          -quit-                                     *
    *************************
    """)


def Input_command():

    while True:
        
        
        perintah = input("\n>>").lower()
       
        acceptable_perintah = ["quitgame", "jalan ke utara", "jalan ke timur", "jalan ke selatan", "jalan ke barat", "lihat", "ambil", "gunakan", "inventory", "buang", "masuk", "keluar","buat",'help']
        while perintah not in acceptable_perintah:
            print("perintah tidak ada")
            perintah = input("\n>>").lower()
        else : 
            if perintah == "quitgame":
                sys.exit()
            elif perintah == "help":
                help_in_game()
            elif perintah in ["jalan ke utara", "jalan ke timur", "jalan ke selatan", "jalan ke barat", "masuk", "keluar"]:
                move(perintah)
            elif perintah in ["lihat", "ambil", "gunakan", "inventory","buang", "buat", "gunakan"]:
                interact(perintah)

        handling_story(perintah)
    

def interact(Input_perintah):
    if Input_perintah == 'lihat':
        lihat()
    elif Input_perintah == 'ambil':
        ambil()
    elif Input_perintah == 'buang':
        buang()
    elif Input_perintah == 'inventory':
        inventory()
    elif Input_perintah == 'buat':
        buat()
    elif Input_perintah == 'gunakan':
        gunakan()
    else : 
        pass


def handling_story(perintah):
    global pondok1
    global pondok2
    global hutan2_1
    global hutan2_2
    global pantai
    global triger_statue
    if pemain.location == "PONDOK" and pondok1 == 0:
            story_1()
            pondok1 += 1
    if pemain.location == 'HUTAN2' and  hutan2_1 == 0:
        if perintah == 'lihat' and choice in ['patung batu', 'patung', 'patung rani']:
            story_2()
            hutan2_1 += 1
    if pemain.location == 'HUTAN2' and hutan2_1 > 0:
        if perintah == 'ambil' and itemToTake in ['patung batu', 'patung', 'patung rani'] :
            if 'Nital' in pemain.inventory:
                story_3()
                hutan2_2 += 1
                pemain.location = 'PONDOK'

    if triger_statue == 2:
        story_4()
        triger_statue += 2
    if triger_statue == 4:
        story_5()
        triger_statue += 2
    condition = False
    if 'Pasir' in pemain.inventory and 'Kerang' in pemain.inventory and 'Rumput Laut' in pemain.inventory and 'Ikan Laut' in pemain.inventory:
        condition = True

    if pemain.location == 'PANTAI' and condition == True and triger_statue > 4:
        story_6()
        triger_statue += 2
    

def move(Input_perintah):
    move_code = move_handling(Input_perintah)
    if move_code == 10 :
        print("tidak bisa jalan ke sana")
    else: 
        new_location = location_dict[pemain.location][DIRECTION][move_code]
        pemain.location = new_location
        print(f"\nKau berada di {pemain.location}")


def move_handling(moving_to):
    if moving_to == "jalan ke utara":
        choice = 0
    elif moving_to == "jalan ke timur":
        choice = 1
    elif moving_to == "jalan ke selatan":
        choice = 2
    elif moving_to == "jalan ke barat":
        choice = 3
    elif moving_to == "masuk":
        choice = 4
    elif moving_to == "keluar":
        choice = 5
    
    if location_dict[pemain.location][DIRECTION][choice] == 0 :
        return 10
    else:
        return choice


def displayLocation(loc):
    print(loc)
    print('=' * len(loc))

    print('\n'.join(textwrap.wrap(location_dict[loc][DESCRIPTION], SCREEN_WIDTH)))

    exits = ['UTARA', 'TIMUR', 'SELATAN', 'BARAT','MASUK', 'KELUAR']   

    if len(location_dict[loc][ITEM_GROUND]) > 0:
        print()
        for item in list(set(location_dict[loc][ITEM_GROUND])):
            print(Item_dict[item][GROUNDDESC])
    print()

    index = 0
    for i in location_dict[loc][DIRECTION]:
        if i in ['GUA','HUTAN1', 'SUNGAI','PONDOK','HUTAN2','PANTAI','LAUT','RUMAH POHON']:
            print(f"{exits[index]} : {location_dict[loc][DIRECTION][index]}")
        index += 1
        
    print()       


def inventory():
    if len(pemain.inventory) == 0:
        print('Inventory:\n  (kosong)')
        return

    itemCount = {}
    for item in pemain.inventory:
        if item in itemCount.keys():
            itemCount[item] += 1
        else:
            itemCount[item] = 1

    print('Inventory:')
    for item in set(pemain.inventory):
        if itemCount[item] > 1:
            print('  %s (%s)' % (item, itemCount[item]))
        else:
            print('  ' + item)


def getAllItemsMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) 
    matchingItems = []
    for item in itemList:
        if desc in Item_dict[item][DESCWORDS]:
            matchingItems.append(item)
    return matchingItems

def getAllDescWords(itemList):
    itemList = list(set(itemList)) 
    descWords = []
    for item in itemList:
        descWords.extend(Item_dict[item][DESCWORDS])
    return list(set(descWords))

def getFirstItemMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) 
    for item in itemList:
        if desc in Item_dict[item][DESCWORDS]:
            return item
    return None

def getAllFirstDescWords(itemList):
    itemList = list(set(itemList))
    descWords = []
    for item in itemList:
        descWords.append(Item_dict[item][DESCWORDS][0])
    return list(set(descWords))


def ambil():
    """"mengambil item."""
    global itemToTake
    print("apa yang ingin anda ambil?")
    itemToTake = input('nama item: ')
    if 'Nital' in pemain.inventory and  hutan2_1 > 0:
        Item_dict['Patung'][TAKEABLE] = True
        
        
    if itemToTake == '':
        print('KETIK "lihat" -> "area" untuk melihat item di lokasi.')
        return

    cantTake = False

    
    for item in getAllItemsMatchingDesc(itemToTake, location_dict[pemain.location][ITEM_GROUND]):
        if Item_dict[item].get(TAKEABLE, True) == False:
            cantTake = True 
            continue 
        print('kau mengambil %s.' % (Item_dict[item][SHORTDESC]))
        location_dict[pemain.location][ITEM_GROUND].remove(item)
        pemain.inventory.append(item) 
        return

    if cantTake:
        print('Kau tidak bisa mengambil "%s".' % (itemToTake))
    else:
        print('Item Tidak ada.')


def buang():
    print("apa yang ingin anda buang?")
    itemToDrop =input("nama item: ")

    invDescWords = getAllDescWords(pemain.inventory)

    
    if itemToDrop not in invDescWords:
        print('Kamu tidak punya "%s" di inventorymu.' % (itemToDrop))
        return

    
    item = getFirstItemMatchingDesc(itemToDrop, pemain.inventory)

    if item != None:
        print('%s dihapus dari inventorymu' % (Item_dict[item][SHORTDESC]))
        pemain.inventory.remove(item) 
        location_dict[pemain.location][ITEM_GROUND].append(item) 


def lihat():
    global choice
    choice = input("lihat apa? ")

    if choice == 'area':
        displayLocation(pemain.location)
        return
    else:
        item = getFirstItemMatchingDesc(choice, location_dict[pemain.location][ITEM_GROUND])
        if item != None:
            print(" ")
            print(''.join(textwrap.wrap(Item_dict[item][LONGDESC], SCREEN_WIDTH)))
            return
        item = getFirstItemMatchingDesc(choice, pemain.inventory)
        if item != None:
            print(''.join(textwrap.wrap(Item_dict[item][LONGDESC], SCREEN_WIDTH)))
            return
    print("keyword tidak ada")


def buat():
    craft = ['Nital']
    print("buat apa? : ") 
    item_craft = input(":>").lower()        
    if item_craft in getAllFirstDescWords(craft):
        match_item = getAllItemsMatchingDesc(item_craft,craft)

        for i in match_item:
            for item in Item_dict[i][INGREDIENTS]:
                print(f"  kamu butuh :  {Item_dict[item][SHORTDESC]}")
        
        canBeMade = True
        for item in Item_dict[i][INGREDIENTS]:
            if item not in pemain.inventory:
                print("     \nitem tidak bisa dibuat\n")
                canBeMade = False
                break
            
        if canBeMade == True:
            for item in Item_dict[i][INGREDIENTS]:
            
                pemain.inventory.remove(item)
            pemain.inventory.append(i)

            print("     \nitem berhasil dibuat\n")
    else:
        print("Tidak bisa membuat item tersebut")


def gunakan():
    global item_use
    item_use = input("masukan nama item: ").lower()
    useable_item = ['Tungku api', 'Tombak','Nital']
   
    if item_use not in getAllFirstDescWords(useable_item):
        print("item tidak bisa digunakan")
        
    else:
        item_inven = getAllItemsMatchingDesc(item_use, location_dict[pemain.location][ITEM_GROUND])
        if item_inven != []:
            for item in item_inven:
                if Item_dict[item][FUNC][0] == 'Masak':
                    masak()
                    return

        item_inven = getAllItemsMatchingDesc(item_use, pemain.inventory)
        if item_inven != []:
            for item in item_inven:
                if Item_dict[item][FUNC][0] == 'To_object':
                    apply_to_object(item)
                    return
        
        print("item tidak ada di inventory dan area")        


def masak():
    cookable_item = ['Buah anggur']
    
    cook_item = input('Masukan item yang mau dimasak : ')
    if cook_item in getAllFirstDescWords(cookable_item):
        match_item = getAllItemsMatchingDesc(cook_item,cookable_item)
            
        for item in match_item:
            if item in pemain.inventory:

                cook = Item_dict[item][COOK]    
                print(f"{cook} berhasil didapatkan")
                pemain.inventory.remove(item)
                pemain.inventory.append(cook)
            else:
                print("Belum punya item")
    else:
        print("item tidak dapat dimasak")


def apply_to_object(item_use):
    global objek
    global triger_statue
    object_item = ['Patung']
    objek = input(f"gunakan {Item_dict[item_use][SHORTDESC]} untuk : ")
    match_item = getAllItemsMatchingDesc(objek,location_dict[pemain.location][ITEM_GROUND])
    
    if hutan2_2 > 0:
        Item_dict['Patung'][CAN_USE] = True
    if match_item != []:

        for item in match_item:
            if item not in object_item:
                print("tidak bisa digunakan pada item tersebut")
            else:
                if Item_dict[item][USE] == item_use and Item_dict[item][CAN_USE]:    
                    print("berhasil digunakan")
                    triger_statue = 2
                else:
                    print("tidak bisa digunakan pada item tersebut")
    else: 
        print("tidak bisa digunakan pada item tersebut, mungkin masih diinventory letakkan dulu di tanah")


def story():
    print(" ")
    print('\n'.join(textwrap.wrap("Suatu ketika muncullah sebuah kabut misterius dibumi yang membuat seluruh umat manusia menjadi batu, menyebabkan keruntuhan peradaban manusia yang telah dibangun jutaan tahun, tapi dibalik itu seorang pemuda bernama sun yang tetap memegang teguh harapannya , sun tetap berhitung hingga triliunan detik untuk menjaga kesadarannya dia yakin suatu saat dirinya akan bangun dan bebas dari proses pembatuan ini.\n", SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap('name : "aghhh,  apa yang terjadi dimana aku?,  apa ini , serpihan batu  jadi waktu itu memang bukan mimpi"',SCREEN_WIDTH)))
    time.sleep(skip_time)
    print("\n--------------------- KAU BERADA DI GUA---------------------")
    print("")
    time.sleep(skip_time)
    Input_command()


def story_1():  
    time.sleep(0.5)
    print("""            
                         vv
                     vvv^^^^vvvvv
                 vvvvvvvvv^^vvvvvv^^vvvvv
        vvvvvvvvvvv^^^^^^^^^^^^^vvvvv^^^vvvvv
    vvvvvvv^^^^^^^^^vvv^^^^^^^vvvvvvvvvvv^^^vvv
  vvvv^^^^^^vvvvv^^^^^^^vv^^^^^^^vvvv^^^vvvvvv
 vv^^^^^^^^vvv^^^^^vv^^^^vvvvvvvvvvvv^^^^^^vv^
 vvv^^^^^vvvv^^^^^^vvvvv^^vvvvvvvvv^^^^^^vvvvv^
  vvvvvvvvvv^^^v^^^vvvvvv^^vvvvvvvvvv^^^vvvvvvvvv
   ^vv^^^vvvvvvv^^vvvvv^^^^^^^^vvvvvvvvv^^^^^^vvvvvv
     ^vvvvvvvvv^^^^vvvvvv^^^^^^vvvvvvvv^^^vvvvvvvvvv^v
        ^^^^^^vvvv^^vvvvv^vvvv^^^v^^^^^^vvvvvv^^^^vvvvv
 vvvv^^vvv^^^vvvvvvvvvv^vvvvv^vvvvvv^^^vvvvvvv^^vvvvv^
vvv^vvvvv^^vvvvvvv^^vvvvvvv^^vvvvv^v##vvv^vvvv^^vvvvv^v
 ^vvvvvv^^vvvvvvvv^vv^vvv^^^^^^_____##^^^vvvvvvvv^^^^
    ^^vvvvvvv^^vvvvvvvvvv^^^^/\@@@@@@\#vvvv^^^
         ^^vvvvvv^^^^^^vvvvv/__\@@@@@@\^vvvv^v
             ;^^vvvvvvvvvvv/____\@@@@@@\vvvvvvv
             ;      \_  ^\|[  -:] ||--| | _/^^
             ;        \   |[   :] ||_/| |/
             ;         \\ ||___:]______/
             ;          \   ;=; /
             ;           |  ;=;|
             ;          ()  ;=;|
            (()          || ;=;|
                        / / \;=;""")
    input
    print("Seseorang Keluar Dari rumah pohon")
    input()
    print("sun : dasar kau payah akhirnya bangun juga ")
    input( )
    print("name : kau masih hidup sun,")
    input()
    print('\n'.join(textwrap.wrap("sun : hei kau payah jangan coba memelukku dengan tubuh telanjang mu itu, cepat gunakan pakaian yang telah aku buat , aku akan membuatmu terus bekerja",SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap("name : serahkan saja padaku bagian kerja kasar ,kau cukup gunakan otakmu yang pintar itu, ngomong2 bagaimana kau bisa bebas.",SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap("sun : aku menduga cairan yang ada di gua itu lah yg menyebabkan kita bisa keluar dari pembatuan. Aku telah mencobanya pada beberapa patung tapi tidak berhasil, entah kenapa itu bekerja padamu mungkin sifat keras kepalamu itu yang menyebabkannya. Jika saja aku punya anggur aku bisa memasaknya jadi etanol lalu menggabungkannya dengan cairan dari gua maka menjadi nital dengan kata lain aku bisa mendapatkan cairan pembangkit",SCREEN_WIDTH)))
    if 'Buah anggur' in pemain.inventory:
        input()
        print("name : bukannya kita bisa buat dari anggur ini.")
        input()
        print("sun : dimana kau menemukannya???")
        input()
        print("name : didepan gua tempat kau pertama kali bangun")
        input()
        print('\n'.join(textwrap.wrap("sun : yosh, sekarang kita bisa membuat cairan pembangkit, pertama masaklah dulu anggurnya dengan tungku api",SCREEN_WIDTH)))

    else : 
        input()
        print('\n'.join(textwrap.wrap("name : Aku ingat sepertinya ada sebuah tanaman anggur didepan gua tempat aku pertama kali bangun. Sun tunggulah disini aku akan mengambilnya",SCREEN_WIDTH)))
        input()
        print('\n'.join(textwrap.wrap("sun : tunggu, setelah kau dapat buah anggurnya, masaklah anggurnya menggunakan tungku api yang ada disini",SCREEN_WIDTH)))

def story_2():
    print(" ")
    print("sun : name lihat apa yang kutemukan ")
    input("")
    print("name : tidak mungkin, rani?, akhirnya kita menemukannya")
    input("")
    if 'Nital' in pemain.inventory:
        print("name : sun kita bisa membebaskan nya dengan cairan pembangkit yg kita buat tadi.")
    else:
        print("name : sun kita harus segera membuat cairan pembangkit")
        input()
        print("sun : yah kita akan segera membuatnya, lalu kita kembali ke sini lagi ")
    input("")


def story_3():
    print("\nsun : patung ini sangat berat cepat bawalah patungnya")
    input()
    print("Terdengar suara dari semak-semak")
    input()
    print("sun : hei name diamlah, ada sesuatu disemak2")
    input()
    print("seekor singa muncul dari dalam semak-semak")
    input()
    print("""...oO
                 ...oO                ...o                             __
                            \|\||             |\          __      _.--"  "-.
                            -- |||/         -' | \    _.-"  ""-.-"
                           /7   |||/    __./7     \.-"
             __..--._  _.-/    |||||/.-"  /        `-_
                                         \
..--""--.--'"        ""   \-' |||||||/`   \-'_        `-._____________
___________________________-|||||||||______-__\                   /   \_____
               V     v       |/||||           /                  /     \
 V    \|/             _______/    /_  _______/    /_       _____|_____  |-,
                     /,__________/  `/,__________/__`-.___/,__(____________)
         \|/   v           |\               v
  \/        v         v        /            \|/       V         \|/        \/ 
            \/       v     \/        \/         v             V  
      V         \|/      ' v          v       \/      v
\|/       \/          v            \|/            \/          V       \|/
  __________________________________________________________________________""")
    input()
    print("name : apa!!! seekor singa")
    input()
    print("sun : sial, lariiiii")
    input()
    print('\n'.join(textwrap.wrap("saat mereka lari sun melihat patung sebuah pria yang pernah dilihatnya dulu dia adalah seorang petarung yang sangat kuat dia dikenal dengan sebutan 'GORILA DARI TAWANGSARI'",SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap("name :singa itu akan menangkap kita, sun larilah bawa patung rani aku akan menghadapinya",SCREEN_WIDTH)))
    input()
    print("sun : jangan gila kau otak udang")
    input()
    print('\n'.join(textwrap.wrap("name : selama dirimu masih ada peradaban manusia dapat dibangun kembali, kuserahkan rani padamu",SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap("sun : tidak !!!, aku adalah otak dan kau adalah otot. kita boleh kehilangan salah satunya, aku punya rencana ",SCREEN_WIDTH)))
    input()
    print("sun dan name berlari mengarah ke patung tersebut dan langsung menuangkan ramuan, pria itu pun bangkit ")
    pemain.inventory.remove('Nital')
    input()
    print("pria : seperti apa situasinya")
    input()
    print("sun : ada sekumpulan singa didepan kita")
    input()
    print("pria : oke")
    input()
    print('\n'.join(textwrap.wrap("pria itu langsung berdiri dan berlari lalu meninju salah satu singa, singa itupun mati hanya dengan satu pukulannya",SCREEN_WIDTH)))
    input()
    print("pria : sekarang kalian tidak akan ada dalam bahaya lagi selama ada aku, namaku july")
    input()
    print('\n'.join(textwrap.wrap("name : luar bisa july.  sun kita sekarang punya otot, otak, dan kekuatan bertarung.3 pillar utama membangun peradaban ",SCREEN_WIDTH)))
    input()
    print("sun : yah, ayo kita kembali ke rumah pohon")
    print("\nmereka pun kembali ke pondok")
    input()
    print('\n'.join(textwrap.wrap("sun : july, pakailah pakaian yang ada di rumah pohon, hari mulai petang sebaiknya kita istirahat",SCREEN_WIDTH)))
    input()
    print("name : bagaimana dengan patung rani?")
    input()
    print("sun : kita akan membebaskannya besok")
    input()
    print("Keesokan harinya")
    input()
    print("sun : mau kemana kau july?")
    input()
    print("july : aku akan pergi berburu. setidaknya hanya inilah yang bisa kulakukan ")
    input()
    print("sun : oke, berhati-hatilah")
    input()
    if 'Nital' in pemain.inventory:
        print("name : sun, kau sudah bangun ini waktunya membebaskan rani")
        input()
        print("sun : letakkan patungnya ditanah lalu tuangkan cairan pembangkitnya")
    else:
        print("name : sun, kau sudah bangun ini waktunya membebaskan rani")
        input()
        print('\n'.join(textwrap.wrap("sun : buatlah lagi cairan pembangkit, kita sudah menggunakannya pada july saat dikejar singa kemarin",SCREEN_WIDTH)))
        input()
        print("name : benar juga , baiklah aku akan membuatnya lagi tunggulah disini")
        input()
        print("sun : setelah kau membuatnya, letakkan patungnya ditanah lalu tuangkan cairan pembangkitnya")


def story_4():
    time.sleep(skip_time)
    location_dict[pemain.location][ITEM_GROUND].remove('Patung')
    print("\nmereka menuangkan cairan pembangkit pada patung rani")
    input()
    print("name: kok tidak terjadi apa-apa?!")
    input()
    print('\n'.join(textwrap.wrap("sun : reaksinya butuh waktu, ini namanya cyrostatis ini seperti lapisan pelindung dari bekas logam ditubuh. Intinya jika satu bagian saja terkenan nital dan hancur itu menyebabkan efek berantai yang menjalar ke seluruh tubuh dan pembatuan pun terhenti",SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap("name: woahh, itu mulai berekasi. (bangunlah rani , berkat kau aku bisa bertahan hidup selama ini, aku mencintaimu selama ratusan tahun....ribuan tahun )",SCREEN_WIDTH)))
    input()
    print("Rani pun terbebas dari pembantuan , name memeluknya dengan berkucuran air mata")
    input()
    print("name : rani, kau bisa mendengarku? rani!!")
    input()
    print("rani : name??, apa yang terjadi? kepalaku pusing")
    input()
    print("name : kau tidak apa2")
    input()
    print("rani : yah aku tahu name, kau pasti akan menyelamatkanku, terima kasih.")
    input()
    print('\n'.join(textwrap.wrap("name : bukan aku , ini semua berkat sun dia menghabiskan satu tahun penuh demi cairan pembangkit ini",SCREEN_WIDTH)))
    input()
    print("name : dimana july")
    input()
    print("rani : july???")
    input()
    print("name : dia orang yang kami bebaskan dengan cairan pembangkit")
    input()
    print("sun : si monster itu sedang berburu, sebentar lagi dia pasti pulang")
    input()
    print("sun : kemarilah sebentar name ")
    input()
    print("name : ada apa sun?")
    input()
    print('\n'.join(textwrap.wrap("sun : Ingat kata ini baik-baik. rahasiakanlah resep cairan pembangkit dari july dan rani apapun yang terjadi",SCREEN_WIDTH)))
    input()
    print("name : Aku tidak perlu bertanya apa alasannya, aku percaya padamu sun.")
    
  
def story_5():
    input()
    print('\n'.join(textwrap.wrap("\n\njuly kembali dari berburu dengan membawa banyak hasil buruan, mereka pun memasaknya dan menikmatinya bersama",SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap("sun : kau memang ahli berburu july .ngomong-ngomong utara pondok ini adalah laut, kita akan pergi kesana",SCREEN_WIDTH)))
    input()
    print("name :  kita pasti akan mencari ikan laut kan, sudah lama aku gak makan seafood.")
    input()
    print('\n'.join(textwrap.wrap("sun : pikiranmu hanya makanan otak udang. aku tanya apa yang paling kita butuhkan untuk membangun peradaban maju?",SCREEN_WIDTH)))
    input()
    print("name : hmm....... , ponsel .")
    input()
    print("sun : kita bisa main ml lagi ya....., matamu ponsel !!!!")
    input()
    print("july : besi")
    input()
    print('\n'.join(textwrap.wrap("sun : itu bisa juga tapi itu masih nanti, yg paling kita butuhkan adalah kalsium karbonat atau kapur kulit kerang dapat mencukur berewokmu kan otak udang , jika kau menumbuknya hingga halus,  kau akan mendapatkan kapur.",SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap("sun : ada 4 cara menggunakannya pertama agikultur kita bisa menyingkirkan semua ion hidrogen dengan kata lain kita bisa membuat tanah subur, kedua konstruksi kau bisa membuat semen jika membakarnya bersama pasir ketiga  yang paling penting yaitu sabun kumpulkan sodium karbonat dari rumput laut campurkan dengan minyak dan jadilah sabun",SCREEN_WIDTH)))
    input()
    print("july : lalu yang keempat")
    input()
    print("sun : apa aku tadi bilang empat, sepertinya aku salah bicara hanya ada tiga cara.")
    input()
    print("name : yosh ayo kita segera pergi kelaut dan mengumpulkan semua bahanya\n")
    input()
    print("sun : ingat selain kerang , kumpulkan juga ikan laut, pasir, dan rumput laut")
    

def story_6():
    print("\nsun : name kembalilah dulu")    
    input()
    print("sun berjalan kearah july")    
    input()
    print('\n'.join(textwrap.wrap("july : kerang ini bukan milik siapapun , begitu juga daratan dan lautan , tidak ada lagi orang dewasa yang serakah dan tamak , dunia sekarang sudah bebas",SCREEN_WIDTH)))
    input()
    print("july memenggal kepala salah satu patung manusia dewasa didekatnya dihadapan sun")    
    input()
    print("sun : kau tahu yang kau lakukan kan, july? kau baru saja membunuh seseorang lo ")    
    input() 
    print('\n'.join(textwrap.wrap("july : aku tahu kok, begitu peradaban kembali orang2 seperti ini pada awalnya akan berterima kasih kepada kita. lalu apa?, mereka hanya akan berkata 'ini adalah wilayahku dulu', 'bayar sewamu', 'bayar pajakmu' tidak peduli dengan semua masalahmu semua penderitaanmu mereka hanya memikirkan dirinya sendiri, aku tidak akan mengembalikan dunia yang busuk seperti itu, kita hanya akan mengembalikan pemuda berhati murni.Inilah kesempatan untuk memurnikan manusia kau setuju denganku kan sun ?",SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap("sun : sama sekali tidak, aku hanyalah bocah yang kegirangan akan ilmu pengetahuan, aku akan menggunakan kekuatan ilmu pengetahuan untuk menyelamatkan semua orang tanpa terkecuali.",SCREEN_WIDTH)))
    input()
    print('\n'.join(textwrap.wrap("sun : (dia ini benar2 bahaya, tapi jika saat itu aku tidak membangkitkannya, kami pasti mati dimakan singa, sepertinya dia masih bisa kuatasi hingga dia tau resep cairan pembangkit.  meski aku harus mati aku harus merahasiakannya)\n",SCREEN_WIDTH)))
    time.sleep(5)
    sys.exit("""
     ______     ______     __    __     ______   ______     __          __     __  __     __    __     ______   ______    
    /\  ___\   /\  __ \   /\ "-./  \   /\  == \ /\  __ \   /\ \        /\ \   /\ \/\ \   /\ "-./  \   /\  == \ /\  __ \   
    \ \___  \  \ \  __ \  \ \ \-./\ \  \ \  _-/ \ \  __ \  \ \ \      _\_\ \  \ \ \_\ \  \ \ \-./\ \  \ \  _-/ \ \  __ \  
     \/\_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_\    \ \_\ \_\  \ \_\    /\_____\  \ \_____\  \ \_\ \ \_\  \ \_\    \ \_\ \_\ 
      \/_____/   \/_/\/_/   \/_/  \/_/   \/_/     \/_/\/_/   \/_/    \/_____/   \/_____/   \/_/  \/_/   \/_/     \/_/\/_/ 


                             _____     __        ______   ______     ______     ______      __     __    
                            /\  __-.  /\ \      /\  == \ /\  __ \   /\  == \   /\__  _\    /\ \   /\ \   
                            \ \ \/\ \ \ \ \     \ \  _-/ \ \  __ \  \ \  __<   \/_/\ \/    \ \ \  \ \ \  
                             \ \____-  \ \_\     \ \_\    \ \_\ \_\  \ \_\ \_\    \ \_\     \ \_\  \ \_\ 
                              \/____/   \/_/      \/_/     \/_/\/_/   \/_/ /_/     \/_/      \/_/   \/_/
    """)

   
if __name__ == "__main__":
    title_screen()
    