
from rov.rov import make_url

def test_make_url_ゴレンジャーのURLが作れること():
    url = make_url(1)
    assert url == "https://ja.wikipedia.org/wiki/秘密戦隊ゴレンジャー"

def test_make_url_キューレンジャーのURLが作れること():
    url = make_url(41)
    assert url == "https://ja.wikipedia.org/wiki/宇宙戦隊キュウレンジャー"
