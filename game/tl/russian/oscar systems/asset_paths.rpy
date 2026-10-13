


init -100 python:
    def ad_asset_file(directory):
        prefix = directory.rstrip("/") + "/"
        image_extensions = (".png", ".webp", ".jpg", ".jpeg")
        matches = sorted(
        filename for filename in renpy.list_files()
        if filename.startswith(prefix) and filename.lower().endswith(image_extensions)
    )
        if len(matches) != 1:
            raise Exception("Place exactly one image in {}.".format(directory))
        return matches[0]


define ad_ui_background = ad_asset_file("oscar assets/ui/background")
define ad_ui_close = ad_asset_file("oscar assets/ui/close")
define ad_ui_barbed_horizontal = ad_asset_file("oscar assets/ui/barbed_horizontal")
define ad_ui_barbed_vertical = ad_asset_file("oscar assets/ui/barbed_vertical")

define ad_item_flowers = ad_asset_file("oscar assets/items/flowers")
define ad_item_plush_toy = ad_asset_file("oscar assets/items/plush_toy")
define ad_item_chocolates = ad_asset_file("oscar assets/items/chocolates")

define ad_replay_bright_talk = ad_asset_file("oscar assets/replay/bright_talk")
define ad_replay_warehouse_investigation = ad_asset_file("oscar assets/replay/warehouse_investigation")
define ad_replay_first_fight = ad_asset_file("oscar assets/replay/first_fight")
define ad_replay_first_dream = ad_asset_file("oscar assets/replay/first_dream")
define ad_replay_locked = ad_asset_file("oscar assets/replay/locked")

define ad_tamara_work_button_idle = ad_asset_file("oscar assets/tamara_work/button_idle")
define ad_tamara_work_button_hover = ad_asset_file("oscar assets/tamara_work/button_hover")
define ad_tamara_work_greeting_01 = ad_asset_file("oscar assets/tamara_work/greeting_01")
define ad_tamara_work_greeting_02 = ad_asset_file("oscar assets/tamara_work/greeting_02")
define ad_tamara_work_greeting_03 = ad_asset_file("oscar assets/tamara_work/greeting_03")
define ad_tamara_work_greeting_04 = ad_asset_file("oscar assets/tamara_work/greeting_04")
define ad_tamara_work_greeting_05 = ad_asset_file("oscar assets/tamara_work/greeting_05")
define ad_tamara_work_shift = ad_asset_file("oscar assets/tamara_work/shift")

define ad_yuki_store_button_idle = ad_asset_file("oscar assets/yuki_store/button_idle")
define ad_yuki_store_button_hover = ad_asset_file("oscar assets/yuki_store/button_hover")

define ad_freeroam_inventory_button_idle = ad_asset_file("oscar assets/freeroam_inventory/button_idle")
define ad_freeroam_inventory_button_hover = ad_asset_file("oscar assets/freeroam_inventory/button_hover")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
