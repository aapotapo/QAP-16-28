from pages.main import MainPage
import pytest


@pytest.mark.location
def test_location(web_browser):
    """Проверка возможности изменения региона"""
    page = MainPage(web_browser)
    page.location.click()
    page.location_input.send_keys("Ульяновск")
    page.first_element_in_location.click()
    page.wait_page_loaded(3)

    assert page.location.get_text() == "Ульяновск"


@pytest.mark.pages
def test_top_fashion_page(web_browser):
    """Проверка ссылки на страницу TOP Fashion"""
    page = MainPage(web_browser)
    page.top_fashion.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/highlight/top-fashion/' in page.get_current_url()


@pytest.mark.pages
def test_premium_page(web_browser):
    """Проверка ссылки на страницу Premium"""
    page = MainPage(web_browser)
    page.premium.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/highlight/premium/' in page.get_current_url()


@pytest.mark.pages
def test_ozon_card_page(web_browser):
    """Проверка ссылки на страницу Ozon Card"""
    page = MainPage(web_browser)
    page.ozon_card.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/context/detail/id/149074294/' in page.get_current_url()


@pytest.mark.pages
def test_live_page(web_browser):
    """Проверка ссылки на страницу Live"""
    page = MainPage(web_browser)
    page.live.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/live/' in page.get_current_url()


@pytest.mark.pages
def test_sale_page(web_browser):
    """Проверка ссылки на страницу Акции"""
    page = MainPage(web_browser)
    page.sale.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/info/actions/' in page.get_current_url()
    assert page.h1.get_text() == 'Акции и спецпредложения'


@pytest.mark.pages
def test_brands_page(web_browser):
    """Проверка ссылки на страницу Бренды"""
    page = MainPage(web_browser)
    page.brands.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/brand/' in page.get_current_url()
    assert page.h1.get_text() == 'Все бренды'


@pytest.mark.pages
def test_seller_page(web_browser):
    """Проверка ссылки на страницу Магазины"""
    page = MainPage(web_browser)
    page.seller.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/seller/' in page.get_current_url()


@pytest.mark.pages
def test_certificates_menu_page(web_browser):
    """Проверка ссылки на страницу Сертификаты"""
    page = MainPage(web_browser)
    page.certificates_menu.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/context/detail/id/135382627/?perehod=menu' in page.get_current_url()
    assert page.h1.get_text() == 'Электронный подарочный сертификат Миллион подарков'


@pytest.mark.pages
def test_electronics_page(web_browser):
    """Проверка ссылки на страницу Электроника"""
    page = MainPage(web_browser)
    page.electronics.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/category/elektronika-15500/' in page.get_current_url()
    assert page.h1.get_text() == 'Электроника'


@pytest.mark.pages
def test_main_apparel_page(web_browser):
    """Проверка ссылки на страницу Одежда и обувь"""
    page = MainPage(web_browser)
    page.main_apparel.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/info/main-apparel/' in page.get_current_url()


@pytest.mark.pages
def test_for_kids_page(web_browser):
    """Проверка ссылки на страницу Детские товары"""
    page = MainPage(web_browser)
    page.for_kids.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/category/detskie-tovary-7000/' in page.get_current_url()
    assert page.h1.get_text() == 'Детские товары'


@pytest.mark.pages
def test_garden_page(web_browser):
    """Проверка ссылки на страницу Дом и сад"""
    page = MainPage(web_browser)
    page.garden.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/category/dom-i-sad-14500/' in page.get_current_url()
    assert page.h1.get_text() == 'Дом и сад'


@pytest.mark.pages
def test_business_page(web_browser):
    """Проверка ссылки на страницу Покупайте как юрлицо"""
    page = MainPage(web_browser)
    page.business.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/business/?perehod=header' in page.get_current_url()


@pytest.mark.pages
def test_appspromo_page(web_browser):
    """Проверка ссылки на страницу Мобильное приложение"""
    page = MainPage(web_browser)
    page.appspromo.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/info/appspromo/' in page.get_current_url()
    assert page.h2.get_text() == 'OZON ещё лучше в приложении'


@pytest.mark.pages
def test_referral_page(web_browser):
    """Проверка ссылки на страницу Реферальная программа"""
    page = MainPage(web_browser)
    page.referral.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/referral/?perehod=header' in page.get_current_url()


@pytest.mark.pages
def test_catalog_electric_page(web_browser):
    """Проверка ссылки на страницу Зарабатывайте с Ozon"""
    page = MainPage(web_browser)
    page.make_money_with_us.click()
    page.wait_page_loaded(3)

    assert 'https://business.ozon.ru/?perehod=header' in page.get_current_url()
    assert page.h1.get_text() == 'Развивайте бизнес и зарабатывайте вместе с нами'


@pytest.mark.pages
def test_certificates_header_page(web_browser):
    """Проверка ссылки на страницу Подарочные сертификаты"""
    page = MainPage(web_browser)
    page.certificates_header.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/context/detail/id/135382627/?perehod=header' in page.get_current_url()
    assert page.h1.get_text() == 'Электронный подарочный сертификат Миллион подарков (3000)'


@pytest.mark.pages
def test_desks_map_page(web_browser):
    """Проверка ссылки на страницу Пункты выдачи"""
    page = MainPage(web_browser)
    page.desks_map.click()
    page.wait_page_loaded(3)

    assert "- пункты выдачи заказов OZON" in page.h1.get_text()


@pytest.mark.pages
def test_postamat_page(web_browser):
    """Проверка ссылки на страницу Постаматы"""
    page = MainPage(web_browser)
    page.postamat.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/postamat/' in page.get_current_url()
    assert page.h2.get_text() == 'Особый вид доставки!'


@pytest.mark.pages
def test_help_page(web_browser):
    """Проверка ссылки на страницу Помощь"""
    page = MainPage(web_browser)
    page.help.click()
    page.wait_page_loaded(3)

    assert 'https://docs.ozon.ru/common/' in page.get_current_url()


@pytest.mark.pages
def test_free_delivery_page(web_browser):
    """Проверка ссылки на страницу Бесплатная доставка"""
    page = MainPage(web_browser)
    page.free_delivery.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/my/deliveryPriceInfo' in page.get_current_url()
    assert page.h2.get_text() == 'Стоимость доставки'


@pytest.mark.pages
def test_ozon_travel_page(web_browser):
    """Проверка ссылки на страницу Ozon Travel"""
    page = MainPage(web_browser)
    page.ozon_travel.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/travel/?perehod=ozon_menu_header' in page.get_current_url()
    assert page.h1.get_text() == 'Поиск дешёвых авиабилетов'


@pytest.mark.pages
def test_discount_page(web_browser):
    """Проверка ссылки на страницу Dисконт"""
    page = MainPage(web_browser)
    page.discount.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/highlight/discount/' in page.get_current_url()


@pytest.mark.pages
def test_order_list_page(web_browser):
    """Проверка ссылки на страницу Заказы"""
    page = MainPage(web_browser)
    page.order_list.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/my/orderlist' in page.get_current_url()


@pytest.mark.pages
def test_favorites_page(web_browser):
    """Проверка ссылки на страницу Избранное"""
    page = MainPage(web_browser)
    page.favorites.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/my/favorites' in page.get_current_url()


@pytest.mark.pages
def test_cart_page(web_browser):
    """Проверка ссылки на страницу Корзина"""
    page = MainPage(web_browser)
    page.cart.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/cart' in page.get_current_url()


@pytest.mark.pages
def test_catalog_menu_open(web_browser):
    """Проверка открытия меню Каталог и перехода по ссылке Смартфоны"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.catalog_smartphones.click()
    page.wait_page_loaded(3)

    assert 'https://www.ozon.ru/category/smartfony-15502/' in page.get_current_url()
    assert page.h1.get_text() == 'Смартфоны'


@pytest.mark.sort
def test_check_sort_by_price_low_to_high(web_browser):
    """Проверка поиска и сортировки по цене по возрастанию"""

    page = MainPage(web_browser)
    page.search_input.send_keys("кондиционер")
    page.search_btn.click()
    page.wait_page_loaded()
    page.sort.click()
    page.sort_by_price_low_to_high.click()
    page.wait_page_loaded()

    prices = page.products_prices.get_text()
    prices = [float(p.split('\u202f')[0]) for p in prices]

    assert prices[0] < prices[-1]


@pytest.mark.sort
def test_check_sort_by_price_high_to_low(web_browser):
    """Проверка поиска и сортировки по цене по убыванию"""

    page = MainPage(web_browser)
    page.search_input.send_keys("футболка")
    page.search_btn.click()
    page.wait_page_loaded()
    page.sort.click()
    page.sort_by_price_high_to_low.click()
    page.wait_page_loaded()

    prices = page.products_prices.get_text()
    prices = [float(p.split('\u202f')[0]) for p in prices]

    assert prices[0] > prices[-1]


@pytest.mark.sort
def test_check_sort_by_popularity(web_browser):
    """Проверка поиска и сортировки по популярности"""

    page = MainPage(web_browser)
    page.search_input.send_keys("телефон")
    page.search_btn.click()
    page.wait_page_loaded()
    page.sort.click()
    page.sort_by_popular.click()
    page.wait_page_loaded()

    assert page.products_prices.count() > 0


@pytest.mark.sort
def test_check_sort_by_discount(web_browser):
    """Проверка поиска и сортировки по размеру скидкм"""

    page = MainPage(web_browser)
    page.search_input.send_keys("фен")
    page.search_btn.click()
    page.wait_page_loaded()
    page.sort.click()
    page.sort_by_discount.click()
    page.wait_page_loaded()

    discounts = page.products_discounts.get_text()
    discounts = [float(p[1:-1]) for p in discounts]

    assert discounts[0] > discounts[-1]


@pytest.mark.sort
def test_check_sort_by_rating(web_browser):
    """Проверка поиска и сортировки по рейтингу"""

    page = MainPage(web_browser)
    page.search_input.send_keys("телевизор")
    page.search_btn.click()
    page.wait_page_loaded()
    page.sort.click()
    page.sort_by_rating.click()
    page.wait_page_loaded()

    assert page.products_prices.count() > 0


@pytest.mark.sort
def test_check_sort_by_new(web_browser):
    """Проверка поиска и сортировки по новизне"""

    page = MainPage(web_browser)
    page.search_input.send_keys("стол")
    page.search_btn.click()
    page.wait_page_loaded()
    page.sort.click()
    page.sort_by_new.click()
    page.wait_page_loaded()

    assert page.products.count() > 0


@pytest.mark.search
def test_check_search(web_browser):
    """Проверка поиска"""
    page = MainPage(web_browser)
    page.search_input.send_keys('iPhone 12')
    page.search_btn.click()

    assert page.products_titles.count() > 0

    for title in page.products_titles.get_text():
        assert 'iphone' in title.lower()


@pytest.mark.search
def test_check_search_with_wrong_layout(web_browser):
    """Проверка поиска с ошибочной раскладкой клавиатуры"""
    page = MainPage(web_browser)
    # "смартфон" в английской раскладке
    page.search_input.send_keys("cvfhnajy")
    page.search_btn.click()

    assert page.products_titles.count() > 0

    for title in page.products_titles.get_text():
        assert 'смартфон' in title.lower()


@pytest.mark.search
def test_check_search_with_misprint(web_browser):
    """Проверка поиска с ошибкой в набраном слове"""
    page = MainPage(web_browser)
    page.search_input.send_keys("смртфно")
    page.search_btn.click()

    assert page.products_titles.count() > 0

    for title in page.products_titles.get_text():
        assert 'смартфон' in title.lower()


@pytest.mark.search
def test_check_search_not_found(web_browser):
    """Проверка поиска несуществующего товара"""
    page = MainPage(web_browser)
    page.search_input.send_keys("dplhs;yt")
    page.search_btn.click()

    assert page.products_titles.count() < 1
    assert page.search_not_found.get_text() == 'Простите, по вашему запросу товаров сейчас нет.'


@pytest.mark.footer
def test_seller_footer_page(web_browser):
    """Проверка ссылки на страницу Ваши товары на Ozon"""
    page = MainPage(web_browser)
    page.first_line_footer[0].click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://seller.ozon.ru' in page.get_current_url()


@pytest.mark.footer
def test_referral_footer_page(web_browser):
    """Проверка ссылки на страницу Реферальная программа в футере"""
    page = MainPage(web_browser)
    page.second_line_footer[0].click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://www.ozon.ru/manager/?perehod=footer' in page.get_current_url()


@pytest.mark.footer
def test_ozon_box_footer_page(web_browser):
    """Проверка ссылки на страницу Установите постамат Ozon Box в футере"""
    page = MainPage(web_browser)
    page.third_line_footer[0].click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://www.ozon.ru/ozon-box/' in page.get_current_url()


@pytest.mark.footer
def test_ozon_business_partner_footer_page(web_browser):
    """Проверка ссылки на страницу Откройте пункт выдачи Ozon в футере"""
    page = MainPage(web_browser)
    page.ozon_business_partner_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://business.ozon.ru/partners?perehod=footer' in page.get_current_url()


@pytest.mark.footer
def test_ozon_business_footer_page(web_browser):
    """Проверка ссылки на страницу Стать Поставщиком Ozon в футере"""
    page = MainPage(web_browser)
    page.ozon_business_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://business.ozon.ru/?perehod=footer' in page.get_current_url()


@pytest.mark.footer
def test_what_to_sell_footer_page(web_browser):
    """Проверка ссылки на страницу Что продавать на Ozon в футере"""
    page = MainPage(web_browser)
    page.what_to_sell_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://seller.ozon.ru/what_to_sell?perehod=footer' in page.get_current_url()


@pytest.mark.footer
def test_what_to_sell_footer_page(web_browser):
    """Проверка ссылки на страницу Что продавать на Ozon в футере"""
    page = MainPage(web_browser)
    page.what_to_sell_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://seller.ozon.ru/what_to_sell?perehod=footer' in page.get_current_url()


@pytest.mark.footer
def test_what_to_sell_footer_page(web_browser):
    """Проверка ссылки на страницу Ecommerce Online School в футере"""
    page = MainPage(web_browser)
    page.ecomschool_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://www.ozon.ru/info/ecomschool' in page.get_current_url()


@pytest.mark.footer
def test_vk_footer(web_browser):
    """Проверка ссылки на страницу Ozon в vk.com"""
    page = MainPage(web_browser)
    page.vk_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://vk.com/ozon' in page.get_current_url()


@pytest.mark.footer
def test_facebook_footer(web_browser):
    """Проверка ссылки на страницу Ozon в Facebook"""
    page = MainPage(web_browser)
    page.facebook_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://www.facebook.com/ozon.ru' in page.get_current_url()


@pytest.mark.footer
def test_twitter_footer(web_browser):
    """Проверка ссылки на страницу Ozon в Twitter"""
    page = MainPage(web_browser)
    page.social_networks_footer[2].click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://twitter.com/Ozon_ru' in page.get_current_url()


@pytest.mark.footer
def test_instagram_footer(web_browser):
    """Проверка ссылки на страницу Ozon в Instagram"""
    page = MainPage(web_browser)
    page.social_networks_footer[3].click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://www.instagram.com/ozonru' in page.get_current_url()
