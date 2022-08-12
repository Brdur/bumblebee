import os
import shutil
import zipfile

import telebot

bot = telebot.TeleBot(os.environ.get("INPUT_BOT_TOKEN"))


def main():
    protect_c, disable_n, parse_m = None, None, None
    message = os.environ.get('INPUT_MESSAGE')
    if not os.environ.get('INPUT_PROTECT_CONTENT'):
        protect_c = True
    if not os.environ.get('INPUT_DISABLE_NOTIFICATION'):
        disable_n = True
    if os.environ.get('INPUT_PARSE_MODE') in ("MarkdownV2", "HTML", "Markdown"):
        parse_m = os.environ.get('INPUT_PARSE_MODE')
    else:
        print(f'WARNING: PARSE MODE IS NOT RECOGNISED: {parse_m}')
    msg = bot.send_message(int(os.environ.get('INPUT_CHAT_ID')), message,
                           parse_mode=parse_m,
                           disable_notification=disable_n,
                           protect_content=protect_c
                           )
    if msg:
        print("::set-output name=result::Done!")
    artpath = os.environ.get('INPUT_FILE_PATH')
    if artpath:
        name = os.path.basename(artpath)
        if os.path.isdir(artpath):
            shutil.make_archive(f'{name}', 'zip', artpath)
        elif os.path.isfile(artpath):
            with zipfile.ZipFile(f'{name}', 'w') as arc_zip:
                arc_zip.write(artpath)
        with open(f'{name}.zip', 'rb') as doc:
            file_msg = bot.send_document(int(os.environ.get('INPUT_CHAT_ID')), doc,
                                         disable_notification=disable_n,
                                         protect_content=protect_c
                                         )
    if file_msg:
        print("::set-output name=result_file::Done!")


if __name__ == "__main__":
    main()
