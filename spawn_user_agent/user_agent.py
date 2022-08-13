"""Main classes and functions for spawn_user_agent"""


class SpawnUserAgent:
    """Class containing methods for spawning user agents."""

    _GENERAL_TOKEN: str = "Mozilla/5.0"
    _WIN_PREFIX: str = "Windows NT 10.0; Win64; x64"
    _MAC_PREFIX: str = "Macintosh; Intel Mac OS X"
    _UBUNTU_PREFIX: str = "X11; Ubuntu; Linux x86_64"

    @staticmethod
    def firefox() -> list[str]:
        """Spawns a list of common firefox user agents

        Returns:
            list[str]: The list of common firefox user agents
        """
        return [f"{SpawnUserAgent._GENERAL_TOKEN} ({platform}; rv:{version}.0) Gecko/20100101 Firefox/{version}.0" for platform in (f"{SpawnUserAgent._MAC_PREFIX} 10.15", SpawnUserAgent._WIN_PREFIX, SpawnUserAgent._UBUNTU_PREFIX) for version in range(100, 104)]

    @staticmethod
    def chrome() -> list[str]:
        """Spawns a list of common chrome user agents

        Returns:
            list[str]: The list of common chrome user agents
        """
        return [f"{SpawnUserAgent._GENERAL_TOKEN} ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36" for platform in (f"{SpawnUserAgent._MAC_PREFIX} 10_15_7", SpawnUserAgent._WIN_PREFIX, "X11; Linux x86_64") for version in range(100, 105)]

    @staticmethod
    def safari() -> list[str]:
        """Spawns a list of common safari user agents

        Returns:
            list[str]: The list of common safari user agents
        """
        return [f"{SpawnUserAgent._GENERAL_TOKEN} ({platform}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15" for platform in (f"{SpawnUserAgent._MAC_PREFIX} 10_15_7",) for version in (15 + i/10 for i in range(0, 7))]

    @staticmethod
    def safari_mobile() -> list[str]:
        """Spawns a list of common mobile safari user agents

        Returns:
            list[str]: The list of common safari mobile user agents
        """
        return [f"{SpawnUserAgent._GENERAL_TOKEN} (iPhone; CPU iPhone OS 15_{minor} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.{minor} Mobile/15E148 Safari/604.1" for minor in range(2, 7)]

    @staticmethod
    def generate_all() -> list[str]:
        """Convenience method, spawns common user agents for all supported browsers

        Returns:
            list[str]: The list of common user agents for all supported browsers in spawn_user_agent.
        """
        return SpawnUserAgent.firefox() + SpawnUserAgent.chrome() + SpawnUserAgent.safari() + SpawnUserAgent.safari_mobile()


if __name__ == "__main__":
    for s in SpawnUserAgent.generate_all():
        print(s)
