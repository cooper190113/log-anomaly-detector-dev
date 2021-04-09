# -*- coding:utf-8 -*-
import errno
import logging
from logging.handlers import TimedRotatingFileHandler
import os


def mkdir_path(path):
    try:
        os.makedirs(path, exist_ok=True)  # Python>3.2
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise


class Logger:
    def __init__(self, loggername):
        # 创建一个logger
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        # 指定文件输出路径，注意logs是个文件夹，一定要加上/，不然会导致输出路径错误，把logs变成文件名的一部分了
        # 指定输出的日志文件名.指定utf-8格式编码，避免输出的日志文本乱码
        file_path = str(os.path.dirname(os.getcwd() + "/logs/"))
        mkdir_path(file_path)
        file_name = file_path + "/log-anomaly-detector.log"
        fh = logging.handlers.TimedRotatingFileHandler(file_name, when='D', backupCount=10, encoding='utf-8')
        fh.suffix = "%Y-%m-%d.log"
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger
