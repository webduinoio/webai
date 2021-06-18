cd makeRes
./go.sh
cd ..
docker rm $(docker ps -aq --filter name=k210_min_build)
docker rm $(docker ps -aq --filter name=k210_std_build)
source ./make_kboot.sh
source ./make_oo_fileSystem.sh
source ./make_k210_min.sh
source ./make_k210_std.sh
rm webAI/webai.kfpkg
cd webAI && zip webai.kfpkg * && cd ..
python3 hash.py webAI/m_0x020000_webai_std.bin
python3 hash.py webAI/m_0x2A0000_webai_min.bin
