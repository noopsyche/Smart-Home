# Recode
NUM_BLOCK = 2000    # pyAudio内部缓存的块的大小
RATE = 16000        # 取样频率
LEVEL = 4000        # 声音保存的阈值
COUNT_NUM = 50      # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 10    # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样
CHANNEL = 1         # 录音声道数


