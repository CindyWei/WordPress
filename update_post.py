#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time 
import unittest
import random
from public import login  #引入login文件

class WordPress_Update(unittest.TestCase):
	post_list_url = "http://127.0.0.1:8080/wordpress/wp-admin/edit.php"

	def setUp(self):
		self.dr = webdriver.Chrome()

	def test_update_post(self):
		"""更新文章的用例"""
		login.login(self.dr)   #调用login公用方法
		self.dr.get(self.post_list_url)
		post = self.dr.find_element_by_partial_link_text("new post")
		time.sleep(3)
		#移动鼠标到要更新的文章上,并等待编辑菜单出现
		ActionChains(self.dr).move_to_element(post).perform()
		w = WebDriverWait(self.dr,10)
		w.until(lambda dr: self.dr.find_element_by_class_name("row-actions").is_displayed())
		self.dr.find_element_by_class_name("edit").click()
		#编辑标题，添加字符“Cindy"+随机数,并保存
		n = str(random.randint(1, 100))
		self.dr.find_element_by_id("title").send_keys("Cindy"+n)
		self.dr.find_element_by_id('publish').click()
		#再次进入所有文章列表,并断言含"Cindy"+随机数
		self.dr.get(self.post_list_url)
		post_list_table = self.dr.find_element_by_class_name('wp-list-table')
		self.assertTrue("Cindy"+n in post_list_table.text)
		print "UpdatePost: success"

	def tearDown(self):
		time.sleep(3)
		self.dr.quit()

if __name__ == "__main__":
	unittest.main()
