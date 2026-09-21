init python:

    def unlock_event(person_obj, title, label_name):
        if not hasattr(person_obj, 'completed_events'):
            person_obj.completed_events = []
        
        event_tuple = (title, label_name)
        
        if event_tuple not in person_obj.completed_events:
            person_obj.completed_events.append(event_tuple)
            
            renpy.retain_after_load() 


    def get_neighbor(current_person, direction=1):
        people = get_people()
        try:
            idx = people.index(current_person)
        except ValueError:
            return people[0]
        return people[(idx + direction) % len(people)]

    def get_people():
        return [Yuki, Izra, June, Mei, Autumn, Nora, Lily, 
            Grace, Brooklyn, Riley, Tamara, Zara, Yejin, 
            Jordyn, Kyra, Parker, Utami]


define config.developer = True

init python:
    def get_neighbor(current_person, direction=1):
        people = get_people()
        
        try:
            idx = people.index(current_person)
        except ValueError:
            return people[0]
        
        
        new_idx = (idx + direction) % len(people)
        return people[new_idx]
    class person:
        def __init__(self, name, image, thumb):
            self.name = name
            self.image = image
            self.thumb = thumb
            self.affection = 0
            self.lust = 0
            self.quest = "Продвинуться по сюжету."
            self.completed_events = []

    class quest_handler:
        def __init__(self, pages):
            self.pages = pages




default Yuki = person("Юки", "yuki_gallery", "yuki_gallery_thumb")
default Izra = person("Изра", "izra_gallery", "izra_gallery_thumb")
default June = person("Джун", "june_gallery", "june_gallery_thumb")
default Mei = person("Мэй", "mei_gallery", "mei_gallery_thumb")
default Autumn = person("Отэм", "autumn_gallery", "autumn_gallery_thumb")
default Nora = person("Нора", "nora_gallery", "nora_gallery_thumb")
default Lily = person("Лили", "lily_gallery", "lily_gallery_thumb")
default Grace = person("Грейс", "grace_gallery", "grace_gallery_thumb")
default Brooklyn = person("Бруклин", "brooklyn_gallery", "brooklyn_gallery_thumb")
default Riley = person("Райли", "riley_gallery", "riley_gallery_thumb")
default Tamara = person("Тамара", "tamara_gallery", "tamara_gallery_thumb")
default Zara = person("Зара", "zara_gallery", "zara_gallery_thumb")
default Yejin = person("Йеджин", "yejin_gallery", "yejin_gallery_thumb")
default Jordyn = person("Джордин", "jordyn_gallery", "jordyn_gallery_thumb")
default Kyra = person("Кайра", "kyra_gallery", "kyra_gallery_thumb")
default Parker = person("Паркер", "parker_gallery", "parker_gallery_thumb")
default Utami = person("Утами", "utami_gallery", "utami_gallery_thumb")


default quests = quest_handler(
    [
        Autumn, Brooklyn, Grace, Izra,
        Jordyn, June, Kyra, Lily,
        Mei, Nora, Parker, Riley,
        Tamara, Utami, Yejin, Yuki, Zara
    ]
)




init python:
    def get_people():
        
        return [
        Autumn, Brooklyn, Grace, Izra,
        Jordyn, June, Kyra, Lily,
        Mei, Nora, Parker, Riley,
        Tamara, Utami, Yejin, Yuki, Zara
    ]

    def refresh_quests():
        
        quests.pages = list(get_people())


label after_load:
    python:

        for person_item in get_people():
            
            if not hasattr(person_item, 'completed_events'):
                person_item.completed_events = []
            
            
            if not hasattr(person_item, 'quest'):
                person_item.quest = "Нет активного задания."
            
            
            setattr(person_item, 'completed_events', person_item.completed_events)

    $ refresh_quests()
    return








style quest_text:
    size 200
    xalign 1.0
    font "NotoSansDisplay-ExtraBold.ttf"
    outlines [(16, "#000000", 0, 0)]




screen quests(g=quests):
    tag menu
    add "game_menu.png"
    use game_menu(_("Задания"), scroll="viewport"):
        hbox:
            align (0.5, 0.5)
            box_wrap True

            for i in get_people():
                button:
                    vbox:
                        add i.thumb xalign .5
                        text "[i.name]" xalign .5
                    action Show("character_page", g = i)

screen character_page(g=Yuki):
    style_prefix "quest" tag menu

    add "quest"
    add g.image align (0.0, 1.0)



    imagebutton:
        idle "questleft.png"
        hover im.MatrixColor("questleft.png", im.matrix.brightness(0.12))
        action Show("character_page", g=get_neighbor(g, direction=-1))
        align (0.001, 0.5)


    imagebutton:
        idle "questright.png"
        hover im.MatrixColor("questright.png", im.matrix.brightness(0.12))
        action Show("character_page", g=get_neighbor(g, direction=1))
        align (0.98, 0.5)


    frame:
        xalign 1.0
        yfill True
        vbox:
            xalign .5
            spacing -40
            text g.name size 400
            text "Симпатия: [g.affection]"
            text "Возбуждение: [g.lust]"

        imagebutton:
            idle "gui/eventreplay_idle.png"
            hover "gui/eventreplay_hover.png"
            action Show("event_replay", g=g)
            xalign 0.5
            yalign 0.5
        vbox:
            align (.6, 0.9)
            yoffset -50
            spacing -75
            text "Задание" size 400 xalign 0.5
            if g.quest:
                text "[g.quest]" xalign 0.5
            else:
                text "Нет задания." xalign 0.5


    button:
        text "Назад"
        action ShowMenu("quests")




label quest_example:
    "Давай дадим задание Юки."
    $ Yuki.quest = "Поговорить с Джун в классе утром."

    $ renpy.restart_interaction()
    "Теперь проверь её страницу заданий."
    return
return
