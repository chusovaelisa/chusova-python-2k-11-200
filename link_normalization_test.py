import pytest
import urllib.parse


def normalize_image_url(image_url, domain):
    parsed_url = urllib.parse.urlparse(image_url)

    if not parsed_url.scheme or not parsed_url.netloc:
        image_url = urllib.parse.urljoin(domain, image_url)

    return image_url


@pytest.mark.parametrize("image_url, domain, expected_url", [
    ("https://http.cat/200.jpg", "http.cat", "https://http.cat/200.jpg"),
    ("//http.cat/200.jpg", "http.cat", "http://http.cat/200.jpg"),
    ("/200.jpg", "example.com", "http://example.com/200.jpg"),
    ("/200.jpg", "yandex.ru", "http://yandex.ru/200.jpg")
])
def test_normalize_image_url(image_url, domain, expected_url):
    assert normalize_image_url(image_url, domain) == expected_url


if __name__ == "__main__":
    pytest.main()