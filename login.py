#coding=utf-8
import time

#登录WordPress
def login(dr):
	dr.get("http://127.0.0.1:8080/wordpress/wp-login.php")
	dr.find_element_by_name('log').send_keys("admin")
	dr.find_element_by_name('pwd').send_keys("1234567")
	dr.find_element_by_name('wp-submit').click()
	time.sleep(3)
