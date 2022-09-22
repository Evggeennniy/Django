from rest_framework.throttling import AnonRateThrottle


class AnonCurrencyThrottle(AnonRateThrottle):
    scope = 'currency'
    # ^ Scope is a group of url work with it throttle class
# Only for anonim users


class AnonSupportsThrottle(AnonRateThrottle):
    scope = 'contactus'
