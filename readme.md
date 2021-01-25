# AutoCheck Script for JNU

This is a autoscript for JNU health check needless of database or complex encryption. Purely written in python, it uses **Selenium** to complete the work.

## Configuration of thr running environment
  
### 1. Install chrome
```shell
> sudo apt-get update
> sudo apt-get -f install
> wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
> sudo dpkg -i google-chrome*
```
### 2. Install chromedriver
Be careful that you should install the correct version of chromedriver according to the version of chrome. 
```shell
> wget https://npm.taobao.org/mirrors/chromedriver/87.0.4280.88/chromedriver_linux64.zip
> unzip chromedriver*
> mv chromedriver /usr/bin
```

### 3. Install selenium
```shell
> pip install selenium
```

### 4. Set your id and passwd
The Change the correspongding code in the script for your account
```python
log_name.send_keys("") # input your student id the bracket
pwd.send_keys("") # # input your password the bracket
```

## Start the script
```shell script
nohup python -u autoCheck.py >> autoCheck.log 2>&1 &
```
Use the parament u to disable  the output cache of python, otherwise it will not output stdout to the log file. 

