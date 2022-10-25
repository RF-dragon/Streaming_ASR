# Streaming ASR

([简体中文](README.md) | English)

### Description
This program is a real-time recording version of the PaddleSpeech streaming ASR
program.

### Installation
1. Clone or download this repository.
2. Install Python. Please make sure that you have added Python to PATH.
3. Install PaddlePaddle and PaddleSpeech on https://www.paddlepaddle.org.cn/en
   according to your OS and CUDA version. If you are unfamiliar with CUDA,
   please select "CPU" on the "Compute Platform" column.
4. Enter the folder where you installed Python and open Lib\site-packages. Copy
   the [paddlespeech](paddlespeech) folder into it to replace the existing
   files.
5. Install PyAudio with the following command:
```shell
python -m pip install pyaudio -U
```
6. Download zlib123dll. (
   [32-bit](http://www.winimage.com/zLibDll/zlib123dll.zip) | 
   [64-bit](http://www.winimage.com/zLibDll/zlib123dllx64.zip) | 
   [Intel Itanium](http://www.winimage.com/zLibDll/zlib123dllia64.zip)) After
   the downloading process is finished, unzip the file and add the dll (or 
   dll_x64) folder to environment variables.
If you encounter any problem while installing, please see
https://blog.csdn.net/weixin_48978134/article/details/125686296 for details.

### Run
Simple execute the program by running [Streaming ASR.py](Streaming%20ASR.py).
The program may need to spend about 1 minute to load the model. Please wait
patiently.

### References
@inproceedings{zhang2022paddlespeech,
    title = {PaddleSpeech: An Easy-to-Use All-in-One Speech Toolkit},
    author = {Hui Zhang, Tian Yuan, Junkun Chen, Xintong Li, Renjie Zheng, Yuxin Huang, Xiaojie Chen, Enlei Gong, Zeyu Chen, Xiaoguang Hu, dianhai yu, Yanjun Ma, Liang Huang},
    booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies: Demonstrations},
    year = {2022},
    publisher = {Association for Computational Linguistics},
}
@inproceedings{zheng2021fused,
  title={Fused acoustic and text encoding for multimodal bilingual pretraining and speech translation},
  author={Zheng, Renjie and Chen, Junkun and Ma, Mingbo and Huang, Liang},
  booktitle={International Conference on Machine Learning},
  pages={12736--12746},
  year={2021},
  organization={PMLR}
}