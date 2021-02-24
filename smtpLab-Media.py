from socket import *
import base64
import ssl 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

# instance of MIMEMultipart 
message = MIMEMultipart()  
message['From'] = "deneme1530@gmail.com"  
message['To'] = "fnuakyol@gmail.com"   
message['Subject'] = "Image Sending"
body = "\r\n I love computer networks! "
  
# Add Image
message.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "Image.png"
attachment = open("Image.png", "rb")    
image = MIMEBase('application', 'octet-stream') 
image.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(image) 
  
#add filename and positional argument in header
image.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# add image to the message
message.attach(image) 
  
# creates SMTP session 
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.starttls() 
server.login("deneme1530@gmail.com", "EK123456") 
text = message.as_string() 
server.sendmail("deneme1530@gmail.com", "fnuakyol@gmail.com", text) 
print("\nMail is sended!")
server.quit() 


