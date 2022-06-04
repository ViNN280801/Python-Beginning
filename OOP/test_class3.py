from class3 import Player

# Working of classmethod decorator
# Setting class fields by 'set_cls_fields()' method
Player.set_cls_fields(5, 125)
player = Player()
player.show()

# This method can be emplty
Player.set_cls_fields()
player_2 = Player()
player_2.show()
