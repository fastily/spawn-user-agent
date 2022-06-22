class SpawnUserAgent:

    _GENERAL_TOKEN: str = "Mozilla/5.0"
    _WINDOWS: str = "Windows NT 10.0; Win64; x64"
    _MAC_PREFIX: str = "Macintosh; Intel Mac OS X"

    @staticmethod
    def firefox():
        return [f"{SpawnUserAgent._GENERAL_TOKEN} ({platform}; rv:{version}.0) Gecko/20100101 Firefox/{version}.0" for platform in (f"{SpawnUserAgent._MAC_PREFIX} 10.15", SpawnUserAgent._WINDOWS) for version in range(100, 102)]

    @staticmethod
    def chrome():
        return [f"{SpawnUserAgent._GENERAL_TOKEN} ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36" for platform in (f"{SpawnUserAgent._MAC_PREFIX} 10_15_7", SpawnUserAgent._WINDOWS, "X11; Linux x86_64") for version in range(100, 104)]

    @staticmethod
    def safari():
        return [f"{SpawnUserAgent._GENERAL_TOKEN} ({platform}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15" for platform in (f"{SpawnUserAgent._MAC_PREFIX} 10_15_7",) for version in (15 + i/10 for i in range(0, 6))]

    @staticmethod
    def generate_all():
        return SpawnUserAgent.firefox() + SpawnUserAgent.chrome() + SpawnUserAgent.safari()
