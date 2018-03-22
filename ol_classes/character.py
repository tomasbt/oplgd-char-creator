
class character:
    """
    This is a class definition used for a character in open legend
    """
    def __init__(self, name, xp=0, debug=False):
        
        ## General information
        self.name = name
        self.race = "human"
        self.xp = xp
        self.level = int(self.xp/3)
    
        ## Attributes
        self.attribute_points = 40 + 3 * self.xp
        self.attribute_list = [0] * 18

        # feats
        self.feat_points = 6 + self.xp

        self.feat_list = []

        # perks 

        # favor actions

        # equipment

    def add_xp(self, xp):
        """
        This function adds xp to the character and corrects the level, attribute points and feat points
        """
        self.xp += int(xp)
        self.level = int(self.xp/3)

        self.attribute_points += xp*3
        self.feat_points += xp
        


