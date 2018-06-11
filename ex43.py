class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
class Engine(object):
    def__init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_secne = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name_
        current_scene.enter()
class Death(Scene):
    quips = [
            "You died. You kinda suck at this.",
            "Your Mom would be proud ... if she were smarter.",
            "such a luser",
            I have a small puppy that's better at this."'
            You're worse than your Dad's jokes."
            ]
    def enter(self):
        print(Death.quips[randit(0, len (self.quips)-10])
        exit(1)
class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
                The Gothons of Planet Percal #25 have invaded your ship and 
                destroyed your entire crew. You are the last surviving
                member and your last mission is to get the neutron destruct
                bomb from the Weapons Armory , put it in the bridge, and 
                blow the ship up after getting into an escape pod.

                You're running down the central corridor to the Weapons
                Armory when a Gothon jumps out , red scaly skin, dark grimy
                teeth, and evil clown costume flowing around his hate 
                filled body. He's blocking the door to the Armory and 
                about to  pull a weapon to blast you.
                """))
        action = input(". ")
        if action == "shoot!":
            print(dedent("""
            Quick on the draw you yank out your blaster and fire
            it at the Gothon. His clown costume is flowing and 
            moving arond his body ,which throws off your aim.
            Your laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his mother
            bought him ,which makes fly into an insane rage
            and bllast you repratedly in the face until you are 
            dead.Then he eats you.
            """))
            return 'death'
        elif action =="dodge!":
            print(dedent("""
            Like a world class boxer you dodge,weave,slip and 
            slide right as the gothon's blaster cranks a laser 
            past your head , In the middle of your artful dodge
            your foot slips and you bang your head on the metal
            walland passout. You wake up shortly after only to 
            die as the gothon stomps on your head and eats you.
            """))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
            Lucky for you they made learn Gothoninsults in 
            the academy , YOu tell the one Gothon joke you know:
            Lbe zbgure vf fb sng ,jura fur fvgf nebhaq gur ubhfr,
            fur.The Gothon stops,tries not to laugh ,then busts out laughing and
            can't move.While he's laughing you run up and shoot him square in
            the head putting him down,then jump through the Weapon Armory door.
            """))
            return 'laser_weapon_armory'
        else:
            print("Does Not Compute!")
            return 'central_corridor'
class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
                YOu do a dive roll into the Weapon Armory,crouch and scan
                the room for more Gothons that might be hiding. It's dead 
                quiet ,too quiet.YOu stand up and run to the far side of
                the room and find the neutron bomb in its container.
                There's a keypad lock on the box and you need the code to 
                get the bomb out.If you get the code wrong 10 times then
                thelock closes forever and you can't get the bomb.The 
                code is 3 digits."""))
        


       
