
# coding: utf-8

# In[2]:


from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup as bsoup


# In[15]:


driver = webdriver.Firefox()
driver.get("http://web.whatsapp.com")


# In[16]:


class Whatsapp:
    def __init__(self):
        tmp = 2
        
    def isonline(self, name,driver=driver):
        driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text']").clear()

        search = driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
        search.send_keys(name)

        time.sleep(1)

        user = driver.find_element_by_xpath('//span[@title = "{}" and @class="emoji-texttt _ccCW FqYAR i0jNr"]'.format(name))
        user.click()
        
        time.sleep(1)

        a = 'user offline'
        try:
            status = driver.find_element_by_xpath('//span[@title = "{}"]'.format('online'))
            status.click()
            a = 'user online'
        except:
            pass
        return a
        
    def stalk(self, name,driver=driver):
        with open(name+'online status.txt','w+') as f2:
            b = 0
            while True:
                a = self.isonline(name)
                if a == 'user online' and b == 0:
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    f2.write(str(dt_string))
                    f2.write('\t to \t')
                    b = 1
                if a == 'user offline' and b == 1:
                    time.sleep(2)
                    if a == 'user offline' and b == 1:
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        f2.write(str(dt_string))
                        f2.write('\n')
                        b = 0
                        
    def profiledownloader(self ,name,driver=driver):
        driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='3']").clear()

        search = driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='3']")
        search.send_keys(name)

        time.sleep(1)

        user = driver.find_element_by_xpath('//span[@title = "{}" and @class="emoji-texttt _ccCW FqYAR i0jNr"]'.format(name))
        user.click()
        
        time.sleep(1)
        
        pic_url = driver.find_element_by_xpath('//div[@class="_2YnE3"]/div/img').get_attribute("src")

        profile = driver.find_element_by_xpath('//div[@class="_21nHd"]/span')
        profile.click()
        
        time.sleep(1)
        
        try:
            status = driver.find_element_by_xpath('//span[@class="emoji-texttt _2Qc5p i0jNr selectable-text copyable-text"]').get_attribute("title")
        except:
            status = 'no status found'
            
        driver.get(pic_url)
        driver.save_screenshot(name+".png")
        
        driver.execute_script('''window.open("http://web.whatsapp.com", "_blank");''')
       
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        with open(name+' status.txt','w+') as f1:
            f1.write(str(status))
            
    def bulksend(self, name, msg, iteration):
        driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='3']").clear()

        search = driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='3']")
        search.send_keys(name)

        time.sleep(1)

        user = driver.find_element_by_xpath('//span[@title = "{}" and @class="emoji-texttt _ccCW FqYAR i0jNr"]'.format(name))
        user.click()
        
        time.sleep(1)
        
        for i in range(iteration):
            driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='9']").clear()
            message = driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='9']")
            message.send_keys(msg)
            time.sleep(0.5)

            send = driver.find_element_by_xpath("//div[@class='_3HQNh _1Ae7k']")
            send.click()
            
        if iteration==0:
            try:
                for i in msg:
                    driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='9']").clear()
                    message = driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='9']")
                    message.send_keys(i)
                    send = driver.find_element_by_xpath("//div[@class='_3HQNh _1Ae7k']")
                    send.click()
            except:
                pass
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
    def savealldp(self):
        newchat = driver.find_element_by_xpath("//div[@class='_26lC3' and @title='New chat']")
        newchat.click()
        
        driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
        
        total_links = []
        total_names = []
        for i in range(30):
            box = driver.find_elements_by_xpath('//div[@class="_2nY6U"]')
            for i in box:
                B = i.get_attribute('innerHTML')
                soup = bsoup(B)
                images = soup.findAll('img')
                names = soup.find_all("span", {"class": "emoji-texttt _ccCW FqYAR i0jNr"})
                try:
                    if images[0]['src'] not in total_links:
                        total_links.append(images[0]['src'])
                        total_names.append(names[0]['title'])
                except:
                    pass
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            
        c = 0
        for i in range(len(total_links)):
            try:
                driver.get(total_links[i])
                driver.save_screenshot('/home/vishal/Desktop/cool_python/whatsapp/images/'+total_names[i]+".png")

                driver.execute_script('''window.open("http://web.whatsapp.com", "_blank");''')

                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                c = c + 1
            except:
                pass
        print ('Total pictures saved : '+str(c))
        
    def schedular(self, name, tim, msg):#time as dd/mm/yyyy hr:min
        while True:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            if tim != dt_string[0:16]:
                time.sleep(45)
                #print ('Waiting for the correct time')
            else:
                driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text']").clear()

                search = driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
                search.send_keys(name)

                time.sleep(1)

                user = driver.find_element_by_xpath('//span[@title = "{}" and @class="emoji-texttt _ccCW FqYAR i0jNr"]'.format(name))
                user.click()
                
                driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='9']").clear()
                message = driver.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text' and @data-tab='9']")
                message.send_keys(msg)
                send = driver.find_element_by_xpath("//div[@class='_3HQNh _1Ae7k']")
                send.click()
                
                break
        print ('Message sent!!')


# In[17]:


what = Whatsapp()

