import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Service.LoginPageService import LoginPageService
from Service.ChromeService import ChromeService
from Service.PostsPageService import PostsPageService
from Service.IOService import IOService
from Entities.Politician import Politician
# -----------Globals-------------
chrome_service=ChromeService()
login_page_service=LoginPageService(chrome_service)
posts_page_service=PostsPageService(chrome_service)
io_service=IOService()

#--------------------------------
login_page_service.login_user()
categories=IOService.get_data_from_file('Data/Categories.txt')
politicians=IOService.get_data_from_file('Data/politicians.txt')
politicians=[Politician(full_name) for full_name in politicians]




for politician in politicians:
    url = f'https://irony.cs.bgu.ac.il/#/politician/acknowledgements/{politician.first_name}%20{politician.last_name}'
    print(f'\nStarts download for politician: {str(politician)}')
    comments=posts_page_service.get_comments_from_posts(url)
    print('\n Starts save comments for politician')
    io_service.save_lst_to_file('Data/Comments.csv',comments)

