
screen ad_gifting_input_blocker():



    modal True
    zorder 199
    key "dismiss" action NullAction() capture True
    button:
        xsize config.screen_width
        ysize config.screen_height
        background None
        hover_background None
        focus_mask None
        action NullAction()

transform ad_gift_notification_pop:
    alpha 0.0
    zoom 0.94
    yoffset 8
    on show:
        parallel:
            easeout 0.16 alpha 1.0
            pause 1.58
            easein 0.32 alpha 0.0
        parallel:
            easeout 0.16 zoom 1.0 yoffset 0
            pause 1.58
            easein 0.32 zoom 0.98 yoffset -4

transform ad_gift_error_fade:
    alpha 0.0
    easeout 0.16 alpha 1.0
    pause 1.5
    easein 0.42 alpha 0.0

transform ad_gift_result_fade:
    alpha 0.0
    easeout 0.16 alpha 1.0
    pause 1.0
    easein 0.42 alpha 0.0

screen ad_gift_notification_screen():
    zorder 1000




    $ ad_gift_notice_measure = renpy.text.text.Text(ad_gift_notification_text, font=ad_gothic_body_font, size=34, outlines=[(2, "#000000", 0, 0)])
    $ ad_gift_notice_text_width, _ad_gift_notice_text_height = ad_gift_notice_measure.size()
    $ ad_gift_notice_width = max(420, int(ad_gift_notice_text_width) + 148)
    timer 0.01 repeat True action Function(ad_update_gift_notification_position)
    timer 2.0 action Hide("ad_gift_notification_screen")

    fixed:
        xpos ad_gift_notification_x
        ypos ad_gift_notification_y
        xsize ad_gift_notice_width
        ysize 116
        at ad_gift_notification_pop
        add Solid("#08080FE8"):
            xpos 8
            ypos 8
            xsize ad_gift_notice_width - 16
            ysize 100
        use ad_barbed_border(ad_gift_notice_width, 116, 12, 15)
        if ad_gift_notification_item_id in ad_items:
            add ad_items[ad_gift_notification_item_id]["icon"]:
                xpos 22
                yalign 0.5
                xsize 70
                ysize 70
        text ad_gift_notification_text:
            xpos 110
            yalign 0.5
            xsize ad_gift_notice_width - 132
            text_align 0.0
            size 34
            color "#D8D8E0"
            outlines [(2, "#000000", 0, 0)]
            font ad_gothic_body_font


screen ad_gift_error_screen():
    zorder 260
    $ ad_error_panel_height = int(config.screen_height * 0.84)
    $ ad_error_right_x = int(config.screen_width * 0.5925)
    $ ad_error_right_width = int(config.screen_width * 0.36)
    timer 2.1 action [SetVariable("ad_gift_message", ""), Hide("ad_gift_error_screen")]
    fixed:
        xpos ad_error_right_x
        ypos int((config.screen_height - ad_error_panel_height) * 0.5 + (ad_error_panel_height * 0.93))
        xsize ad_error_right_width
        ysize 80
        text ad_gift_message:
            xalign 0.5
            yalign 0.5
            xmaximum int(ad_error_right_width * 0.74)
            text_align 0.5
            size int(config.screen_height * 0.020) + 10
            color "#D7D7E0"
            outlines [(2, "#000000", 0, 0)]
            font ad_gothic_body_font
            at ad_gift_error_fade


screen ad_character_gifting_screen():



    modal True
    zorder 200
    default ad_riley_gift_quantity_input = VariableInputValue("ad_gift_quantity", default=False)
    $ ad_gift_panel_height = int(config.screen_height * 0.84)
    $ ad_gift_left_width = int(config.screen_width * 0.52)
    $ ad_gift_right_width = int(config.screen_width * 0.36)
    $ ad_gift_gap = int(config.screen_width * 0.025)
    $ ad_gift_grid_width = int(ad_gift_left_width * 0.88)
    $ ad_gift_grid_height = int(ad_gift_panel_height * 0.66)
    $ ad_gift_grid_gap = max(4, int(config.screen_height * 0.008))
    $ ad_gift_horizontal_gap = ad_gift_grid_gap + 75
    $ ad_gift_slot_size = int(min((ad_gift_grid_width - 48 - (ad_gift_horizontal_gap * 3)) / 4, (ad_gift_grid_height - 48 - (ad_gift_grid_gap * 3)) / 4))
    $ ad_gift_slot_border = max(8, int(ad_gift_slot_size * 0.12))


    key "dismiss" action NullAction() capture True

    if ad_gift_is_error:
        timer 2.1 action [SetVariable("ad_gift_is_error", False), SetVariable("ad_gift_message", "")]
    elif ad_gift_show_result:
        timer 1.6 action [SetVariable("ad_gift_show_result", False), SetVariable("ad_gift_message", "")]

    fixed:
        xalign 0.5
        yalign 0.5
        xsize config.screen_width
        ysize config.screen_height
        at ad_gothic_screen_open
        add ad_ui_background:
            xsize config.screen_width
            ysize config.screen_height
            alpha 0.66
        add Solid("#05050A82"):
            xsize config.screen_width
            ysize config.screen_height
        use ad_barbed_border(config.screen_width, config.screen_height, 64, 74)



        button:
            xsize config.screen_width
            ysize config.screen_height
            background None
            focus_mask None
            action [ad_riley_gift_quantity_input.Disable(), NullAction()]

        hbox:
            xalign 0.5
            yalign 0.5
            spacing ad_gift_gap

            fixed:
                xsize ad_gift_left_width
                ysize ad_gift_panel_height
                add Solid("#090A108C"):
                    xpos 26
                    ypos 26
                    xsize ad_gift_left_width - 52
                    ysize ad_gift_panel_height - 52
                use ad_barbed_border(ad_gift_left_width, ad_gift_panel_height, int(config.screen_height * 0.035), int(config.screen_height * 0.045))
                text "ИНВЕНТАРЬ ПОДАРКОВ":
                    xalign 0.5
                    ypos int(ad_gift_panel_height * 0.045)
                    text_align 0.5
                    size int(config.screen_height * 0.052)
                    color "#F0F0F2"
                    outlines [(2, "#24070B", 1, 1), (1, "#000000", 0, 0)]
                    font ad_inventory_title_font
                text "ВЫБЕРИТЕ ПРЕДМЕТ ДЛЯ ПОДАРКА":
                    xalign 0.5
                    ypos int(ad_gift_panel_height * 0.115)
                    text_align 0.5
                    size int(config.screen_height * 0.024)
                    color "#BDBDC7"
                    outlines [(1, "#000000", 0, 0)]
                    font ad_gothic_body_font
                fixed:
                    xalign 0.5
                    ypos int(ad_gift_panel_height * 0.17)
                    xsize int(ad_gift_left_width * 0.52)
                    ysize int(ad_gift_panel_height * 0.11)
                    add Solid("#101017A8"):
                        xpos 8
                        ypos 6
                        xsize int(ad_gift_left_width * 0.52) - 16
                        ysize int(ad_gift_panel_height * 0.11) - 12
                    use ad_barbed_border(int(ad_gift_left_width * 0.52), int(ad_gift_panel_height * 0.11), int(config.screen_height * 0.022), int(config.screen_height * 0.030))
                    text "ДЕНЬГИ  [ad_format_money(ad_money)]":
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5
                        size int(config.screen_height * 0.034)
                        color "#D4D4DB"
                        outlines [(1, "#000000", 0, 0)]
                        font ad_inventory_money_font
                fixed:
                    xalign 0.5
                    ypos int(ad_gift_panel_height * 0.30)
                    xsize ad_gift_grid_width
                    ysize ad_gift_grid_height
                    add Solid("#08080E9B"):
                        xpos 12
                        ypos 12
                        xsize ad_gift_grid_width - 24
                        ysize ad_gift_grid_height - 24
                    use ad_barbed_border(ad_gift_grid_width, ad_gift_grid_height, int(config.screen_height * 0.025), int(config.screen_height * 0.034))
                    grid 4 4:
                        xalign 0.5
                        yalign 0.5
                        xspacing ad_gift_horizontal_gap
                        yspacing ad_gift_grid_gap
                        for item_id in ad_item_order:
                            $ item = ad_items[item_id]
                            button:
                                xsize ad_gift_slot_size
                                ysize ad_gift_slot_size
                                sensitive ad_item_amount(item_id) > 0
                                background None
                                hover_background None
                                selected_background None
                                focus_mask None
                                selected False
                                action [ad_riley_gift_quantity_input.Disable(), Function(ad_toggle_gift_selection, item_id)]
                                add Solid("#0909109B" if ad_selected_inventory_item == item_id else "#0D0D157C"):
                                    xpos ad_gift_slot_border
                                    ypos ad_gift_slot_border
                                    xsize ad_gift_slot_size - (ad_gift_slot_border * 2)
                                    ysize ad_gift_slot_size - (ad_gift_slot_border * 2)
                                use ad_barbed_border(ad_gift_slot_size, ad_gift_slot_size, ad_gift_slot_border, int(ad_gift_slot_size * 0.14))
                                add item["icon"]:
                                    xcenter int(ad_gift_slot_size * 0.5)
                                    yalign 0.40
                                    yoffset 10
                                    xsize int(ad_gift_slot_size * 0.63)
                                    ysize int(ad_gift_slot_size * 0.63)
                                    at ad_item_hover
                                text "x[ad_item_amount(item_id)]":
                                    xalign 0.5
                                    yalign 0.84
                                    text_align 0.5
                                    size int(config.screen_height * 0.020)
                                    color "#D4D4DB"
                                    outlines [(1, "#000000", 0, 0)]
                                    font ad_gothic_body_font
                        for empty_slot in range(16 - len(ad_item_order)):
                            fixed:
                                xsize ad_gift_slot_size
                                ysize ad_gift_slot_size
                                add Solid("#0D0D157C"):
                                    xpos ad_gift_slot_border
                                    ypos ad_gift_slot_border
                                    xsize ad_gift_slot_size - (ad_gift_slot_border * 2)
                                    ysize ad_gift_slot_size - (ad_gift_slot_border * 2)
                                use ad_barbed_border(ad_gift_slot_size, ad_gift_slot_size, ad_gift_slot_border, int(ad_gift_slot_size * 0.14))
                                text "X":
                                    xalign 0.5
                                    yalign 0.5
                                    text_align 0.5
                                    size int(ad_gift_slot_size * 0.22)
                                    color "#686873"
                                    outlines [(1, "#000000", 0, 0)]
                                    font ad_gothic_body_font

            fixed:
                xsize ad_gift_right_width
                ysize ad_gift_panel_height
                add Solid("#090A108C"):
                    xpos 26
                    ypos 26
                    xsize ad_gift_right_width - 52
                    ysize ad_gift_panel_height - 52
                use ad_barbed_border(ad_gift_right_width, ad_gift_panel_height, int(config.screen_height * 0.035), int(config.screen_height * 0.045))
                text "ПОДАРИТЬ":
                    xalign 0.5
                    ypos int(ad_gift_panel_height * 0.045)
                    text_align 0.5
                    size int(config.screen_height * 0.052)
                    color "#F0F0F2"
                    outlines [(2, "#24070B", 1, 1), (1, "#000000", 0, 0)]
                    font ad_inventory_title_font
                text "ДЛЯ [ad_localized_character_name(ad_gift_target).upper()]":
                    xalign 0.5
                    ypos int(ad_gift_panel_height * 0.115)
                    text_align 0.5
                    size int(config.screen_height * 0.024)
                    color "#BDBDC7"
                    outlines [(1, "#000000", 0, 0)]
                    font ad_gothic_body_font
                fixed:
                    xalign 0.5
                    ypos int(ad_gift_panel_height * 0.20)
                    xsize int(ad_gift_right_width * 0.78)
                    ysize int(ad_gift_panel_height * 0.43)
                    add Solid("#08080E9B"):
                        xpos 12
                        ypos 12
                        xsize int(ad_gift_right_width * 0.78) - 24
                        ysize int(ad_gift_panel_height * 0.43) - 24
                    use ad_barbed_border(int(ad_gift_right_width * 0.78), int(ad_gift_panel_height * 0.43), int(config.screen_height * 0.025), int(config.screen_height * 0.034))
                    if ad_selected_inventory_item in ad_items:
                        $ selected_item = ad_items[ad_selected_inventory_item]
                        add selected_item["icon"]:
                            xalign 0.5
                            yalign 0.34
                            xsize int(ad_gift_right_width * 0.22)
                            ysize int(ad_gift_right_width * 0.22)
                            at ad_item_hover
                        text selected_item["name"].upper():
                            xalign 0.5
                            ypos int(ad_gift_panel_height * 0.27)
                            text_align 0.5
                            size int(config.screen_height * 0.030)
                            color "#E0E0E7"
                            outlines [(1, "#000000", 0, 0)]
                            font ad_gothic_body_font
                        text selected_item["description"]:
                            xalign 0.5
                            ypos int(ad_gift_panel_height * 0.34)
                            xmaximum int(ad_gift_right_width * 0.60)
                            text_align 0.5
                            size int(config.screen_height * 0.020)
                            color "#BDBDC7"
                            outlines [(1, "#000000", 0, 0)]
                            font ad_gothic_body_font
                    else:
                        text "ВЫБЕРИТЕ ПОДАРОК":
                            xalign 0.5
                            yalign 0.5
                            text_align 0.5
                            size int(config.screen_height * 0.030)
                            color "#8C8C97"
                            outlines [(1, "#000000", 0, 0)]
                            font ad_gothic_body_font
                fixed:
                    xalign 0.5
                    ypos int(ad_gift_panel_height * 0.67)
                    xsize int(ad_gift_right_width * 0.52)
                    ysize int(ad_gift_panel_height * 0.11)
                    add Solid("#101017A8"):
                        xpos 6
                        ypos 6
                        xsize int(ad_gift_right_width * 0.52) - 12
                        ysize int(ad_gift_panel_height * 0.11) - 12
                    use ad_barbed_border(int(ad_gift_right_width * 0.52), int(ad_gift_panel_height * 0.11), int(config.screen_height * 0.020), int(config.screen_height * 0.028))
                    button:
                        xalign 0.5
                        yalign 0.5
                        xsize int(ad_gift_right_width * 0.52)
                        ysize int(ad_gift_panel_height * 0.11)
                        background None
                        hover_background None
                        focus_mask None
                        key_events True
                        action ad_riley_gift_quantity_input.Enable()
                        input:
                            xalign 0.5
                            yalign 0.5
                            value ad_riley_gift_quantity_input
                            prefix "x"
                            allow "0123456789"
                            length 9
                            text_align 0.5
                            size int(config.screen_height * 0.037)
                            color "#F0F0F2"
                            outlines [(1, "#000000", 0, 0)]
                            font ad_inventory_money_font
                imagebutton:
                    xpos max(0, int(ad_gift_right_width * 0.32) - 216)
                    ypos int(ad_gift_panel_height * 0.725)
                    yanchor 0.5
                    idle Transform("arrowleft_idle.png", size=(161, 161))
                    hover Transform("arrowleft_hover.png", size=(171, 171))
                    action [ad_riley_gift_quantity_input.Disable(), Function(ad_gift_change_quantity, -1)]
                imagebutton:
                    xpos int(ad_gift_right_width * 0.68) + 60
                    ypos int(ad_gift_panel_height * 0.725)
                    yanchor 0.5
                    idle Transform("arrowleft_idle.png", xzoom=-1, size=(161, 161))
                    hover Transform("arrowleft_hover.png", xzoom=-1, size=(171, 171))
                    action [ad_riley_gift_quantity_input.Disable(), Function(ad_gift_change_quantity, 1)]
                button:
                    xalign 0.5
                    ypos int(ad_gift_panel_height * 0.84)
                    xsize int(ad_gift_right_width * 0.72)
                    ysize int(ad_gift_panel_height * 0.075)
                    background None
                    hover_background None
                    focus_mask None
                    action [ad_riley_gift_quantity_input.Disable(), Function(ad_give_gift, ad_gift_quantity_value())]
                    text "ПОДАРИТЬ":
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5
                        color "#F1EEF0"
                        outlines [(1, "#000000", 0, 0)]
                        font ad_gothic_body_font
                        size int(config.screen_height * 0.028)
                        at ad_item_hover
                if ad_gift_is_error:
                    fixed:
                        xalign 0.5
                        ypos int(ad_gift_panel_height * 0.925)
                        xsize int(ad_gift_right_width * 0.74)
                        ysize 72
                        at ad_gift_error_fade
                        text ad_gift_message:
                            xalign 0.5
                            yalign 0.5
                            text_align 0.5
                            size int(config.screen_height * 0.020) + 10
                            color "#D7D7E0"
                            outlines [(2, "#000000", 0, 0)]
                            font ad_gothic_body_font
                elif ad_gift_show_result:
                    fixed:
                        xalign 0.5
                        ypos int(ad_gift_panel_height * 0.925)
                        xsize int(ad_gift_right_width * 0.74)
                        ysize 72
                        at ad_gift_result_fade
                        text ad_gift_message:
                            xalign 0.5
                            yalign 0.5
                            text_align 0.5
                            size int(config.screen_height * 0.020) + 10
                            color "#D7D7E0"
                            outlines [(2, "#000000", 0, 0)]
                            font ad_gothic_body_font

        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -49
            yoffset 24
            idle Transform(ad_ui_close, size=(122, 122), alpha=0.82)
            hover Transform(ad_ui_close, size=(138, 138), alpha=1.0)
            action [ad_riley_gift_quantity_input.Disable(), SetVariable("ad_gift_is_error", False), SetVariable("ad_gift_show_result", False), SetVariable("ad_gift_message", ""), Hide("ad_gift_notification_screen"), Hide("ad_gifting_input_blocker"), Hide("ad_character_gifting_screen")]
        text "ЗАКРЫТЬ":
            xalign 1.0
            yalign 0.0
            xoffset -49
            yoffset 131
            size 25
            color "#E0E0E4"
            outlines [(1, "#000000", 0, 0)]
            font ad_gothic_body_font
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
