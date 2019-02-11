# -*- coding: utf-8 -*-
from mahjong.hand_calculating.yaku import Yaku


class YakuhaiOfPlace(Yaku):
    
    def __init__(self, yaku_id):
        super(YakuhaiOfPlace, self).__init__(yaku_id)

    def set_attributes(self):
        self.name = 'Yakuhai (wind of place)'
        self.english = 'Value Tiles (Seat)'

        self.han_open = 1
        self.han_closed = 1

        self.is_yakuman = False

    def is_condition_met(self, hand, *args):
        return True
