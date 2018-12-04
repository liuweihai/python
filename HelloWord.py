# /usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
driver = webdriver.Chrome()
driver.current_window_handle
driver.window_handles