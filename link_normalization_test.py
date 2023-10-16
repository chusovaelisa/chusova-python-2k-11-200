import urllib.parse
def normalize_image_url(image_url):
    if not image_url.startswith("http://") and not image_url.startswith("https://"):
        image_url = "http:" + image_url

    parsed_url = urllib.parse.urlparse(image_url)
    if not parsed_url.netloc:
        return image_url

    return image_url

image_url1 = "https://http.cat/200.jpg"
image_url2 = "//http.cat/200.jpg"
image_url3 = "/200.jpg"

def test_normalize_image_url():
    assert normalize_image_url(image_url1) == "https://http.cat/200.jpg"
    assert normalize_image_url(image_url2) == "http://http.cat/200.jpg"
    assert normalize_image_url(image_url3) == "http:/200.jpg"

if __name__ == "__main__":
    import pytest

    pytest.main()
