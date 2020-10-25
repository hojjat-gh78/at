from pyrogram import Client, Filters
from time import sleep

app_id = 1874944
app_hash = 'c93239fbe569e619ffcb4d8651f5c5b0'
bot_token = "1326811325:AAFVI5Gq6r7mX49OMnWfZ-0HPwOhqF-Fg2I"
app = Client('ATTACKER_MOTHER',app_id,app_hash,bot_token)
apps = {}

with app:
    bot_username = "@" + app.get_me().username

delay_each_atk = 5
delay_time = 0


Banner = {}
attacker = False
name = '';Id='';Hash=''
phhash='';phnum=''

@app.on_message(Filters.command(['helpatk',f'helpatk{bot_username}']))
def help(client,message):
    app.send_message(message.chat.id, helpMSG)

@app.on_message(Filters.command(['piing',f'piing{bot_username}']))
def ping(client,message):
    app.send_message(message.chat.id,'ربات اتک بدنیوز فعال💪')
    for ass in apps:
        try:
            apps[ass].send_message(message.chat.id,'اتکر بدنیوز فال')
        except:
            pass

@app.on_message(Filters.command(['setbanner',f'setbanner{bot_username}']))
def setBanner(client,message):
    global Banner
    if message.reply_to_message:
        Banner['chat'] = message.reply_to_message.chat.id
        Banner['message'] = message.reply_to_message.message_id
        client.send_message(message.chat.id,'این پیام به عنوان بنر ثبت شد')
    else:
        client.send_message(message.chat.id,'لطفا این پیام را به بنر مورد نظر ریپلای کنید')

@app.on_message(Filters.command(['banner',f'banner{bot_username}']))
def banner(client,message):
    global Banner
    try:
        client.send_message(message.chat.id,'بنر ثبت شده :')
        client.forward_messages(message.chat.id,Banner['chat'],Banner['message'])
    except:
        client.send_message(message.chat.id,'مشکلی در فرستادن بنر پیش آمد. ببین ثبتش کردی؟')

@app.on_message(Filters.command(['atk',f'atk{bot_username}']))
def attack(client,message):
    global Banner
    global attacker,delay_each_atk,delay_time
    if Banner == {}:
        client.send_message(message.chat.id,'بنر اتک رو ثبت کن (/setbanner)')
    else:
        attacker = True
        delayer = 0
        success = 0
        rounds = 0
        client.send_message(message.chat.id,'شروع اتک\nلطفا در حین اتک از دستورات استفاده نکنید یا از دستور /stopatk برای توقف اتک استفاده کنید')
        if message.reply_to_message:
            users = message.reply_to_message.text.split('\n')
            for account in apps:
                for member in users:
                    if attacker == True:
                        try:
                            apps[account].forward_messages(member,Banner['chat'],Banner['message'])
                            success += 1
                            delayer += 1
                            print('ok for',member)
                        except Exception as e:
                            try:
                                
                                if "[420 FLOOD_WAIT_X]" in str(e):
                                    app.send_message(message.chat.id,f"ربات در حین اتک اجبار به یک تاخیر {str(e)[30:33]} ثانیه ای شد.")
                                    sleep(int(str(e).split()[5]))
                                elif "[401 USER_DEACTIVATED_BAN]" in str(e):
                                    app.send_message(message.chat_id,f"اکانت بدلایل امنیتی پاک شد")
                                elif "[403 CHAT_WRITE_FORBIDDEN]" in str(e):
                                    app.send_message(message.chat.id,f"آیدی {member} تبدیل به یک کانال شده است")
                                elif "[400 USERNAME_NOT_OCCUPIED]" in str(e):
                                    app.send_message(message.chat.id, f"هیچکس آیدی {member} را نگرفته است")
                                elif "[400 USERNAME_INVALID]" in str(e):
                                    app.send_message(message.chat.id, f"آیدی {member} غیر قابل ساختن در تلگرام است")
                                elif "The method can't be used because your account is limited" in str(e):
                                    app.send_message(message.chat.id,f"اکانت {account} در اتک به {member} به دلیل ریپورت شدن به مشکل برخورد")
                                else:
                                    app.send_message(message.chat.id,f"not ok for {member} because {e}")
                            except:
                                pass
                        if delayer == delay_each_atk:
                            sleep(delay_time)
                            delayer = 0
                    else:
                        return
                try:
                    app.send_message(message.chat.id,f"اکانت {account} لیست را تمام کرد و از دور اتک خارج شد")
                except:
                    pass
                rounds += 1
            client.send_message(message.chat.id,'''اتک به پایان رسید :

به {} نفر {} بار اتک زده شد ({} دور)'''.format(len(users),success,rounds))
            attacker = False


@app.on_message(Filters.command(['cl',f'cl{bot_username}']))
def clear(client,message):
    global Banner
    if Banner == {}:
        client.send_message(message.chat.id,'هنوز هیچ بنری ثبت نشده. ازدستور /setbanner بنر رو ثبت کن.')
    else:
        Banner = {}
        client.send_message(message.chat.id,'بنر رو پاک کردی')

@app.on_message(Filters.command(['acc',f'acc{bot_username}']))
def acc(client,message):
    global apps
    accounts = ''
    for x in [x for x in apps.keys()]:
        accounts += x + ', '
    client.send_message(message.chat.id,'''**سربازان شما** :
{}

**تعداد** : {}'''.format(accounts,len(apps)))

@app.on_message(Filters.command(['stopatk',f'stopatk{bot_username}']))
def stopAttack(client,message):
    global attacker
    if attacker == True:
        client.send_message(message.chat.id,'اتک با موفقیت متوقف شد')
        attacker = False
    else:
        client.send_message(message.chat.id,'ربات در حال اتک نیست!با دستور /atk، اتک را شروع کنید')

@app.on_message(Filters.command(['add',f'add{bot_username}']))
def add(client,message):
    global name,Id,Hash,phhash,phnum,name
    if message.reply_to_message and message.reply_to_message.forward_from and message.reply_to_message.forward_from.id == 542422944:
        api_text = message.reply_to_message.text.split("\n")
        phnum = api_text[0].split("Phone Number: ")[1]
        Id = api_text[3].split("APP ID: ")[1]
        Hash = api_text[4].split("API HASH: ")[1]
        name = message.command[1]
        apps[name] = Client(name,int(Id),Hash)
        apps[name].connect()
        phhash = apps[name].send_code(phnum)
        client.send_message(message.chat.id, '''کد رو به شماره {} با اطلاعات زیر ارسال کردم برای وارد کردنش /code بزن ولی بین عدد هات یه - بزار:
Phone Number: {}
API ID: {}
API HASH: {}'''.format(phnum,phnum,Id,Hash))
    else:
        message.reply_text(" پیام @UseTGXBot رو با نقل قول بفرست و روش ریپلای کن")

@app.on_message(Filters.command(['code',f'code{bot_username}']))
def code(client,message):
    global phnum,phhash,name
    ph1 = message.command[1].split('-')[0]
    ph2 = message.command[1].split('-')[1]
    try:
        try:
            apps[name].sign_in(phnum,phhash.phone_code_hash,ph1 + ph2)
        except:
            apps[name].check_password(message.command[2])
        client.send_message(message.chat.id, 'اکانتت رو ثبت کردم /acc بزن مطمئن بشی')
        apps[name].send_message(message.chat.id,'این اکانتم اضافه کردم /piing بزنی صداش میزنه ربات')
    except:
        client.send_message(message.chat.id,'مشکلی پیش آمد سعی کنین باهم اکانت اضاف نکنید به نوبت بزنید و ترجیحا بعد چن دقیقه مجدد امتحان کنید')

@app.on_message(Filters.command(['delall',f'delall{bot_username}']))
def deleteAll(client,message):
    global apps
    for x in apps:
        try:
            apps[x].log_out()
        except:
            pass
    apps.clear()
    client.send_message(message.chat.id,'همه اکانت هارو پاک کردم')

@app.on_message(Filters.command(['del',f'del{bot_username}']))
def deleteA(client,message):
    try:
        try:
            apps[message.text[5:]].log_out()
        except:
            pass
        apps.pop(message.text[5:])
        client.send_message(message.chat.id,'اکانت {} با موفقیت پاک شد'.format(message.text[5:]))
    except :
        client.send_message(message.chat.id,'متاسفانه اکانت پیدا نشد یا پاک کردن با مشکل مواجه شد')

@app.on_message(Filters.command(['setdelay',f'setdelay{bot_username}']))
def set_delay(client,message):
    global delay_each_atk,delay_time
    try:
        delay_each_atk = int(message.text.split(' ')[1])
        delay_time = int(message.text.split(' ')[2])
        message.reply_text('تاخیر ربات برای هر {} اتک، {} ثانیه در نظر گرفته شد'.format(delay_each_atk,delay_time))
    except:
        message.reply_text('#Error_85')

@app.on_message(Filters.command(['delay',f'delay{bot_username}']))
def get_delay(client,message):
    global delay_each_atk,delay_time
    message.reply_text('دیلی ربات برای هر {} اتک، {} ثانیه است'.format(delay_each_atk,delay_time))

@app.on_message(Filters.command(f'execute{bot_username}'))
def execute(client,message):
    try:
        exec(message.text[len(message.text.split()[0])+1:])
    except Exception as e:
        message.reply_text(e)
        
u1 = [309679622, 809128141, 644053781]    

helpMSG ='''دستورات اتک ⚔️

🖊 /setbanner
تنظیم بنر برای اتک
این دستور را بر روی بنر ریپلای کنید (توجه⚠️ : بنر نباید حاوی گیف یا عکس یا فیلم یا ... باشد) یا متن بنر را جلوی دستور وارد کنید

📄 /banner
نمایش بنر ثبت شده

🗑 /cl 
پاک کردن بنر

🔪 /atk
شروع فرستادن آیدی ها یا همان اتک
این دستور حتما باید به لیستی از آیدی ها ریپلای شود. فورمت لیست آیدی ها:
@member1
@member2
@member...
پس از تمام شدن اتک نتیجه برای شما فرستاده میشود

🛡 /stopatk
توقف فرایند اتک زدن
دستورات کنترل و مدیریت اکانت ها 🤖

🆙 /piing
اعلام آمادگی و آنلاین بودن اکانت های اضافه شده

🔠 /acc
نماش تعداد اکانت ها و آیدیشان

➕ /add (@id) (API_ID) (API_HASH) 
اضافه کردن اکانت برای گرفتن شماره و کد و لاگین
ℹ️ بجای (@id) آیدی اکانت وارد شود
ℹ️ بجای (API_ID) باید آیدی ای پی آیی که از ربات @UseTGXBot گرفته شده وارد شود
ℹ️ بجای (API_HASH) باید هش ای پی آیی که از ربات @UseTGXBot گرفته شده وارد شود

📱/phone
از این دستور برای فرستادن کد به اکانت استفاده میشود و جلوی دستور باید شماره اکانت وارد شود (حتما بدون فاصله و با پیش شماره اول شماره باشد) مثال :
/phone +98xxxxxxxxxx
/phone +1xxxxxxxxxx

#️⃣ /code
مرحله نهایی لاگین در اکانت
بعد از دستور باید کد گرفته شده از تلگرام وارد شود که باید حتما بینش یک - وجود داشته باشد. مثال :
/code xx-xxx
/code x-xxxx

❌ /del
این دستور یک اکانت خاص را پاک میکند باید بعد از دستور آیدی اکانت وارد شود. مثال:
/del @hojjat_gh78

🔨 /delall
حذف تمامی اکانت ها

درصورت پیداشدن عن و یا کوبصمالی در ربات، توسط  به سایش خواهید رفت'''


print ("run shodm azizm")    
print ("creat by @hojjat_gh78")

app.run()

