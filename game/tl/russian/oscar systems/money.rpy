



default ad_money = 0

init python:

    def ad_add_money(amount):
        if amount <= 0:
            return False
        store.ad_money += amount
        return True

    def ad_spend_money(amount):
        if amount <= 0 or store.ad_money < amount:
            return False
        store.ad_money -= amount
        return True

    def ad_has_money(amount):
        return store.ad_money >= amount

    def ad_format_money(amount):
        return "$" + str(int(amount))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
