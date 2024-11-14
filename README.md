# 使い方
1. 7行目の"URL"をダウンロードしたい動画のURLに変更する
2. terminalでプログラムを実行
   ```
   python youtube_download.py
   ```

# 注意点
- 本プログラムでは`yt-dlp`モジュールを用いるので，事前にterminalで`pip install yt-dlp`を実行する必要がある
- "`,`"を用いてURLを複数並べることで，複数の動画を同時にダウンロードできる
  - 例：`[URL1, URL2, URL3, ...]`
