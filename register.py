from selenium import webdriver
import unittest
import time
import csv

class TestRegister(unittest.TestCase):
        """导航到cnode注册页面"""
        def setUp(self):
            self.dr=webdriver.Chrome(executable_path='./chromedriver')
            url='http://118.31.19.120:3000/signup/'
            time.sleep(5)
            self.dr.get(url)
            print('*************Test Cases Execution Begin*************')

        def tearDown(self):
            print('*************Test Cases Execution End*************')
            self.dr.close()


        def test_regis(self):
            """测试登录"""
            #获取要读取的csv文件路径
            my_file='./datas.csv'
            datas=csv.reader(open(my_file,'r'))

            for data in datas:
                print(data[4])
                #定位登录页面的元素
                cid_name="loginname"
                cid_pwd="pass"
                cid_rpd="re_pass"
                cid_cmail="email"
                ccname_cli="span-primary"
                c_info='//*[@id="content"]//strong'

                self.dr.find_element_by_id(cid_name).send_keys(data[0])
                self.dr.find_element_by_id(cid_pwd).send_keys(data[1])
                self.dr.find_element_by_id(cid_rpd).send_keys(data[2])
                self.dr.find_element_by_id(cid_cmail).send_keys(data[3])
                self.dr.find_element_by_class_name(ccname_cli).click()
                time.sleep(5)
                message=self.dr.find_element_by_xpath(c_info).text
                #每次case页面截图存放到当前路径下的screenshot中（首先在当前路径下新建screenshot文件夹）
                self.dr.get_screenshot_as_file('./screenshot/'+data[5]+".png")
                try:
                    self.assertEqual(message,data[6])
                    print('页面提示信息和预期一致: pass')
                    print('预期提示:',data[6])
                    print('实际提示:', message)
                except:
                    print('页面提示信息和预期不一致: fail')
                    print('预期提示:',data[6])
                    print('实际提示:', message)

                self.dr.back()
                self.dr.refresh()


if __name__=='__main__':
    unittest.main