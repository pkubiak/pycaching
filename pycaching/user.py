class User:
    """Represent Geocacher instance with provided username and uuid."""
    __slots__ = ('_name', '_uuid')

    URLS = {
        'profile': 'p/default.aspx'
    }

    @property
    def name(self):
        return self._name

    @property
    def uuid(self):
        return self._uuid

    def __init__(self, name, uuid=None, lazy_load_from_code=None):
        if not isinstance(name, str):
            raise ValueError("User name '{}' is not a string.".format(name))

        if not (uuid or lazy_load_from_code):
            raise ValueError("You must provide 'uuid' or 'lazy_load_from_code'")

        if lazy_load_from_code:
            assert lazy_load_from_code.startswith(('GC', 'PR', 'TB'))
        self._name = name.strip()
        self._uuid = uuid.strip() if uuid else None

    @classmethod
    def from_username(cls, geocaching, username):
        #
        res = geocaching._request(cls.URLS['profile'], params={"u": username})
        # print(res.status_code)
        # assert res.status_code == 200

        name = res.find(id="ctl00_ProfileHead_ProfileHeader_lblMemberName").text.strip()

        _, uuid = res.find(id="ctl00_ProfileHead_ProfileHeader_lnkSendMessage")['href'].split('recipientId=')

        return User(name=name, uuid=uuid)

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.name == other.name) and (self.uuid == other.uuid)
        return self.name == other

    def __getattr__(self, key):
        return getattr(self.name, key)

    def __add__(self, other):
        return self.name + other

    def __radd__(self, other):
        return other + self.name

    def __mul__(self, other):
        return self.name * other

    def __rmul__(self, other):
        return other * self.name

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return self.name
