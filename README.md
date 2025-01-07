<div align="center"> 
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/mukesh-manral/"><img src="https://img.shields.io/badge/LinkedIn-411AFF?style=for-the-badge&logo=LinkedIn&logoColor=white" /></a>  
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.kaggle.com/mukeshmanral"><img src="https://img.shields.io/badge/Kaggle-411AFF?style=for-the-badge&logo=Kaggle&logoColor=white" /></a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://medium.com/@manralai/lists"><img src="https://img.shields.io/badge/Medium-411AFF?style=for-the-badge&logo=Medium&logoColor=white" /></a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.youtube.com/@manralai"><img src="https://img.shields.io/badge/Youtube-411AFF?style=for-the-badge&logo=Youtube&logoColor=white" /></a>
&nbsp;&nbsp;&nbsp;&nbsp; 
<a href="https://www.instagram.com/manralai/"><img src="https://img.shields.io/badge/Instagram-411AFF?style=for-the-badge&logo=Instagram&logoColor=white" /></a>
</div>

## Common WorkFlow to consider

1. Write `config.yaml` code
2. Write `secrets.yaml` code (senstive data, say if in case you want to connect to db and putting in credentials) [Optinal to cases]
3. Write `params.yaml` code (general parameters values)
4. Write `entity module` code

**`Getting inside src`**

5. Write `config` manager present in src config
6. Write `components` one after others say (data_ingestion, model_training, model_evaluation .... so on)
7. Write `pipeline` code
8. Write end point code in `main.py`

# Tree
<pre>
.
├── artifacts
│   └── data_ingestion
│       ├── classifier_data_v01
│       └── dataV01.zip
├── config
│   └── config.yaml
├── LICENSE
├── logs
│   └── running_logs.log
├── main.py
├── params.yaml
├── README.md
├── requirements.txt
├── research_env
│   ├── check_baseModel_v04.ipynb
│   ├── check_dataIngestion_v03.ipynb
│   └── trials_n.ipynb
├── setup.py
├── src
│   ├── imageClassifier
│   │   ├── components
│   │   │   ├── data_ingestion.py
│   │   │   ├── __init__.py
│   │   │   └── modelPrep_base.py
│   │   ├── config
│   │   │   ├── configuration.py
│   │   │   └── __init__.py
│   │   ├── constants
│   │   │   └── __init__.py
│   │   ├── entity
│   │   │   ├── config_entity.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── pipeline
│   │   │   ├── data_ingestion_v01.py
│   │   │   ├── __init__.py
│   │   │   └── modelPrep_base_v02.py
│   │   └── utils
│   │       ├── common.py
│   │       └── __init__.py
│   └── imageClassifier.egg-info
│       ├── dependency_links.txt
│       ├── PKG-INFO
│       ├── SOURCES.txt
│       └── top_level.txt
├── template.py
└── test.py
</pre>

## Logs View
[Tensor Logs](https://github.com/MvMukesh/ImageClassifier-Pipeline/blob/main/TensorBoard.html)

<div align="center"> 
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/mukesh-manral/"><img src="https://img.shields.io/badge/LinkedIn-411AFF?style=for-the-badge&logo=LinkedIn&logoColor=white" /></a>  
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.kaggle.com/mukeshmanral"><img src="https://img.shields.io/badge/Kaggle-411AFF?style=for-the-badge&logo=Kaggle&logoColor=white" /></a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://medium.com/@manralai/lists"><img src="https://img.shields.io/badge/Medium-411AFF?style=for-the-badge&logo=Medium&logoColor=white" /></a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.youtube.com/@manralai"><img src="https://img.shields.io/badge/Youtube-411AFF?style=for-the-badge&logo=Youtube&logoColor=white" /></a>
&nbsp;&nbsp;&nbsp;&nbsp; 
<a href="https://www.instagram.com/manralai/"><img src="https://img.shields.io/badge/Instagram-411AFF?style=for-the-badge&logo=Instagram&logoColor=white" /></a>
</div>
