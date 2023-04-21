import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from website_scripts.Entities.Politician import Politician
from website_scripts.Entities.Comment import Comment
from tqdm import tqdm

class PostsPageService:
    def __init__(self, chrome_service):
        self.chrome_service = chrome_service

    def get_posts_preview_urls(self):
        politician_file = open('../Data/Politicians.txt')
        category_file = open('../Data/Categories.txt')
        politicians_names = politician_file.read().split('\n')
        categories = category_file.read().split('\n')
        politicians = [Politician(full_name) for full_name in politicians_names]
        ret_urls = []
        for category in categories:
            for politician in politicians:
                url = f'https://irony.cs.bgu.ac.il/#/politician/{category}/{politician.first_name}%20{politician.last_name}'
                ret_urls.append(url)
        return ret_urls

    def get_posts_urls_by_post_preview_url(self, post_preview_url):
        ret_urls=[]
        self.chrome_service.move_to_url(post_preview_url)
        div =self.chrome_service.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div")
        wait = WebDriverWait(self.chrome_service.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'post')))
        posts=self.chrome_service.driver.find_elements(By.CLASS_NAME,'post')
        for post in posts:
            url=post.find_element(By.TAG_NAME, 'a').get_attribute('href')
            ret_urls.append(url)
        return ret_urls

    def get_comments_from_post(self,post_url):
        ret_comments=[]
        self.chrome_service.move_to_url(post_url)
        # self.chrome_service.driver.implicitly_wait(500)
        wait = WebDriverWait(self.chrome_service.driver, 40)
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'regular_comment')))
        regular_comments_objects=self.chrome_service.driver.find_elements(By.CLASS_NAME,'regular_comment')
        for regular_comment_object in regular_comments_objects:
            comment_url=regular_comment_object.find_elements(By.TAG_NAME,'a')[1].get_attribute('href')
            comment_index=int(regular_comment_object.find_element(By.TAG_NAME,'h6').text.split('|')[1].split(' ')[2].replace('#',''))
            post_index=post_url.split('index=')[1]
            politician_name=self.chrome_service.driver.find_element(By.TAG_NAME,'h5').text.split('|')[0]
            curr_comment=Comment(comment_url,comment_index,post_index,politician_name,'regular-comment')
            ret_comments.append(curr_comment)
        nested_comments_objects=self.chrome_service.driver.find_elements(By.CLASS_NAME,'nested_comment')
        for nested_comment_object in nested_comments_objects:
            comment_url=nested_comment_object.find_elements(By.TAG_NAME,'a')[1].get_attribute('href')
            comment_index=int(nested_comment_object.find_element(By.TAG_NAME,'h6').text.split('|')[1].split(' ')[2].replace('#',''))
            post_index=post_url.split('index=')[1]
            politician_name=self.chrome_service.driver.find_element(By.TAG_NAME,'h5').text.split('|')[0]
            curr_comment=Comment(comment_url,comment_index,post_index,politician_name,'nested-comment')
            ret_comments.append(curr_comment)
        ret_comments.sort(key=lambda x:x.comment_index)
        return ret_comments

    def get_comments_from_posts(self,post_preview_url):
        ret_comments=[]
        posts_urls=self.get_posts_urls_by_post_preview_url(post_preview_url)
        for post_url in tqdm(posts_urls):
            try:
                ret_comments.extend(self.get_comments_from_post(post_url))
            except:
                x=3
        return ret_comments




        
