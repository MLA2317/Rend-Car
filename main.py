from aiogram import executor
from config import dp, bot
from Inline import *
from Keyboard import *
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, CallbackQuery

import logging

@dp.message_handler(commands='start')
async def start(msg: Message):
    txt = f"Assalomu Aleykum {msg.from_user.full_name}!\n Moshina Arenda botga, Hush kelibsiz!"
    await msg.answer(txt, reply_markup=menuStart)

# help
@dp.message_handler(commands='help')
async def help(msg: Message):
    await msg.answer(f"Murajat uchun: @lazizbek_a", reply_markup=menuStart)

# menuStart
@dp.message_handler(text="Mashinalar rent")
async def bolim(msg: Message):
    print(logging.info(msg.from_user.id))
    print(logging.info(msg.from_user.full_name))
    print(logging.info(msg.from_user.get_profile_photos))
    print(msg.from_user.values)
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png", "rb")
    await msg.answer_photo(img, f"Quidagilarni Tanlang!", reply_markup=Moshinala)

@dp.callback_query_handler(text="👍🏻")
async def like(call: CallbackQuery):
    await call.answer(f"Yo'qti", show_alert=True)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="❌")
async def exit(call: CallbackQuery):
    await call.message.delete()

@dp.callback_query_handler(text="👎🏻")
async def dislike(call: CallbackQuery):
    await call.answer(f"Yo'qmadi", show_alert=True)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="orqaga")
async def orqaga(call: CallbackQuery):
    img = open("image/336070405.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Audi)
    await call.message.delete()


@dp.callback_query_handler(text="bentleyorqaga")
async def bentorqaga(call: CallbackQuery):
    img = open("image/Bentley logo emblem_ Always loved this logo.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Bentley)
    await call.message.delete()

@dp.callback_query_handler(text="bmworqaga")
async def bentorqaga(call: CallbackQuery):
    img = open("image/Без названия.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Bmw)
    await call.message.delete()

@dp.callback_query_handler(text="kadilakorqaga")
async def kadorqaga(call: CallbackQuery):
    img = open("image/Cadillac Logo Wallpaper.png", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Kadilak)
    await call.message.delete()

@dp.callback_query_handler(text="ferrariorqaga")
async def ferorqaga(call: CallbackQuery):
    img = open("image/Ferrari logo.jpeg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Ferrari)
    await call.message.delete()

@dp.callback_query_handler(text="hyundaiorqaga")
async def hyuorqaga(call: CallbackQuery):
    img = open("image/Hyundai Australia (@HyundaiAus) _ Twitter.jpeg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Hyundai)
    await call.message.delete()

@dp.callback_query_handler(text="kiaorqaga")
async def kiaorqaga(call: CallbackQuery):
    img = open("image/Kia Motors presenta en el KIPRIS la patente de su nuevo logo corporativo.jpeg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Kia)
    await call.message.delete()

@dp.callback_query_handler(text="lamborgorqaga")
async def lamboorqa(call: CallbackQuery):
    img = open("image/Lamborghini Logo.jpeg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Lamborghini)
    await call.message.delete()

@dp.callback_query_handler(text="maserorqaga")
async def maserorqa(call: CallbackQuery):
    img = open("image/maserati.jpeg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Maserati)
    await call.message.delete()

@dp.callback_query_handler(text="rangeorqaga")
async def rangeorqa(call: CallbackQuery):
    img = open("image/Land Rover (@LandRover).png", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Rangerover)
    await call.message.delete()

@dp.callback_query_handler(text="dodgeorqaga")
async def rangeorqa(call: CallbackQuery):
    img = open("image/Dodge logo.jpeg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Dodge)
    await call.message.delete()

@dp.callback_query_handler(text="teslaorqaga")
async def teslaorqa(call: CallbackQuery):
    img = open("image/tesla.jpeg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Tesla)
    await call.message.delete()

@dp.callback_query_handler(text="shevrorqaga")
async def chevorqa(call: CallbackQuery):
    img = open("image/GM _ Chevrolet Bowtie Logo Camaro Corvette Truck Adult T-shirt  _ eBay.jpeg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, caption=txt, reply_markup=Chevrolet)
    await call.message.delete()

@dp.callback_query_handler(text="🛒")
async def boglash(call: CallbackQuery):
    txt = f"Ish Voqti - 9:00 vs 20:00\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=menuStart)





@dp.message_handler(text="Bog'lanish")
async def boglanish(msg: Message):
    txt = f"Bizga bog'lanish uchun shunga murajat qiling: @lazizbek_a" \
          f"\n" \
          f"\n" \
          f"\nTel: 99-085-23-17" \
          f"\nhttps://www.instagram.com/lazizbek__a/"
    await msg.answer(txt, reply_markup=menuStart)



@dp.message_handler(text="Bizning botlar")
async def bizningbot(msg: Message):
    txt = f"1. @musics_xit_bot\n" \
          f"2. @free_lesson_course_bot\n" \
          f"3. @fast_food_ml_bot"
    await msg.answer(txt, reply_markup=menuStart)



@dp.callback_query_handler(text="audi")
async def audi(call: CallbackQuery):
    img = open("image/336070405.jpg", "rb")
    await call.message.answer_photo(img, reply_markup=Audi)
    await call.message.delete()

@dp.callback_query_handler(text="a1")
async def audia1(call: CallbackQuery):
    img = open("Moshinala/Audi/2015_Facelift_Audi_A1_Typ_8X_1.8_TFSI_S_tronic_141_kW_Vorderansicht_Misanorot-Perleffekt_Col_de_Braus.jpg", "rb")
    txt = f"Audi A1 - 2015\n" \
          f"Rangi - Qizil🚘\n" \
          f"100km - 10.3L🚘\n" \
          f"𝗡𝗮𝗿𝘅𝗶 - 𝟭𝟱𝟬$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="a3")
async def audia3(call: CallbackQuery):
    img = open("Moshinala/Audi/2020_Audi_A3_S_Line_Edition_1_35_TD_2.0.jpg", "rb")
    txt = f"Audi A3 - 2020\n" \
          f"Rangi - Oq🚘\n" \
          f"100km - 12.3L🚘\n" \
          f"𝗡𝗮𝗿𝘅𝗶 - 𝟭𝟱𝟬$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="a4")
async def audia4(call: CallbackQuery):
    img = open("Moshinala/Audi/Audi_A4_B9_Limousine_3.0_TDI_quattro.jpg", "rb")
    txt = f"Audi A4 - 2021\n" \
          f"Rangi - Oq🚘\n" \
          f"100km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟑𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="a6")
async def audia6(call: CallbackQuery):
    img = open("Moshinala/Audi/Audi_A6_2018_(44686505662).jpg", "rb")
    txt = f"Audi A6 - 2021\n" \
          f"Rangi - Qora🚘\n" \
          f"100km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟔𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="q4")
async def audiq4(call: CallbackQuery):
    img = open("Moshinala/Audi/Audi_Q4_Sportback_e-tron_IAA_2021_1X7A0159.jpg", "rb")
    txt = f"Audi Q4 - 2022\n" \
          f"Rangi - Qora🚘\n" \
          f"Electrict - full 400km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="q7")
async def audiq7(call: CallbackQuery):
    img = open("Moshinala/Audi/Audi_Q7_3.0_TDI_Quattro.png", "rb")
    txt = f"Audi Q7 - 2022\n" \
          f"Rangi - Qora🚘\n" \
          f"100km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="q8")
async def audiq8(call: CallbackQuery):
    img = open("Moshinala/Audi/2019_Audi_Q8_Front.jpg", "rb")
    txt = f"Audi Q8 - 2022\n" \
          f"Rangi - Qora🚘\n" \
          f"Electrict -full 400km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟒𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="r8")
async def audir8(call: CallbackQuery):
    img = open("Moshinala/Audi/Audi_R8_2017_Convertible.jpg", "rb")
    txt = f"Audi R8 - 2022\n" \
          f"Rangi - Qora🚘\n" \
          f"100km - 20L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟎𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="audiorqa")
async def audiorqaga(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png", "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()




@dp.callback_query_handler(text="bentley")
async def bentley(call: CallbackQuery):
    img = open("image/Bentley logo emblem_ Always loved this logo.jpg", "rb")
    await call.message.answer_photo(img, reply_markup=Bentley)
    await call.message.delete()

@dp.callback_query_handler(text="bent1")
async def bentazure(call: CallbackQuery):
    img = open("Moshinala/Bentley/07_Bentley_Azure_(9885310443).jpg", "rb")
    txt = f"Bentley Azure - 2006\n" \
          f"Rangi - Qora🚘\n" \
          f"100km - 14.3L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks1)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="bent3")
async def bentbrook(call: CallbackQuery):
    img = open("Moshinala/Bentley/Bentley_Brooklands_–_Frontansicht,_10._August_2011,_Düsseldorf.jpg", "rb")
    txt = f"Bentley Brooklands - 2011\n" \
          f"Rangi - Qora🚘\n" \
          f"100km - 15.6L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks1)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="bent4")
async def bentazure1(call: CallbackQuery):
    img = open("Moshinala/Bentley/1996_Bentley_Azure,_front_right.jpg", "rb")
    txt = f"Bentley Azure - 1996\n" \
          f"Rangi - Seriy🚘\n" \
          f"100km - 13.1L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks1)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="bent6")
async def bentarnage(call: CallbackQuery):
    img = open("Moshinala/Bentley/2009_Bentley_Arnage_Final_Series.jpg", "rb")
    txt = f"Bentley Arnage - 2009\n" \
          f"Rangi - Qora🚘\n" \
          f"100km - 12.4L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟒𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks1)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="bent7")
async def bentcontiental(call: CallbackQuery):
    img = open("Moshinala/Bentley/2010-2011_Bentley_Continental_(3W)_Supersports_convertible_(2011-11-01)_01.jpg", "rb")
    txt = f"Bentley Continental(ochiq tom) - 2011\n" \
          f"Rangi - Oq🚘\n" \
          f"100km - 13.3L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks1)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="bent8")
async def bentcontiental1(call: CallbackQuery):
    img = open("Moshinala/Bentley/2019_Bentley_Continental_GT_Automatic_6.0.jpg", "rb")
    txt = f"Bentley Continental - 2019\n" \
          f"Rangi - Oq🚘\n" \
          f"100km - 11.1L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟏𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks1)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="bent9")
async def bentspur(call: CallbackQuery):
    img = open("Moshinala/Bentley/2019_Bentley_Flying_Spur_W12_Front.jpg", "rb")
    txt = f"Bentley Flying Spur - 2021\n" \
          f"Rangi - Och kok🚘\n" \
          f"100km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟓𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks1)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="bent2")
async def bentbenteyga(call: CallbackQuery):
    img = open("Moshinala/Bentley/2022_Bentley_Bentayga_S_(V8).jpg", "rb")
    txt = f"Bentley Benteyga S - 2022\n" \
          f"Rangi - OQ🚘\n" \
          f"100km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟏𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks1)
    await call.answer(cache_time=30)
    await call.message.delete()


@dp.callback_query_handler(text="bentorqa")
async def bentorqaga(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png", "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()




@dp.callback_query_handler(text="bmw")
async def bmw(call: CallbackQuery):
    img = open("image/Без названия.jpg", "rb")
    await call.message.answer_photo(img, reply_markup=Bmw)
    await call.message.delete()

@dp.callback_query_handler(text="b1")
async def bmw8s(call: CallbackQuery):
    img = open("Moshinala/BMW/2018_BMW_8_Series_G15.jpg", "rb")
    txt = f"Bmw 8series - 2019\n" \
          f"Rangi - Kok🚘\n" \
          f"100km - 15L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()


@dp.callback_query_handler(text="b2")
async def bmwx2(call: CallbackQuery):
    img = open("Moshinala/BMW/2018_BMW_X2_xDrive20D_M_Sport_X_Automatic_2.0.jpg", "rb")
    txt = f"Bmw X2 - 2018\n" \
          f"Rangi - Sariq🚘\n" \
          f"100km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟒𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b3")
async def bmwx3(call: CallbackQuery):
    img = open("Moshinala/BMW/2019_BMW_X3_au_SIAM_2019.jpg", "rb")
    txt = f"Bmw X3 - 2019\n" \
          f"Rangi - Kok🚘\n" \
          f"100km - 13L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟒𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b4")
async def bmwx5(call: CallbackQuery):
    img = open("Moshinala/BMW/2019_BMW_X5_M50d_3.0_Front.jpg", "rb")
    txt = f"Bmw X5 - 2019\n" \
          f"Rangi - Oq🚘\n" \
          f"100km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟓𝟎𝟓$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b5")
async def bmwz4(call: CallbackQuery):
    img = open("Moshinala/BMW/2019_BMW_Z4_sDrive_M40i_Sport.jpg", "rb")
    txt = f"Bmw Z4 - 2019\n" \
          f"Rangi - Qizil🚘\n" \
          f"100km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟐𝟓$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b6")
async def bmwm2(call: CallbackQuery):
    img = open("Moshinala/BMW/2020_BMW_M235i_xDrive_Gran_Coupe_Front.jpg", "rb")
    txt = f"Bmw M2 - 2020\n" \
          f"Rangi - kok🚘\n" \
          f"100km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟓𝟓$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b7")
async def bmwX6(call: CallbackQuery):
    img = open("Moshinala/BMW/2020_BMW_X6_xDrive30d_M_Sport_Automatic_3.0.jpg", "rb")
    txt = f"Bmw X6 - 2020\n" \
          f"Rangi - kok🚘\n" \
          f"100km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟒𝟎𝟓$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b8")
async def bmw6s(call: CallbackQuery):
    img = open("Moshinala/BMW/2021_BMW_6-Series_630i_GT_M_Sport.jpg", "rb")
    txt = f"Bmw 6s - 2021\n" \
          f"Rangi - Seriy🚘\n" \
          f"100km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟓𝟓𝟓$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b9")
async def bmwx1(call: CallbackQuery):
    img = open("Moshinala/BMW/2022_BMW_X1_CRI_02_2022_5075.jpg", "rb")
    txt = f"Bmw X1 - 2022\n" \
          f"Rangi - Kok🚘\n" \
          f"100km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟒𝟑𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b10")
async def bmw7s(call: CallbackQuery):
    img = open("Moshinala/BMW/BMW_7_SERIES_LWB_(G11)_China_(4).jpg", "rb")
    txt = f"Bmw S7 - 2022\n" \
          f"Rangi - Qora🚘\n" \
          f"100km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b11")
async def bmw7s(call: CallbackQuery):
    img = open("Moshinala/BMW/BMW x5.jpeg", "rb")
    txt = f"Bmw X7 - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"100km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟕𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b12")
async def bmwg20(call: CallbackQuery):
    img = open("Moshinala/BMW/BMW_G20_JM_0026.jpg", "rb")
    txt = f"Bmw G20 - 2022\n" \
          f"Rangi - Kok🚘\n" \
          f"100km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b13")
async def bmwgi7(call: CallbackQuery):
    img = open("Moshinala/BMW/BMW_i7.jpg", "rb")
    txt = f"Bmw i7 - 2022\n" \
          f"Rangi - Seriy🚘\n" \
          f"Electric full 400km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟖𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="b14")
async def bmwgix(call: CallbackQuery):
    img = open("Moshinala/BMW/BMW_iX_Sport_CRI_04_2022_5609 — копия.jpg", "rb")
    txt = f"Bmw iX - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"Electric full 450km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 1000$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks2)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="bmworqa")
async def bmworqaga(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png", "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()



@dp.callback_query_handler(text="cadilac")
async def cadilak(call: CallbackQuery):
    img = open("image/Cadillac Logo Wallpaper.png", "rb")
    await call.message.answer_photo(img, reply_markup=Kadilak)
    await call.message.delete()

@dp.callback_query_handler(text="c1")
async def k1(call: CallbackQuery):
    img = open("Moshinala/Cadilac/1965_Cadillac_Eldorado_(28371304067).jpg", "rb")
    txt = f"Cadilak Eldorado - 1965\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 16L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟕𝟑𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks3)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="c2")
async def k2(call: CallbackQuery):
    img = open("Moshinala/Cadilac/2014_Cadillac_ELR_trimmed.jpg", "rb")
    txt = f"Cadilak ELR - 2014\n" \
          f"Rangi - Qora🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟓𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks3)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="c3")
async def k3(call: CallbackQuery):
    img = open("Moshinala/Cadilac/2018_Cadillac_XTS_(facelift,_front).jpg", "rb")
    txt = f"Cadilak XTS - 2018\n" \
          f"Rangi - Qora🚘\n" \
          f"100 km - 13L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟓𝟕𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks3)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="c4")
async def k4(call: CallbackQuery):
    img = open("Moshinala/Cadilac/2019_Cadillac_CT5_350T_with_door_opened,_front_NYIAS_2019.jpg", "rb")
    txt = f"Cadilak CT5 - 2019\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟒𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks3)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="c5")
async def k5(call: CallbackQuery):
    img = open("Moshinala/Cadilac/2019_Cadillac_CT6_Premium_Luxury,_front_8.28.19.jpg", "rb")
    txt = f"Cadilak CT6 - 2019\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟕𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks3)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="c6")
async def k6(call: CallbackQuery):
    img = open("Moshinala/Cadilac/2019_Cadillac_CT6_V-Sport_front_4.2.18.jpg", "rb")
    txt = f"Cadilak CT6 (sport) - 2019\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟕𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks3)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="c7")
async def k7(call: CallbackQuery):
    img = open("Moshinala/Cadilac/2020_Cadillac_CT4_Premium_Luxury,_front_5.7.21.jpg", "rb")
    txt = f"Cadilak CT4 - 2020\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks3)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="c8")
async def k8(call: CallbackQuery):
    img = open("Moshinala/Cadilac/2021_Cadillac_Escalade_ESV_4WD_Premium_Luxury_in_Satin_Steel_Metallic,_front_right.jpg", "rb")
    txt = f"Cadilak Escilade - 2021\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks3)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="c9")
async def k9(call: CallbackQuery):
    img = open("Moshinala/Cadilac/Cadillac_XLR_2006.jpg", "rb")
    txt = f"Cadilak XLR - 2006\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟒𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks3)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="Cadilakorqa")
async def cadiorqaga(call: CallbackQuery):
    img = open(
        "image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png",
        "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()


@dp.callback_query_handler(text="ferrari")
async def cadilak(call: CallbackQuery):
    img = open("image/Ferrari logo.jpeg", "rb")
    await call.message.answer_photo(img, reply_markup=Ferrari)
    await call.message.delete()

@dp.callback_query_handler(text="f1")
async def f1(call: CallbackQuery):
    img = open("Moshinala/Ferrari/1959_Ferrari_250GT_Coupé_by_Pinin_Farina_-_fvr-1_(4637722958).jpg", "rb")
    txt = f"Ferrari 250GT - 1959\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 16L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟖𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks4)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="f2")
async def f2(call: CallbackQuery):
    img = open("Moshinala/Ferrari/1965_Ferrari_275.jpg", "rb")
    txt = f"Ferrari 275 - 1965\n" \
          f"Rangi - Sariq🚘\n" \
          f"100 km - 20L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟗𝟐𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks4)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="f3")
async def f3(call: CallbackQuery):
    img = open("Moshinala/Ferrari/2019_Ferrari_812_Superfast_S-A_6.5.jpg", "rb")
    txt = f"Ferrari 812 SuperFast - 2019\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 22L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟏𝟐𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks4)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="f4")
async def f4(call: CallbackQuery):
    img = open("Moshinala/Ferrari/2020_Ferrari_F8_Tributo_3.9.jpg", "rb")
    txt = f"Ferrari F8 - 2020\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 22L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟏𝟐𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks4)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="f5")
async def f5(call: CallbackQuery):
    img = open("Moshinala/Ferrari/Ferrari_328_GTS_-_Flickr_-_Alexandre_Prévot_(4)_(cropped).jpg", "rb")
    txt = f"Ferrari 328 GTS - 1990\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 20L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟖𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks4)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="f6")
async def f6(call: CallbackQuery):
    img = open("Moshinala/Ferrari/Ferrari_488_GTB.jpg", "rb")
    txt = f"Ferrari 488 GTB - 2020\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 20L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟒𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks4)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="f7")
async def f7(call: CallbackQuery):
    img = open("Moshinala/Ferrari/Ferrari_612_Scaglietti_-_Flickr_-_Alexandre_Prévot_(16)_(cropped).jpg", "rb")
    txt = f"Ferrari 612 - 2018\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 18L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟖𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks4)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="f8")
async def f8(call: CallbackQuery):
    img = open("Moshinala/Ferrari/Ferrari_F60_America_-_Museo_Ferrari_(17514670344).jpg", "rb")
    txt = f"Ferrari F60 - 2018\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 17L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟏𝟗𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks4)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="f9")
async def f9(call: CallbackQuery):
    img = open("Moshinala/Ferrari/Ferrari_Portofino_M_IMG_4351.jpg", "rb")
    txt = f"Ferrari ortofino - 2021\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 16L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟐𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks4)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="Ferrariorqa")
async def cadiorqaga(call: CallbackQuery):
    img = open(
        "image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png",
        "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()




@dp.callback_query_handler(text="hyundai")
async def hyundai(call: CallbackQuery):
    img = open("image/Hyundai Australia (@HyundaiAus) _ Twitter.jpeg", "rb")
    await call.message.answer_photo(img, reply_markup=Hyundai)
    await call.message.delete()

@dp.callback_query_handler(text="h1")
async def h1(call: CallbackQuery):
    img = open("Moshinala/Hyundai/2018_Hyundai_i30_Premium_S-A_Fastback_1.3_Front.jpg", "rb")
    txt = f"Hyundai i30 - 2018\n" \
          f"Rangi - Mokriy asfalt🚘\n" \
          f"100 km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks5)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="h2")
async def h2(call: CallbackQuery):
    img = open("Moshinala/Hyundai/2019_Hyundai_Accent_Preferred_in_Urban_Grey,_Front_Left,_05-22-2022.jpg", "rb")
    txt = f"Hyundai Preffered - 2019\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟔𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks5)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="h3")
async def h3(call: CallbackQuery):
    img = open("Moshinala/Hyundai/2020_Hyundai_Palisade_SEL,_front_3.2.20.jpg", "rb")
    txt = f"Hyundai Palisade - 2020\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks5)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="h4")
async def h4(call: CallbackQuery):
    img = open("Moshinala/Hyundai/2021_Hyundai_Accent_1.4_Value_(Chile)_front_view.jpg", "rb")
    txt = f"Hyundai 1.4Value - 2020\n" \
          f"Rangi - Qora🚘\n" \
          f"100 km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks5)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="h5")
async def h5(call: CallbackQuery):
    img = open("Moshinala/Hyundai/2021_Hyundai_Alcazar_2.0_Signature_(India)_front_view.png", "rb")
    txt = f"Hyundai Alcazar - 2020\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟐𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks5)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="h6")
async def h6(call: CallbackQuery):
    img = open("Moshinala/Hyundai/2021_Hyundai_Sonata_1.6T_Luxury,_Front_Right,_05-24-2021.jpg", "rb")
    txt = f"Hyundai Sonata - 2021\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟒𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks5)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="h7")
async def h7(call: CallbackQuery):
    img = open("Moshinala/Hyundai/2023_Hyundai_HB20_1.0_T-GDi_Platinum_Plus_(Brazil)_front_view.png", "rb")
    txt = f"Hyundai HB20 - 2023\n" \
          f"Rangi - Seriy🚘\n" \
          f"Electrikt - Hybrid 300km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟗𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks5)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="h8")
async def h8(call: CallbackQuery):
    img = open("Moshinala/Hyundai/Hyundai_Avante_CN7_white_(10)_(cropped).jpg", "rb")
    txt = f"Hyundai Elentra - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟏𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks5)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="h9")
async def h9(call: CallbackQuery):
    img = open("Moshinala/Hyundai/Hyundai_Bayon_IMG_5005.jpg", "rb")
    txt = f"Hyundai Bayon - 2021\n" \
          f"Rangi - Oq🚘\n" \
          f"100km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟏𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks5)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="Hyundaiorqa")
async def hyunorqaga(call: CallbackQuery):
    img = open(
        "image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png",
        "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()



@dp.callback_query_handler(text="kia")
async def kia(call: CallbackQuery):
    img = open("image/Kia Motors presenta en el KIPRIS la patente de su nuevo logo corporativo.jpeg", "rb")
    await call.message.answer_photo(img, reply_markup=Kia)
    await call.message.delete()

@dp.callback_query_handler(text="k1")
async def k1(call: CallbackQuery):
    img = open("Moshinala/Kia/2020_Kia_Sorento_4_HEV_AWD_Automatic_1.6_Front.jpg", "rb")
    txt = f"Kia Sorento - 2021\n" \
          f"Rangi - Oq🚘\n" \
          f"100km - 13L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟏𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k2")
async def k2(call: CallbackQuery):
    img = open("Moshinala/Kia/2021_Kia_EV6_GT-Line_S.jpg", "rb")
    txt = f"Kia EV6 - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"Electric - 300km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟑𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k3")
async def k3(call: CallbackQuery):
    img = open("Moshinala/Kia/2021_Kia_Rio_3_MHEV_facelift_1.0.jpg", "rb")
    txt = f"Kia Rio3 - 2020\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟗𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k4")
async def k4(call: CallbackQuery):
    img = open("Moshinala/Kia/2021_Kia_Seltos_EX_AWD_in_Gravity_Grey,_Front_Left,_06-16-2022.jpg", "rb")
    txt = f"Kia Seltos - 2017\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟕𝟓$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k5")
async def k5(call: CallbackQuery):
    img = open("Moshinala/Kia/2021_Kia_Sonet_1.5_Premiere_(Indonesia)_front_view_03.jpg", "rb")
    txt = f"Kia Sonet - 2016\n" \
          f"Rangi - Sariq🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k6")
async def k6(call: CallbackQuery):
    img = open("Moshinala/Kia/2022_Kia_Forte5_GT_in_Snow_White_Pearl,_Front_Left,_05-22-2022.jpg", "rb")
    txt = f"Kia Forte 5 - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k7")
async def k7(call: CallbackQuery):
    img = open("Moshinala/Kia/2022_Kia_K5_GT-Line_in_Pacific_Blue,_Front_Left,_09-05-2022.jpg", "rb")
    txt = f"Kia K5 - 2022\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟑𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k8")
async def k8(call: CallbackQuery):
    img = open("Moshinala/Kia/20201013_Kia_Carnival_Front_Side_(cropped).jpg", "rb")
    txt = f"Kia Carnival - 2021\n" \
          f"Rangi - Qora🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟏𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k9")
async def k9(call: CallbackQuery):
    img = open("Moshinala/Kia/Kia_K7_YG_FL_white_(cropped).jpg", "rb")
    txt = f"Kia K7 - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟕𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k10")
async def k10(call: CallbackQuery):
    img = open("Moshinala/Kia/Kia_K8_Hybrid_GL3_HEV_Snow_White_Pearl_(1)_(cropped).jpg", "rb")
    txt = f"Kia K8 - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟎𝟓$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="k11")
async def k11(call: CallbackQuery):
    img = open("Moshinala/Kia/Kia_K9_RJ_FL_Silky_Silver_(1)_(cropped).jpg", "rb")
    txt = f"Kia K9 - 2022\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks6)
    await call.answer(cache_time=30)
    await call.message.delete()


@dp.callback_query_handler(text="Kiaorqa")
async def kiaorqa(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png",
               "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()




@dp.callback_query_handler(text="lamborghini")
async def kia(call: CallbackQuery):
    img = open("image/Lamborghini Logo.jpeg", "rb")
    await call.message.answer_photo(img, reply_markup=Lamborghini)
    await call.message.delete()

@dp.callback_query_handler(text="l1")
async def l1(call: CallbackQuery):
    img = open("Moshinala/Lamborghini/2014-03-04_Geneva_Motor_Show_1375.jpg", "rb")
    txt = f"Lamborghini Aventador - 2021\n" \
          f"Rangi - Sariq🚘\n" \
          f"100 km - 22L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟔𝟕𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks7)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="l2")
async def l2(call: CallbackQuery):
    img = open("Moshinala/Lamborghini/This Lamborghini Sian is trying to be discreet in that Silver spec.jpeg", "rb")
    txt = f"Lamborghini Sian - 2022\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 30L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟏𝟎𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks7)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="l3")
async def l3(call: CallbackQuery):
    img = open("Moshinala/Lamborghini/Gray_Lamborghini_LP640.jpg", "rb")
    txt = f"Lamborghini 1 - 2014\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 23L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟖𝟕𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks7)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="l4")
async def l4(call: CallbackQuery):
    img = open("Moshinala/Lamborghini/Lamborghini_350_GT_1964.jpg", "rb")
    txt = f"Lamborghini 350 GT - 1990\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 15L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟐𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks7)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="l5")
async def l5(call: CallbackQuery):
    img = open("Moshinala/Lamborghini/Lamborghini_Aventador_LP_700-4_-_Flickr_-_Alexandre_Prévot_(2)_(cropped).jpg", "rb")
    txt = f"Lamborghini Aven - 2012\n" \
          f"Rangi - Orange🚘\n" \
          f"100 km - 18L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟗𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks7)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="l6")
async def l6(call: CallbackQuery):
    img = open("Moshinala/Lamborghini/Lamborghini_Countach_LP500S.jpg", "rb")
    txt = f"Lamborghini Countach - 1987\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 22L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟕𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks7)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="l7")
async def l7(call: CallbackQuery):
    img = open("Moshinala/Lamborghini/Lamborghini_Urus_20180306_Genf_2018.jpg", "rb")
    txt = f"Lamborghini Urus - 2021\n" \
          f"Rangi - Sariq🚘\n" \
          f"100 km - 25L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟑𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks7)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="l8")
async def l8(call: CallbackQuery):
    img = open("Moshinala/Lamborghini/Yellow_Lamborghini_Gallardo_edit.jpg", "rb")
    txt = f"Lamborghini Gollardo - 2013\n" \
          f"Rangi - Sariq🚘\n" \
          f"100 km - 21L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟖𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks7)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="Lamboorqa")
async def lamborqaga(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png", "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()



@dp.callback_query_handler(text="maserati")
async def kia(call: CallbackQuery):
    img = open("image/maserati.jpeg", "rb")
    await call.message.answer_photo(img, reply_markup=Maserati)
    await call.message.delete()

@dp.callback_query_handler(text="m1")
async def m1(call: CallbackQuery):
    img = open("Moshinala/Maserati/Maserati_GranCabrio_Fendi_(6147394898).jpg", "rb")
    txt = f"Maserati Fendi - 2022\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 20L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟐𝟑𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks8)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="m2")
async def m2(call: CallbackQuery):
    img = open("Moshinala/Maserati/Maserati_GranCabrio_Sport,_Melbourne_IMS_2011.jpg", "rb")
    txt = f"Maserati Sport - 2022\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 22L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟒𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks8)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="m3")
async def m3(call: CallbackQuery):
    img = open("Moshinala/Maserati/Maserati_Gransport_Spyder_-_gray.jpg", "rb")
    txt = f"Maserati Spyder - 2013\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 15L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟓𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks8)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="m4")
async def m4(call: CallbackQuery):
    img = open("Moshinala/Maserati/Maserati_GranTurismo_-_Flickr_-_exfordy_(1).jpg", "rb")
    txt = f"Maserati Flickr - 2015\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 16L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟔𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks8)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="m5")
async def m5(call: CallbackQuery):
    img = open("Moshinala/Maserati/Maserati_MC20_Milano_1.jpg", "rb")
    txt = f"Maserati MC20 - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 18L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟒𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks8)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="Maseorqa")
async def maserorqa(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png",
               "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()





@dp.callback_query_handler(text="rangerover")
async def kia(call: CallbackQuery):
    img = open("image/Land Rover (@LandRover).png", "rb")
    await call.message.answer_photo(img, reply_markup=Rangerover)
    await call.message.delete()

@dp.callback_query_handler(text="r1")
async def r1(call: CallbackQuery):
    img = open("Moshinala/Range rover/2004_Range_Rover_V8_Vogue_by_The_Car_Spy.jpg", "rb")
    txt = f"Range Rover Vogue - 2004\n" \
          f"Rangi - Qora🚘\n" \
          f"100 km - 18L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks9)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="r2")
async def r2(call: CallbackQuery):
    img = open("Moshinala/Range rover/2012_Land_Rover_Discovery_4_(L319_MY12)_TDV6_wagon_(2015-08-07)_01.jpg", "rb")
    txt = f"Range Rover Discovery - 2005\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 16L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks9)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="r3")
async def r3(call: CallbackQuery):
    img = open("Moshinala/Range rover/2015_Land_Rover_Range_Rover_Sport_HSE_3.0_Front.jpg", "rb")
    txt = f"Range Rover Sport - 2015\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟐𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks9)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="r4")
async def r4(call: CallbackQuery):
    img = open("Moshinala/Range rover/2017_Land_Rover_Range_Rover_Velar_First_Edition_D3_3.0_Front.jpg", "rb")
    txt = f"Range Rover Velar - 2017\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟔𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks9)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="r5")
async def r5(call: CallbackQuery):
    img = open("Moshinala/Range rover/2017_Range_Rover_Vogue.jpg", "rb")
    txt = f"Range Rover Vogue - 2017\n" \
          f"Rangi - Qora🚘\n" \
          f"100 km - 13L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks9)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="r6")
async def r6(call: CallbackQuery):
    img = open("Moshinala/Range rover/2022_Land_Rover_Range_Rover_SE_P440e_AWD_Automatic_3.0_Front.jpg", "rb")
    txt = f"Range Rover SE - 2022\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟒𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks9)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="Rangeorqa")
async def rangeorqa(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png",
               "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()


@dp.callback_query_handler(text="dodge")
async def dodge(call: CallbackQuery):
    img = open("image/Dodge logo.jpeg", "rb")
    await call.message.answer_photo(img, reply_markup=Dodge)
    await call.message.delete()

@dp.callback_query_handler(text="d1")
async def d1(call: CallbackQuery):
    img = open("Moshinala/Dodge/1969_Dodge_Charger_(21572136732).jpg", "rb")
    txt = f"Dodge Charger - 1969\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 16L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks10)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="d2")
async def d2(call: CallbackQuery):
    img = open("Moshinala/Dodge/1969_Dodge_Coronet_Super_Bee_A12_(21700148724).jpg", "rb")
    txt = f"Dodge Coronet - 1969\n" \
          f"Rangi - Orange🚘\n" \
          f"100 km - 18L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks10)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="d3")
async def d3(call: CallbackQuery):
    img = open("Moshinala/Dodge/2007_Dodge_Charger_SRT8_Super_Bee.jpg", "rb")
    txt = f"Dodge Charger SRT8 - 2007\n" \
          f"Rangi - Sariq🚘\n" \
          f"100 km - 15L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟏𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks10)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="d4")
async def d4(call: CallbackQuery):
    img = open("Moshinala/Dodge/2015_Dodge_Charger_SRT_392_with_Scat_Pack.jpg", "rb")
    txt = f"Dodge Charger SRT - 2015\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 15L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟒𝟏𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks10)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="d5")
async def d5(call: CallbackQuery):
    img = open("Moshinala/Dodge/2016_Dodge_Challenger_Hellcat_(28456827004).jpg", "rb")
    txt = f"Dodge Charger HELLCAT - 2016\n" \
          f"Rangi - Orange🚘\n" \
          f"100 km - 22L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟐𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks10)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="d6")
async def d6(call: CallbackQuery):
    img = open("Moshinala/Dodge/2018_Dodge_Durango_RT_5.7L_Hemi_front_4.20.19.jpg", "rb")
    txt = f"Dodge Durango RT - 2018\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 17L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟐𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks10)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="Dodgeorqa")
async def rangeorqa(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png", "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()



@dp.callback_query_handler(text="tesla")
async def dodge(call: CallbackQuery):
    img = open("image/tesla.jpeg", "rb")
    await call.message.answer_photo(img, reply_markup=Tesla)
    await call.message.delete()

@dp.callback_query_handler(text="t1")
async def t1(call: CallbackQuery):
    img = open("Moshinala/Tesla/2017_Tesla_Model_X_100D_Front.jpg", "rb")
    txt = f"Tesla Model X - 2017\n" \
          f"Rangi - Seriy🚘\n" \
          f"Electrikt - full 300km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks11)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="t2")
async def t2(call: CallbackQuery):
    img = open("Moshinala/Tesla/2018_Tesla_Model_S_75D.jpg", "rb")
    txt = f"Tesla Model S - 2018\n" \
          f"Rangi - Qizil🚘\n" \
          f"Electrikt - full 350km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟕𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks11)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="t3")
async def t3(call: CallbackQuery):
    img = open("Moshinala/Tesla/2019_Tesla_Model_3_Performance_AWD_Front.jpg", "rb")
    txt = f"Tesla Model 3 - 2019\n" \
          f"Rangi - Oq🚘\n" \
          f"Electrikt - full 400km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟑𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks11)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="t4")
async def t4(call: CallbackQuery):
    img = open("Moshinala/Tesla/2020_Tesla_Model_Y,_front_8.1.20.jpg", "rb")
    txt = f"Tesla Model Y - 2020\n" \
          f"Rangi - Seriy🚘\n" \
          f"Electrikt - full 500km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟑𝟔𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks11)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="Teslaorqa")
async def teslaorqa(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png", "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()




@dp.callback_query_handler(text="chevrolet")
async def dodge(call: CallbackQuery):
    img = open("image/GM _ Chevrolet Bowtie Logo Camaro Corvette Truck Adult T-shirt  _ eBay.jpeg", "rb")
    await call.message.answer_photo(img, reply_markup=Chevrolet)
    await call.message.delete()

@dp.callback_query_handler(text="sh1")
async def sh1(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2019_Chevrolet_Colorado_LTZ.jpg", "rb")
    txt = f"Chevrolet Colorado 4*4 - 2019\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh2")
async def sh2(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2019_Chevrolet_Cruze_LT_RS,_Front_Right,_06-22-2021.jpg", "rb")
    txt = f"Chevrolet Cruze - 2019\n" \
          f"Rangi - Mokriy🚘\n" \
          f"100 km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟏𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh3")
async def sh3(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2019_Chevrolet_Malibu_(facelift)_LT,_front_10.19.19.jpg", "rb")
    txt = f"Chevrolet Malibu - 2021\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟕𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh4")
async def sh4(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2020_Chevrolet_Blazer_RS,_front_10.25.20.jpg", "rb")
    txt = f"Chevrolet Blazer - 2021\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟒𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh5")
async def sh5(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2020_Chevrolet_Camaro_LT1_1SS,_front_3.2.20.jpg", "rb")
    txt = f"Chevrolet Camaro - 2020\n" \
          f"Rangi - Seriy🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟖𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh6")
async def sh6(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2021_Chevrolet_Onix_1.0T_Premier_(Chile)_front_view.jpg", "rb")
    txt = f"Chevrolet Onix - 2021\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟗𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh7")
async def sh7(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2021_Chevrolet_Suburban_LT,_rear_6.14.21.jpg", "rb")
    txt = f"Chevrolet Tahoe - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟐𝟑𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh8")
async def sh8(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2021_Chevrolet_TrailBlazer_RS_AWD,_front_7.11.20.jpg", "rb")
    txt = f"Chevrolet TrailBlazer - 2022\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 11L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟒𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh9")
async def sh9(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2022_Chevrolet_Bolt_EUV_(Canada)_front_view.png", "rb")
    txt = f"Chevrolet Bolt - 2022\n" \
          f"Rangi - Seriy🚘\n" \
          f"Electrik - full 250km🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟒𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh10")
async def sh10(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2022_Chevrolet_Groove_Premier_(Mexico)_front_view.png", "rb")
    txt = f"Chevrolet Groove - 2022\n" \
          f"Rangi - Qizil🚘\n" \
          f"100 km - 12L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh11")
async def sh11(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/2022_Chevrolet_Traverse_LT_True_North_Edition_in_Silver_Sage_Metallic,_Front_Left,_07-31-2022.jpg", "rb")
    txt = f"Chevrolet Traverse - 2022\n" \
          f"Rangi - Zelyoniy🚘\n" \
          f"100 km - 14L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟖𝟓$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh12")
async def sh12(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/Chevrolet_Equinox_III_facelift_IMG001_(cropped).jpg", "rb")
    txt = f"Chevrolet Equinox - 2022\n" \
          f"Rangi - Qora🚘\n" \
          f"100 km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟏𝟕𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh13")
async def sh13(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/Chevrolet_Spark_(14114286768).jpg", "rb")
    txt = f"Chevrolet Spark - 2021\n" \
          f"Rangi - Oq🚘\n" \
          f"100 km - 8L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟓𝟎$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="sh14")
async def sh14(call: CallbackQuery):
    img = open("Moshinala/Chevrolet/Chevrolet_Tracker_2021_(front)_(cropped).png", "rb")
    txt = f"Chevrolet Tracker - 2022\n" \
          f"Rangi - Kok🚘\n" \
          f"100 km - 10L🚘\n" \
          f"𝐍𝐚𝐫𝐱𝐢 - 𝟗𝟓$ 𝗽𝗲𝗿 𝗱𝗮𝘆🚘" \
          f"\n" \
          f"Tel: 99-085-23-17\n" \
          f"Telegram - @lazizbek_a\n" \
          f"Instagram - https://www.instagram.com/lazizbek__a/"
    await call.message.answer_photo(img, caption=txt, reply_markup=Iks12)
    await call.answer(cache_time=30)
    await call.message.delete()

@dp.callback_query_handler(text="Shevorqa")
async def shevorqa(call: CallbackQuery):
    img = open("image/kisspng-car-rental-luxury-vehicle-toyota-innova-car-rental-5ad91370764ea4.9379777315241757284846.png", "rb")
    txt = f"Quyidagilarni tanlang"
    await call.message.answer_photo(img, caption=txt, reply_markup=Moshinala)
    await call.message.delete()

















































































if __name__ == '__main__':
    executor.start_polling(dp)