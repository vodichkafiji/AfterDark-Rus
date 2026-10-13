










default persistent.visual_text_help = _preferences.self_voicing


default persistent.audio_cues = True

default persistent.screenshake = True

default persistent.say_window_alpha = 0.75

default persistent.pref_text_scale = "regular"

default persistent.say_dialogue_kerning = 0

default persistent.pref_text_font = "Barlow-Black.ttf"

default persistent.pref_text_size = 60

default persistent.pref_text_color = "#333333"

default persistent.pref_text_spacing = 0


init python:
    
    
    size_dict = {
        "Heraldic Shadows.ttf" : {
            "regular" : 80,
            "large" : 90,
            "line_spacing" : -15,
            },

        "Barlow-Black.ttf" : {
            "regular" : 60,
            "large" : 70,
            "line_spacing" : 0,
            },
        "OpenDyslexic.otf" : {
            "regular" : 50,
            "large" : 60,
            "line_spacing" : 0,
            },
        "AtkinsonBold.otf" : {
            "regular" : 60,
            "large" : 70,
            "line_spacing" : 0,
            },    
        
        }
    
    
    music_dictionary = {
    }
    
    
    sfx_dictionary = {
    }

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
