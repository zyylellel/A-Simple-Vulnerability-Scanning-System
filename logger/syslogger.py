#-*- coding:utf-8 -*-
'''
    demo03-logging-file.py
    ------------------------
    日志写入文件

    @Copyright: Chinasoft International·ETC
'''

# 导入模块
import logging
import os
import time

# 首先，创建并设置日志logger对象
# 创建logger对象并设置信息源对象名称
logger = logging.getLogger('mainlogger')
# 设置日志的输出的输出级别
logger.setLevel(logging.DEBUG)
# 设置日志的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# 其次，创建并设置文件处理器FileHandler对象
dirPath = os.path.join(os.getcwd(), 'log')
if not os.path.exists(dirPath):
    os.mkdir(dirPath)
logFileName = time.strftime('%Y%m%d', time.localtime())+'.log'
logPath = dirPath + os.sep + logFileName
# 创建FileHandler对象
fileHandler = logging.FileHandler(logPath)
# 设置Filehandler对象的写入信息级别
fileHandler.setLevel(logging.DEBUG)
# 设置FileHandler对象的信息格式
fileHandler.setFormatter(formatter)


# 创建一个 StreamHandler对象
consoleHandler = logging.StreamHandler()
# 设置控制台输出的信息级别
consoleHandler.setLevel(logging.DEBUG)
# 设置consoleHandler对象的信息格式
consoleHandler.setFormatter(formatter)

# 最后，logger对象添加Handler对象替换原有默认的Handler对象
logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)



# 测试输出不同级别的日志信息
'''
logger.fatal('系统崩溃或发生致命性错误，导致程序中断时需要输出的信息')
logger.critical('系统资源浩劫时需要输出的信息（一般很少用到）')
logger.error('系统报错异常时需要输出的信息')
logger.warning("系统运行警告时需要输出的信息")
logger.info("一般信息数据")
logger.debug("测试调试时需要输出的信息数据")
'''