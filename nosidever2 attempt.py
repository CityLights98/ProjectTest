space="\n"*6
space1="\n"*2
from time import sleep
#--------begining game states-----------------
game_state= {
    #locations status --maybe can be integrated into map checks?
    "frontDoorOpen": False,
    "bedroomDoorOpen": False,
    "bathroomDoorOpen": False,
    "kitchenDoorOpen": False,
    "lairDoorOpen": False,

    #poi status
    "validTree": True,
    "validNest": True,
    "validWell": True,
    "validDog": True,
    "validHay": True,
    "validCow": True,
    "validBalloons": True,
    "validFireplace": True,
    "validStatue": True,
    "validUnderBed": True,
    "validShelf": True,
    "validClothes": True,
    "validFrontDoor": True,
    "validSneeze": False,
    "validSneeze1": False,
    "validSink": True,
    "validBathtub": True,
    "validBox": True,
    "validClock": True,
    "validDryer": True,
    "validWallBox": True,
    "validWindow": True,
    "validWheat": True,
    "validSugar": True,
    "validCookbook": True,
    "validCabinet": True,
    "validOven":True,

    #puzzle status
    "sneezeOn": True,
    "fireOn": True,
    "balloonsOn": True,
    "photoViewed": False,
    "clockClosed": True,
    "audioHint": False,
    "potViewed": False,
    "phoneOn": False,
    "noside1": False
}
#--------item descriptions--------------------
item_descriptions= {
    "item_branch": f'''
    An old branch
    ''',
    "decor_emptytree": f'''
    You've already grabbed one branch. You don't need more
    ''',
    "puzzle_well":f''' 
    A water well. Currently, the basket is down, but the crank handle is missing.
    ''',
    "decor_fixedwell": f'''
    You've already gotten the water. No need for more.
    ''',
    "decor_nest": f'''
    A nest full of shiny objects and two different eggs. The first egg is a normal egg. It seems to be freshly laid. The other egg is a Pica Pica egg (aka the theiving magpie). This egg is larger, and you see a slight crack in the egg. Could it be hatching soon?
    ''',
    "decor_emptynest": f'''
    There's only shiny bobbles and trash left. You've already taken the eggs.
    ''',
    "item_egg1": f'''
    A farm fresh egg laid this day.
    ''',
    "item_egg2": f'''
    It's Pica Pica egg. You see a slight crack in the shell. Could it be hatching soon?
    ''',
    "puzzle_dog": f'''
    A bulldog. Despite what he looks like, this dog seems to be in a playful mood. As if he knew you.
    ''',
    "decor_dog": f'''
    He seems tired now. Best to let sleeping dogs lie.
    ''',
    "puzzle_cow": f'''
    A strange-looking cow stands before you, proudly sporting a brain in a jar on its head—complete with its horns poking right through the glass. \nIt smells especially bad, even by cow standards, which is saying something.
    ''',
    "decor_cow": f'''
    You've already milked her. What more do you want from her?
    ''',
    "puzzle_hay": f'''
    It's your typical haystack.
    ''',
    "decor_hay": f'''
    It's less of a stack now that you've rummaged through it. More of a pile, really. No one finds things in 'haypiles'.
    ''',
    "item_needle": f'''
    You found this needle in a haystack. Imagine that.
    ''',
    "lock_frontdoor": f'''
    The door to Noside’s house is locked, naturally —and just to make things more fun, the keyhole appears to be stuffed with something unhelpful.
    Getting inside was never going to be that easy, was it?
    There’s a keypad on the doorframe, and it looks like you’ll need a 4-digit code to get in. Because of course you do.
    ''',
    "item_crank": f'''
    The dog brought you this crank instead of the stick you threw. At least this might be useful.
    ''',
    "item_key": f'''
    There is a key attached to a message-- or is there a message attached to the key?
    ''',
    "item_keyMessage" : f'''

    I replaced your door lock with a keypad.
    The entry code is... But?
    But what's all that smoke?


    ----+#+----++---------------------------------+++---------------------+++###+++----++#++--------------------------------
    +--------------------------+++---------------------+##+++-------------###+++#########++---------------++----------------
    #+-------------------------+###+---------------------++####++----------+##+-----+--------------------+#++---------------
    -----------------------------+###+------------------------+##+----------+###--------++-------------++##+----+++#++------
    ------------+-------------------+##+--------------------------------------+##+---+###++------------+##+-+++####++++++---
    -----------+#+---------------------------------------------------------+---++##+###+--------------+##++####++++######+--
    -----------+##+----------------------+##+-----------------+##+-------+###########++--------------+#####++---++##+--+##++
    ------------+#+------------------------+-------------------+###+---------+++#+######+-----------+##+##++---+##++----##+-
    ------------+#+--------------------------------------+++########++-------------++++++----------+##+++##+---+#++----+##-+
    ------------+#+----+#+-------------------------------++++++++##+##+------------------------------+--++#+--+##+----+##++#
    ------------++----+##+--------------------------------------+##++###+------------++------------------+##+-+##+---+##++##
    -----------------+##+-----##+-------------------+#####++----+##+--+##+----------+#++----------------------++#+++###++###
    ------------+#+---+###+++##+-------------------+#+-+++###+---+#+----++--------+##++------------------------++####+++##++
    ------------++------++#####+-------------------+#+-----+###++##+-------------+##+----+++###+-----------------------##++-
    ---------------+######++-+####+-------------++-+##+------+##++##+-----------+##+++#######+++++---------------------+++++
    -------------+##+----++##+---++------------+###--##+------+##+##+----------+#######++--+####+##+---------------------+++
    -------------+#+--------+##+-----------------+###-+##+----+##+------------#####++-----+##++--+##+---------------+-------
    -----------++++##+--------+#+-----------------+###+++#######+------------+##++##+----+##+----+#++-+##+------------------
    -----------+##++###++-----+#+---------------+##+++##+---++--------------------+##+--+##+-----##+-+##+###+---------------
    ------------+##+--++########+---------------+++---+###+-----------------------+##+-+##+-----+##+###+-+++#+--------------
    -------------+#+-----+++++-------------------------+##+------------------------++--+##+---+##++###+---------------------
    --------------+#+-------------+#+----------------+##++------------------------------+##++###++#####++-------------------
    -------+###+---+#+--++###+-----+----------------++++---------------------------------++++++-+##+++##++------+-----------
    ---------++###++######++---------++--------------------------------------------------------+##+--------------------++++-
    ------------++#####+-------------+##+---------------------------------------------+#++------++-------------------+###+++
    ----------------+####+------------+##+----------------------------+-----+++++-----+##++------------------------+###++---
    --------------------++-------------+##+--------------------------##+---######+-----+##+-++++----+-------------+##+++----
    -----------++-----------------------++#+------------------------+##+--+##--+##+-+++#########+---------------++#++--++++-
    ----------+#+--------------------------+----------------+#+-----+##---+#++--+######+##+-+##++------+------++-++-------+-
    --------+##+------------------------------+#+-----------+##+----##+---+##+---##+----+##+##+++------------+##++----------
    -------+##+----++####+--------------------+++------------##+---+##+----##+---+##----+####++--------------+++-----+++---+
    ------+##+++#####+++++#++--------------------------------+##+-+###+----+##+--+#+-----+###+-------------------------+-++-
    -----+#####++++--++##+++##+---------------+#+------------+##+-+##+-++++++##++##+-----+##+----------------------------+++
    ----##++##------+##+----+#+---------------+#+-------------+#+++########+-+####++------------------------------+##++-++++
    #--+#+--##+----+##+-----##+-+###+---------+#+-------------+##+###++++------++++-----------------------------+###+++-----
    #+------+##+--+##+-----+##-+##++##+-------+##--------------+#++-------------------------------------------++##++--++++--
    #+-------+#+--+#+-----+##-+##+---+++------+##----------------------------------------+++-------------------+###++-++#+++
    #+------------+#+----###-###---------------##+---------------------------------------+#+---------+-+++-++++++++#####++++
    ##------------+#######+-######+------------------------------------------------------+##+------------+########++####++++
    #+---------------+++--+##+--++#+---------------------------------------++------------+##+---------++++#+++--++##++###+++
    ----------------------##+--------------------+##+-----------------++#####-------------+#++-----+--+#++##++----++##+++#++
    ++------------------------------------------+##+------------------+##++---------------+#++--------+##++##++-++--+##+++++
    #+----------------------------------------+##+---------++-+#####+--##+-----------------+++---------##+++###++---+##+++++
    ----------------------------------------+##++---------+##+##++++##++##+-++++------------+++---+----##++-++####++###+++-+

    ''',
    "item_bucketWater": f'''
    A simple bucket of water
    ''',
    "item_bucketMilk": f'''
    A bucket full of creamy milk. Yummy!
    ''',
    "item_bucketEmpty": f'''
    The bucket is empty now.
    ''',
    "item_bucketButter": f'''
    James spun in the bucket so much that the milk became butter
    ''',
    "item_photo": f''' 
    A child’s drawing—so why on earth would Noside try to burn this?
    The picture shows the Noside family, each member clearly labeled like a very organized kindergarten project.
    From left to right:
    ‘Mom’ in yellow,
    ‘Dad’ in red,
    ‘Me’ in purple (little Anatole Noside looked downright adorable back then),
    ‘Connie’ in pink—maybe his twin sister?
    And ‘Janet,’ a brown dog who definitely isn’t the bulldog you saw earlier.
    ''',
    "puzzle_sneeze": f'''
    The Sneezotator™ was hiding right in the hearth all along! This sneaky machine blows peppery smoke up the chimney."
    ''',
    "decor_sneeze": f'''
    You've already plugged up The Sneezotator™, so it can't cause any further irration"
    ''',
    "puzzle_balloons": f'''
    A wall of balloons! What a blast!
    ''',
    "puzzle_fireplace": f'''
    This nice fire invites you to relax and toy with the bear skin...
    ''',
    "decor_fireplace": f'''
    You fish the photo out of the ashes—it's a bit soggy and singed around the edges, but the image is still clear enough.
    PHOTO added to inventory.
    Then, wait—what’s this? A hidden compartment tucked away back here... There it is!
    A wall slides upward, revealing The Sneezotator™. Looks like you’ve just uncovered the very source of that mysterious (and peppery) smoke!
    ''',
    "puzzle_clothes": '''
    You look through the clothes, and notice the shirts are all numbered:
    pink 3
    green 8
    yellow 9
    blue 4
    purple 5
    black 7
    red 1
    ''',
    "item_catapult1":f'''
    Wow! A plastic catapult! This weapon of mass destruction for kids is the cream of the crop. It's currently unloaded
    ''',
    "item_catapult2":f'''
    The catapult is filled with honey. You're ready to fight!
    ''',
    "item_windingKey": f'''
    Tuco got this off the shelf for you. You wonder what it's for.
    ''',
    "puzzle_bathroomDoor": '''
    The bathroom door is chained and locked tight, and you’ll need a four-digit code to get it open.
    The picture on the door shows a laundry basket—odd choice. Could that be a clue, or just someone’s idea of bathroom décor?
    ''',
    "decor_bathroomDoor": f'''
    You've opened the door already. It'll take more than a chain to keep you locked out.
    ''',
    "decor_sink": f'''
    The sink has a murky gray liquid, but nothing else of interest.
    ''',
    "item_dentures1":f'''
    You spot a spring mechanism on the back of the dentures —and it looks like something’s missing.
    ''',
    "item_dentures2":f'''
    You now have motorized dentures. These would probably grind up anything that gets too close.
    ''',
    "puzzle_dryer":'''
    This has got to be Noside’s skull dryer. It actually looks like it’s still in working order.
    Just like Noside’s head, the dryer has a distinctly egg-shaped design—charming, in a weirdly practical sort of way.
    ''',
    "decor_dryer":f'''
    You've already used the heat to hatch Tuco. Besides, your normal-shaped head wouldn't fit in this thing.
    ''',
    "puzzle_clock": f'''
    The grandfather clock is missing its hands, which are conveniently lying on the floor just a few steps away.
    ''',
    "decor_clock": f'''
    The clock swung forward to reveal Noside's secret lair.
    ''',
    "item_snorkel": f'''
    A tiny snorkeling gear set —because you never know when a tiny underwater adventure might pop up!
    ''',
    "item_stopper":f'''
    The drain plug from the tub. It still has a lock of hair wrapped around it.
    ''',
    "decor_bathtub": f'''
    Against your better judgment, you reach into the murky bathtub water and pull out a drain stopper —complete with a lock of Noside’s unmistakably green hair wrapped around it. Lovely.
    ''',
    "decor_emptyTub": f'''
    The water has been drained, revealing the stains and hair left behind. Has this thing ever been cleaned?
    ''',
    "item_tuco":f'''
    Tweet, Tweet, Tuco! \nEven though he is freshly hatched, you get the sense he can fly just fine.
    ''',
    "item_wheat": f'''
    A golden shaft of wheat.
    ''',
    "item_flour": f'''
    Freshly "milled" flour.
    ''',
    "item_sugar": f'''
    A bag of sugar (helps the medicine go down)
    ''',
    "decor_window":f'''
    The open window has a view of the forest. It's truly magnificient.
    A gentle breeze fills the room
    ''',
    "item_honey":f'''
    "Sugar, Honey, Honey"
    (Famous Tune)
    ''',
    "item_cookbook":f'''
    A recipe book for the Cak-o-Matic™! It's open to a simple cake recipe. 
    Just add eggs, sugar, flour, and butter to the Cak-o-Matic™, and presto!
    ''',
    "puzzle_oven":f'''
    Wow! A Cak-o-Matic™! I always wanted to have one!
    ''',
    "item_cake":f'''
    It's the cake you made in the Cak-o-Matic™. It's still piping hot.
    ''',
    "puzzle_catureNote":f'''
    ----------------------------------------------------------------------------------------------------
    ----------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------###----------------------
    .....---..--.--.....---.-------------------------------+------------------+####+------------+-------
    --....---...---+++--------+#####--------##+----+#++---##+-----#####-------###+##----------####------
    -----------.--#####-..---####+##+-----+#####+--####+--+#+----####+###-----##+-##+--------####+------
    -----.--------#####-----###----###----##--+#####++###-##----+##----+##----##+--+#+-----+#####-------
    -----.------.---+-------##---.-+##----##---+###+---##+##-----###++--##----##----##+---+##-##+-------
    ----.------------------+##------##+--##----+####---+###+------++#######+-+##-----##+-+#+--##+-------
    ---.-------------------+##------##+--##-----###+----###+-----------+##+--+#+-----+####+--+##+-------
    ---------------+###-----##------##+--##-----###+-----##+-----------###---+#-------###----+##+-------
    ---------------####+----+##----+##---##------+##-----##+---+#+----+##----##+-------------+##+-------
    ---------------####+-----+###-###----##--------------##+----##+--###+----##--------------###+-------
    ---------------------------+###+----###--------------##+-----#####++-----##--------------###--------
    ----------------------------------------------------------------+-------+##--------------##+--------
    -------------------------------.---------------------------------------------------------##---------
    ---------------------------------------------------.--------------------------------------+---------
    -----------------------------------------------.----------------------------------------------------
    -----------------------------------------.----.-----------------------------------------------------
    ---------####++------------###----------------------------------------------------------------------
    --------#########----------###-----+##-.----------+####+---------##########+------------------------
    --------###++####+---------###------##----------+###+###+--------###+++++##+------------------------
    --------+###--+###+--------##+------##+--------+##-----##+---------------##-------------------------
    ---------####--+###--------+##------###--------##-------##---------------##+------------------------
    ---------##########--------+###########+------+##-------##---------+########------------------------
    ---------+##-+####----------##----------------+##-------##--------###+--+##+------------------------
    ---------+##-------.-...----##----------------+##+-----+##-------##+--------------------------------
    --------.-##---------------+##-----------------####----##+-------+##--------------------------------
    ----------##---------------+##-------------------#######+---------###-----+##-----------------------
    ----------##+---.-----------+#---.---.-------------++++-------------########------------------------
    ----------+#+---.-----------------------------------------------------------------------------------
    -------...---.----.-----.----------------.----------------------------------------------------------
    -----------..-----..-..----------------------------------------------.------------------------------
    ''',
    "item_james":f'''
    James the rat is still being a bit timid.
    You remember he cooperated well enough last time. 
    Maybe he could be useful again?
    ''',
    "item_james1":f'''
    He's all dressed up and ready to swim!
    ''',
    "item_bear":f'''
This bear, attracted by the scent of fresh cake, barged into Noside's lair.
You get the feeling that, in the right sticky situation, this bear could be very... persuasive.
For now, the bear seems content with the cake.
''',
    "audio_hint":f'''
        "The GroggySocks™ are proud to give you the time!
        With GroggySocks™, you'll get groggy, and soggy!
        It is now 3PM!"
    '''
}
#-----------location descriptions-----------------
enter_outside='''
As you approch the address Detective Veal gave you, you quickly regret answering your phone this morning.
Billows of noxious black smoke pour from a comically oversized chimney jutting out of what can only be described as a cartoonishly evil-looking house.
As you get closer, you pass a dried-up tree, valiantly clinging to a few remaining branches—one of which still holds a bird’s nest, as if no one told the bird to move out.
Just off the winding path to the house sits an old water well, looking like it hasn't seen water —or hope— in quite some time.
You also come across a bulldog and a very peculiar-looking cow, both eyeing you with vague interest. 
Nearby, there’s a haystack, which you assume is the cow’s lunch—or possibly a bed. Hard to say.
'''
location_outside = '''
Billows of noxious black smoke pour from a comically oversized chimney jutting out of what can only be described as a cartoonishly evil-looking house.
As you get closer, you pass a dried-up tree, valiantly clinging to a few remaining branches—one of which still holds a bird’s nest, as if no one told the bird to move out.
Just off the winding path to the house sits an old water well, looking like it hasn't seen water —or hope— in quite some time.
You also come across a bulldog and a very peculiar-looking cow, both eyeing you with vague interest. 
Nearby, there’s a haystack, which you assume is the cow’s lunch—or possibly a bed. Hard to say.
'''
enter_livingRoom='''
You step into the living room and are immediately greeted by a roaring fire in the fireplace —complete with what looks like a recently discarded picture crackling away in the flames.
In the right corner stands a statue of Noside, watching over the room like a very dramatic guardian. 
On the left wall, a bunch of balloons are clustered together, and it definitely seems like something is hiding behind them.
In the center of the room lies a bear skin rug —or possibly just a bear who gave up.
A trail of white footprints winds its way from the balloon pile, loops suspiciously around the maybe-dead bear, and heads toward the statue.
You also spot a white handprint on the door you just walked through, which is... comforting.
'''
enter_bedroom= '''
This bedroom is a disaster zone with strong “science experiment gone rogue” vibes.
Near the center, there’s a suspicious puddle —possibly acid— judging by the nicely scorched hole it’s burned straight through the floorboards.
The dresser drawers are half-open, as if they gave up trying, and clothes are scattered everywhere in a dramatic fashion.
Something shiny catches your eye from a high shelf, while something else —less shiny but equally mysterious— is poking out from under the bed.
To the right, there’s a door marked with a sign featuring a laundry basket. For reasons known only to the universe, it’s been thoroughly chained and locked.
'''
enter_bathroom='''
You step into the bathroom and quickly realize it’s not your average setup.
To your left is a sink and, rather unexpectedly, a strange tentacle emerging from the toilet like it belongs there.
Straight ahead, a grandfather clock stands next to a perfectly normal standing shower, as if timekeeping in the bathroom is standard practice.
To your right, there's a hair-dryer chair, a bathtub filled with water, and a red box mounted on the wall —complete with a glass-breaking hammer, just in case things take a turn.
'''
enter_kitchen='''
You open your cage and step into the kitchen, which looks like it’s recently survived a baking-related tornado.
Floury footprints trail across the floor, marking Noside’s not-so-subtle escape route.
The window —possibly the only thing in here that isn’t sticky— is open, letting in a gentle breeze.
A nearby cabinet holds a jar of honey. Oddly enough, it is the only thing in the cabinet.
On the table, an open book lounges beside an open bag of sugar, as if they were caught mid-recipe and then promptly abandoned.
Near the counter, batter has been splattered across the floor in a bold artistic statement, and on the counter sits a strange baking device —The Cak-o-Matic™— next to a vase proudly displaying raw wheat stalks 
—because nothing says “culinary chaos” like unprocessed agriculture as décor.
You are now alone (and as free as a bird).
'''
enter_lair= '''
The grandfather clock creaks open, revealing a hidden passage. Classic!
Inside, you spot a phone. Finally, a chance to call for help!
But your hope is short-lived, because there’s Noside at the far end of the room, proudly manning his prized invention: the Sausage o'Gun™. 
As for the phone... it’s completely dead. Probably because Noside has his Sausage o'Gun™ plugged straight into the generator, hogging all the power. Priorities.
'''
capture_text='''
You jam the drain stopper into the exhaust pipe.
The Sneezotator™ gets backed up, and the room quickly fills with thick, eye-watering smoke.
Through the haze, you suddenly find yourself face to face with Noside! He's completely covered in flour and not looking particularly thrilled.
Before you can react, he grabs you, shoves you into a cage, and strolls off.
'''   
def location_livingRoom(): 
    lrDes= [] 
    if game_state.get("fireOn"):
        lrDes.append("You look around to see a roaring fire in the fireplace —complete with what looks like a recently discarded picture crackling away in the flames.") 
    if not game_state.get("fireOn") and game_state.get("sneezeOn"):
        lrDes.append(f'''You look around to see the soggy remains of a fire —You already rescued the photo from the ashes. 
A compartment in the back of the hearth was hiding The Sneezotator(TM). It's still pouring out pepper-smoke.''')          
    if not game_state.get("sneezeOn") and not game_state.get("fireOn"):
        lrDes.append('''You look around to see the soggy remains of a fire —You already rescued the photo from the ashes. 
A compartment in the back of the hearth was hiding The Sneezotator(TM), but you've plugged that up already.''')  
    if game_state.get("validStatue"):    
        lrDes.append("In the right corner stands a statue of Noside, watching over the room like a very dramatic guardian.")          
    if game_state.get("balloonsOn"):
        lrDes.append("On the left wall, a bunch of balloons are clustered together, and it definitely seems like something is hiding behind them.")
    if not game_state.get("balloonsOn"):
        lrDes.append("Now that you've relieved the balloons of guard duty, you can enter the bedroom.")
    lrDes.append('''In the center of the room lies a bear skin rug —or possibly just a bear who gave up.
A trail of white footprints winds its way across the room, loops around the maybe-dead bear, and heads toward the right corner of the room.
You also spot a white handprint on the door leading outside, which is... comforting.''')
    return "\n".join(lrDes)
def location_kitchen():
    kDes = ["You look around the kitchen. \nFloury footprints trail across the floor, marking Noside’s not-so-subtle escape route."]
    if game_state.get("validWindow"):
        kDes.append("The window is open, letting in a gentle breeze.")
    if not game_state.get("validWindow"):
        kDes.append("There are remnants of cake splattered about the windowsill. There goes the one non-sticky surface.")    
    if game_state.get("validCabinet"):
        kDes.append("A nearby cabinet holds a jar of honey.")        
    if game_state.get("validSugar"):
        kDes.append("On the table, an open book lounges beside an open bag of sugar")
    if not game_state.get("validSugar"):
        kDes.append("A cookbook has been left open on the table") 
    if game_state.get("validWheat"):
        kDes.append("On the counter sits a The Cak-o-Matic™ next to a vase proudly displaying raw wheat stalks.")        
    if not game_state.get("validWheat"):
        kDes.append("On the counter sits a The Cak-o-Matic™ next to a newly emptied vase.")    
    return "\n".join(kDes)
def location_bedroom():
    bedDes= ['''
This bedroom is a disaster zone with strong “science experiment gone rogue” vibes.
Near the center, there’s a suspicious puddle —possibly acid— judging by the nicely scorched hole it’s burned straight through the floorboards.
The dresser drawers are half-open, as if they gave up trying, and clothes are scattered everywhere in a dramatic fashion.''']
    if game_state.get("validShelf"):
        bedDes.append("Something shiny catches your high from a high shelf.")
    if game_state.get("validUnderBed"):
        bedDes.append("Something mysterious is poking out from under the bed.")
    if not game_state.get("bathroomDoorOpen"):
        bedDes.append("To the right, there’s a door marked with a sign featuring a laundry basket. For reasons known only to the universe, it’s been thoroughly chained and locked.")
    if game_state.get("bathroomDoorOpen"):
        bedDes.append("To the right, there’s a door marked with a sign featuring a laundry basket. The chain lies on the floor and the door now leads to the bathroom.")
    return "\n".join(bedDes)
def location_bathroom():
    bathDes= ["To your left is a sink and, rather unexpectedly, a strange tentacle emerging from the toilet like it belongs there."]
    if game_state.get("validClock"):
        bathDes.append("Straight ahead, a grandfather clock stands next to a perfectly normal standing shower, as if timekeeping in the bathroom is standard practice.")
    if game_state.get("validBathtub"):
        bathDes.append("To your right, there's a hair-dryer chair and a bathtub filled with water.")
    if not game_state.get("validBathtub"):
        bathDes.append("To your right, there's a hair-dryer chair, a drained bathtub.")
    if game_state.get("validWallBox"):
        bathDes.append("You also see a red box mounted on the wall —complete with a glass-breaking hammer")
    if not game_state.get("validWallBox"):
        bathDes.append("You see a red box mounted on the wall —You've already broken the glass.")
    if not game_state.get("validClock"):
        bathDes.append("Straight ahead, a grandfather clock has hinged forward to reveal a hidden passage to Noside's secret lair.")
    return "\n".join(bathDes)
def location_lair():
    lairDes= []
    if not game_state.get("noside1") and not game_state.get("phoneOn"):
        lairDes.append('''
When you look around, you spot a phone. Finally, a chance to call for help!
But your hope is short-lived, because there’s Noside at the far end of the room, proudly manning his prized invention: the Sausage o'Gun™. 
As for the phone... it’s completely dead. Probably because Noside' Sausage o'Gun™ is hogging all the power.''')
    if game_state.get("noside1") and not game_state.get("phoneOn"):
        lairDes.append('''You have finally found a way to call for help, but you haven't dealt with Noside yet.
He's currently covered in honey, and his Sausage o'Gun™ is jammed, but he's still blocking you from the power box.''')
    if game_state.get("noside1") and game_state.get("phoneOn"):
        lairDes.append('''The phone rest on a nearby table, with the lights blinking to indicate it is now powered on. 
Noside has been pinned under the sweets-loving bear, so now is the perfect chance to make your move!''')

#-----------inventory management------------------
inventory={
    "BRANCH":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_branch")
        },
    "FRESH EGG":{
        "has":  False, 
        "usable": True,
        "description": item_descriptions.get("item_egg1")
        },
    "PICA EGG":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_egg2")
        },
    "CRANK":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_crank")
        },
    "NEEDLE":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_needle")
        },
    "WATER BUCKET":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_bucketWater")
        },
    "EMPTY BUCKET":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_bucketEmpty")
        },
    "MILK BUCKET":{
        "has": False, 
        "description": item_descriptions.get("item_bucketMilk"),
        "can_combine_with": ["JAMES"]
        },
    "KEY":{
        "has": False, 
        "description": item_descriptions.get("item_key")
        },
    "MESSAGE":{
        "has": False, 
        "description": item_descriptions.get("item_keyMessage")
        },
    "PHOTO":{
        "has": False, 
        "description": item_descriptions.get("item_photo")
        },
    "CATAPULT":{
        "has": False,
        "usable": True,
        "state": 1, #1=unloaded, 2=honey-loaded
        "descriptions": {
            1: item_descriptions.get("item_catapult1"), 
            2: item_descriptions.get("item_catapult2")
        },
        "can_combine_with": ["HONEY"]
    },
    "WINDUP KEY":{
        "has": False, 
        "description": item_descriptions.get("item_windingKey"),
        "can_combine_with": ["DENTURES"]
        },
    "DENTURES":{
        "has": False, 
        "description": item_descriptions.get("item_dentures1"),
        "can_combine_with": ["WINDUP KEY"]
        },
    "CHATTERING TEETH":{
        "has": False, 
        "description": item_descriptions.get("item_dentures2"),
        "can_combine_with": ["WHEAT"]
        },
    "TUCO":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_tuco")
        },
    "SNORKEL":{
        "has": False, 
        "description": item_descriptions.get("item_snorkel"),
        "can_combine_with": ["JAMES"]
        },
    "STOPPER":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_stopper")
        },
    "JAMES":{
        "has": False, 
        "state": 1, #1= naked James, 2= snorkel James
        "descriptions":{
            1: item_descriptions.get("item_james"),
            2: item_descriptions.get("item_james1")
        },
        "can_combine_with": ["SNORKEL"],
        "can_combine_with": ["MILK BUCKET"]
    },
    "WHEAT":{
        "has": False, 
        "description": item_descriptions.get("item_wheat"),
        "can_combine_with": ["CHATTERING TEETH"]
        },
    "FLOUR":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_flour")
        },
    "SUGAR":{
        "has": False,
        "usable": True,
        "description": item_descriptions.get("item_sugar")
        },
    "BUTTER":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_bucketButter")
        },
    "CAKE":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_cake")
        },
    "HONEY":{
        "has": False, 
        "description": item_descriptions.get("item_honey"),
        "can_combine_with": ["CATAPULT"]
        },
    "BEAR":{
        "has": False, 
        "usable": True,
        "description": item_descriptions.get("item_bear")
        },
}
def show_inventory():
    print(space1)
    print("Current Inventory:")
    for item_name, data in inventory.items():
        if data["has"]:
            print(f" - {item_name}")
    print(space1)
def get_valid_inventory_items():
    return [name.lower() for name, data in inventory.items() if data["has"]]
def inspect_item(item_name):
    item_key = inventory.get(item_name.upper())
    if not item or not item.get("has"):
        print("You don't have that item.")
        input("> RETURN")
        
    if "descriptions" in item:
        state= item.get("state", 1)
        print(item["descriptions"].get(state))
        input("> RETURN")
    else:
        print(item.get("description"))
        input("> RETURN")
def handle_inventory():
    while True:
        show_inventory()
        print("Type an item name to inspect it.")
        print("Or type: 'COMBINE item 1 + item 2' to combine two items.")
        print("Type 'CLOSE' to exit inventory.")
        
        inv_choice = input("> ").strip().lower()
        
        if inv_choice == "close":
            break
            
         # ----- Handle "combine item1 + item2" -----
        elif inv_choice.startswith("combine"):
            # Split on 'combine' and then split around '+'
            try:
                _, items = inv_choice.split("combine", 1)
                item1, item2 = map(str.strip, items.split("+"))

                try_combine(item1, item2)
            except ValueError:
                print("Please use the format: COMBINE item1 + item2")
                input("> RETURN")  

        # ----- Inspect single item -----
        elif inv_choice in get_valid_inventory_items():
            inspect_item(inv_choice)
            input("> RETURN") 
        
        else:
            print("You don't have that item.")
            input("> RETURN")
def addToInv(item_name): #addToInv("fresh egg")
    item_name = item_name.upper()
    if item_name in inventory:
        inventory[item_name]["has"] = True
        print(f"{item_name.upper()} added to inventory.")
    else:
        print(f"Error: {item_name} doesn't exist.")
def remFromInv(item_name): #remFromInv("fresh egg")
    item_name = item_name.upper()
    if item_name in inventory and inventory[item_name]["has"]:
        inventory[item_name]["has"] = False
        print(f"{item_name.upper()} removed from inventory.")
    #else: #maybe just remove this? in practice this is just a background task and player does not need to see removal errors.
        #print(f"{item_name.upper()} is not in your inventory.")

#-------Checking for an Item--------
#for game state check purposes
def has_item(item_name):
    return inventory.get(item_name.upper(), {}).get("has", False)

#-------Inventory cleanup-----------
#Should remove the item from show_inventory()
#inventory["item_name"]["has"] = False

combine_recipes = { #must be alphabetical
#template
#("ITEM1", "ITEM2"): {
 #       "result": "NEW_ITEM",
  #      "consume": ["ITEM1", "ITEM2"]
   # },
   
    #get Butter
    ("JAMES", "MILK BUCKET"): {
        "result": "BUTTER",
        "consume": ["JAMES", "MILK BUCKET"],
        "message": f'''
James spins in the milk. He spins so much, that the milk ends up becoming butter.
''',
        "failedMessage": f'''
James looks longingly at the milk bucket, but he can't swim without the proper equipment.
        ''',
        "conditions": [
            {"item": "JAMES", "state": 2}
        ]
    },
    #get james1
    ("JAMES", "SNORKEL"):{
        "result": "JAMES",
        "consume": ["SNORKEL"],
        "set_state": ("JAMES", 2), 
        "message": (f'''
James allows you to dress him in the tiny snorkeling gear. He's ready for a swim now!"''') 
    },
    #get chattering teeth
    ("DENTURES", "WINDUP KEY"): {
        "result": "CHATTERING TEETH",
        "consume": ["DENTURES", "WINDUP KEY"],
        "message": (f'''
The wind up key fits here quite nicely. You turn the key a few times, and the teeth start chomping at an alarming speed. 
You now have motorized dentures. These would probably grind up anything that gets too close.
''')     
    },
    #get flour
    ("CHATTERING TEETH", "WHEAT"): {
        "result": "FLOUR",
        "consume": ["CHATTERING TEETH", "WHEAT"],
        "message": (f'''
The chattering teeth make quick work of turning the raw wheat stalks into a fine flour.
        ''')
    },
    #get catapult2
    ("CATAPULT", "HONEY"): {
        "result": "CATAPULT",
        "consume": ["CATAPULT", "HONEY"],
        "set_state": ("CATAPULT", 2),
        "message": (f'''
You load the honey into the catapult. You're ready to fight!
        ''')
    }   
}
            
def try_combine(item1, item2):
    item1 = item1.upper()
    item2 = item2.upper()
    
    combo_key = tuple(sorted([item1, item2]))
    if combo_key in combine_recipes:
        recipe = combine_recipes[combo_key]
        
        if not all(inventory.get(i, {}).get("has") for i in recipe["consume"]):
            print("You don't have the required items.")
            input("> RETURN")
        
        #check for conditions---
        elif "conditions" in recipe:
            for condition in recipe["conditions"]:
                item = condition["item"]
                required_state = condition.get("state")
                current_state = inventory.get(item, {}).get("state", 1)
                if required_state is not None and current_state != required_state:
                    print(recipe["failedMessage"])
                    input("> RETURN")  
                
                else:                    
                    # Add new item
                    addToInv(recipe["result"])
                    if "message" in recipe:
                        print(recipe["message"])

                    # Remove consumed items
                    for i in recipe["consume"]:
                        inventory[i]["has"] = False
                        remFromInv(i)

                    # Handle state change, if any
                    if "set_state" in recipe:
                        target_item, new_state = recipe["set_state"]
                        inventory[target_item]["state"] = new_state

                    input("> RETURN")
        
            
    else:
        print("Those items can't be combined.")
    
#------Map management-----------------
map={
    "OUTSIDE":{
        "has": True,
        "state": 1,
        "descriptions": {
            1: enter_outside,
            2: location_outside
        }
    },
    "LIVING ROOM":{
        "has": False, 
        "state": 1,
        "descriptions": {
            1: enter_livingRoom,
            2: location_livingRoom()
        }
    },
    "BEDROOM":{
        "has": False,
        "state": 1,
        "descriptions": {
            1: enter_bedroom,
            2: location_bedroom()
        }
    },
    "BATHROOM":{
        "has": False,
        "state": 1,
        "descriptions":{
            1: enter_bathroom,
            2: location_bathroom()
        }
    },
    "KITCHEN":{
        "has": False,
        "state": 1,
        "descriptions":{
            1: enter_kitchen,
            2: location_kitchen()
        }
    },
    "SECRET LAIR":{
        "has": False,
        "state": 1,
        "descriptions":{
            1: enter_lair,
            2: location_lair()
            }
    }
}

def show_map():
    print(space1)
    print("Current locations:")
    for location_name, data in map.items():
        if data["has"]:
            print(f" - {location_name}")
    print(space1)
def get_valid_map_areas():
    return [name.upper() for name, data in map.items() if data["has"]]
def inspect_area(location_name):
    area_key = map.get(location_name.upper())
    if not area_key or not area_key.get("has"):
        print("Location not found.")
        input ("> RETURN")
    if "descriptions" in area_key:
        state = area_key.get("state", 1)
        print(area_key["descriptions"].get(state))
        input("> RETURN")        
def handle_map():
   while True:
        print(space)
        show_map()
        print("Type a location's name to see a description of the area again, or type 'close' to return to game.")            
        mapChoice= input("> ").upper().strip() 
        
        if mapChoice == "close":
            break
        #-----Inspect map locations---------
        elif mapChoice in get_valid_map_areas():
            inspect_area(mapChoice)           
        else:
            print("Location not found.")
            input("> RETURN") 
def addToMap(location_name): #addToMap("OUTSIDE")
    location_name = location_name.upper()
    if location_name in map:  #else: print(f"Error: {location_name} doesn't exist) -- not required in this version of game.
        map[location_name]["has"] = True
        print(f"{location_name.upper()} added to map.")
def remFromMap(location_name): 
    location_name = location_name.upper()
    if location_name in map and map[location_name]["has"]:
        map[location_name]["has"] = False
        print(f"{location_name.upper()} removed from map.")
       

gameOver= False
while not gameOver:
    print("Testing, game not yet complete")
    examineChoice= input("> ").lower().strip()
    
    #------Calling the inventory in game-------
    if examineChoice=="inventory":
        handle_inventory()
    #------Calling the map in game-------------
    if examineChoice== "map":
        handle_map()
