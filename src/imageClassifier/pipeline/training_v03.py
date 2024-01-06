from imageClassifier import logger
from imageClassifier.config import ConfigurationManager
from imageClassifier.components import PrepareCallback,Training


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        #calling callbacks related pipeline
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
        #calling training related pipeline
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callback_list)
        