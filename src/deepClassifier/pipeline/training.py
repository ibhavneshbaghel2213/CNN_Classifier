from deepClassifier.config import ConfigurationManager
from deepClassifier import logger
from deepClassifier.components.prepare_callback import PrepareCallback



STAGE_NAME= "Prepare Call Back stage"


def main():
    config = ConfigurationManager()
    prepare_callback_config= config.get_prepare_call_back()
    prepare_callback= PrepareCallback(config=prepare_callback_config)
    callback_list=  prepare_callback.get_tb_ckpt_callbacks()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e