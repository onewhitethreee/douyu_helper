# encoding:utf-8
import requests
from common.dirs import LOGS_DIR, LOG_FILE
from common.logger import logger
import re


def log_reader():
    with open(LOG_FILE, 'r', encoding="UTF-8") as lg:
        logs = lg.readlines()
        logs_str = ''.join(logs).replace("\n","\n\n")
    return logs_str


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
