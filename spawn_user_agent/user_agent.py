"""Main classes and functions for spawn_user_agent"""

_GENERAL_TOKEN: str = "Mozilla/5.0"
_WIN_PREFIX: str = "Windows NT 10.0; Win64; x64"
_MAC_PREFIX: str = "Macintosh; Intel Mac OS X"
_UBUNTU_PREFIX: str = "X11; Ubuntu; Linux x86_64"


class SpawnUserAgent:
    """Class containing methods for spawning user agents."""

    @staticmethod
    def firefox() -> list[str]:
        """Spawns a list of common firefox user agents

        Returns:
            list[str]: The list of common firefox user agents
        """
        return [f"{_GENERAL_TOKEN} ({platform}; rv:{version}.0) Gecko/20100101 Firefox/{version}.0" for platform in (f"{_MAC_PREFIX} 10.15", _WIN_PREFIX, _UBUNTU_PREFIX) for version in range(119, 130)]

    @staticmethod
    def chrome() -> list[str]:
        """Spawns a list of common chrome user agents

        Returns:
            list[str]: The list of common chrome user agents
        """
        return [f"{_GENERAL_TOKEN} ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36" for platform in (f"{_MAC_PREFIX} 10_15_7", _WIN_PREFIX, "X11; Linux x86_64") for version in range(119, 128)]

    @staticmethod
    def safari() -> list[str]:
        """Spawns a list of common safari user agents

        Returns:
            list[str]: The list of common safari user agents
        """
        return [f"{_GENERAL_TOKEN} ({_MAC_PREFIX} 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{major}.{minor} Safari/605.1.15" for major, minors in [(16, range(5, 7)), (17, range(0, 7))] for minor in minors]

    @staticmethod
    def safari_mobile() -> list[str]:
        """Spawns a list of common mobile safari user agents

        Returns:
            list[str]: The list of common safari mobile user agents
        """
        return [f"{_GENERAL_TOKEN} (iPhone; CPU iPhone OS {major}_{minor} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{major}.{minor} Mobile/15E148 Safari/604.1" for major, minors in [(16, range(5, 8)), (17, range(0, 7))] for minor in minors]

    @staticmethod
    def generate_all() -> list[str]:
        """Convenience method, spawns common user agents for all supported browsers

        Returns:
            list[str]: The list of common user agents for all supported browsers in spawn_user_agent.
        """
        return SpawnUserAgent.firefox() + SpawnUserAgent.chrome() + SpawnUserAgent.safari() + SpawnUserAgent.safari_mobile()
