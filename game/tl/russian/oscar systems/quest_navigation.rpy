



screen oscar_quest_page_key_navigation(g):
    key "K_LEFT" action Show("character_page", g=get_neighbor(g, direction=-1))
    key "K_a" action Show("character_page", g=get_neighbor(g, direction=-1))
    key "K_RIGHT" action Show("character_page", g=get_neighbor(g, direction=1))
    key "K_d" action Show("character_page", g=get_neighbor(g, direction=1))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
