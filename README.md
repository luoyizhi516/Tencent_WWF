# Tencent_WWF


## Introduction
<p align="left"> 
This is the data preprocessing repository for for animal surveillance project that Tencent cooperates with World Wildlife Foundation.
</p>
A general naming rules:

<br />

- 🔭 I’m currently working at [Tencent AI Lab](https://ai.tencent.com/ailab/en/index) as a research intern.
- 🌱 I’m currently a incoming computer science freshman student at University of Rochester.
- 🤝 I'm currently a visiting researcher at [Artificial Intelligent and Machine Vision Lab](http://iip.whu.edu.cn/index.html) at Wuhan University.
- 😄 My main reserach domain includes computer vision, pattern recoginition and machine learning with a focus on mid&high level vision tasks such as video understanding, object detection, etc.
- -💬 Ask me about anything [here](https://github.com/jingyuanchan/jingyuanchan/issues)

<br />

<br />

-Raw data: Raw data represents the unlabeled data that are divided to serveral batches and multiple catogiries of animal for each batch.
-Pos data: Pos data represents the labled data that is returned from the annotation staff. Both the valuable data and disqualified data are stored here. 
-Final data: Final data represents the final labled data that are splitted in various critiria.

<br />

## Pipeline for data preprossing

### Drop txt
This folder contains the txt files storing the samples that are below the mark which will be droped and further returned to annotation staff.
### Final_data_building
This folder contains the code for the building of the final data for training. Generally two diffenrent kinds of data splitting rule were made.
### Final_data_stat 
This folder store the frame and video-level information for splitted samples inluding modality, numbers, path, categories, etc.


