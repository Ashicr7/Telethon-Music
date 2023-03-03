import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5520373776:AAGwPsIO_7p31D4KUcp26bJX83y8LqRH0gY)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOHUBu5IDTiSlAl66wqLtBG1_roqKqB0CiiWZt327TGtoi17DIvfO3QPyrpp1Sq2v6bgY26kGwrjO6cJFn4hXVvHn_jyhzBTrwkcBBQ4sx0ya-bVcG8-yFMJ13TWQF5VCvAfT9-_x2md7siPa8EGQKGa1mAmYolH4bYVT5p2RjSK-WC7-5lLiEaIwy2aFfpHLg6gtj8FOBDiwmkJAOpjsLRdm5EBMI7ea0DwAVxWx1vOuVd2rwUynQ1Y0bnly0YhAcKYolv-fUo8gYNe3Kk_3ZGgCR5UCaNvOehzWieZR55EjGwkjdzR559abH8P4lxK4s5BHzdU2lqJksUXVNRzpImfD52I=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
