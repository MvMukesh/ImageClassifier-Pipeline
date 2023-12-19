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