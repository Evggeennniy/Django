from django.core.management.base import BaseCommand
from datetime import date, timedelta
from trainingapps.utils import get_json_from_url, to_datetime
from trainingapps.models import Rate, Source
from . import utils
from time import sleep


class Command(BaseCommand):
    help = 'Closes the specified poll for voting' # NOQA

    LAST_OPERATION_DATE = date.today()

    def add_arguments(self, parser) -> None:
        # Add launch parameter
        parser.add_argument('-l', '--launch', type=str, help='Launch options.')

    def handle(self, *args, **options):
        # Get options
        self.options_handler(options)

        # Run module
        try:
            self.parser_privatbank_archive(self.LAST_OPERATION_DATE)
        except KeyboardInterrupt:
            self.pause_or_stopped()
        except:  # NOQA
            self.timeout_and_reload()

    def options_handler(self, options: dict):
        """
        Input parameter handler
        """
        launch_arg = options.get('launch', None)

        if launch_arg is not None:
            self.LAST_OPERATION_DATE = to_datetime(launch_arg)

    def timeout_and_reload(self, timeout: float = 3.0):
        """
        Timeout before reload module
        """
        sleep(timeout)

        self.handle()

    def pause_or_stopped(self):
        """
        Pause module menu
        """
        command = input(' *PAUSE* Waiting for a command. \'p\' is proceed proccess, \'s\' is stopped module. \n')
        if command == 'p':
            self.handle()
        elif command == 's':
            pass
        else:
            self.pause_or_stopped()

    # def get_last_date_archive(self) -> date:
    #     """
    #     Quite slow, but does its job well,
    #     the call is only passed in the launch='lastdate' value.
    #     """
    #     breakpoint()
    #     queryset_worker = Rate.objects.filter(
    #         source=Source.objects.get(name='PrivatBank'),
    #         module_that_processed='CommandWorker')
    #     queryset_worker_sorted = queryset_worker.order_by('created')
    #     last_value = queryset_worker_sorted.last()

    #     return last_value

    def parser_privatbank_archive(
            self,
            datestart: date = date.today(),
            max_failure: int = 3,
            permitted_objects: list = utils.default_currency_objects):

        """
        Function for collecting PrivatBank archive data
        Failure is be equal empty dataset in getting
        """

        attempts_left = max_failure

        while attempts_left > 0:
            # Anti - throttle request
            sleep(3)

            # Formation of url
            url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date={0}.{1}.{2}'
            url = url.format(datestart.day, datestart.month, datestart.year)

            # Receiving the information Json
            ratejson = get_json_from_url(url)
            ratedata = ratejson['exchangeRate']  # Currency data

            # Skip if empty data
            if not ratedata:
                attempts_left -= 1
                continue

            # Formation of a valid date, receipt of the source
            str_date = ratejson['date']  # Save last date
            datetime = to_datetime(strdate=str_date)
            source = Source.objects.get(name='PrivatBank')

            # Collecting data
            for rate in ratedata:
                base_ccy = rate.get('baseCurrency')
                ccy = rate.get('currency', None)
                nbu_sell = rate.get('saleRateNB')

                # Skip check, skip identical data UAH-UAH
                if ccy in permitted_objects and ccy != base_ccy:
                    # Creating
                    Rate.objects.create(
                        ccy=ccy,
                        buy=0.00,
                        sell=0.00,
                        nbu_sell=nbu_sell,
                        source=source,
                        created=datetime,
                        module_that_processed='CommandWorker'
                    )

            # After the code passes the body of the function without raising an exception
            datestart -= timedelta(days=1)
            self.LAST_OPERATION_DATE -= timedelta(days=1)
