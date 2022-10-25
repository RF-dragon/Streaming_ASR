# Streaming ASR

([简体中文](README.md) | English)

### Description

This program is a real-time recording version of the PaddleSpeech streaming ASR
program.

### Installation
1. Clone or download this repository.
2. Install Python. Please make sure that you have added Python to PATH.
3. Install PaddlePaddle and PaddleSpeech on https://www.paddlepaddle.org.cn/en according to your OS and CUDA version. If you are unfamiliar with CUDA, please select "CPU" on the "Compute Platform" column.
4. Enter the folder where you installed Python and open Lib\site-packages. Copy the [paddlespeech](paddlespeech) folder into it to replace the existing files.
5. Install PyAudio with the following command:
```shell
python -m pip install pyaudio -U
```
6. Download zlib123dll ([32-bit](http://www.winimage.com/zLibDll/zlib123dll.zip) | [64-bit](http://www.winimage.com/zLibDll/zlib123dllx64.zip) | [Intel Itanium](http://www.winimage.com/zLibDll/zlib123dllia64.zip)). After the downloading process is finished, unzip the file and add the dll (or dll_x64) folder to environment variables.

If you encounter any problem while installing, please see [my blog](https://blog.csdn.net/weixin_48978134/article/details/125686296) for details.

### Run
Simple execute the program by running [Streaming ASR.py](Streaming%20ASR.py). The program may need to spend about 1 minute to load the model. Please wait patiently.

### References
Zhang, H., Yuan, T., Chen, J., Li, X., Zheng, R., Huang, Y., Chen, X., Gong, E., Chen, Z., Hu, X., Yu, D., Ma, Y., & Huang, L. (2022). PaddleSpeech: An Easy-to-Use All-in-One Speech Toolkit. _Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies: Demonstrations_.

Zheng, R., Chen, J., Ma, M., & Huang, L. (2021). _International Conference on Machine Learning_ (pp. 12736-12746). PMLR.