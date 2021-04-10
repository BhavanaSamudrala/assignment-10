from LocationNode_provided import LocationNode as LN


class MobilityProfile(object):

    def __init__(self, aList=None):
        """
        Purpose: creates a mobility profile. If no aList is given, profile is set to None
        Pre-condition:
            aList: A list of five strings, showing the sequential locations that the user had visited.
        Post-condition: A mobility profile is created
        Return: None
        """
        # create an empty profile
        self.profile = None
        # calls create_profile with the given list
        self.create_profile(aList)

    def create_profile(self, aList):
        """
        Purpose:
            Creates a mobility profile using the given aList
        Pre-conditions:
            aList: A list of five strings, showing the sequential locations that the user had visited.
            aList should only have five locations.
        Post-condition:
            A mobility profile is created
        Return:
            None
        """
        if len(aList) ==5:
            self.profile = None
            current = self.profile
            for loc in aList:
                if current != None:
                    current.set_next(LN(loc))
                    current= current.get_next()
                else:
                    self.profile = LN(loc)
                    current = self.profile

    def compare_profile(self, otherProfile):
        """
        Purpose:
            Compare two mobility profiles. Return True when the two mobility profile as a location matched.
        Pre-conditions:
            otherProfile: Another user's mobility profile for comparison.
            Both self and other profiles must not be None.
        Post-condition:
            None
        Return:
            True if there is a match, False for otherwise.
        """

        if self.profile != None and otherProfile.profile != None:
            p1 = self.profile
            p2 =otherProfile.profile
            while p1 != None and p2 != None:

                if p2.get_current_location()==p1.get_current_location() :
                    return True
                # move curr and other to next location
                p1= p1.get_next_location()
                p2 = p2.get_next_location()

        return False  # no match in this and otherProfile

