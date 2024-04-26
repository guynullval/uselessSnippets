# “Marry, and you will regret it; don’t marry, you will also regret it; marry or don’t marry, you will regret it either way. Laugh at the world’s foolishness, you will regret it; weep over it, you will regret that too; laugh at the world’s foolishness or weep over it, you will regret both. Believe a woman, you will regret it; believe her not, you will also regret it… Hang yourself, you will regret it; do not hang yourself, and you will regret that too; hang yourself or don’t hang yourself, you’ll regret it either way; whether you hang yourself or do not hang yourself, you will regret both. This, gentlemen, is the essence of all philosophy.”
# ― Søren Kierkegaard 

from enum import Enum

class Mood(Enum):
    regret = 1

def EssenceOfAllPhilosophy(_self):
    if _self:
        return "regret"
    if not(_self):
        return "regret"
    if _self or not(_self):
        return "regret"
    return "regret"

def marry(_self):
    return EssenceOfAllPhilosophy(_self)


def laughAtTheWorldsFoolishness(_self):
    return EssenceOfAllPhilosophy(_self)


def believeAWoman(_self):
    return EssenceOfAllPhilosophy(_self)


def hangYourSelf(_self):
    return EssenceOfAllPhilosophy(_self)


