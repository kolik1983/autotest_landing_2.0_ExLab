import os

from page.base import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class Landing_Page(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'http://test.exlab.team/'

        super().__init__(web_driver, url)

    # HeadersLocators
    HEADER_LENDING = WebElement(xpath='//div[@id="header"]')
    LOGO_PIC_EXLAB = WebElement(xpath='(//div[@id="logo_mobile"])[1]')
    HEADER_LINK_ABOUT = WebElement(xpath='//a[@data-scroll-to="#about"]')
    HEADER_LINK_PROJECTS = WebElement(xpath='//a[@data-scroll-to="#projects"]')
    SWITCH_LIGHT_THEME = WebElement(xpath='//div[@class="sc-fnykZs fEkGUM"]')
    LIGHT_THEME = WebElement(xpath='//div[@class ="sc-bczRLJ cxdoLY"]')
    PARAGRAPH_ABOUT = WebElement(xpath='//div[@id="about"]')
    PARAGRAPH_PROJECT = WebElement(xpath='//div[@id="projects"]')
    HEADER_LINK_MENTORS = WebElement(xpath='//a[@data-scroll-to="#mentors"]')
    PARAGRAPH_MENTORS = WebElement(xpath='//div[@id="mentors"]')
    HEADER_LINK_STARTUP = WebElement(xpath='//a[@href="#startup"]')
    PARAGRAPH_STARTUP_FOR = WebElement(xpath='//div[@id="startup-title-wrapper"]/div')
    JOIN_BUTTON = WebElement(xpath='//div[@class="sc-hAZoDl hrEelO"]')

    # PossibilityBlock
    LOGO_EXLAB = WebElement(xpath='//img[@class="sc-idiyUo gJxphU"]')
    TITLE_POSSIBILITY = WebElement(xpath='//div[@class="sc-dmRaPn ljhwJa"]')
    TEXT_UNDO_T = WebElement(xpath='//div[@class="sc-kgflAQ gUFAgN"]')

    # AboutUsBlock
    TITLE_ABOUT = WebElement(xpath='//div[@class="sc-ikZpkk fAmEjI"]/div[1]')
    TEXT_UNDO_TITLE = WebElement(xpath='//p[@class="sc-himrzO bgsrpw"]')
    TITLE_WHY = WebElement(xpath='//div[@class="sc-ciZhAO fBFmnR"]')
    TEXT_UNDO_WHY = WebElement(xpath='//ol[@class="sc-bZnhIo fYGDkJ"]')
    JOIN_BTN = WebElement(xpath='//div[@class="sc-jdAMXn gLqyEH"]/a')

    # ProjectBlock
    TITLE_PROJECT = WebElement(xpath='//div[@id="projects"]/div[1]')
    PIC_EXLAB = WebElement(xpath='//img[@alt="ExLab"]')
    PIC_HL = WebElement(xpath='//img[@alt="Healthy life "]')
    PIC_EH = WebElement(xpath='//img[@alt="Easyhelp "]')
    THREE_LOGO = ManyWebElements(xpath='//img[@class="sc-jOrMOR eGXkMj"]')
    THREE_TEXT_BLOCK = ManyWebElements(xpath='//p[@class="sc-dPyBCJ elZmsx"]')

    # MentorsBlock
    TITLE_MENTORS = ManyWebElements(xpath='//div[@id="mentors"]/div[1]')
    CROSS_MENTORS = ManyWebElements(xpath='//span[@class="sc-eKBdFk cFcyNJ"]')
    MINUS_MENTORS = ManyWebElements(xpath='//span[@class="sc-eKBdFk gGHWQo"]')
    NAME_MENTORS = ManyWebElements(xpath='//div[@class="sc-jIAOiI eSpxWu"]')
    SPOILERS_MENTOR = ManyWebElements(xpath='//div[@class="sc-bUbCnL fJhsUc"]')
    PHOTOS_MENTORS = ManyWebElements(xpath='//img[@class="sc-kIKDeO oyXhj"]')
    DESCRIPTIONS_MENTORS = ManyWebElements(xpath='//ul[@class="sc-dsQDmV iZMcmm"]')
    CLOSE_AREA = WebElement(xpath='//div[@class="sc-ZyCDH kgnDMn"]')
    HIDDEN_AREA = ManyWebElements(xpath='//div[@class="sc-bUbCnL fJhsUc"]')

    # StartUpBlock
    TITLE_STARTUP = WebElement(xpath='//div[@class="sc-iNWwEs eMChwx"]/div[1]')
    TEXT_BLOCK = WebElement(xpath='//div[@class="sc-lbxAil bXZnGi"]')

    # HelpPjtBlock
    TITLE_HELP = WebElement(xpath='//div[@class="sc-jTYCaT coDMnK"]')
    TEXT_HELP = WebElement(xpath='//div[@class="sc-fctJkW gfwicC"]')
    BTN_BOOSTY = WebElement(xpath='//a[@href="https://boosty.to/exlab_startup"]')
    BTN_PATREON = WebElement(xpath='//a[@class="sc-hKMtZM etdNbW"]')

    # SiTBlock
    TITLE_SiT = WebElement(xpath='//div[@class="sc-bhVIhj uaVnA"]')
    TEXT_SiT = WebElement(xpath='//div[@class="sc-eGAhfa cacMWv"]')

    # FutterBlock
    LOGO_FUT_EXLAB = WebElement(xpath='//div[@class="sc-fIavCj fEzmxG"]')
    TEXT_UNDER_LOGO = WebElement(xpath='//div[@class="sc-gITdmR hYaavu"]')
    LNKD = WebElement(xpath='//a[@href="https://www.linkedin.com/company/exlab-start-up/mycompany/"]')
    INST = WebElement(xpath='//a[@href="https://www.instagram.com/exlab_startup/"]')
    TLGR = WebElement(xpath='//a[@href="https://t.me/ExLabChannel"]')
    YTB = WebElement(xpath='//a[@href="https://www.youtube.com/channel/UC-TAnVYVN7qg5dgsYQJkuvA"]')
    EMAIL = WebElement(xpath='//a[@href="mailto:info@exlab.team"]')
