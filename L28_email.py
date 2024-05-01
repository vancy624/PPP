#寄送 Email 的程式
#準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]="bright_62_53@yahoo.com.tw"
msg["To"]="kaycen2tw@gmail.com"
msg["Subject"]="你好, 德軒"
#寄送純文字的內容
msg.set_content("蛤")
#寄送比較多樣式的內容 (html)
#msg.add_alternative("<h3>優惠券</h3>buy慧give德軒哦", subtype="html")
#連線到 SMTP Sever. 驗證寄件人身分並發送郵件 
import smtplib
#到網路上搜尋 yahoo mail smtp server
server=smtplib.SMTP_SSL("smtp.mail.yahoo.com", 587)
server.login("帳號", "密碼")
server.send_message(msg)
server.close()
