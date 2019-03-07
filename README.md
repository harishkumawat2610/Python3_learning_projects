# Python3_learning_projects

[![N|Solid](https://drive.google.com/uc?id=1n2QFBY4yFSkgpzs_PaxWrTIHo8lMaBbW)](https://github.com/harishkumawat2610/Python3_learning_projects)

[![N|Solid](https://drive.google.com/uc?id=188X9uTU1_VT7TBu4wpnnIvmPizPxSTze)](https://www.facebook.com/harish.kumawat.9638)

# Browser Automation Using Selenium for Facebook auto login and post status on facebook.



[![N|Solid](https://drive.google.com/uc?id=1DXFNnlU789tG8k6Ag28sQaLvmipyCzl4)](https://www.facebook.com/harish.kumawat.9638)
# intro of Selenium
Selenium is a powerful tool for controlling web browser through program. It is functional for all browsers, works on all major OS and its scripts are written in various languages i.e Python, Java, C# etc, we will be working with Python.

Mastering Selenium will help you automate your day to day tasks like controlling your tweets, Whatsapp texting and even just googling without actually opening a browser in just 15-30 lines of python code. The limits of automation is endless with selenium.
# 1.install selenium
```sh
$ pip3 install seleninum
```

##  Web Drivers

  - Selenium requires a web driver to interface with the chosen browser.Web drivers is a package to interact with web browser
  - It interacts with the web browser or a remote web server through a wire protocol which is common to all. You can check out and install the web drivers of your browser choice.
* [Chrome:] - https://sites.google.com/a/chromium.org/chromedriver/downloads
* [Firefox:] - https://github.com/mozilla/geckodriver/releases
* [Safari:] - https://webkit.org/blog/6900/webdriver-support-in-safari-10/

[![N|Solid](https://drive.google.com/uc?id=1DvC0Bb6bg_sMZe3rjgJ5Wh9XnP_bNJdC)](https://www.facebook.com/harish.kumawat.9638)


# Voice Search Engine Assistant
## 1 webbrowser
    The webbrowser module includes functions to open URLs in interactive browser applications. The module includes a registry     of available browsers, in case multiple options are available on the system. It can also be controlled with the BROWSER       environment variable.
    
    webbrowser is part of the python standard library, you don't have to install a separate package to use it because it         comes bundled with your python installation.
    If you get an error like…
    
    ImportError: No module named webbrowser
    
   this means you don’t have installed webbrowser library.

   If it is not installed on your system, you can install it using pip by the following command.
   
```sh
$ pip3 install webbrowser
```

    
    
    
    
## Example
webbrowser.open_new(url)
    Open url in a new window of the default browser, if possible, otherwise,
    open url in the only browser window.

webbrowser.open_new_tab(url)
    Open url in a new page (“tab”) of the default browser, if possible, 
    otherwise equivalent to open_new().
    
    The following table lists predefined browser types. The left column are names that can be passed into the webbrowser.get() method and the right column lists the class names for each browser type.

 - Opening URL in Default Browser:

```sh
# importing webbrowser python module
import webbrowser
#Assigning URL to be opened
strURL = "http://www.myactualfriends.com"
#Open url in default browser
webbrowser.open(strURL, new=2)

```
The new  parameter have special significance.

If new = 0, open URL in same browser window
If new = 1,  opens URL in new browser window
If new = 2, open URL in same tab.

 - Opening URL in specific browser, let’s say in Firefox and Chrome:
 
```sh
import webbrowser
webbrowser.get('firefox').open_new_tab('www.myactualfriends.com')
#Opens URL in Firefox browser
 
webbrowser.get('chrome').open_new_tab('http://www.myactualfriends.com')
#Opens URL in Chrome browser

``` 
   
   
   
   |Type Name | Class Name |
| ------ | ------ |
| 'mozilla' | Mozilla('mozilla') |
| 'firefox' | Mozilla('mozilla') |
| 'netscape' | Mozilla('netscape') |
| 'galeon'| Galeon('galeon') |
|'epiphany' | Galeon('epiphany') |
| 'skipstone'| BackgroundBrowser('skipstone') |
| 'kfmclient' |Konqueror() |
| 'konqueror' | Konqueror() |
| 'kfm' | Konqueror() |
| 'chrome'| Chrome('chrome') |
|'google-chrome' | Chrome('google-chrome') |
| 'safari'| MacOSX('safari') |
| 'chromium' |Chromium('chromium') 
| 'chromium-browser' |Chromium('chromium-browser') |
| 'windows-default' | WindowsDefault |
| 'opera'|Opera() |
|'macosx' | MacOSX('default') |
    
[![N|Solid](https://drive.google.com/uc?id=1traH05ponmZ-CIq2-QmDY7WwIlu7JyYN)](https://www.facebook.com/harish.kumawat.9638)    
# Browser Automation Using Selenium for What'sapp auto message and Chating with terminal.
# intro of Selenium
Selenium is a powerful tool for controlling web browser through program. It is functional for all browsers, works on all major OS and its scripts are written in various languages i.e Python, Java, C# etc, we will be working with Python.

Mastering Selenium will help you automate your day to day tasks like controlling your tweets, Whatsapp texting and even just googling without actually opening a browser in just 15-30 lines of python code. The limits of automation is endless with selenium.
# 1.install selenium
```sh
$ pip3 install seleninum
```

##  Web Drivers

  - Selenium requires a web driver to interface with the chosen browser.Web drivers is a package to interact with web browser
  - It interacts with the web browser or a remote web server through a wire protocol which is common to all. You can check out and install the web drivers of your browser choice.
* [Chrome:] - https://sites.google.com/a/chromium.org/chromedriver/downloads
* [Firefox:] - https://github.com/mozilla/geckodriver/releases
* [Safari:] - https://webkit.org/blog/6900/webdriver-support-in-safari-10/

## Example
1 - Scan Qr code

[![N|Solid](https://drive.google.com/uc?id=130eKCveR_QLj2SmotDtW1d4v6g0iAPbM)]

## 2 - Enter count Value

### if count value Greater then 1
#### output:-
[![N|Solid](https://drive.google.com/uc?id=1yIQgCHVeZ1NswCz-jNujjRNpXIRuw-7z)] 

### if count value equal to 1
#### output:-
[![N|Solid](https://drive.google.com/uc?id=1wmlu7-wQHn_0WqMCpDAFrfiBsERmM4Dx)]

## Stop Chating
#### output:-
[![N|Solid](https://drive.google.com/uc?id=1HbFTDO7cuBJnX0roL8jxh_ka07ugaSRd)]() 

[![N|Solid](https://drive.google.com/uc?id=1w0uI2u4SMUwpJgiSo00fBcbgIlZm6tO2)]() 

#  Recording Video From CCTV and Rstp ip address with Help of OpenCv and Python3


   
### Given an IP camera:

- Find your camera IP address
- Find the port where the IP address is accessed
- Find the protocol (HTTP/RTSP etc.) specified by the camera provider
Then, if your camera is protected go ahead and find out:

- your username
- your password
import cv2

```sh stream = cv2.VideoCapture('protocol://IP:port/1') ```

### Use the next line if your camera has a username and password
 ```sh stream = cv2.VideoCapture('protocol://username:password@IP:port/1') ```
 
 
 # Next project is gui for download youtube videos and audios by our applications
