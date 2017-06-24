from selenium import webdriver
import urllib2
from pyvirtualdisplay import Display
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import time 
import re
import smtplib
import gtk.gdk
import os
from time import sleep
 
def intialize():
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	driver = webdriver.Chrome(chrome_options=options)
	driver.get('http://sjce.ac.in/results/')
	Check_Result(driver)

def Check_Result(driver):
	user=driver.find_element_by_css_selector('#USN')
	user.send_keys('4jc11is021')
	login=driver.find_element_by_css_selector('body > div.container.container_12 > div > div > div > div:nth-child(3) > form > input[type="submit"]:nth-child(3)')
	login.click()
	html_content=driver.page_source
	matches=re.findall('No result found',html_content)
	if len(matches)==0:
		driver.execute_script("window.scrollTo(0, 450)")	
		sleep(5)
		w = gtk.gdk.get_default_root_window()
		sz = w.get_size()
		print "The size of the window is %d x %d" % sz
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
		pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
		if (pb != None):
	 	   pb.save("/home/secret95/Desktop/Tracker/screenshot.png","png")
		else:
 	 	  print "Unable to get the screenshot."
 		driver.close()
		img_data = open("/home/secret95/Desktop/Tracker/screenshot.png", 'rb').read()
		msg = MIMEMultipart()
		msg['Subject'] = 'subject'
		msg['From'] = 'test@gmail.com'
		msg['To'] = 'test@gmail.com'
		text = MIMEText("test")
		msg.attach(text)
		image = MIMEImage(img_data, name=os.path.basename("/home/secret95/Desktop/Tracker/screenshot.png"))
		msg.attach(image)
		s = smtplib.SMTP('smtp.gmail.com:587')
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login("test@gmail.com","testpassword") 
		s.sendmail("test@gmail.com","test@gmail.com",msg.as_string())
		s.quit()
		print 'Email sent'

	else:
		back=driver.find_element_by_css_selector('body > div > div > div > div > form > input[type="submit"]')
		back.click()
		print "Results not yet announced. Waiting "
		Check_Result(driver)

intialize()





