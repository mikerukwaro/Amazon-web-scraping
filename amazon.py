from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pandas as pd

class AmazonScrapper:
    def __init__(self):
        self.driver = None
        self.items_to_search = None
        
    def initialize_defaults(self):
        self.driver = webdriver.Chrome("C:/Users/dnnsw/Desktop/my_projects/selenium_5/assets/chromedriver.exe")
        self.items_to_search = ["Redmi Note 11", "Redmi Note 10"]
        self.homepage_link = "https://www.amazon.in"

    def setup_driver(self):
        self.driver.maximize_window()
        self.page_load_strategy = 'eager'

    def navigate_to_homepage(self):
        self.driver.get(self.homepage_link)
        time.sleep(3)

    def search_input_interaction(self, product_to_search):
        search_element = self.driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
        search_element.send_keys(product_to_search)
        search_submit_btn = self.driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
        search_submit_btn.click()

    def elements_to_search(self, item):
        all_phone_models = self.driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

        for model in all_phone_models:
            try:
                data_assigned = model.get_attribute('data-asin')
                model_name = self.driver.find_element(By.XPATH, f"//div[@data-asin='{data_assigned}']//span[contains(text(), '{item}')]").text
                model_price = self.driver.find_element(By.XPATH, f'''//div[@data-asin="{data_assigned}"]//span[@class="a-price-whole"]''').text
                print(f"{model_name} >> {model_price}\n")

            except Exception as e:
                pass

    def process_provided_links(self):
        for item in self.items_to_search:
            self.search_input_interaction(item)
            self.elements_to_search(item)
            self.navigate_to_homepage()
        self.driver.close()

    def run(self):
        self.initialize_defaults()
        self.setup_driver()
        self.navigate_to_homepage()
        self.process_provided_links()

if __name__ == "__main__":
    scrapper = AmazonScrapper()
    scrapper.run()
