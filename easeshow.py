from aqt import mw
from aqt import gui_hooks


def init():
    gui_hooks.reviewer_did_show_question.append(init_ease_info)
    gui_hooks.reviewer_did_show_answer.append(init_ease_info)


def init_ease_info(card):

    ease = get_card_ease(card)

    color = '#23bbff'
    if ease >= 300:
        color = '#8bc34a'
    elif ease <= 200:
        color = '#ff6358'


    container = """
                      $("#ease-container").remove()
                      $('body').prepend(`
                            <div id="ease-container">
                                <span>E</span><span>%s</span>
                            </div>
                      `)
                      $('head').append(`
                            <style>
                                #ease-container {
                                    text-align: right;
                                    color: #545151;
                                    margin: 0 auto;
                                }
                                #ease-container span:nth-child(1), #ease-container span:nth-child(2) {
                                    background: %s;
                                    padding: 0 3px
                                }
                                #ease-container span:nth-child(1) {
                                    border-right: solid 1px;
                                    border-radius: 3px 0px 0px 3px;
                                }
                                #ease-container span:nth-child(2) {
                                    border-radius: 0px 3px 3px 0;
                                }

                                #ease-container {
                                    font-size: 15px;
                                    font-weight: 600;
                                    margin: 0 auto;
                                    width: 730px;
                                    margin-top: 20px;
                                    margin-bottom: -5px;
                                }
                            </style>
                      `)
              """ % (str(ease), color)
    mw.reviewer.web.eval(container)


def get_card_ease(card):
    cmd = f"select ease, id, ivl, factor,type from revlog where cid = '{card.id}' ORDER BY id ASC "
    rating_list = mw.col.db.all(cmd)
    ease = 2500
    if len(rating_list) > 0:
        ease = rating_list[-1][3]
    return ease // 10
