import atari_py
print(atari_py.__file__)

import os
print(os.path.join(atari_py.__path__[0], 'roms'))
print('pong' in atari_py.list_games())