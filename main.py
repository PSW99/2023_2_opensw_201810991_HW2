from datetime import datetime
import telegram
import asyncio
import platform
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

async def push_alert(bot, chat_id):
    time_data = datetime.now().strftime("현재 시간은 %H:%M:%S 입니다.")
    await bot.sendMessage(chat_id, time_data)

async def main():
    token = "6455259880:AAH0iMxCwo0rMdctG6EPyYTLonfJvFfRlZs"
    chat_id = "6278623112"

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    bot = telegram.Bot(token)

    test = AsyncIOScheduler()
    test.add_job(push_alert, 'cron', hour='6-23', minute='*', second='*/3', args=[bot, chat_id], max_instances=10)

    test.start()

    while True:
        await asyncio.sleep(1000)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        AsyncIOScheduler().shutdown()
        pass