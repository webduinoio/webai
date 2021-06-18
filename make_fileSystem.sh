docker run --name fileSystem_build -v `pwd`:/media/shared/ webduino/k210_build \
/bin/bash -c \
"cd /media/shared/MaixPy/tools/spiffs/ && \
python3 gen_spiffs_image.py ../../projects/maixpy_k210_minimum/config_defaults.mk && \
cp fs_image/maixpy_spiffs.img ../../../webAI/m_0x400000_maixpy_spiffs.img" \
&& docker rm fileSystem_build
