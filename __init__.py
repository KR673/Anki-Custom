from aqt import mw
from aqt import gui_hooks

def init():
    gui_hooks.reviewer_did_show_question.append(init_ease_info)
    gui_hooks.reviewer_did_show_answer.append(init_ease_info)

def init_ease_info(card):
    ease = get_card_ease(card)

    container = """
                      $("#ease-container").remove()
                      $('body').append(`
                            <div id="ease-container">
                                <span>E : </span>
                                <span>%s</span>
                            <div>
                      `)
                      $('head').append(`
                            <style>
                                #ease-container {
                                    text-align: right;
                                    color: #888888;
                                    margin: 10px 0 0 0;
                                }
                            </style>
                      `)
              """ % ease
    mw.reviewer.web.eval(container)

def get_card_ease(card):
    cmd = f"select ease, id, ivl, factor,type from revlog where cid = '{card.id}' ORDER BY id ASC "
    rating_list = mw.col.db.all(cmd)
    ease = 2500
    if len(rating_list) > 0:
        ease = rating_list[-1][3]
    return ease / 10

init()
