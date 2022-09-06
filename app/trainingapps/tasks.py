from celery import shared_task
from django.core.mail import send_mail

from trainingapps import utils
from trainingapps import model_choises as mch

from bs4 import BeautifulSoup


@shared_task
def sending_mail(subject, email_from, email_to):
    email_subject = "Subject Django Project"
    message = f"""
    Subject : {subject}
    Email from : {email_from}
    Wants to contact
    """

    send_mail(
        email_subject,
        message,
        email_from,
        [email_to],
        fail_silently=False,
    )  # ^ Sending messages


@shared_task
def parse_privatbank():
    from trainingapps.models import Rate, Source

    source_name = 'PrivatBank'
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    url_data = utils.get_json_from_url(url)

    permitted_objects = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_EUR,
        'BTC': mch.CurrencyType.CURRENCY_TYPE_BTC,
    }  # ^ Specifying the supported fields

    # try:
    #     source = Source.objects.get(
    #         name=source_name,
    #     )
    # except Source.DoesNotExist:
    #     source = Source.objects.create(
    #         name=source_name,
    #         source_url=url,
    #     )

    # source, created = Source.objects.get_or_create(
    #     name=source_name,
    #     defaults={
    #         'url': url
    #     })

    source = Source.objects.get_or_create(
        name=source_name,
        defaults={'name': source_name, 'source_url': url})[0]
    # ^ Search to name or create to default args

    for rate_data in url_data:
        ccy = rate_data['ccy']
        base_ccy = rate_data['base_ccy']

        # if ccy not in permitted_objects or base_ccy not in permitted_objects:
        #     continue
        # ^ We indicate that if ccy or base_ccy does not match the supported fields, we do not accept it

        if str(ccy) in permitted_objects and str(base_ccy) in permitted_objects:
            pass
        else:
            continue

        buy = utils.to_decimal(rate_data['buy'])
        sell = utils.to_decimal(rate_data['sale'])
        # ^ To decimal type

        try:
            last_value = Rate.objects.filter(
                ccy=ccy,
                base_ccy=base_ccy,
                source=source,
            ).last()
            # ^ Got last value
        except Rate.DoesNotExist:
            last_value = None
        # ^ Filter rate object

        if last_value is None or last_value.sell != sell or last_value.buy != buy:
            Rate.objects.create(
                ccy=ccy,
                base_ccy=base_ccy,
                buy=buy,
                sell=sell,
                source=source,
            )
        else:
            pass


@shared_task
def parse_monobank():
    from trainingapps.models import Rate, Source

    source_name = 'Monobank'
    url = 'https://api.monobank.ua/bank/currency'
    url_data = utils.get_json_from_url(url)

    permitted_objects = {
        '980': mch.CurrencyType.CURRENCY_TYPE_UAH,
        '840': mch.CurrencyType.CURRENCY_TYPE_USD,
        '978': mch.CurrencyType.CURRENCY_TYPE_EUR,
    }

    source = Source.objects.get_or_create(
        name=source_name,
        defaults={'name': source_name, 'source_url': url})[0]

    for rate_data in url_data:
        ccy = str(rate_data['currencyCodeA'])
        base_ccy = str(rate_data['currencyCodeB'])

        if ccy in permitted_objects and base_ccy in permitted_objects:
            pass
        else:
            continue

        ccy = permitted_objects[ccy]
        base_ccy = permitted_objects[base_ccy]
        buy = utils.to_decimal(rate_data['rateBuy'])
        sell = utils.to_decimal(rate_data['rateSell'])

        try:
            last_value = Rate.objects.filter(
                ccy=ccy,
                base_ccy=base_ccy,
                source=source,
            ).last()
        except Rate.DoesNotExist:
            last_value = None

        if last_value is None or last_value.sell != sell or last_value.buy != buy:
            Rate.objects.create(
                ccy=ccy,
                base_ccy=base_ccy,
                buy=buy,
                sell=sell,
                source=source,
            )
        else:
            pass


@shared_task
def parse_vkurseua():
    from trainingapps.models import Rate, Source

    source_name = 'VkurseUA'
    url = 'http://vkurse.dp.ua/course.json'
    url_data = utils.get_json_from_url(url)

    permitted_objects = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'Dollar': mch.CurrencyType.CURRENCY_TYPE_USD,
        'Euro': mch.CurrencyType.CURRENCY_TYPE_EUR,
    }

    source = Source.objects.get_or_create(
        name=source_name,
        defaults={'name': source_name, 'source_url': url})[0]

    for rate_data in url_data:
        ccy = rate_data

        if ccy in permitted_objects:
            pass
        else:
            continue

        ccy = permitted_objects[ccy]
        base_ccy = permitted_objects['UAH']
        buy = utils.to_decimal(url_data[rate_data].get('buy'))
        sell = utils.to_decimal(url_data[rate_data].get('sale'))

        try:
            last_value = Rate.objects.filter(
                ccy=ccy,
                base_ccy=base_ccy,
                source=source,
            ).last()
        except Rate.DoesNotExist:
            last_value = None

        if last_value is None or last_value.sell != sell or last_value.buy != buy:
            Rate.objects.create(
                ccy=ccy,
                base_ccy=base_ccy,
                buy=buy,
                sell=sell,
                source=source,
            )
        else:
            pass


@shared_task
def parse_ukrainekurs():
    from trainingapps.models import Rate, Source

    source_name = 'KursUA'
    url = 'https://kurs.com.ua/'
    url_data = utils.get_txt_from_url(url)

    soup = BeautifulSoup(url_data, 'html5lib')
    # ^ Сreate an object a BeautifulSoup
    raw_table_data = soup.find('tbody', class_='text-right')
    # ^ Select the desired table by search
    raw_names_data = raw_table_data.find_all('a', class_='dotted')
    raw_values_data = raw_table_data.find_all('div', class_='course')
    # ^ Select the necessary data

    ready_names_data = utils.eazyhandler(data=raw_names_data, max_len=2)
    ready_values_data = utils.eazyhandler(data=raw_values_data, cutright=5, max_len=8)
    # ^ Data processing

    url_data = utils.picker_datas_onetofour(ready_names_data, ready_values_data)
    # ^ Data collection

    permitted_objects = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_EUR,
    }

    source = Source.objects.get_or_create(
        name=source_name,
        defaults={'name': source_name, 'source_url': url})[0]

    for rate_data in url_data:
        ccy = rate_data['ccy']

        if ccy in permitted_objects:
            pass
        else:
            continue

        ccy = permitted_objects[ccy]
        base_ccy = permitted_objects['UAH']
        buy = utils.to_decimal(rate_data['buy'])
        sell = utils.to_decimal(rate_data['sale'])

        try:
            last_value = Rate.objects.filter(
                ccy=ccy,
                base_ccy=base_ccy,
                source=source,
            ).last()
        except Rate.DoesNotExist:
            last_value = None

        if last_value is None or last_value.sell != sell or last_value.buy != buy:
            Rate.objects.create(
                ccy=ccy,
                base_ccy=base_ccy,
                buy=buy,
                sell=sell,
                source=source,
            )
        else:
            pass


@shared_task
def parse_financeua():
    from trainingapps.models import Rate, Source

    source_name = 'FinanceUA'
    url = 'https://finance.i.ua/'
    url_data = utils.get_txt_from_url(url)

    soup = BeautifulSoup(url_data, 'html5lib')
    raw_table_data = soup.find('table', class_='table table-data -important')
    raw_names_data = raw_table_data.find_all('th')
    raw_values_data = raw_table_data.find_all('span', class_='value -decrease')

    ready_names_data = utils.eazyhandler(data=raw_names_data, max_len=2)
    ready_values_data = utils.eazyhandler(data=raw_values_data, cutright=5, max_len=4)

    url_data = utils.picker_datas_onetotwo(ready_names_data, ready_values_data)

    permitted_objects = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_EUR,
    }

    source = Source.objects.get_or_create(
        name=source_name,
        defaults={'name': source_name, 'source_url': url})[0]

    for rate_data in url_data:
        ccy = rate_data['ccy']

        if ccy in permitted_objects:
            pass
        else:
            continue

        ccy = permitted_objects[ccy]
        base_ccy = permitted_objects['UAH']
        buy = utils.to_decimal(rate_data['buy'])
        sell = utils.to_decimal(rate_data['sale'])

        try:
            last_value = Rate.objects.filter(
                ccy=ccy,
                base_ccy=base_ccy,
                source=source,
            ).last()
        except Rate.DoesNotExist:
            last_value = None

        if last_value is None or last_value.sell != sell or last_value.buy != buy:
            Rate.objects.create(
                ccy=ccy,
                base_ccy=base_ccy,
                buy=buy,
                sell=sell,
                source=source,
            )
        else:
            pass


@shared_task
def parse_bankcreditdnepr():
    from trainingapps.models import Rate, Source

    source_name = 'BankCreditDnepr'
    url = 'https://creditdnepr.com.ua/currency'
    url_data = utils.get_txt_from_url(url)

    soup = BeautifulSoup(url_data, 'html5lib')
    raw_table_data = soup.find('table')
    raw_names_data = raw_table_data.find_all('td', class_='tx-green tal')
    raw_values_data = raw_table_data.find_all('td', style='text-align: center')

    ready_names_data = utils.eazyhandler(data=raw_names_data, cutright=3, max_len=4)
    ready_values_data = utils.eazyhandler(data=raw_values_data, iftype=float, max_len=8)

    url_data = utils.picker_datas_onetotwo(ready_names_data, ready_values_data)

    permitted_objects = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_EUR,
    }

    source = Source.objects.get_or_create(
        name=source_name,
        defaults={'name': source_name, 'source_url': url})[0]

    for rate_data in url_data:
        ccy = rate_data['ccy']

        if ccy in permitted_objects:
            pass
        else:
            continue

        ccy = permitted_objects[ccy]
        base_ccy = permitted_objects['UAH']
        buy = utils.to_decimal(rate_data['buy'])
        sell = utils.to_decimal(rate_data['sale'])

        try:
            last_value = Rate.objects.filter(
                ccy=ccy,
                base_ccy=base_ccy,
                source=source,
            ).last()
        except Rate.DoesNotExist:
            last_value = None

        if last_value is None or last_value.sell != sell or last_value.buy != buy:
            Rate.objects.create(
                ccy=ccy,
                base_ccy=base_ccy,
                buy=buy,
                sell=sell,
                source=source,
            )
        else:
            pass
