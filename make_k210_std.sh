docker run --name k210_std_build -v `pwd`:/media/shared/ webduino/k210_build \
/bin/bash -c \
"cd /media/shared/MaixPy/projects/maixpy_k210/ && \
python3 project.py distclean && \
python3 project.py build && \
cp /media/shared/MaixPy/projects/maixpy_k210/build/maixpy.bin \
../../../webAI/m_0x020000_webai_std.bin" \
&& docker rm k210_std_build
