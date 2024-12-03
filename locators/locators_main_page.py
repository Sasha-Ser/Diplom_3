from selenium.webdriver.common.by import By


class LocatorsMainPage:

    PERSONAL_CABINET_BUTTON = By.XPATH, ".//header/nav/a"  # Кнопка "личный кабинет" на главной
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text() = 'Конструктор']" #Кнопка "Конструктор" в хедере
    ORDER_FEED_BUTTON = By.XPATH, ".//p[text() = 'Лента Заказов']" #Кнопка"Лента Заказов" в хедере
    BUN_FOR_BURGER = By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']" #Булка для бургера "Флюоресцентная булка R2-D3"
    ADD_INFO_CLOSE_BUTTON = By.XPATH, (".//button[@class = 'Modal_modal__close_modified__3V5XS"
                                    " Modal_modal__close__TnseK']") #Кнопка закрывающая окно с информацией
    TITLE_ADD_INFO_WINDOW = By.XPATH, (".//h2[@class = 'Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m "
                                       "text text_type_main-large pl-10']") #Заголовок всплывающего окна с доп. информацией об ингредиенте
    CONSTRUCTOR_BURGER = By.XPATH, ".//span[@class = 'constructor-element__row']" #Элемент куда перетащить ингридиент
    COUNTER_FOR_BUN = By.XPATH, ".//p[@class = 'counter_counter__num__3nue1']" #Счетчик для количества флюоресцентной булки
    CREATE_ORDER_BUTTON = By.XPATH, ".//button[text() = 'Оформить заказ']" #Кнопка "Оформить"заказ
    ID_ORDER = By.XPATH, ("//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m "
                          "text text_type_digits-large mb-8']") #Номер заказа в модальном окне на главной
    CLOSE_INFO_ORDER_BUTTON = By.XPATH, ("//button[@class = 'Modal_modal__close_modified__3V5XS "
                                         "Modal_modal__close__TnseK']") #Кнопка закрытия модального окна с информацией о заказе
    MODAL_WINDOW = By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"