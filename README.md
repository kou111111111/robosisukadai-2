# robosisukadai-2
ロボットシステム学課題2

# 解説
https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/　
にある上田先生のスライドとプログラムを参考にして開発した。

# 環境
OS:Ubuntu 20.04

# インストール方法と動かし方
```
$ cd ~/catkin_ws/src

$ git clone https://github.com/kou111111111/robosisukadai-2.git

$ cd ~/catkin_ws

$ catkin_make

$ source ~/.bashrc

端末1$ cd catkin_ws/src

端末2$ cd catkin_ws/src

端末3$ cd catkin_ws

端末4$ cd catkin_ws/src 
```


上の手順でインストールし、端末を用意する。

↓


端末1に```roscore```と入力する。

↓
端末2に```chmod +x count.py```,```rosrun mypkg count.py```と入力する

# 実装機能
count.py で出力された文字と同じ文字列がtwice.py　で出力される。

# 協力者
嶋田雅　加藤舞子

# 作成者
上田先生　西廣巧

# 動画URL
https://www.youtube.com/watch?v=dV57AuG6MCs

# ライセンス
BSD 3-Clause License

