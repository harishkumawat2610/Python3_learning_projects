from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
input('Enter anything after scanning QR code..typing ok  ')

name = input('Enter the name of user or group : ')

#count number importate 
count = int(input('Enter the count : '))



user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()




if count >=2:
	msg = input('Enter your message : ')
	for i in range(count):
		msg_box = driver.find_element_by_class_name('_2S1VP')
		msg_box.send_keys(msg)
		button = driver.find_element_by_class_name('_35EW6')
		button.click()
elif count == 1:
	while True:
		msg = input('Enter your message : ')
		msg_box = driver.find_element_by_class_name('_2S1VP')
		msg_box.send_keys(msg)
		button = driver.find_element_by_class_name('_35EW6')
		button.click()
		if msg == 'stop':
			break
