# PoseTrack
基于mediapipe在unity中实现姿态追踪
# 第三方库要求
  mediapipe
# 使用方法
## 1.首先运行udptracker.py
  可以根据需要更改ip地址和端口
## 2.然后使用unity2021.3.13f1c1打开Track副本
  点击运行就可以实现追踪
  
  
# 一些碎碎念
  ## 写了一个unity.py可以生成一个视频的追踪点的txt文件，这个文件可以用到unity中实现追踪
  ## 使用了udp来实现数据的传输，效果还可以
  ## 只是在unity中实现了点对点的复现，并不可以使用到通用模型上
