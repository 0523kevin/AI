import logging

if __name__ == '__main__':
    logger = logging.getLogger('main')
    logging.basicConfig(level = logging.DEBUG)
    

    stream_handler = logging.FileHandler()
    logger.debug('틀렸어!!')
    logger.info('확인해!!')
    logger.warning('조심해!!')
    logger.error('에러냈어!!')
    logger.critical('망했다!!') 