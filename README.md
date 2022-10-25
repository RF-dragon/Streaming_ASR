# Streaming ASR

（简体中文 | [English](README.en.md)）

### 介绍
本程序为参考PaddleSpeech的流式语音识别demo编写的实时录音版本。

### 安装
1. 将仓库克隆或下载到本地。
2. 安装Python。请确保在安装过程中将Python添加到PATH。
3. 访问[PaddlePaddle](https://www.paddlepaddle.org.cn/)，根据自己的操作系统和CUDA版本安装
   PaddlePaddle和PaddleSpeech。如果你对CUDA不熟悉，请在“计算平台”一栏中选择“CPU”。
4. 进入到Python的安装目录下，打开Lib\site-packages，并把[paddlespeech](paddlespeech)文件夹复制进去替换
   原有文件。
5. 使用以下命令安装PyAudio：
```shell
python -m pip install pyaudio -i https://pypi.tuna.tsinghua.edu.cn/simple -U
```
6. 下载zlib123dll。（
   [32位](http://www.winimage.com/zLibDll/zlib123dll.zip) | 
   [64位](http://www.winimage.com/zLibDll/zlib123dllx64.zip) | 
   [Intel Itanium](http://www.winimage.com/zLibDll/zlib123dllia64.zip)）下载完毕后，将文
   件解压，并将其中的dll（或dll_x64）文件夹添加到环境变量。
如安装时遇到问题，请见https://blog.csdn.net/weixin_48978134/article/details/125686296。

### 运行
直接运行[Streaming ASR.py](Streaming%20ASR.py)即可。程序在开始运行时需要花一段时间加载模型，大约需要1分钟，请耐心等待。

### 参考文献
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