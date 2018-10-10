from .. baiduaip.BaiduAip import text2audio

audio_file = text2audio("今天是 2018年10月10日 周三 晚上 20点41 快下班了")

with open("result1.mp3", 'wb') as of:
    of.write(audio_file)