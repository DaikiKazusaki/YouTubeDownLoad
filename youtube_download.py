# 以下のモジュールは必須
# pip install yt-dlp
from yt_dlp import YoutubeDL

#動画のURLを指定
yt_opts = YoutubeDL({'format':'best'})
yt_opts.download(['https://www.youtube.com/watch?v=iFyKRRA9TY8&t=320s'])