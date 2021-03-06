
import sys
import requests
import bs4
import re

RANGERS = (
    "秘密戦隊ゴレンジャー",
    "ジャッカー電撃隊",
    "バトルフィーバーJ",
    "電子戦隊デンジマン",
    "太陽戦隊サンバルカン",
    "大戦隊ゴーグルファイブ",
    "科学戦隊ダイナマン",
    "超電子バイオマン",
    "電撃戦隊チェンジマン",
    "超新星フラッシュマン",
    "光戦隊マスクマン",
    "超獣戦隊ライブマン",
    "高速戦隊ターボレンジャー",
    "地球戦隊ファイブマン",
    "鳥人戦隊ジェットマン",
    "恐竜戦隊ジュウレンジャー",
    "五星戦隊ダイレンジャー",
    "忍者戦隊カクレンジャー",
    "超力戦隊オーレンジャー",
    "激走戦隊カーレンジャー",
    "電磁戦隊メガレンジャー",
    "星獣戦隊ギンガマン",
    "救急戦隊ゴーゴーファイブ",
    "未来戦隊タイムレンジャー",
    "百獣戦隊ガオレンジャー",
    "忍風戦隊ハリケンジャー",
    "爆竜戦隊アバレンジャー",
    "特捜戦隊デカレンジャー",
    "魔法戦隊マジレンジャー",
    "轟轟戦隊ボウケンジャー",
    "獣拳戦隊ゲキレンジャー",
    "炎神戦隊ゴーオンジャー",
    "侍戦隊シンケンジャー",
    "天装戦隊ゴセイジャー",
    "海賊戦隊ゴーカイジャー",
    "特命戦隊ゴーバスターズ",
    "獣電戦隊キョウリュウジャー",
    "烈車戦隊トッキュウジャー",
    "手裏剣戦隊ニンニンジャー",
    "動物戦隊ジュウオウジャー",
    "宇宙戦隊キュウレンジャー"
)

WIKI_URL = "https://ja.wikipedia.org/wiki/"

def make_url(no):
    # TODO 引数チェック

    title = RANGERS[no - 1]
    return WIKI_URL + title

def pick_out_content(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")


    # TODO 抽出処理を別途分けてテストできるようにする
    title = soup.find("h1").string
    overview = soup.find_all("h2")[1].nextSibling.nextSibling.text
    return [title, overview]


def main():
    # 引数の数字からURLを取り出す
    args = sys.argv

    # URLから本文を取り出す
    response = requests.get(make_url(args[1]))



    # 本文からタイトルと概要を抜き出す

    # 概要のトリミング

    # タイトルと、トリミングした概要を表示


# メイン処理を呼び出す
if __name__ == '__main__':
    main()