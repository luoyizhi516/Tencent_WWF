# Tencent_WWF


## Introduction
This is the data preprocessing repository for the animal surveillance project that Tencent cooperates with [World Wildlife Foundation](https://www.worldwildlife.org/). This work is done by [Tencent AI Lab](https://ai.tencent.com/ailab/en/index).

## General naming rules for data

- 📊 Ori data: represents the original data obtained from WWF with original folder structure.
- 🛠 Raw data: represents the unlabeled data divided into several batches and multiple animal categories for each batch.
- ✨ Pos data: represents the labeled data that is returned from the annotation staff. Both the valuable data and disqualified data are stored here.
- 📝 Final data: represents the final labeled data that is split according to various criteria.

## Folder Functions
### Ori data cleaning
This folder contains the data cleaning code of the original data; one portion of the code makes statistical analysis on data distribution, and another constructs the raw dataset.

### Label data building
This folder contains the code for constructing the label task data sampled from the raw data. The data will be further assigned to annotation staff. 

### Raw annotations
This folder stores the raw annotations and the concatenated annotations for each batch of labeled data.

### Pos data building
This folder contains the code for the building of the labeled data, including checking the annotation quality and make statistical analysis on data.

### Drop txt
This folder contains the txt files storing the samples below the mark, which will be dropped and returned to the annotation staff.

### Pos data stat
This folder stores the statistic analysis results obtained from the Pos data building module.

### Final data building
This folder contains the code for the building of the final data for training. Generally, two different kinds of data splitting rules were made.

### Raw data stat
This folder contains the modality and split-criteria stats which gives us an objective analysis.

### Final data stat 
This folder stores the frame and video-level information for split samples, including modality, numbers, path, categories, etc.

