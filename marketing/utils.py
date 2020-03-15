from django.conf import settings


MAILCHIMP_API_KEY = getattr(settings, "MAILCHIMP_API_KEY", None)
MAILCHIMP_DATA_CENTER = getattr(settings, "MAILCHIMP_DATA_CENTER", None)
MAILCHIMP_EMAIL_AUDIENCE_ID = getattr(settings, "MAILCHIMP_EMAIL_AUDIENCE_ID", None)


class Mailchimp(object):
    def __init__(self):
        super(Mailchimp, self).__init__()
        self.key = MAILCHIMP_API_KEY
        self.api_url  = 'https://{dc}.api.mailchimp.com/3.0'.format(dc=MAILCHIMP_DATA_CENTER)
        self.audience_id = MAILCHIMP_EMAIL_AUDIENCE_ID
        self.list_endpoint = '{api_url}/audience/{audience_id}'.format(api_url = self.api_url,
                                audience_id=self.audience_id)
    
    def check_subscription_status(self, email):

        return


