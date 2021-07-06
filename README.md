# Tencent_WWF


## Introduction
This is the data preprocessing repository for for animal surveillance project that Tencent cooperates with [World Wildlife Foundation](https://www.worldwildlife.org/). This work is done by [Tencent AI Lab](https://ai.tencent.com/ailab/en/index).

## General naming rules for data
<br />

- 📊 Ori data: represents the original data obtained from WWF with original folder structure.
- 🛠 Raw data: represents the unlabeled data that are divided to serveral batches and multiple catogiries of animal for each batch.
- ✨ Pos data: represents the labled data that is returned from the annotation staff. Both the valuable data and disqualified data are stored here.
- 📝 Final data: represents the final labled data that are splitted in various critiria.

<br />


## Pipeline for data preprossing

### Ori data cleaning
This folder contains the data cleaning code of the original data; one portion of code make statistic analysis on data ditribution and another contruct the raw dataset.

### Label data building
This folder contains the code for the constructing the label task data sampled from the raw data. The data will be further assigned to annotation staff. 

### Raw annotations
This folder stores the raw annotations and the concatinated annotations for each batch of labeled data.

#### Pos data building
This folder contains the code for the building of the labled data including checking the annotation quality and make statistic analysis on data.

### Drop txt
This folder contains the txt files storing the samples that are below the mark which will be droped and further returned to annotation staff.

### Pos data stat
This folder stores the statistic analysis result obtained from Pos data building module.

### Final_data_building
This folder contains the code for the building of the final data for training. Generally two diffenrent kinds of data splitting rule were made.

### Raw data stst
This folder contains the modality and split-critiria stats which gives us a objective analysis.

### Final data stat 
This folder stores the frame and video-level information for splitted samples inluding modality, numbers, path, categories, etc.




