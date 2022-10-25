import logging
import pyaudio
from paddlespeech.server.utils.config import get_config
from paddlespeech.server.engine.asr.online.asr_engine import PaddleASRConnectionHanddler
from paddlespeech.server.engine.engine_pool import get_engine_pool, init_engine_pool

config_path = r'ws_conformer_wenetspeech_application.yaml'
config = get_config(config_path)
init_engine_pool(config)
asr_engine = get_engine_pool()['asr']
handler = PaddleASRConnectionHanddler(asr_engine)
pa = pyaudio.PyAudio()
stream = pa.open(16000,
                 1,
                 pyaudio.paInt16,
                 input=True,
                 frames_per_buffer=32000)
print('Start recording...')
logging.disable()
while True:
    wav = stream.read(32000)
    handler.extract_feat(wav)
    handler.decode()
    text = handler.get_result()
    print(text)