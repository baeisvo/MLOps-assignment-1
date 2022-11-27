class variables:
    def __init__(self, env):
        self.env = env
        self.prefix = self._get_prefix(env)
        self.account = self._get_account(env)
        self.pg_host = self._get_host(env)

    def _get_prefix(self, env):
        if env == "dev":
            return "DataStore_dev"
        elif env == "pre-prod"
            return "DataStore_pre-prod"
        elif env =="prod"
            return "DataStore"
        else:
            raise Exception("Unknown env")

    def _get_account(self, env):
        if env == "dev":
            return "123456789"
        elif env == "pre-prod"
            return "123123123"
        elif env =="prod"
            return "100100100"
        else:
            raise Exception("Unknown env")


    def _get_host(self, env):
        if env == "dev":
            return "1.2.3.4"
        elif env == "pre-prod"
            return "5.3.2.1"
        elif env =="prod"
            return "30.52.201.10"
        else:
            raise Exception("Unknown env")


# ENV = "dev"
# prefix = "DataStore"
# account = "123456789"
