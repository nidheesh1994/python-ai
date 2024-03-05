def select_traveller(candidates):
    
    for first in range(len(candidates)):
        yield [candidates[first]]
    
    for first in range(len(candidates)):
        for second in range(first+1, len(candidates)):
            yield[candidates[first], candidates[second]]


def safe(state):
    person_side, _ = state

    for side in ["left", "right"]:

        lone_side_kicks = [index for person,index in person_side 
                           if person == 'kick' 
                           if person_side[person,index] == side
                           if person_side['hero',index] != side]

        present_hero = [index for person, index in person_side 
                        if person == 'hero' 
                        if person_side[person, index] == side]

        if lone_side_kicks and present_hero:
            return False
    return True

other_side = {"left":"right","right":"left"}

class HeroSide:

    def start(self):
        return {(person, index):"left" for person in ["hero", "kick"] for index in [1,2,3]}, "left"

    def goal(self, state):

        person_side, _ = state

        return set(person_side[person] for person in person_side if person_side) == {"right"}

    def succ(self, state):

        person_side, boat = state

        person_with_boats = [person for person in person_side if person_side[person] == boat]

        for traveller_group in select_traveller(person_with_boats):
            new_side = person_side.copy()

            for traveller in traveller_group:
                new_side[traveller] = other_side[person_side[traveller]]

            new_state = new_side, other_side[boat]

            if safe(new_state):
                yield new_state
