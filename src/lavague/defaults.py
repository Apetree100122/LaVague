from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from .driver import SeleniumDriver
from dotenv import load_dotenv

load_dotenv()

DEFAULT_EMBED_MODEL = "text-embedding-3-large"


class DefaultEmbedder(OpenAIEmbedding):
    def __init__(self, model=DEFAULT_EMBED_MODEL):
        super().__init__(model=model)


from llama_index.llms.openai import OpenAI
import os


class DefaultLLM(OpenAI):
    def __init__(self):
        max_new_tokens = 512
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        else:
            super().__init__(api_key=api_key, max_tokens=max_new_tokens)


def default_get_driver() -> SeleniumDriver:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    import os.path



    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1600,900")

    homedir = os.path.expanduser("~")

    # Paths to the chromedriver files
    path_linux = f"{homedir}/chromedriver-linux64/chromedriver"
    path_testing = f"{homedir}/chromedriver-testing/chromedriver"
    path_mac = "Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
    
    # To avoid breaking change kept legacy linux64 path
    if os.path.exists(path_linux):
        chrome_options.binary_location = f"{homedir}/chrome-linux64/chrome"
        webdriver_service = Service(f"{homedir}/chromedriver-linux64/chromedriver")
    elif os.path.exists(path_testing):
        if os.path.exists(f"{homedir}/chrome-testing/{path_mac}"):
            chrome_options.binary_location = f"{homedir}/chrome-testing/{path_mac}"
        # Can add support here for other chrome binaries with else if statements
        webdriver_service = Service(f"{homedir}/chromedriver-testing/chromedriver")
    else:
        raise FileNotFoundError("Neither chromedriver file exists.")




    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    return SeleniumDriver(driver)
