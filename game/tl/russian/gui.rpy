init offset = -2









init python:

    gui.init(3840, 2160)













define gui.accent_color = '#9933ff'


define gui.idle_color = '#FFFFFF'



define gui.idle_small_color = '#aaaaaa'


define gui.hover_color = '#c184ff'



define gui.selected_color = '#ffffff'


define gui.insensitive_color = '#8888887f'



define gui.muted_color = '#3d1466'
define gui.hover_muted_color = '#5b1e99'


define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'





define gui.text_font = "Fonts/NotoSansDisplay-ExtraBold.ttf"
define gui.text_outlines = [(0.0, "#000", 0, 0)]


define gui.name_text_font = "Fonts/Another-Danger-Demo.ttf"


define gui.interface_text_font = "Fonts/Another-Danger-Demo.ttf"

translate russian python:
    gui.text_font = "Fonts/NotoSansDisplay-ExtraBold.ttf"
    gui.name_text_font = "Fonts/Another-Danger-Demo.ttf"
    gui.interface_text_font = "Fonts/Another-Danger-Demo.ttf"


define gui.text_size = 65

define gui.name_text_size = 90


define gui.interface_text_size = 90


define gui.label_text_size = 72


define gui.notify_text_size = 48


define gui.title_text_size = 150





define gui.main_menu_background = Movie(play="gui/main_menu.webm", size=(3840, 2160))
define gui.game_menu_background = "gui/game_menu.png"








define gui.textbox_height = 500





define gui.textbox_yalign = 1.0





define gui.name_xpos = 720
define gui.name_ypos = 3



define gui.name_xalign = 0.0



define gui.namebox_width = None
define gui.namebox_height = None



define gui.namebox_borders = Borders(5, 5, 5, 5)



define gui.namebox_tile = False





define gui.dialogue_xpos = 804
define gui.dialogue_ypos = 200


define gui.dialogue_width = 2232



define gui.dialogue_text_xalign = 0.0








define gui.button_width = None
define gui.button_height = None


define gui.button_borders = Borders(12, 12, 12, 12)



define gui.button_tile = False


define gui.button_text_font = gui.interface_text_font


define gui.button_text_size = gui.interface_text_size


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0








define gui.radio_button_borders = Borders(54, 12, 12, 12)

define gui.check_button_borders = Borders(54, 12, 12, 12)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(30, 12, 30, 12)

define gui.quick_button_borders = Borders(30, 12, 30, 0)
define gui.quick_button_text_size = 42
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color












define gui.choice_button_width = 2370
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(300, 15, 300, 15)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#FFFFFF"
define gui.choice_button_text_hover_color = "#202020"
define gui.choice_button_text_insensitive_color = "#444444"









define gui.slot_button_width = 828
define gui.slot_button_height = 618
define gui.slot_button_borders = Borders(30, 30, 30, 30)
define gui.slot_button_text_size = 42
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color


define config.thumbnail_width = 768
define config.thumbnail_height = 432


define gui.file_slot_cols = 3
define gui.file_slot_rows = 2









define gui.navigation_xpos = 120


define gui.skip_ypos = 30


define gui.notify_ypos = 135


define gui.choice_spacing = 66


define gui.navigation_spacing = 12


define gui.pref_spacing = 30


define gui.pref_button_spacing = 0


define gui.page_spacing = 0


define gui.slot_spacing = 30


define gui.main_menu_text_xalign = 1.0








define gui.frame_borders = Borders(12, 12, 12, 12)


define gui.confirm_frame_borders = Borders(120, 120, 120, 120)


define gui.skip_frame_borders = Borders(48, 15, 150, 15)


define gui.notify_frame_borders = Borders(48, 15, 120, 15)


define gui.frame_tile = False











define gui.bar_size = 75
define gui.scrollbar_size = 36
define gui.slider_size = 75


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(12, 12, 12, 12)
define gui.scrollbar_borders = Borders(12, 12, 12, 12)
define gui.slider_borders = Borders(12, 12, 12, 12)


define gui.vbar_borders = Borders(12, 12, 12, 12)
define gui.vscrollbar_borders = Borders(12, 12, 12, 12)
define gui.vslider_borders = Borders(12, 12, 12, 12)



define gui.unscrollable = "hide"







define config.history_length = 250



define gui.history_height = 420



define gui.history_name_xpos = 465
define gui.history_name_ypos = 0
define gui.history_name_width = 465
define gui.history_name_xalign = 1.0


define gui.history_text_xpos = 510
define gui.history_text_ypos = 6
define gui.history_text_width = 2220
define gui.history_text_xalign = 0.0







define gui.nvl_borders = Borders(0, 30, 0, 60)



define gui.nvl_list_length = 6



define gui.nvl_height = 345



define gui.nvl_spacing = 30



define gui.nvl_name_xpos = 1290
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 450
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 1350
define gui.nvl_text_ypos = 24
define gui.nvl_text_width = 1770
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 720
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 2340
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 1350
define gui.nvl_button_xalign = 0.0







define gui.language = "unicode"






init python:



    @gui.variant
    def touch():
        
        gui.quick_button_borders = Borders(120, 42, 120, 0)



    @gui.variant
    def small():
        
        
        gui.text_size = 90
        gui.name_text_size = 108
        gui.notify_text_size = 75
        gui.interface_text_size = 90
        gui.button_text_size = 90
        gui.label_text_size = 102
        
        
        gui.textbox_height = 530
        gui.name_xpos = 300
        gui.dialogue_xpos = 270
        gui.dialogue_width = 3300
        
        
        gui.slider_size = 108
        
        gui.choice_button_width = 3720
        gui.choice_button_text_size = 90
        
        gui.navigation_spacing = 60
        gui.pref_button_spacing = 30
        
        gui.history_height = 570
        gui.history_text_width = 2070
        
        gui.quick_button_text_size = 60
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 510
        
        gui.nvl_name_width = 915
        gui.nvl_name_xpos = 975
        
        gui.nvl_text_width = 2745
        gui.nvl_text_xpos = 1035
        gui.nvl_text_ypos = 15
        
        gui.nvl_thought_width = 3720
        gui.nvl_thought_xpos = 60
        
        gui.nvl_button_width = 3720
        gui.nvl_button_xpos = 60