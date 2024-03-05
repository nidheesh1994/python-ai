import hero_side_kick

class Hero_Token(hero_side_kick.HeroSide):
    def token(self, state):

        pairs = sorted(state[0].items())

        return tuple(pairs), state[1]
    
