#coding=utf-8
import time


def create_post(dr):
	"""创建post方法"""
	creat_post_url = 'http://127.0.0.1:8080/wordpress/wp-admin/post-new.php'
	dr.get(creat_post_url)
	title_or_content = 'new post' + str(time.time())
	dr.find_element_by_name('post_title').send_keys(title_or_content)
	js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" + title_or_content + "'"
	print js
	dr.execute_script(js)
	dr.find_element_by_id('publish').click()
	return title_or_content


"""
经乙醇指导：将此操作独立出来，因为删除用例和更新用例在操作前先调用执行此方法，之后再进行删除更新操作，这样保持了用例的独立性
	此公共方法涉及到业务逻辑，不能和login公共方法写在一个.py文件里

"""

