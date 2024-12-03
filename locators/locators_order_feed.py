from selenium.webdriver.common.by import By


class LocatorsOrderFeedPage:

    LIST_OF_ORDER = By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']" #Список всех заказов
    ORDER_IN_PROGRESS = By.XPATH, ".//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li"
                                                                        #Заказы в работе
    COUNTER_ORDERS_ALL_TIME = By.XPATH, (".//p[text() = 'Выполнено за все время:']/following-sibling::p[@class="
                                         "'OrderFeed_number__2MbrQ text text_type_digits-large']") #Счетчик заказов за все время
    COUNTER_ORDERS_TODAY = By.XPATH, (".//p[text() = 'Выполнено за сегодня:']/following-sibling::p[@class="
                                         "'OrderFeed_number__2MbrQ text text_type_digits-large']") ##Счетчик заказов за сегодня