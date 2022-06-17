
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US')

all_keywords = [

    'event management',

    'event planning',

    'event planner'

    ]

cat = '14' #people&society

timeframes = [

    'today 5-y',

    'today 12-m',

    'today 3-m',

    'today 1-m'

    ]

geo = '' #worldwide

gprop = '' #websearch

pytrends.build_payload(

    kw_list,

    cat,

    timeframes[0],

    geo,

    gprop

    )