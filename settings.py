import logging


API_ID = 21315760
API_HASH = 'd7859700b83543cba8405a0498d3e27f'

ASO_ID = '@bot_ASO_bot'

PHONE = '+380687781744'

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(levelname)s | %(message)s'
LOG_DIR = 'logs'

CATEGORIES = [
    {'name': '♾Overall', 'sub_categories': None},
    {'name': '📖Books', 'sub_categories': None},
    {'name': '💼Business', 'sub_categories': None},
    {'name': '🗂Catalogs', 'sub_categories': None},
    {'name': '🔨Developer Tools', 'sub_categories': None},
    {'name': '🌍Education', 'sub_categories': None},
    {'name': '🍿Entertainment', 'sub_categories': None},
    {'name': '💰Finance', 'sub_categories': None},
    {'name': '🥤Food & Drink', 'sub_categories': None},
    {'name': '🚀Game', 'sub_categories': [
        {'name': '🚀All Games'},
        {'name': 'Action'},
        {'name': 'Adventure'},
        {'name': 'Board'},
        {'name': 'Card'},
        {'name': 'Casino'},
        {'name': 'Casual'},
        {'name': 'Dice'},
        {'name': 'Educational'},
        {'name': 'Family'},
        {'name': 'Music'},
        {'name': 'Puzzle'},
        {'name': 'Racing'},
        {'name': 'Role Playing'},
        {'name': 'Simulation'},
        {'name': 'Sports'},
        {'name': 'Strategy'},
        {'name': 'Trivia'},
        {'name': 'Word'},
    ]},
    {'name': '🖼Graphics & Design', 'sub_categories': None},
    {'name': '🚲Health & Fitness', 'sub_categories': None},
    {'name': '🎈Kids', 'sub_categories': [
        {'name': '🎈All Kids'},
        {'name': 'Ages 5 & Under'},
        {'name': 'Ages 6-8'},
        {'name': 'Ages 9-11'}
    ]},
    {'name': '🪑Lifestyle', 'sub_categories': None},
    {'name': '📰Magazines & Newspapers', 'sub_categories': [
        {'name': '📰All Magazines & Newspapers'},
        {'name': 'News & Politics'}
    ]},
    {'name': '🩺Medical', 'sub_categories': None},
    {'name': '🎧Music', 'sub_categories': None},
    {'name': '🧭Navigation', 'sub_categories': None},
    {'name': '📡News', 'sub_categories': None},
    {'name': '📸Photo & Video', 'sub_categories': None},
    {'name': '☑Productivity', 'sub_categories': None},
    {'name': '🔎Reference', 'sub_categories': None},
    {'name': '🛍Shopping', 'sub_categories': None},
    {'name': '💬Social Networking', 'sub_categories': None},
    {'name': '⚽Sports', 'sub_categories': None},
    {'name': '📌Stickers', 'sub_categories': [
        {'name': '📌All Stickers'},
        {'name': 'Animals & Nature'},
        {'name': 'Art'},
        {'name': 'Celebrations'},
        {'name': 'Celebrities'},
        {'name': 'Comics & Cartoons'},
        {'name': 'Eating & Drinking'},
        {'name': 'Emoji & Expressions'},
        {'name': 'Fashion'},
        {'name': 'Gaming'},
        {'name': 'Kids & Family'},
        {'name': 'Movies & TV'},
        {'name': 'Music'},
        {'name': 'People'},
        {'name': 'Places & Objects'},
        {'name': 'Sports & Activities'}

    ]},
    {'name': '🏝Travel', 'sub_categories': None},
    {'name': '🧮Utilities', 'sub_categories': None},
    {'name': '🌦Weather', 'sub_categories': None}
]

COUNTRIES = [
    'US',
    'CA',
    'GB',
    'UA',
    'IN',
    'ID',
    'MY'
]

FULL_COUNTRIES = {
    'US': 'United States',
    'CA': 'Canada',
    'GB': 'United Kingdom',
    'UA': 'Ukraine',
    'IN': 'India',
    'ID': 'Indonesia',
    'MY': 'Malaysia'
}
