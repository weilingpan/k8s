from datetime import datetime
import logging.config

def keep_log():
    log_filename = datetime.now().strftime("%Y-%m-%d.log")
    log_config = "logging.conf"
    try:
        logging.config.fileConfig(log_config, 
                                  defaults={"logfilename": f"log/{log_filename}"})
        print(f"Load logging configuration from '{log_config}'")
    except Exception as e:
        print(f"Failed to load logging configuration from '{log_config}'")
        raise e

    # 使用 root logger 記錄消息
    # logging.info('This is an info message')
    # 使用 MainLogger 記錄消息
    # MainLogger = logging.getLogger('MainLogger')
    # MainLogger.info('This is an info message from MainLogger')


    logger = logging.getLogger('MainLogger')
    return logger