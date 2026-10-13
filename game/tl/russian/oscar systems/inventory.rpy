
default ad_inventory = {}
default ad_selected_inventory_item = None

define ad_gothic_heading_font = "oscar assets/fonts/oscar_UnifrakturCook.ttf"
define ad_gothic_body_font = "oscar assets/fonts/oscar_NewRocker.ttf"
define ad_inventory_title_font = "oscar assets/fonts/oscar_MetalMania.ttf"
define ad_inventory_money_font = "oscar assets/fonts/oscar_NewRocker.ttf"

init python:

    def ad_add_item(item_id, amount=1):
        if item_id not in store.ad_items or amount <= 0:
            return False
        store.ad_inventory[item_id] = store.ad_inventory.get(item_id, 0) + amount
        return True

    def ad_remove_item(item_id, amount=1):
        if amount <= 0 or store.ad_inventory.get(item_id, 0) < amount:
            return False
        store.ad_inventory[item_id] -= amount
        if store.ad_inventory[item_id] <= 0:
            del store.ad_inventory[item_id]
        return True

    def ad_item_amount(item_id):
        return store.ad_inventory.get(item_id, 0)


transform ad_item_idle:
    zoom 1.0
    rotate 0
    xoffset 0
    yoffset 0





transform ad_item_hover:
    zoom 1.0
    yoffset 0
    on idle:
        parallel:
            easeout 0.14 zoom 1.0
        parallel:
            easeout 0.14 yoffset 0
    on hover:
        parallel:
            easeout 0.14 zoom 1.075
        parallel:
            easeout 0.14 yoffset -6

transform ad_item_selected:
    zoom 1.075
    xoffset 0
    yoffset -6

transform ad_gothic_screen_open:
    alpha 0.0
    easeout 0.28 alpha 1.0


screen ad_barbed_border(card_width, card_height, edge_size=54, corner_size=96, seam_inset=8):

    fixed:
        xsize card_width
        ysize card_height


        add ad_ui_barbed_horizontal:
            xpos 0
            ypos 0
            xsize card_width
            ysize edge_size
        add Transform(ad_ui_barbed_horizontal, yzoom=-1):
            xpos 0
            ypos card_height - edge_size
            xsize card_width
            ysize edge_size
        add ad_ui_barbed_vertical:
            xpos 0
            ypos 0
            xsize edge_size
            ysize card_height
        add Transform(ad_ui_barbed_vertical, xzoom=-1):
            xpos card_width - edge_size
            ypos 0
            xsize edge_size
            ysize card_height


screen ad_inventory_screen():

    modal True
    zorder 200
    default ad_hovered_item = None
    $ ad_panel_width = int(config.screen_width * 0.92)
    $ ad_header_height = int(config.screen_height * 0.22)
    $ ad_header_card_width = int(ad_panel_width * 0.38)
    $ ad_header_card_height = int(ad_header_height * 0.58)
    $ ad_slot_width = int(config.screen_width * 0.125)
    $ ad_slot_height = ad_slot_width
    $ ad_slot_border_size = int(ad_slot_height * 0.115)
    $ ad_info_height = int(ad_slot_height * 0.285)
    $ ad_grid_spacing = 25


    add Solid("#0101034D")

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

        fixed:
            xalign 0.5
            ypos int(config.screen_height * 0.045)
            xsize ad_panel_width
            ysize ad_header_height

            add Solid("#0A0A118C"):
                xpos int(config.screen_height * 0.030)
                ypos int(config.screen_height * 0.030)
                xsize ad_panel_width - int(config.screen_height * 0.060)
                ysize ad_header_height - int(config.screen_height * 0.060)
            use ad_barbed_border(ad_panel_width, ad_header_height, int(config.screen_height * 0.045), int(config.screen_height * 0.052))

            fixed:
                xpos int(ad_panel_width * 0.06)
                yalign 0.5
                xsize ad_header_card_width
                ysize ad_header_card_height
                add Solid("#0D0D16B8"):
                    xpos int(config.screen_height * 0.022)
                    ypos int(config.screen_height * 0.018)
                    xsize ad_header_card_width - int(config.screen_height * 0.044)
                    ysize ad_header_card_height - int(config.screen_height * 0.036)
                use ad_barbed_border(ad_header_card_width, ad_header_card_height, int(config.screen_height * 0.025), int(config.screen_height * 0.030))

                text "ИНВЕНТАРЬ":
                    xalign 0.5
                    yalign 0.5
                    text_align 0.5
                    size int(config.screen_height * 0.056)
                    color "#F0F0F2"
                    outlines [(2, "#24070B", 1, 1), (1, "#000000", 0, 0)]
                    font ad_inventory_title_font

            fixed:
                xpos int(ad_panel_width * 0.56)
                yalign 0.5
                xsize ad_header_card_width
                ysize ad_header_card_height
                add Solid("#101017A8"):
                    xpos int(config.screen_height * 0.020)
                    ypos int(config.screen_height * 0.017)
                    xsize ad_header_card_width - int(config.screen_height * 0.040)
                    ysize ad_header_card_height - int(config.screen_height * 0.034)
                use ad_barbed_border(ad_header_card_width, ad_header_card_height, int(config.screen_height * 0.026), int(config.screen_height * 0.032))
                text "ДЕНЬГИ  [ad_format_money(ad_money)]":
                    xalign 0.5
                    yalign 0.5
                    text_align 0.5
                    size int(config.screen_height * 0.044) + 15
                    color "#D4D4DB"
                    outlines [(2, "#000000", 1, 1)]
                    font ad_inventory_money_font

        fixed:
            xpos 0
            ypos 0
            xsize config.screen_width
            ysize config.screen_height

            grid 5 2:
                xalign 0.5
                yalign 0.557
                yoffset 62
                spacing ad_grid_spacing

                for item_id in ad_item_order:
                    $ item = ad_items[item_id]
                    fixed:
                        xsize ad_slot_width
                        ysize ad_slot_height + ad_info_height + 5

                        button:
                            xsize ad_slot_width
                            ysize ad_slot_height
                            background None
                            hover_background None
                            selected_background None
                            action (SetVariable("ad_selected_inventory_item", None) if ad_selected_inventory_item == item_id else SetVariable("ad_selected_inventory_item", item_id))
                            focus_mask None
                            selected False
                            hovered SetScreenVariable("ad_hovered_item", item_id)
                            unhovered SetScreenVariable("ad_hovered_item", None)


                            add Solid("#0909109B" if ad_selected_inventory_item == item_id else "#0D0D157C"):
                                xpos ad_slot_border_size
                                ypos ad_slot_border_size
                                xsize ad_slot_width - (ad_slot_border_size * 2)
                                ysize ad_slot_height - (ad_slot_border_size * 2)
                            use ad_barbed_border(ad_slot_width, ad_slot_height, ad_slot_border_size, int(ad_slot_height * 0.145))

                            add item["icon"]:
                                xcenter int(ad_slot_width * 0.5)
                                ycenter int(ad_slot_height * 0.5) + 10
                                xsize (int(ad_slot_height * 0.73) - 43 if item_id == "flowers" else int(ad_slot_height * 0.73) - 33)
                                ysize (int(ad_slot_height * 0.73) - 43 if item_id == "flowers" else int(ad_slot_height * 0.73) - 33)
                                at ad_item_hover

                        fixed:
                            ypos ad_slot_height + 5
                            xsize ad_slot_width
                            ysize ad_info_height
                            add Solid("#0B0B12D8"):
                                xpos 3
                                ypos 3
                                xsize ad_slot_width - 6
                                ysize ad_info_height - 6
                            use ad_barbed_border(ad_slot_width, ad_info_height, int(ad_info_height * 0.18), int(ad_info_height * 0.25))
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing -4
                                text item["name"]:
                                    xalign 0.5
                                    text_align 0.5
                                    size int(config.screen_height * 0.028) - 4
                                    color ("#FFFFFF" if (ad_hovered_item == item_id or ad_selected_inventory_item == item_id) else "#E8E8EC")
                                    outlines [(1, "#000000", 0, 0)]
                                    font ad_gothic_body_font
                                text "ЕСТЬ  x[ad_item_amount(item_id)]":
                                    xalign 0.5
                                    text_align 0.5
                                    size int(config.screen_height * 0.019) - 4
                                    color "#BDBDC7"
                                    outlines [(1, "#000000", 0, 0)]
                                    font ad_gothic_body_font

                for empty_slot in range(7):
                    fixed:
                        xsize ad_slot_width
                        ysize ad_slot_height + ad_info_height + 5
                        fixed:
                            xsize ad_slot_width
                            ysize ad_slot_height
                            add Solid("#0D0D157C"):
                                xpos ad_slot_border_size
                                ypos ad_slot_border_size
                                xsize ad_slot_width - (ad_slot_border_size * 2)
                                ysize ad_slot_height - (ad_slot_border_size * 2)
                            use ad_barbed_border(ad_slot_width, ad_slot_height, ad_slot_border_size, int(ad_slot_height * 0.145))
                            text "X":
                                xalign 0.5
                                yalign 0.5
                                text_align 0.5
                                size int(config.screen_height * 0.055)
                                color "#777782"
                                outlines [(1, "#000000", 0, 0)]
                                font ad_gothic_body_font
                        fixed:
                            ypos ad_slot_height + 5
                            xsize ad_slot_width
                            ysize ad_info_height
                            add Solid("#09090FC2"):
                                xpos 3
                                ypos 3
                                xsize ad_slot_width - 6
                                ysize ad_info_height - 6
                            use ad_barbed_border(ad_slot_width, ad_info_height, int(ad_info_height * 0.18), int(ad_info_height * 0.25))

        fixed:
            xalign 0.5
            ypos int(config.screen_height * 0.955)
            yoffset -160
            xsize ad_panel_width
            ysize int(config.screen_height * 0.045) + 30
            add Solid("#0A0A118C"):
                xpos 3
                ypos 3
                xsize ad_panel_width - 6
                ysize int(config.screen_height * 0.045) + 24
            use ad_barbed_border(ad_panel_width, int(config.screen_height * 0.045) + 30, int(config.screen_height * 0.006), int(config.screen_height * 0.010))

            if ad_selected_inventory_item in ad_items:
                $ selected = ad_items[ad_selected_inventory_item]
                text selected["description"]:
                    xalign 0.5
                    yalign 0.5
                    text_align 0.5
                    size int(config.screen_height * 0.034)
                    color "#DADAE0"
                    outlines [(1, "#000000", 0, 0)]
                    font ad_gothic_body_font
            else:
                text "Выберите предмет для осмотра.":
                    xalign 0.5
                    yalign 0.5
                    text_align 0.5
                    size int(config.screen_height * 0.034)
                    color "#B6B6BF"
                    outlines [(1, "#000000", 0, 0)]
                    font ad_gothic_body_font

        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -31
            yoffset 27
            idle Transform(ad_ui_close, size=(112, 112), alpha=0.88)
            hover Transform(ad_ui_close, size=(130, 130), alpha=1.0)
            action Hide("ad_inventory_screen")

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
