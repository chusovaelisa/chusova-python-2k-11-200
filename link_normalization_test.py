import pytest
import urllib.parse


def normalize_image_url(image_url):
    parsed_url = urllib.parse.urlparse(image_url)

    if not parsed_url.scheme or not parsed_url.netloc:
        image_url = "http:" + image_url

    return image_url


@pytest.mark.parametrize("image_url, expected_url", [
    ("https://http.cat/200.jpg", "https://http.cat/200.jpg"),
    ("//http.cat/200.jpg", "http://http.cat/200.jpg"),
    ("/200.jpg", "http:/200.jpg")
])
def test_normalize_image_url(image_url, expected_url):
    assert normalize_image_url(image_url) == expected_url


if __name__ == "__main__":
    pytest.main()