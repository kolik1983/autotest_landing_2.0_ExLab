import pytest

import settings
from page.landing_page import Landing_Page
import time
from pynput.keyboard import Key, Controller
import allure

keyboard = Controller()

@allure.feature('Page_test')
@allure.story('Проверка загрузки страницы лендинга')
#Проверяем что страница лендинга загрузилась
def test_open_my_page(browser):
    lpage = Landing_Page(browser)
    assert lpage.HEADER_LENDING.is_presented(), 'Лендинг не загрузился, логотип ExLab не отображается'


@allure.feature('Page_test')
@allure.story('Проверка запуска темной темы')
def test_open_black_theme(browser):
    # Проверка, что запущена темная тема, по переключателю который находится в положении включить светлую тему.
    lpage = Landing_Page(browser)
    assert lpage.SWITCH_LIGHT_THEME.is_visible(), 'Сейчас светла тема на сайте'


@allure.feature('Logo_test')
@allure.story('Проверка отображения логотипа ExLab')
def test_logo_exlab(browser):
    lpage = Landing_Page(browser)
    assert lpage.LOGO_PIC_EXLAB.is_visible(),'Логотип отсутствует'


@allure.feature('About_test')
@allure.story('Проверка отображения пункта "О нас" в хедере')
def test_link_about(browser):
    lpage = Landing_Page(browser)
    assert lpage.HEADER_LINK_ABOUT, 'Пункт "О нас" отсутствует'


@allure.feature('About_test')
@allure.story('Проверка перехода по ссылке в пункт страницы О нас')
def test_click_on_the_link_about(browser):
    lpage = Landing_Page(browser)
    lpage.HEADER_LINK_ABOUT.click()
    # lpage.PARAGRAPH_ABOUT.wait_until_not_visible(2)
    assert lpage.PARAGRAPH_ABOUT.is_visible(), 'Выбор элемента не ведет в соответсвующий пункт'


@allure.feature('Project_test')
@allure.story('Проверка отображения пункта "Проекты"')
def test_link_project(browser):
    lpage = Landing_Page(browser)
    assert lpage.HEADER_LINK_PROJECTS.is_visible(), 'Пункт "Проекты" отсутствует'


@allure.feature('Project_test')
@allure.story('Проверка перехода по ссылке в  пункт Проекты')
def test_click_on_the_link_project(browser):
    lpage = Landing_Page(browser)
    lpage.HEADER_LINK_PROJECTS.click()
    assert lpage.PARAGRAPH_PROJECT.is_visible(), 'Пункт "Проекты" отсутствует'


@allure.feature('Mentors_test')
@allure.story('Проверка отображения пункта "Менторы"')
def test_link_mentors(browser):
    lpage = Landing_Page(browser)
    assert lpage.HEADER_LINK_MENTORS.is_visible(), 'Пункт "Менторы" отсутствует'


@allure.feature('Mentors_test')
@allure.story('Проверка перехода в пункт Менторы')
def test_click_on_the_link_mentors(browser):
    lpage = Landing_Page(browser)
    lpage.HEADER_LINK_MENTORS.click()
    assert lpage.PARAGRAPH_MENTORS.is_visible(), 'Переход в пункт  о менторах не осуществился'


@allure.feature('Startup_test')
@allure.story('Проверка отображения пункта "StartUp"')
def test_link_startup(browser):
    lpage = Landing_Page(browser)
    assert lpage.HEADER_LINK_STARTUP.is_visible(), 'Пункт "StartUp" отсутствует'


@allure.feature('Startup_test')
@allure.story('Проверка перехода в пункт "StartUp"')
def test_click_on_the_link_startup(browser):
    lpage = Landing_Page(browser)
    lpage.HEADER_LINK_STARTUP.click()
    assert lpage.PARAGRAPH_STARTUP_FOR.is_visible(), 'Переход в пункт  "StartUp для" не осуществился'


@allure.feature('Sun_icon_test')
@allure.story('Проверка отображения Sun_icon')
def test_visible_sun_icon(browser):
    lpage = Landing_Page(browser)
    assert lpage.SWITCH_LIGHT_THEME.is_visible(), 'Sun icon не отображается'


@allure.feature('Sun_icon_test')
@allure.story('Смены темы с темной на светлую')
def test_change_to_white_theme(browser):
    lpage = Landing_Page(browser)
    lpage.SWITCH_LIGHT_THEME.click()
    assert lpage.LIGHT_THEME.is_visible(), 'Нет перехода не светлую тему'


@allure.feature('Join_button_test')
@allure.story('Отображение кнопки "Присоединится" в хедере')
def test_visible_button_join(browser):
    lpage = Landing_Page(browser)
    assert lpage.JOIN_BUTTON.is_visible(), 'Кнопка "Присоединится" не отображается'


@allure.feature('Join_button_test')
@allure.story('Проверка перехода на страницу регистрации при нажатии на кнопку "Присоединится" в хедере')
def test_click_join_button(browser):
    lpage = Landing_Page(browser)
    lpage.JOIN_BUTTON.click()
    browser.switch_to.window(browser.window_handles[1])
    assert lpage.get_current_url() == settings.REGISTRATION_BOT


@allure.feature('Possibility_block_tests')
@allure.story('Отображение логотипа  ExLab в блоке')
def test_logo_visible_in_block(browser):
    lpage = Landing_Page(browser)
    assert lpage.LOGO_EXLAB.is_visible(), 'Логотип в блоке "Твоя возможность" не отобразился'


@allure.feature('Possibility_block_tests')
@allure.story('Отображение надписи Твоя возможность')
def test_visible_title_possibility(browser):
    lpage = Landing_Page(browser)
    assert lpage.TITLE_POSSIBILITY.is_visible(), 'Нет заголовка "Твоя возможность"'


@allure.feature('Possibility_block_tests')
@allure.story('Отображение текста под надписью Твоя возможность')
def test_visible_text_undo_title(browser):
    lpage = Landing_Page(browser)
    assert lpage.TEXT_UNDO_T.is_visible(), 'Текст под заголовком не виден'


@allure.feature('AboutUs_block_tests')
@allure.story('Отображение надписи О нас')
def test_visible_title_about_us(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_ABOUT.scroll_to_element()
    assert lpage.TITLE_ABOUT.is_visible(), 'Нет заголовка "О нас"'

@allure.feature('AboutUs_block_tests')
@allure.story('Отображение текста под надписью О нас')
def test_visibility_text_undo_title(browser):
    lpage = Landing_Page(browser)
    lpage.TEXT_UNDO_TITLE.scroll_to_element()
    assert lpage.TEXT_UNDO_TITLE.is_visible(),  'Текст под заголовком О нас не виден'


@allure.feature('AboutUs_block_tests')
@allure.story('Отображение надписи Почему ExLab?')
def test_visible_title_whyus(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_WHY.scroll_to_element()
    assert lpage.TITLE_WHY.is_visible(), 'Нет заголова "Почему ExLab?"'


@allure.feature('AboutUs_block_tests')
@allure.story('Отображение текста под надписью Почему ExLab?')
def test_visibility_text_undo_whyus(browser):
    lpage = Landing_Page(browser)
    lpage.TEXT_UNDO_WHY.scroll_to_element()
    assert lpage.TEXT_UNDO_WHY.is_visible(), 'Текст под заголовком "Почему ExLab?" не виден'


@allure.feature('AboutUs_block_tests')
@allure.story('Отображение кнопки [Присоединиться]')
def test_visible_bnt_join(browser):
    lpage = Landing_Page(browser)
    lpage.TEXT_UNDO_WHY.scroll_to_element()
    assert lpage.JOIN_BTN.is_visible(), 'Нет кнопки [Присоединиться]'


@allure.feature('AboutUs_block_tests')
@allure.story('При нажатии на кнопку [Присоединиться] открывается форма регистрации')
def test_btn_join_click(browser):
    lpage = Landing_Page(browser)
    lpage.TEXT_UNDO_WHY.scroll_to_element()
    lpage.JOIN_BTN.click()
    browser.switch_to.window(browser.window_handles[1])
    assert lpage.get_current_url() == settings.REGISTRATION_BOT

@allure.feature('Project_block_tests')
@allure.story('Отображение заголовка Проекты')
def test_visible_title_project(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_PROJECT.scroll_to_element()
    assert lpage.TITLE_PROJECT.is_visible(), 'Нет заголовка Проекты'


@allure.feature('Project_block_tests')
@allure.story('Отображение логотипов ExLab, HealthyLife, Easyhelp в блоке')
def test_visible_logo_all_projects(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_PROJECT.scroll_to_element()
    assert lpage.THREE_LOGO.count() == 3, 'Не все логотипы отобразились'


@allure.feature('Project_block_tests')
@allure.story('Отображение текста под логотипами ExLab, HealthyLife, Easyhelp в блоке')
def test_visible_text_block_projects(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_PROJECT.scroll_to_element()
    assert lpage.THREE_TEXT_BLOCK.count() == 3, 'Не отображаются все тексты блока'


@allure.feature('Mentors_block_tests')
@allure.story('Отображение надписи Менторы')
def test_visible_title_mentors(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_MENTORS.scroll_to_element()
    assert lpage.TITLE_MENTORS.is_visible(), 'Не отобразился зоголовок Менторы'


@allure.feature('Mentors_block_tests')
@allure.story('При нажатии на область ментора , открывается спойлер')
def test_open_area_mentor(browser):
    lpage = Landing_Page(browser)
    lpage.PARAGRAPH_MENTORS.scroll_to_element()
    browser.implicitly_wait(4)
    lpage.CROSS_MENTORS.open_spoilers()
    browser.implicitly_wait(4)
    assert lpage.SPOILERS_MENTOR.count() == 4, 'Не все спойлеры открылись'


@allure.feature('Mentors_block_tests')
@allure.story('При открытом спойлере фотография ментора отображается')
def test_visible_photo_mentor(browser):
    lpage = Landing_Page(browser)
    lpage.PARAGRAPH_MENTORS.scroll_to_element()
    lpage.CROSS_MENTORS.open_spoilers()
    browser.implicitly_wait(2)
    assert lpage.PHOTOS_MENTORS.count() == 4, 'Не все фото менторов не отображаются'


@allure.feature('Mentors_block_tests')
@allure.story('При открытом спойлере отображается информации о менторе')
def test_visible_descriptions_mentor(browser):
    lpage = Landing_Page(browser)
    lpage.PARAGRAPH_MENTORS.scroll_to_element()
    lpage.CROSS_MENTORS.open_spoilers()
    browser.implicitly_wait(3)
    assert lpage.DESCRIPTIONS_MENTORS.count() == 4, 'Описание не всех менторов видно'


@allure.feature('Mentors_block_tests')
@allure.story('При нажатии на область ментора (при развернутом спойлере) спойлер закрывается')
def test_close_spoiler(browser):
    lpage = Landing_Page(browser)
    lpage.PARAGRAPH_MENTORS.scroll_to_element()
    lpage.CROSS_MENTORS.open_spoilers()
    browser.implicitly_wait(5)
    lpage.MINUS_MENTORS.open_spoilers()
    lpage.TITLE_MENTORS.scroll_to_element()
    assert lpage.HIDDEN_AREA.count() == 0, "Не все спойлеры закрылись"


@allure.feature('Startup_block_tests')
@allure.story('Отображение надписи StartUp')
def test_visible_startup_title(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_STARTUP.scroll_to_element()
    assert lpage.TITLE_STARTUP.is_visible(), 'Не видно заголовок блока StartUp'

@allure.feature('Startup_block_tests')
@allure.story('Отображение блока текста под StartUp')
def test_visible_txt_block(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_STARTUP.scroll_to_element()
    assert lpage.TEXT_BLOCK.is_visible(), 'Блок с текстом не отображается'


@allure.feature('Help_block_tests')
@allure.story('Отображение надписи Помочь проекту')
def test_visible_title_help(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_HELP.scroll_to_element()
    assert lpage.TITLE_HELP.is_visible(), 'Надпись Помочь проекту не видна'

@allure.feature('Help_block_tests')
@allure.story('Отображение текста в блоке')
def test_visible_text_help(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_HELP.scroll_to_element()
    assert lpage.TEXT_HELP.is_visible(), 'Текст в блоке Помочь проекту не виден'

@allure.feature('Help_block_tests')
@allure.story('Отображение кнопки Boosty')
def test_visible_btn_boosty(browser):
    lpage = Landing_Page(browser)
    lpage.BTN_BOOSTY.scroll_to_element()
    assert lpage.BTN_BOOSTY.is_visible(), 'Кнопка Boosty не видна'

@allure.feature('Help_block_tests')
@allure.story('-При нажатии на кнопку Boosty открывается страница ExLab на сайте Boosty')
def test_btn_bsty_click(browser):
    lpage = Landing_Page(browser)
    lpage.BTN_BOOSTY.scroll_to_element()
    lpage.BTN_BOOSTY.click()
    browser.switch_to.window(browser.window_handles[1])
    assert lpage.get_current_url() == settings.LINK_EX_BOOSTY, 'Страница не открывается'

@allure.feature('Help_block_tests')
@allure.story('Отображение кнопки Patreon')
def test_visible_btn_patreon(browser):
    lpage = Landing_Page(browser)
    lpage.BTN_PATREON.scroll_to_element()
    assert lpage.BTN_PATREON.is_visible(), 'Кнопка Patreon не видна'

# не настроен переход на патреон
@pytest.mark.xfail
@allure.feature('Help_block_tests')
@allure.story('При нажатии на кнопку Patreon открывается страница ExLab на сайте Patreon')
def test_btn_patreon_click(browser):
    lpage = Landing_Page(browser)
    lpage.BTN_PATREON.scroll_to_element()
    lpage.BTN_PATREON.click()
    browser.switch_to.window(browser.window_handles[1])
    assert lpage.get_current_url() == settings.LINK_EX_BOOSTY, 'Страница не открывается'


@allure.feature('SiT_block_tests')
@allure.story('Отображение надписи Оставайся на связи')
def test_visible_title_SiT(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_SiT.scroll_to_element()
    assert lpage.TITLE_SiT.is_visible(), "Заголовка блока нет"

@allure.feature('SiT_block_tests')
@allure.story('Отображение текста в блоке ')
def test_text_in_block_SiT(browser):
    lpage = Landing_Page(browser)
    lpage.TITLE_SiT.scroll_to_element()
    assert lpage.TEXT_SiT.is_visible(), "Текста блока нет"


@allure.feature('SiT_block_tests')
@allure.story('Отображение логотипа ExLab')
def test_visible_logo_fut(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    assert lpage.LOGO_FUT_EXLAB.is_visible(), "Логотип не отображается"

@allure.feature('SiT_block_tests')
@allure.story('Отображение текста под логотипом ExLab')
def test_visible_text_under_logo(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    assert lpage.TEXT_UNDER_LOGO.is_visible(), "Текст под логотипом не отображается"

@allure.feature('SiT_block_tests')
@allure.story('Отображение ссылки LNKDN')
def test_visible_lnkd(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    assert lpage.LNKD.is_visible(), "Ссылка Линкедин не от ображается"

@allure.feature('SiT_block_tests')
@allure.story('Ссылка ведет  на страницу ExLab в LinkedIn')
def test_link_lnkdn(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    lpage.LNKD.click()
    browser.switch_to.window(browser.window_handles[1])
    assert lpage.get_current_url() == settings.URL_LNKD, 'Страница не открылась'

@allure.feature('SiT_block_tests')
@allure.story('Отображение ссылки INST')
def test_visible_inst(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    assert lpage.INST.is_visible(), "Ссылка Инстаграм не от отображается"

@allure.feature('SiT_block_tests')
@allure.story('Ссылка ведет  на страницу ExLab в Instagram')
def test_link_lnkdn(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    lpage.INST.click()
    browser.switch_to.window(browser.window_handles[1])
    assert lpage.get_current_url() == settings.URL_INST, 'Страница не открылась'

@allure.feature('SiT_block_tests')
@allure.story('Отображение ссылки TLGR')
def test_visible_tlgr(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    assert lpage.TLGR.is_visible(),  "Ссылка Telegram от ображается"

@allure.feature('SiT_block_tests')
@allure.story('Ссылка ведет  на страницу ExLab в Telegram')
def test_link_tlgr(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    lpage.TLGR.click()
    browser.switch_to.window(browser.window_handles[1])
    assert lpage.get_current_url() == settings.URL_TLGR, 'Страница не открылась'

@allure.feature('SiT_block_tests')
@allure.story('Отображение ссылки YTB')
def test_visible_ytb(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    assert lpage.YTB.is_visible(), "Ссылка Youtube не от ображается"

@allure.feature('SiT_block_tests')
@allure.story('Ссылка ведет  на страницу ExLab в YTB')
def test_link_ytb(browser):
    lpage = Landing_Page(browser)
    lpage.LOGO_FUT_EXLAB.scroll_to_element()
    lpage.YTB.click()
    browser.switch_to.window(browser.window_handles[1])
    assert lpage.get_current_url() == settings.URL_YTB, 'Страница не открылась'

@allure.feature('SiT_block_tests')
@allure.story('Отображение ссылки info@exlab.team ')
def test_visible_email(browser):
    lpage = Landing_Page(browser)
    lpage.EMAIL.scroll_to_element()
    assert lpage.EMAIL.is_visible(), "Ссылка email не от отображается"







