import os
import telebot

bot = telebot.TeleBot(os.environ.get("INPUT_BOT_TOKEN"))


def main():
    protect_c, disable_n, parse_m = None, None, None
    message = os.environ.get('INPUT_MESSAGE')
    if not os.environ.get('INPUT_PROTECT_CONTENT'):
        protect_c = True
    if not os.environ.get('INPUT_DISABLE_NOTIFICATION'):
        disable_n = True
    if os.environ.get('INPUT_DISABLE_NOTIFICATION') in ("MarkdownV2", "HTML", "Markdown"):
        parse_m = os.environ.get('INPUT_DISABLE_NOTIFICATION')
    else:
        print('WARNING: PARSE MODE IS NOT RECOGNISED')
    msg = bot.send_message(int(os.environ.get('INPUT_CHAT_ID')), message,
                           parse_mode=parse_m,
                           disable_notification=disable_n,
                           protect_content=protect_c
                           )
    print(f"::set-output name=result::{msg.text}")


if __name__ == "__main__":
    main()
