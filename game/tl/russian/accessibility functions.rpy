init python:

    def changeFont(newFont):
        # Если шрифт отсутствует в size_dict, используем первый попавшийся или безопасные значения
        default_sizes = {"regular": 24, "large": 28, "huge": 32, "line_spacing": 0}
        font_data = size_dict.get(newFont, default_sizes)
        
        return (
            SetField(persistent, "pref_text_font", newFont),
            SetField(persistent, "pref_text_size", font_data.get(persistent.pref_text_scale, 24)),
            SetField(persistent, "pref_text_spacing", font_data.get('line_spacing', 0)),
            SelectedIf(persistent.pref_text_font == newFont)
        )

    def changeScale(newScale):
        # Безопасное получение размера: если шрифта нет в size_dict, берутся значения по умолчанию
        default_sizes = {"regular": 24, "large": 28, "huge": 32}
        font_sizes = size_dict.get(persistent.pref_text_font, default_sizes)
        new_size = font_sizes.get(newScale, 24)

        return (
            SetField(persistent, "pref_text_scale", newScale),
            SetField(persistent, "pref_text_size", new_size)
        )

    def changeColor(newColor):
        return SetField(persistent, "pref_text_color", newColor)

    def persistentToggle(persistentfield):
        return ToggleField(persistent, persistentfield, true_value=True, false_value=False)

    def play_sfx(sound_alias, fade=0):
        renpy.sound.play(sound_alias, fadein=fade)
        if persistent.audio_cues:
            playing = renpy.sound.get_playing('sound')
            if playing in sfx_dictionary:
                renpy.notify("SFX: {i}" + sfx_dictionary[playing] + "{/i}")

    def play_music(music_alias, fade=0):
        renpy.music.play(music_alias, fadein=fade)
        if persistent.audio_cues:
            playing = renpy.music.get_playing('music')
            if playing in music_dictionary:
                renpy.notify("Now Playing: " + music_dictionary[playing])

    def shake():
        if persistent.screenshake:
            renpy.with_statement(hpunch)
        else:
            renpy.with_statement(fade) 

define vt = Character(None, condition="persistent.visual_text_help or _preferences.self_voicing", what_italic=True)