#!C:/Python2.7 python
# -*- coding: utf-8 -*-

''' Things to add
Include separate DB for Events data to capture events details
Include separate DB for tagged data(other users or pages who have tagged us in our posts)
Include separate DB for likes by search page include -- name,page,fan_count,about
'''

import sqlite3
import sqlalchemy
import datetime
import facebook as fb
import dateutil.parser as dateparser
from sentiment_analysis_textblob import custom_sentiment_analysis
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Numeric, DateTime, VARCHAR, create_engine

from sqlalchemy.ext.declarative import declarative_base

# Location of database -- Create the file name dummy file with this file name

db_path = 'sqlite:///test.db'

# access token for facebook graphAPI

access_token = 'EAAXDriKJZA0IBAC2APJjJBKwCTbcXpzBQrWNsycPEG1fPQ8L1tzZC6YqntqWyjqTxBm9i4ZAQJcTMblSHB' \
               'h12gZBV42aEgkbPwW8vM0xkRwfdh1TrZCsjm6MSZBOkHVXUIu3cX83iZBNLS5DXnd1aQpdBpB9ZCJdloMZD'

Base = declarative_base()


class Page_Info(Base):

    __tablename__ = 'page_info'
    id = Column(Integer, primary_key=True)
    page_name = Column(String)
    about = Column(String)
    description_html = Column(Text)
    talking_about_count = Column(Integer)
    single_line_address = Column(Text)
    picture = Column(Text)  # remember to handle the url part in api call
    cover = Column(Text)  # remember to use source key for getting the url
    website = Column(Text)
    username = Column(Text)

    def __init__(
        self,
        id,
        page_name,
        about,
#!C:/Python2.7 python
# -*- coding: utf-8 -*-

''' Things to add
Include separate DB for Events data to capture events details
Include separate DB for tagged data(other users or pages who have tagged us in our posts)
Include separate DB for likes by search page include -- name,page,fan_count,about
'''

import sqlite3
import sqlalchemy
import requests
import datetime
import facebook as fb
import dateutil.parser as dateparser
from sentiment_analysis_textblob import custom_sentiment_analysis
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Numeric, DateTime, VARCHAR, create_engine

from sqlalchemy.ext.declarative import declarative_base

# Location of database -- Create the file name dummy file with this file name

db_path = 'sqlite:///test.db'

# access token for facebook graphAPI

access_token = 'EAAXDriKJZA0IBAC2APJjJBKwCTbcXpzBQrWNsycPEG1fPQ8L1tzZC6YqntqWyjqTxBm9i4ZAQJcTMblSHB' \
               'h12gZBV42aEgkbPwW8vM0xkRwfdh1TrZCsjm6MSZBOkHVXUIu3cX83iZBNLS5DXnd1aQpdBpB9ZCJdloMZD'

Base = declarative_base()


class Page_Info(Base):

    __tablename__ = 'page_info'
    id = Column(Integer, primary_key=True)
    page_name = Column(String)
    about = Column(String)
    description_html = Column(Text)
    talking_about_count = Column(Integer)
    single_line_address = Column(Text)
    picture = Column(Text)  # remember to handle the url part in api call
    cover = Column(Text)  # remember to use source key for getting the url
    website = Column(Text)
    username = Column(Text)

    def __init__(
        self,
        id,
        page_name,
        about,
        description_html,
        talking_about_count,
        single_line_address,
        picture,
        cover,
        website,
        username,
        ):
        self.id = id
        self.page_name = page_name
        self.about = about
        self.description_html = description_html
        self.talking_about_count = talking_about_count
        self.single_line_address = single_line_address
        self.picture = picture
        self.cover = cover
        self.website = website
        self.username = username

#possible refactoring include entire write to db call in one class
class Write_Page_Info:#possible refactoring include entire write to db call in one class

    def __init__(self, page_info_data):
        id = page_info_data['id']
        page_name = page_info_data['page_name']
        about = page_info_data['about']
        description_html = page_info_data['description_html']
        talking_about_count = page_info_data['talking_about_count']
        single_line_address = page_info_data['single_line_address']
        picture = page_info_data['picture']
        cover = page_info_data['cover']
        website = page_info_data['website']
        username = page_info_data['username']
        a = Page_Info(
            id,
            page_name,
            about,
            description_html,
            talking_about_count,
            single_line_address,
            picture,
            cover,
            website,
            username,
            )
        b = Main()
        b.add_data(a)
        b.try_commit()


class Posts_Data(Base):

    __tablename__ = 'posts_data'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    created_time = Column(DateTime)
    posted_from_name = Column(String)
    posted_from_id = Column(Integer)
    status_type = Column(String)
    page_name = Column(String)
    name = Column(String)
    date_updated =Column(DateTime)
    message_tags_id = Column(Integer)
    message_tags_name = Column(String)
    post_sentiment_score = Column(Integer)
    post_sentiment_mean = Column(String)
    data_inserted = Column(DateTime)

    def __init__(
        self,
        id,
        message,
        created_time,
        posted_from_name,
        posted_from_id,
        status_type,
        page_name,
        name,
        date_updated,
        message_tags_id,
        message_tags_name,
        post_sentiment_score,
        post_sentiment_mean,
        date_inserted
        ):
        self.id = id
        self.message = message
        self.created_time = created_time
        self.posted_from_name = posted_from_name
        self.posted_from_id = posted_from_id
        self.status_type = status_type
        self.page_name = page_name
        self.message_tags_id = message_tags_id
        self.message_tags_name = message_tags_name
        self.date_updated = date_updated
        self.post_sentiment_score = post_sentiment_score
        self.post_sentiment_mean = post_sentiment_mean
        self.date_inserted = date_inserted

#possible refactoring include entire write to db call in one class
class Write_Post_Data:

    def __init__(self, posts_data):
        id = posts_data['id']
        message = posts_data['message']
        created_time = posts_data['created_time']
        posted_from_name = posts_data['posted_from_name']
        posted_from_id = posts_data['posted_from_id']
        status_type = posts_data['status_type']
        page_name = posts_data['page_name']
        name = posts_data['name']
        date_updated = posts_data['date_updated']
        message_tags_id = posts_data['message_tags_id']
        message_tags_name = posts_data['message_tags_name']
        post_sentiment_score = posts_data['post_sentiment_score']
        post_sentiment_mean = posts_data['post_sentiment_mean']
        date_inserted = posts_data['date_inserted']
        a = Posts_Data(
            id,
            message,
            created_time,
            posted_from_name,
            posted_from_id,
            status_type,
            page_name,
            name,
            date_updated,
            message_tags_id,
            message_tags_name,
            post_sentiment_score,
            post_sentiment_mean,
            date_inserted
            )
        print 'going to save'
        print a
        b = Main()
        b.add_data(a)  #add a try block to catch exception while posting data
        b.try_commit()


class Comments_Data(Base):

    __tablename__ = 'comments_data'
    id = Column(String, primary_key=True)
    page_name = String
    post_id = Column(Integer, ForeignKey(Posts_Data.id))
    comment_count = Column(Integer)
    from_name = Column(String)
    from_id = Column(Integer)
    message_tags = Column(String)
    created_time = Column(DateTime)
    user_likes = Column(String)
    sentiment_score = Column(Integer)
    sentiment_mean = Column(String)

    def __init__(
        self,
        id,
        page_name,
        post_id,
        comment_count,
        from_name,
        from_id,
        message_tags,
        created_time,
        user_likes,
        sentiment_score,
        sentiment_mean,
        ):
        self.id = id
        self.page_name = page_name
        self.post_id = post_id
        self.comment_count = comment_count
        self.from_name = from_name
        self.from_id = from_id
        self.message_tags = message_tags
        self.created_time = user_likes
        self.user_likes = user_likes
        self.sentiment_score = sentiment_score
        self.sentiment_mean = sentiment_mean

#possible refactoring include entire write to db call in one class
class Write_Comment_Post:

    def __init__(self, comments_data):
        id = comments_data['id']
        page_name = comments_data['page_name]']
        post_id = comments_data['post_id']
        comment_count = comments_data['comment_data']
        from_name = comments_data['from_name']
        from_id = comments_data['from_id']
        message_tags = comments_data['message_tags']
        created_time = comments_data['created_time']
        user_likes = comments_data['user_likes']
        sentiment_score = comments_data['sentiment_score']
        sentiment_mean = comments_data['sentiment_score']
        a = Comments_Data(
            id,
            page_name,
            post_id,
            comment_count,
            from_name,
            from_id,
            message_tags,
            created_time,
            user_likes,
            sentiment_score,
            sentiment_mean,
            )
        b = Main()
        b.add_data(a)
        b.try_commit()


class Reactions_Data(Base):

    __tablename__ = 'reactions_data'
    id = Column(String, primary_key=True)
    name = Column(String)
    type = Column(String)
    pic = Column(Text)
    page_name = Column(String)
    gender = Column(String)

    def __init__(
        self,
        id,
        name,
        type,
        pic,
        page_name,
        gender,
        ):
        self.id = id
        self.name = name
        self.type = type
        self.pic = pic
        self.page_name = page_name
        self.gender = gender

#possible refactoring include entire write to db call in one class
class Write_Reaction_Data:

    def __init__(self, reactions_data):
        id = reactions_data['id']
        name = reactions_data['name']
        type = reactions_data['type']
        pic = reactions_data['type']
        page_name = reactions_data['page_name']
        gender = reactions_data['gender']
        a = Reactions_Data(
            id,
            name,
            type,
            pic,
            page_name,
            gender,
            )
        b = Main()
        b.add_data(a)
        b.try_commit()


class Main:

    def __init__(self):
        engine = create_engine(db_path, echo=False)
        Session = sessionmaker()
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)
        self.session = Session()

    def add_data(self, data):
        if data != '':
            self.session.merge(data)
        else:
            print 'Data Field Empty'

    def try_commit(self):
        try:
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            print 'Error: ', SQLAlchemyError

    def main(self):
        keys = ['6096008671',]  # <-- Id for L10nbridge Official Page add more if needed
        for key in keys:
            call_API = call_GraphAPI()
            print '---------------------Fetching Page Info------------------------'
            page_info_data = call_API.get_page_info(key)  # define function for getting the facebook page data
            print '---------------------Page Info Fetched-------------------------'
            Write_Page_Info(page_info_data)
            print '---------------------Fetching Posts Data-----------------------'
            post = call_API.get_post_data(key)
            print '---------------------Posts Fetched-----------------------------'
            # comments_data = call_GraphAPI.get_comment_data(key)
            # reaction_data = call_GraphAPI.get_reaction_data(key)




            # Write_Comment_Post(comments_data)
            # Write_Reaction_Data(reaction_data)

class call_GraphAPI:

    def __init__(self):
        self.graph = fb.GraphAPI(access_token=access_token, version=2.7)
        self.return_data = {}
        self.session = Main()

    def get_next_page(self,url):
        return requests.get(url).json()

    def get_page_info(self, key):

        # calling the graph api to fetch the page data

        api_output = self.graph.get_object(id=key,fields='id,name,about,description_html,talking_about_count,single_line_address,picture{url},cover,website,username')

        # Validating the values before posting to DB
        if api_output != '':
            if 'id' in api_output:
                id = api_output['id']
            else:
                raise KeyError('Error while getting_page_info')

            if 'name' in api_output:
                name = api_output['name']
            else:
                name = ''

            if 'about' in api_output:
                about = api_output['about']
            else:
                about = ''

            if 'description_html' in api_output:
                description = api_output['description_html']
            else:
                description = ''

            if 'talking_about_count' in api_output:
                talking_about_count = api_output['talking_about_count']
            else:
                talking_about_count = 0

            if 'single_line_address' in api_output:
                address = api_output['single_line_address']
            else:
                address = ''

            if 'picture' in api_output:
                picture = api_output['picture']['data']['url']
            else:
                picture

            if 'cover' in api_output:
                cover = api_output['cover']['source']
            else:
                cover = ''

            if 'website' in api_output:
                website = api_output['website']
            else:
                website = ''

            if 'username' in api_output:
                username = api_output['username']
            else:
                username = ''

        # Appending the output to dictionary which will be returned for posting to DB
        self.return_data.update({
            'id': id,
            'page_name': name,
            'about': about,
            'description_html': description,
            'talking_about_count': talking_about_count,
            'single_line_address': address,
            'picture': picture,
            'cover': cover,
            'website': website,
            'username': username,
            })

        # Returning the dict for updating the DB
        return self.return_data

    def get_post_data(self, key):
        self.return_data.clear()
        api_output = self.graph.get_object(id=key+'/feed',fields='id,message,created_time,from,message_tags,status_type,name,updated_time')

        #api_output = api_output['feed']
        print api_output
        a= {}
        post_count = len(api_output['data'])
        page_count = 0
        while(True):
            try:
                if (len(api_output['data']) > 0):
                    for post in api_output['data']:
                        print post
                        if 'id' in post:
                            id = post['id']
                        else:
                            raise KeyError('Error while get_post_data')

                        if 'message' in post:
                            message = post['message']
                        else:
                            message = ''

                        if 'created_time' in post:
                            created_time = dateparser.parse(post['created_time'], ignoretz=True)
                        else:
                            created_time = ''

                        if 'from' in post:
                            post_from_name = post['from']['name']
                            post_from_id = post['from']['id']
                        else:
                            post_from_name = ''
                            post_from_id = ''

                        if 'message_tags' in post:
                            message_tags_name = post['message_tags']['name']
                            message_tags_id = post['message_tags']['id']
                        else:
                            message_tags_name = ''
                            message_tags_id = ''

                        if 'status_type' in post:
                            status_type = post['status_type']
                        else:
                            status_type = ''

                        if 'name' in post:
                            name = post['name']
                        else:
                            name = ''

                        if 'updated_time' in post:
                            updated_time = dateparser.parse(post['updated_time'], ignoretz=True)
                        else:
                            updated_time = ''

                        #Read Page Name from Page_Info Page
                        page_name = self.session.session.query(Page_Info.page_name).filter(Page_Info.id == key)

                        # Calculate the sentiment score of the Post
                        sentiment_value = custom_sentiment_analysis(message)
                        sentiment_score = sentiment_value[0]
                        sentiment_mean= sentiment_value[1]

                        inserted_time = datetime.datetime.now()
                        self.return_data.clear()
                        a.update({
                            'id': id,
                            'message': message,
                            'created_time': created_time,
                            'posted_from_id': post_from_id,
                            'posted_from_name': post_from_name,
                            'status_type': status_type,
                            'page_name': page_name,
                            'name': name,
                            'message_tags_id': message_tags_id,
                            'message_tags_name': message_tags_name,
                            'date_updated': updated_time,
                            'sentiment_score': sentiment_score,
                            'sentiment_mean': sentiment_mean,
                            'date_inserted': inserted_time
                            })

                        Write_Post_Data(a)
                        post_count += 1
                        print 'Post Count: ', post_count
                    page_count += 1
                    api_output = self.get_next_page(api_output['paging']['next'])
                    print '------------------------------Page Count---------------------------------: ', page_count
                else:
                    raise KeyError
                    break

            except KeyError:
                print 'All Posts Extracted!!!'
                print 'Moving On to fetch the Comments for each Post'
                break




    def get_comment_data(self, key):
        pass

    def get_reaction_data(self, key):
        pass


if __name__ == '__main__':
    s = Main()
    s.main()
    print 'Process Completed Successfully!!!!'

            website,
            username,
            )
        b = Main()
        b.add_data(a)
        b.try_commit()


class Posts_Data(Base):

    __tablename__ = 'posts_data'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    created_time = Column(DateTime)
    posted_from = Column(String)  # remember to use key ['Name']
    object_name = Column(String)
    status_type = Column(String)
    page_name = Column(String)
    date_updated =Column(DateTime)
    post_sentiment_score = Column(Integer)
    post_sentiment_mean = Column(String)
    data_inserted = Column(DateTime)

    def __init__(
        self,
        id,
        message,
        created_time,
        posted_from,
        object_name,
        status_type,
        page_name,
        date_updated,
        post_sentiment_score,
        post_sentiment_mean,
        date_inserted
        ):
        self.id = id
        self.message = message
        self.created_time = created_time
        self.posted_from = posted_from
        self.object_name = object_name
        self.status_type = status_type
        self.page_name = page_name
        self.date_updated = date_updated
        self.post_sentiment_score = post_sentiment_score
        self.post_sentiment_mean = post_sentiment_mean
        self.date_inserted = date_inserted

#possible refactoring include entire write to db call in one class
class Write_Post_Data:

    def __init__(self, posts_data):
        id = posts_data['id']
        message = posts_data['message']
        created_time = posts_data['created_time']
        posted_from = posts_data['posted_from']
        object_name = posts_data['object_name']
        status_type = posts_data['status_type']
        page_name = posts_data['page_name']
        date_updated = posts_data['date_updated']
        post_sentiment_score = posts_data['post_sentiment_score']
        post_sentiment_mean = posts_data['post_sentiment_mean']
        a = Posts_Data(
            id,
            message,
            created_time,
            posted_from,
            object_name,
            status_type,
            page_name,
            date_updated,
            post_sentiment_score,
            post_sentiment_mean,
            )
        b = Main()
        b.add_data(a)  #add a try block to catch exception while posting data
        b.try_commit()


class Comments_Data(Base):

    __tablename__ = 'comments_data'
    id = Column(String, primary_key=True)
    page_name = String
    post_id = Column(Integer, ForeignKey(Posts_Data.id))
    comment_count = Column(Integer)
    from_name = Column(String)
    from_id = Column(Integer)
    message_tags = Column(String)
    created_time = Column(DateTime)
    user_likes = Column(String)
    sentiment_score = Column(Integer)
    sentiment_mean = Column(String)

    def __init__(
        self,
        id,
        page_name,
        post_id,
        comment_count,
        from_name,
        from_id,
        message_tags,
        created_time,
        user_likes,
        sentiment_score,
        sentiment_mean,
        ):
        self.id = id
        self.page_name = page_name
        self.post_id = post_id
        self.comment_count = comment_count
        self.from_name = from_name
        self.from_id = from_id
        self.message_tags = message_tags
        self.created_time = user_likes
        self.user_likes = user_likes
        self.sentiment_score = sentiment_score
        self.sentiment_mean = sentiment_mean

#possible refactoring include entire write to db call in one class
class Write_Comment_Post:

    def __init__(self, comments_data):
        id = comments_data['id']
        page_name = comments_data['page_name]']
        post_id = comments_data['post_id']
        comment_count = comments_data['comment_data']
        from_name = comments_data['from_name']
        from_id = comments_data['from_id']
        message_tags = comments_data['message_tags']
        created_time = comments_data['created_time']
        user_likes = comments_data['user_likes']
        sentiment_score = comments_data['sentiment_score']
        sentiment_mean = comments_data['sentiment_score']
        a = Comments_Data(
            id,
            page_name,
            post_id,
            comment_count,
            from_name,
            from_id,
            message_tags,
            created_time,
            user_likes,
            sentiment_score,
            sentiment_mean,
            )
        b = Main()
        b.add_data(a)
        b.try_commit()


class Reactions_Data(Base):

    __tablename__ = 'reactions_data'
    id = Column(String, primary_key=True)
    name = Column(String)
    type = Column(String)
    pic = Column(Text)
    page_name = Column(String)
    gender = Column(String)

    def __init__(
        self,
        id,
        name,
        type,
        pic,
        page_name,
        gender,
        ):
        self.id = id
        self.name = name
        self.type = type
        self.pic = pic
        self.page_name = page_name
        self.gender = gender

#possible refactoring include entire write to db call in one class
class Write_Reaction_Data:

    def __init__(self, reactions_data):
        id = reactions_data['id']
        name = reactions_data['name']
        type = reactions_data['type']
        pic = reactions_data['type']
        page_name = reactions_data['page_name']
        gender = reactions_data['gender']
        a = Reactions_Data(
            id,
            name,
            type,
            pic,
            page_name,
            gender,
            )
        b = Main()
        b.add_data(a)
        b.try_commit()


class Main:

    def __init__(self):
        engine = create_engine(db_path, echo=False)
        Session = sessionmaker()
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)
        self.session = Session()

    def add_data(self, data):
        if data != '':
            self.session.merge(data)
        else:
            print 'Data Field Empty'

    def try_commit(self):
        try:
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            print 'Error: ', SQLAlchemyError

    def main(self):
        keys = ['6096008671',]  # <-- Id for L10nbridge Official Page add more if needed
        for key in keys:
            call_API = call_GraphAPI()
            page_info_data = call_API.get_page_info(key)  # define function for getting the facebook page data

            # posts_data = call_GraphAPI.get_post_data(key)
            # comments_data = call_GraphAPI.get_comment_data(key)
            # reaction_data = call_GraphAPI.get_reaction_data(key)

            Write_Page_Info(page_info_data)


            # Write_Post_Data(posts_data)
            # Write_Comment_Post(comments_data)
            # Write_Reaction_Data(reaction_data)

class call_GraphAPI:

    def __init__(self):
        self.graph = fb.GraphAPI(access_token=access_token, version=2.7)
        self.return_data = {}
        self.read = Main()

    def get_page_info(self, key):

        # calling the graph api to fetch the page data

        api_output = self.graph.get_object(id=key,fields='id,name,about,description_html,talking_about_count,single_line_address,picture{url},cover,website,username')

        # Validating the values before posting to DB
        if api_output != '':
            if 'id' in api_output:
                id = api_output['id']
            else:
                raise KeyError('Error while getting_page_info')

            if 'name' in api_output:
                name = api_output['name']
            else:
                name = ''

            if 'about' in api_output:
                about = api_output['about']
            else:
                about = ''

            if 'description_html' in api_output:
                description = api_output['description_html']
            else:
                description = ''

            if 'talking_about_count' in api_output:
                talking_about_count = api_output['talking_about_count']
            else:
                talking_about_count = 0

            if 'single_line_address' in api_output:
                address = api_output['single_line_address']
            else:
                address = ''

            if 'picture' in api_output:
                picture = api_output['picture']['data']['url']
            else:
                picture

            if 'cover' in api_output:
                cover = api_output['cover']['source']
            else:
                cover = ''

            if 'website' in api_output:
                website = api_output['website']
            else:
                website = ''

            if 'username' in api_output:
                username = api_output['username']
            else:
                username = ''

        # Appending the output to dictionary which will be returned for posting to DB
        self.return_data.update({
            'id': id,
            'page_name': name,
            'about': about,
            'description_html': description,
            'talking_about_count': talking_about_count,
            'single_line_address': address,
            'picture': picture,
            'cover': cover,
            'website': website,
            'username': username,
            })

        # Returning the dict for updating the DB
        return self.return_data

    def get_post_data(self, key):
        api_output = self.graph.get_object(id=key+'/posts',fields='id,message,created_time,from,message_tags,status_type,name,updated_time')

        if api_output != '' :


    def get_comment_data(self, key):
        return

    def get_reaction_data(self, key):
        pass


if __name__ == '__main__':
    s = Main()
    s.main()
    print 'Process Completed Successfully!!!!'
