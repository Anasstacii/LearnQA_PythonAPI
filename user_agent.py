import requests
import pytest


class TestUserAgent:
    user_agents_and_expected = [
        (
            'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, '
            'like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mobile', 'No', 'Android'),
        (
            'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
            'CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
            'Mobile', 'Chrome', 'iOS'),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
         'Googlebot', 'Unknown', 'Unknown'),
        (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 '
            'Safari/537.36 Edg/91.0.100.0',
            'Web', 'Chrome', 'No'),
        (
            'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
            'Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Mobile', 'No', 'iPhone')
    ]

    @pytest.mark.parametrize("user_agents, platform, browser, device", user_agents_and_expected)
    def testuser_agent(self, user_agents, platform, browser, device):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        response = requests.get(url, headers={"User-Agent": user_agents})
        result_platform = response.json()['platform']
        result_browser = response.json()['browser']
        result_device = response.json()['device']

        assert platform in result_platform, f"Cannot find platform:'{platform}' in the response_platform:{result_platform}"
        assert browser in result_browser, f"Cannot find browser:'{browser}' in the response_browser:{result_browser}"
        assert device in result_device, f"Cannot find device:'{device}' in the response_device:{result_device}"
