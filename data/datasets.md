# Datasets

The class encoded 1 is the positive class throughout. IR is the majority count divided by the minority count. Datasets are not redistributed in this repository; please download them from the sources below and respect their licences. Machine-readable versions of these tables are in `datasets_B1.csv` and `datasets_R1_R2.csv`.

## R1 / R2: focused real-data tasks

| Task | Dataset | Positive event | Split policy |
|---|---|---|---|
| Blood | [Blood Transfusion Service Center](https://archive.ics.uci.edu/dataset/176/blood+transfusion+service+center) | Donation = 1 | Stratified 60/20/20 |
| Cervical | [Cervical Cancer (Risk Factors)](https://archive.ics.uci.edu/dataset/383/cervical+cancer+risk+factors) | Biopsy = 1 | Stratified 60/20/20 |
| Infrared | [Infrared Thermography Temperature](https://archive.ics.uci.edu/dataset/925/infrared+thermography+temperature+dataset) | aveOralF >= 38 | Stratified 60/20/20 |
| Credit | [Credit Card Fraud Detection (ULB)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) | Class = 1 | Chronological 60/20/20 |
| Ozone | [Ozone Level Detection](https://archive.ics.uci.edu/dataset/172/ozone+level+detection) | Ozone day = 1 | Chronological 60/20/20 |
| Shill | [Shill Bidding Dataset](https://archive.ics.uci.edu/dataset/562/shill+bidding+dataset) | Class = 1 | Auction-group split |
| APS | [APS Failure at Scania Trucks](https://archive.ics.uci.edu/dataset/421/aps+failure+at+scania+trucks) | pos = 1 | Original test; 75/25 fit/selection |
| CARAVAN | [Insurance Company Benchmark (COIL 2000)](https://archive.ics.uci.edu/dataset/125/insurance+company+benchmark+coil+2000) | CARAVAN = 1 | Original test; 75/25 fit/selection |
| Shoppers | [Online Shoppers Purchasing Intention](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset) | Revenue = True | Stratified 60/20/20 |
| Intrusion | [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) | Non-BENIGN flow | Stratified 60/20/20 |
| Airline | [source to confirm] | recommended = yes | Stratified 60/20/20 |
| BETH | [BETH cybersecurity dataset](https://www.kaggle.com/datasets/katehighnam/beth-dataset) | sus = 1 | Original train/val/test |

## B1: broad benchmark (59 tasks)

| ID | Dataset | Category | Target (positive = 1) | N | Positives | Features | IR | Note |
|---|---|---|---|---|---|---|---|---|
| d001 | [Android Malware Detection](https://www.kaggle.com/datasets/subhajournal/android-malware-detection) | Cybersecurity | Label | 28620 | 4912 | 80 | 4.83 |  |
| d002 | [Classification of Malwares (CLaMP)](https://www.kaggle.com/datasets/saurabhshahane/classification-of-malwares) | Cybersecurity | class | 3032 | 544 | 69 | 4.57 |  |
| d003 | [Dataset for Link Phishing Detection](https://www.kaggle.com/datasets/winson13/dataset-for-link-phishing-detection/data) | Cybersecurity | status | 10861 | 1145 | 86 | 8.49 |  |
| d004 | [Healthcare Ransomware Dataset](https://www.kaggle.com/datasets/rivalytics/healthcare-ransomware-dataset/data) | Cybersecurity | data_stolen | 5000 | 1148 | 15 | 3.36 |  |
| d005 | [Malware Detection Dataset](https://www.kaggle.com/datasets/ankit1743/android-malware-detection-dataset) | Cybersecurity | Result | 5392 | 525 | 86 | 9.27 |  |
| d006 | [CIC-IDS2017 (web-attack subset)](https://www.unb.ca/cic/datasets/ids-2017.html) | Cybersecurity | Label | 29957 | 418 | 78 | 70.67 |  |
| d007 | [Tabular dataset ready for malicious url detection](https://www.kaggle.com/datasets/pilarpieiro/tabular-dataset-ready-for-malicious-url-detection/data) | Cybersecurity | label | 4206 | 895 | 56 | 3.7 |  |
| d008 | [PhiUSIIL Phishing URL](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset) | Cybersecurity | label | 40000 | 4000 | 50 | 9 |  |
| d009 | [RT-IoT2022](https://archive.ics.uci.edu/dataset/942/rt-iot2022) | Cybersecurity | target | 5037 | 37 | 79 | 135.14 |  |
| d010 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d011 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d012 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d013 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d014 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d015 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d016 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d017 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d018 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d019 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d020 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d021 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d022 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d023 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d024 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d025 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d026 | [to confirm] | Finance and marketing |  |  |  |  |  | choose from sheet Finance_candidates |
| d027 | [Airbnb for Boston with fraud detection](https://www.kaggle.com/datasets/hawkingcr/airbnb-for-boston-with-fraud-detection) | Fraud detection | fraud | 3585 | 767 | 20 | 3.67 |  |
| d028 | [Bank Transaction Dataset for Fraud Detection](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection) | Fraud detection | IsFraud | 2512 | 126 | 53 | 18.94 |  |
| d029 | [Credit Card Fraud](https://www.kaggle.com/datasets/kartik2112/fraud-detection) | Fraud detection | is_fraud | 10359 | 48 | 1187 | 214.81 |  |
| d030 | [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data) | Fraud detection | Class | 284807 | 492 | 30 | 577.88 | chronological split |
| d031 | [Fraudulent Claim on Cars Physical Damage](https://www.kaggle.com/datasets/surekharamireddy/fraudulent-claim-on-cars-physical-damage) | Fraud detection | fraud | 17998 | 2816 | 22 | 5.39 |  |
| d032 | [Healthcare Providers Data For Anomaly Detection](https://www.kaggle.com/datasets/tamilsel/healthcare-providers-data) | Fraud detection | PotentialFraud | 100000 | 118 | 20 | 846.46 |  |
| d033 | [Insurance Fraud Detection](https://www.kaggle.com/datasets/arpan129/insurance-fraud-detection) | Fraud detection | police_report_available_YES | 1000 | 314 | 1093 | 2.18 | target is police-report availability, not fraud |
| d034 | [Learning from Imbalanced Insurance Data](https://www.kaggle.com/datasets/arashnic/imbalanced-data-practice) | Fraud detection | Response | 20632 | 3323 | 10 | 5.21 |  |
| d035 | [Loan Application & Transaction Fraud Detection](https://www.kaggle.com/datasets/prajwaldongre/loan-application-and-transaction-fraud-detection) | Fraud detection | Fraudulent | 49428 | 479 | 31 | 102.19 |  |
| d036 | [Alzheimers](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset) | Medical | Diagnosis | 2149 | 760 | 34 | 1.83 |  |
| d037 | [Breast Cancer Prediction](https://www.kaggle.com/datasets/marshalpatel3558/breast-cancer-prediction) | Medical | Status | 4024 | 616 | 15 | 5.53 |  |
| d038 | [CDC Diabetes Health Indicators](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) | Medical | Diabetes_binary | 229474 | 35097 | 21 | 5.54 |  |
| d039 | [Healthy Lifestyle](https://www.kaggle.com/datasets/aditibabu/healthy-lifestyle) | Medical | Label | 11544 | 1924 | 45 | 5 |  |
| d040 | [Hospital Length of Stay Dataset Microsoft](https://www.kaggle.com/datasets/aayushchou/hospital-length-of-stay-dataset-microsoft) | Medical | long_stay | 100000 | 8565 | 24 | 10.68 |  |
| d041 | [ICU Patient Outcome Prediction](https://www.kaggle.com/datasets/fdemoribajolin/death-classification-icu) | Medical | target | 3600 | 503 | 119 | 6.16 |  |
| d042 | [NHS Admissions Data 2011 2020](https://www.kaggle.com/datasets/tomfarnell/nhs-admissions-data-2011-2020) | Medical | Target_High_Admission | 8043 | 1341 | 10 | 5 |  |
| d043 | [Ovarian Cancer](https://www.kaggle.com/datasets/datasetengineer/ovarian-cancer-risk-and-progression-data) | Medical | RiskLabel_Binary | 16000 | 3201 | 33 | 4 |  |
| d044 | [Ovarian Cancer Risk and Progression Data](https://www.kaggle.com/datasets/datasetengineer/ovarian-cancer-risk-and-progression-data) | Medical | RiskLabel | 45000 | 5000 | 32 | 8 |  |
| d045 | [Parkinson Disease (PD) Data Analysis](https://www.kaggle.com/datasets/porinitahoque/parkinsons-disease-pd-data-analysis) | Medical | status | 3564 | 564 | 753 | 5.32 |  |
| d046 | [Stroke Risk](https://www.kaggle.com/datasets/mahatiratusher/stroke-risk-prediction-dataset) | Medical | At_Risk | 27056 | 2500 | 17 | 9.82 |  |
| d047 | [Stunting Wasting Dataset](https://www.kaggle.com/datasets/jabirmuktabir/stunting-wasting-dataset) | Medical | Stunting_binary | 10000 | 2197 | 4 | 3.55 |  |
| d048 | [Support Health Data for Death Prediction](https://archive.ics.uci.edu/dataset/880/support2) | Medical | target | 9105 | 2360 | 43 | 2.86 |  |
| d049 | [Cardiotocography](https://archive.ics.uci.edu/dataset/193/cardiotocography) | Medical | NSP | 2126 | 471 | 40 | 3.51 |  |
| d050 | [Hepatitis C Virus (HCV) for Egyptian Patients](https://archive.ics.uci.edu/dataset/503/hepatitis+c+virus+hcv+for+egyptian+patients) | Medical | Target | 1385 | 336 | 28 | 3.12 |  |
| d051 | [Anomaly detection in helicopter](https://www.kaggle.com/datasets/nagasai524/anomaly-detection-in-helicopter/data) | Predictive maintenance | Lavel | 161 | 62 | 16383 | 1.6 |  |
| d052 | [High-Speed Train Bogie Vibration & Fault Diagnosis](https://www.kaggle.com/datasets/ziya07/high-speed-train-bogie-vibration-and-fault-diagnosis) | Predictive maintenance | condition | 1215 | 215 | 487 | 4.65 |  |
| d053 | [AI4I 2020 Predictive Maintenance](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset) | Predictive maintenance | Machine failure | 10000 | 339 | 11 | 28.5 |  |
| d054 | [Annealing](https://archive.ics.uci.edu/dataset/3/annealing) | Predictive maintenance | Label | 798 | 190 | 84 | 3.2 |  |
| d055 | [APS Failure at Scania Trucks](https://archive.ics.uci.edu/dataset/421/aps+failure+at+scania+trucks) | Predictive maintenance | class | 30000 | 500 | 170 | 59 | prepared 30k subset |
| d056 | [Climate Model Simulation Crashes](https://archive.ics.uci.edu/dataset/252/climate+model+simulation+crashes) | Predictive maintenance | outcome | 540 | 494 | 18 | 10.74 | majority-positive |
| d057 | [HTRU2 (pulsar candidates)](https://archive.ics.uci.edu/dataset/372/htru2) | Predictive maintenance | Class | 17898 | 1639 | 8 | 9.92 |  |
| d058 | [Ionosphere](https://archive.ics.uci.edu/dataset/52/ionosphere) | Predictive maintenance | target | 351 | 126 | 34 | 1.79 |  |
| d059 | [MIT-BIH Arrhythmia (ECG, binary)](https://www.kaggle.com/code/redpen12/anomaly-detection-with-cnn-autoencoders/input) | Predictive maintenance | Label | 21892 | 3774 | 187 | 4.8 |  |
