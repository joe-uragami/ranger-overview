
from rov.rov import make_url, pick_out_content

def test_make_url_ゴレンジャーのURLが作れること():
    url = make_url(1)
    assert url == "https://ja.wikipedia.org/wiki/秘密戦隊ゴレンジャー"

def test_make_url_キューレンジャーのURLが作れること():
    url = make_url(41)
    assert url == "https://ja.wikipedia.org/wiki/宇宙戦隊キュウレンジャー"

def test_pick_out_content_ジャッカーの内容が取れること():
    content = pick_out_content("https://ja.wikipedia.org/wiki/ジャッカー電撃隊")
    assert content[0] == "ジャッカー電撃隊"
    overview = content[1]
    assert overview[:10] == "4人のサイボーグ「ジ"