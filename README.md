# README

【**Introduction**】The prediction of drug-target interactions (DTI) is of critical importance in the realm of drug discovery. Machine learning techniques are typically employed to embed high-dimensional, sparse knowledge graphs into low-dimensional, dense vector spaces. This approach is intended to enhance computational efficiency in the domain of drug discovery. However, knowledge graphs are susceptible to various challenges, including noise, long-tail distribution, sparse data, and complex relationships (1-N, N-1, N-N). Existing methods utilize the node features of knowledge graphs, yet often neglect the inherent biases introduced by network characteristics (e.g., noise, long-tail distribution, sparse data, complex relationships). This results in an incomplete semantic representation of knowledge graphs during embedding, which consequently yields suboptimal prediction results. To address these challenges, we propose a model called DAH-DTI that uses hyperellipsoidal knowledge representation learning for predicting drug-target relationships. 

## environment

+ Python3.6
+ torch1.0.0
+ numpy1.15.4
+ pandas0.22.0

## Run

+ Step1：Extract the data to the data folder.

+ Step2：run `python GenerateData.py`

+ Step3：run `python Train.py`

