


init python:
    def restore_cast_count():
        for i in cast_affection_all:
            if not i in store.cast_affection:
                store.cast_affection[i]=0
            if not i in store.cast_event_done:
                store.cast_event_done[i] = 0
        pass

    def add_point(character, point_num = 1):
        store.cast_affection += point_num

    def character_event_done(char_id):
        if not char_id in store.cast_event_done:
            store.cast_event_done[char_id] = 0
        store.cast_event_done[char_id] += 1

    def get_next_char_event(char_id):
        next_event = ""
        if store.cast_event_done[char_id] < len(cast_events[char_id]):
            if int(cast_events[char_id][store.cast_event_done[char_id]][0]) >= store.cast_affection[char_id]:
                store.next_event = cast_events[char_id][store.cast_event_done[char_id]][1]


label example:
    $ get_next_char_event("char 1 id")
    if next_event:
        call expression next_event from _call_expression
    return

default next_event = ""
default cast_affection = {
    "char 1 id":0,
    "char 2 id":0

}
default cast_event_done = {

}

define cast_affection_all = [ 
    "char 1 id",
    "char 2 id"
]

define cast_events = {
    "char 1 id":[
        ("10","affection_example_1"),
        ("20","affection_example_2")
    ],
    "char 2 id":[

    ]
}

default car1_event1_done = False

label affection_example_1:
    "Это первое событие."
    return


label affection_example_2:
    "Это второе событие."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
