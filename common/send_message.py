# encoding:utf-8
import requests
from common.dirs import LOGS_DIR, LOG_FILE
from common.logger import logger
import re
import os
import sys


def log_reader():
    # 在GitHub Actions环境中，日志会直接输出到控制台
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        # 获取当前进程的标准输出
        try:
            # 尝试从标准输出获取日志
            logs = sys.stdout.getvalue() if hasattr(sys.stdout, 'getvalue') else "无法获取日志内容"
            return logs
        except Exception as e:
            logger.error(f"获取日志内容失败: {str(e)}")
            return "无法获取日志内容"
    else:
        # 本地环境下的处理方式
        if not os.path.exists(LOGS_DIR):
            os.makedirs(LOGS_DIR)
        
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'w', encoding="UTF-8") as f:
                f.write("")
        
        try:
            with open(LOG_FILE, 'r', encoding="UTF-8") as lg:
                logs = lg.readlines()
                logs_str = ''.join(logs).replace("\n","\n\n")
            return logs_str
        except Exception as e:
            logger.error(f"读取日志文件失败: {str(e)}")
            return "无法读取日志文件"


def send_message(send_key, msg):
    url = "https://sctapi.ftqq.com/{}.send".format(send_key)
    data = {
        "title": u"DouYu-Helper执行结果",
        "desp": msg
    }
    try:
        logger.info("------执行server酱推送------")
        requests.post(url, data=data)
        logger.info("------推送成功------")
    except Exception as e:
        logger.error(e)



if __name__ == '__main__':
    send_message()
