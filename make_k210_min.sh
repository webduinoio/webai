docker run --name k210_min_build -v `pwd`:/media/shared/ webduino/k210_build \
/bin/bash -c \
"cd /media/shared/MaixPy/projects/maixpy_k210_minimum/ && \
python3 project.py distclean && \
python3 project.py build && \
cp /media/shared/MaixPy/projects/maixpy_k210_minimum/build/maixpy.bin \
../../../webAI/m_0x2A0000_webai_min.bin" \
&& docker rm k210_min_build
