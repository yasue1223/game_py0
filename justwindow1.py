#Pygameを使用してウィンドウを表示する

#モジュールのインポート
import sys #システムに関連する機能を提供
import pygame
from pygame.locals import QUIT #ウィンドウが閉じられたときに発生する終了イベント

#Pygameの初期化とウィンドウの作成
pygame.init() #Pygameを初期化
SURFACE = pygame.display.set_mode((400, 300)) #ウィンドウのサイズを指定して SURFACE を作成。set_mode() 関数には、ウィンドウの幅と高さのタプルを渡します。
pygame.display.set_caption('Just Window') #ウィンドウのキャプション(ウィンドウのタイトルバーに表示されるテキスト)を設定

#メインループ
def main(): #無限ループ内で実行され、ウィンドウを描画し続けます。
    """main routine"""
    while True:
        SURFACE.fill((255, 255, 255)) #ウィンドウ全体を白色で塗りつぶす

        for event in pygame.event.get(): #イベントのリストを取得し、イベントの処理を行います。
            if event.type == QUIT: #QUIT イベントが発生した場合にPygameを終了し、スクリプトを終了
                pygame.quit()
                sys.exit()

        pygame.display.update() #ウィンドウを更新します。これにより、ウィンドウ上の描画が表示されます。

if __name__ == '__main__':
    main() #このスクリプトが直接実行された場合に main() 関数を呼び出す
