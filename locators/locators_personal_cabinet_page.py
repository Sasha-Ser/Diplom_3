from selenium.webdriver.common.by import By


class LocatorsPersonalCabinet:

    ORDER_HISTORY_BUTTON = By.XPATH, ".//a[text() = 'История заказов']" # Кнопка "История заказов" в личном кабинете
    EXIT_BUTTON = By.XPATH, ".//button[text() = 'Выход']"  # Кнопка "Выход" в личном кабинете
    ORDER_INFO = By.XPATH, ".//li[@class = 'OrderHistory_listItem__2x95r mb-6']" # Информация о заказе в истории заказов
    MODAL_WINDOW_WITH_ORDER = By.XPATH, ".//div[@class = 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"
                                                                    #Модальное окно с заказом в Истории заказов
