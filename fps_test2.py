#Pygameを使用してウィンドウ内にカウンターを表示するプログラム(FPSCLPCK追加)

"""fps_test2.py"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock() #新しい Clock オブジェクトを作成します。このオブジェクトは、ゲームループ内でのフレームレートを管理します。

def main():
    """main routine"""
    sysfont = pygame.font.SysFont(None,36) #デフォルトのシステムフォントを使用し、サイズ36のフォントオブジェクトを取得
    counter = 0 #counter 変数を用意し、カウンターの初期値を0に設定
    while True:
        for event in pygame.event.get(QUIT): #QUIT イベントが発生するまでのイベントを取得し、ウィンドウを閉じるイベントが発生したら、Pygameを終了し、スクリプトを終了
            pygame.quit()
            sys.exit()
        counter += 1 #counter をインクリメント(値を1増やす)
        SURFACE.fill((0,0,0)) #ウィンドウを黒色で塗りつぶします。
        count_image = sysfont.render("count is {}".format(counter),True,(255,255,255)) #カウンターの値を表示するテキストイメージを作成します。このイメージは、白色で描画されます。
        SURFACE.blit(count_image,(50,50)) #(50, 50) の座標にテキストイメージが描画されます。
        pygame.display.update()
        FPSCLOCK.tick(10) #現在のフレームの経過時間を計測し、指定されたフレームレートになるように適切なウェイトを行います。

if __name__ == '__main__':
    main()