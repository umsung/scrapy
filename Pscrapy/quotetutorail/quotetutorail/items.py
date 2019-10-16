# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EntItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()


class QuotelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    img_href = scrapy.Field()
    url = scrapy.Field()
    # author = scrapy.Field()
    # tags = scrapy.Field()
    pass


class JoBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    tag = scrapy.Field()
    content = scrapy.Field()


class ZhiHuItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    account_status = scrapy.Field()
    allow_message= scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    avatar_hue = scrapy.Field()
    avatar_url = scrapy.Field()
    avatar_url_template = scrapy.Field()
    badge = scrapy.Field()
    business = scrapy.Field()
    employments = scrapy.Field()
    columns_count = scrapy.Field()
    commercial_question_count = scrapy.Field()
    cover_url = scrapy.Field()
    description = scrapy.Field()
    educations = scrapy.Field()
    favorite_count = scrapy.Field()
    favorited_count = scrapy.Field()
    follower_count = scrapy.Field()
    following_columns_count = scrapy.Field()
    following_favlists_count = scrapy.Field()
    following_question_count = scrapy.Field()
    following_topic_count = scrapy.Field()
    gender = scrapy.Field()
    # headline = Fscrapy.Field()
    hosted_live_count = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    url_token = scrapy.Field()
    user_type = scrapy.Field()
    logs_count = scrapy.Field()


class TanChePostItem(scrapy.Item):
    modelName = scrapy.Field()
    seriesName = scrapy.Field()
    seriesId = scrapy.Field()
    cityName = scrapy.Field()
    mileageStr = scrapy.Field()
    provinceName = scrapy.Field()
    seriesImg = scrapy.Field()
    contactTel = scrapy.Field()
    shopName = scrapy.Field()
    shopAddr = scrapy.Field()
    cityName = scrapy.Field()
    installmentStr = scrapy.Field()
    prepaidAmount = scrapy.Field()

class WeiboItem(scrapy.Item):
    url = scrapy.Field()
    content = scrapy.Field()
    id = scrapy.Field()
    comment_count = scrapy.Field()
    forward_count = scrapy.Field()
    like_count = scrapy.Field()
    posted_at = scrapy.Field()
    user = scrapy.Field()


class WwwDytt8NetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    publish_time = scrapy.Field()
    images = scrapy.Field()
    download_links = scrapy.Field()
    contents = scrapy.Field()
    pass