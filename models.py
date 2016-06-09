from google.appengine.ext import ndb


class PhoneBookEntry(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()