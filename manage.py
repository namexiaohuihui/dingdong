#!/usr/bin/env python
import os
import sys

"""
是Django用于管理本项目的命令行工具,之后进行站点运行、数据库自动生成、
静态文件收集等都要通过该文件完成.
"""
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dingdong.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
